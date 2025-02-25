# Web Content Q&A Tool

![Screenshot 2025-02-25 152845](https://github.com/user-attachments/assets/a0640a83-2247-4a91-ab53-60dc8fdac6be)

![Screenshot 2025-02-25 152945](https://github.com/user-attachments/assets/15e001bc-7281-4d32-812b-3c0b1178996a)

## 🎯 Objective  
The **Web Content Q&A Tool** is a **Flask-based application** that extracts content from web pages and enables users to ask context-specific questions about the ingested information. The tool ensures responses are **strictly grounded in the scraped content**, making it useful for research, content analysis, and quick information retrieval.  

## 🚀 Features  

### 🔹 **Web Content Extraction**  
- Supports extracting text content from **URLs**.  
- Parses and cleans the extracted content for **accurate information retrieval**.  

### 🔹 **Intelligent Q&A System**  
![download](https://github.com/user-attachments/assets/2bc5e7f5-1974-4375-85f9-47210bebcd18)
- Uses **Google Gemini 1.5 Flash** for **high-accuracy** responses.  
- Answers are **strictly derived from the scraped web content**.  
- Implements **semantic search** to find relevant information quickly.  

### 🔹 **User-Friendly Web Interface**  
- Simple **UI for adding URLs and querying content**.  
- Provides clear, concise responses with a **chat-like experience**.  

### 🔹 **Efficient Vector Search**  
<img width="200" src="https://github.com/user-attachments/assets/17f1010f-78bd-4aaa-93cb-c065d9b9f729"> 


- Uses **FAISS (Facebook AI Similarity Search)** for fast text retrieval.  
- Can be extended to **ChromaDB, Qdrant, Weaviate, CosmosDB**, and more.  

### 🔹 **Admin & API Features**  
- Allows **URL ingestion** for content analysis.  
- API endpoint for **content extraction & Q&A automation**.  

### 🔹 **Fallback Mechanism**  
- Provides **alternative suggestions** when answers are unavailable.  
- Ensures users are **guided to relevant content**.  

## Tools & Technologies Used
- **LLM**: Google Gemini
- **Server Framework**: Flask
- **Text Processing**: `TfidfVectorizer` (for knowledge base search)

## How to Run the Project Locally
### Prerequisites
- Python3 installed
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
