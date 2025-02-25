# Web Content Q&A Tool

## 🎯 Objective  
This project is a **Flask-based Intelligent FAQ Assistant** that utilizes **Large Language Models (LLMs)** and **Generative AI (GenAI)** to provide **context-aware, dynamic responses** based on an ingested knowledge base. The system enables real-time query handling, periodic knowledge base updates, and interaction logging for analysis and improvement.

## 🚀 Features  

### 🔹 **Knowledge Base Integration**  
- Supports structured and unstructured data formats (**JSON, TXT, Markdown**).  
- Allows seamless updates to ensure the assistant remains up-to-date.  

### 🔹 **Intelligent Query Handling**  
- Uses **Google Gemini 1.5 Flash** for high-accuracy responses.  
- Provides **context-aware** answers strictly based on the ingested knowledge base.  
- Implements **semantic search** for better information retrieval.  

### 🔹 **Flask Web Application**  
- User-friendly **web UI** for easy query input and response display.  
- Minimalist design with **fast query processing**.  
 

### 🔹 **Fallback Mechanism**  
- Provides **alternative suggestions** when an answer is unavailable.  
- Ensures a smooth user experience by guiding users to relevant content.  

## Tools & Technologies Used
- **LLM**: Google Gemini
- **Server Framework**: Flask
- **Text Processing**: `TfidfVectorizer` (for knowledge base search)

## How to Run the Project Locally
### Prerequisites
- Python3 installed
- Firebase credentials configured
- API key for Google Gemini

### Steps to Set Up and Run
1. **Clone the repository**:
   ```bash
   git clone https://github.com/Ganeshkharde1/FAQ-assistant.git
   cd Q-A-Tool--Aisensy
   ```


2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Update the Gemini API key**:
   ```bash
   # Set your Gemini API key
    genai.configure(api_key="Paste API Key")
   ```
   

4. **Run the Flask server**:
   ```bash
   python main.py
   ```

7. **Access the application**:
   - Open `http://127.0.0.1:5000/` in a browser.



## License
This project is open-source and available under the MIT License.

---
Feel free to contribute or report issues!
