# 🔠 Autocorrect & Word Suggestion Web App

A Flask-based web application that provides intelligent word suggestions using a probability model and similarity scoring. The app reads text from *Moby Dick* to generate a custom vocabulary and frequency model, then suggests similar words based on user input.

---

## 🌟 Features

- Autocorrect word suggestions using Jaccard similarity.
- Flask-powered web interface.
- NLP using word frequency & edit distance.
- Based on classic English literature (*Moby Dick*).

---

## 🚀 Demo

> Type a word in the input field and get the closest-matching suggestions based on the book.

---

## 🛠️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/autocorrect-flask-app.git
cd autocorrect-flask-app


2. Create a Virtual Environment (Optional)
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

3. Install Dependencies
pip install -r requirements.txt

📂 Project Structure
├── app.py                   # Flask application
├── autocorrect book.txt     # Input text corpus (Moby Dick)
├── templates/
│   └── index.html           # HTML template for web UI
├── Word_Suggestion.ipynb    # Optional Jupyter notebook for logic dev
└── requirements.txt         # Python dependencies

▶️ Running the App
python app.py

Then open your browser and go to:
http://127.0.0.1:5000/

🧠 How It Works
Uses regular expressions to tokenize the text into words.

Calculates word frequency and probability.

Compares user input with known words using Jaccard similarity from the textdistance library.

Ranks and returns the top suggestions.

📦 Dependencies
Flask
pandas
textdistance

📝 License
This project is open-source under the MIT License.

👨‍💻 Author
Hussnain Ali


---

Let me know if you'd like me to generate a matching `requirements.txt` or auto-deploy setup (like with GitHub Pages or Render).

