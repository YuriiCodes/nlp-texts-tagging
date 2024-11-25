
# 📝 Text Collection System

A powerful tool to:
1. Add, view, and search texts with **automatic tags**. 
2. 🕵️‍♂️ Crawl Wikipedia articles directly into your collection.
3. 🌐 Provide an API to fetch articles and their tags.

---

## 🚀 Features
- **Streamlit App**: Add, search, and manage texts easily.
- **Automatic Tagging**: Tags generated using AI-powered `spaCy`.
- **FastAPI**: Access your texts programmatically with filtering options.

---

## 🛠 Setup

### Prerequisites
- Python 3.8+
- pip

### Install Dependencies
```bash
pip install -r requirements.txt
```

---

## 💻 Run the Streamlit App
1. **Install SpaCy Model**:
   ```bash
   python -m spacy download en_core_web_sm
   ```
2. **Start the App**:
   ```bash
   streamlit run main.py
   ```
3. Access it in your browser: [http://localhost:8501](http://localhost:8501)

---

## 🌐 Run the API
1. **Start the API Server**:
   ```bash
   uvicorn api:app --reload
   ```
2. Access the API at: [http://127.0.0.1:8000/articles](http://127.0.0.1:8000/articles)

### API Query Parameters:
- `query`: Search for a keyword in text.
- `tag`: Filter by tag.

#### Examples:
- All articles:  
  ```bash
  curl http://127.0.0.1:8000/articles
  ```
- Search by keyword:  
  ```bash
  curl "http://127.0.0.1:8000/articles?query=example"
  ```
- Filter by tag:  
  ```bash
  curl "http://127.0.0.1:8000/articles?tag=demo"
  ```

---

## 📂 Project Structure
```plaintext
.
├── api.py          # FastAPI service
├── main.py         # Streamlit application
├── db.py           # Database logic
├── analyzer.py     # Automatic tag generation
├── requirements.txt
└── README.md
```

---

## 🤝 Contributing
1. Fork it 🍴  
2. Create a branch: `git checkout -b my-feature`  
3. Commit changes: `git commit -m 'Add feature 🚀'`  
4. Push: `git push origin my-feature`  
5. Open a PR!

