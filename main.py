from flask import Flask, render_template, request, jsonify
import requests
from bs4 import BeautifulSoup
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
import google.generativeai as genai
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)

# Configure Gemini API Key
genai.configure(api_key="Gemini_API_Key")

# Global variables to store scraped data
scraped_text = ""
vectorizer = TfidfVectorizer()
text_vectors = None  # Will hold vectorized scraped text


def scrape_text(url):
    """Fetch and parse webpage text content."""
    global scraped_text, text_vectors

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        paragraphs = [p.get_text() for p in soup.find_all("p")]
        scraped_text = " ".join(paragraphs)
        print(scraped_text)

        if not scraped_text.strip():
            return False  # No meaningful text found

        # Vectorize the scraped text
        text_vectors = vectorizer.fit_transform([scraped_text])
        return True

    except requests.exceptions.RequestException as e:
        print(f"Error scraping URL: {e}")
        return False


def get_gemini_response(user_query, user_vector):
    """Retrieve the most relevant content and pass it to Gemini."""
    global scraped_text, text_vectors, url

    if text_vectors is None:
        return "No data available. Please provide a valid URL first."

    # Compute cosine similarity
    similarity_scores = cosine_similarity(user_vector, text_vectors)
    most_similar_index = np.argmax(similarity_scores)
    context = scraped_text.split(".")[most_similar_index]

    guide = f"""you are a expert Q&A analyst chatbot, you have provided the content from specific website scrapped data. 
        your task is to answer the user questions based on the stored data, answer the user's questions.
        respond to user message as a normal chatbot, and if user ask other than data, just reply as out of knowledge,

        """

    prompt = f"""
    guide: {guide}
    Context: {context}\n
    User: {user_query}\nGemini:
    """

    try:
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error in Gemini API: {e}"


@app.route("/")
def index():
    """Render the chatbot interface."""
    return render_template("index.html")


@app.route("/ingest", methods=["POST"])
def ingest():
    """Accepts a URL and scrapes data before enabling chat."""
    url = request.form.get("url")


    if not url:
        return jsonify({"error": "No URL provided"}), 400

    success = scrape_text(url)

    if not success:
        return jsonify({"error": "Failed to extract meaningful text from the URL."}), 400

    return jsonify({"message": "Data ingested successfully! You can now start chatting."})


@app.route("/chat", methods=["POST"])
def chat():
    """Handles user queries and fetches responses."""
    global text_vectors

    if text_vectors is None:
        return jsonify({"response": "No data available. Please enter a URL first."})

    user_query = request.form["user_input"]
    user_vector = vectorizer.transform([user_query])

    gemini_response = get_gemini_response(user_query, user_vector)

    return jsonify({"response": gemini_response})


if __name__ == "__main__":
    app.run(debug=True)  # Set debug=False in production
