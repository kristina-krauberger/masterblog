# MasterBlog 📝

A simple blog application built with Flask that allows you to:

- Create blog posts
- Update blog posts
- Delete blog posts
- Like blog posts ❤️

## 🚀 Getting Started

### Requirements

- Python 3.10+
- Flask

Install dependencies:

```bash
pip install -r requirements.txt
```

### 🔧 Environment Variables

Create a `.env` file with the following content:

```env
SECRET_KEY=your-secret-key
```

## 💡 How to Run

```bash
python app.py
```

The app will run on `http://0.0.0.0:5001` by default.

## 📁 Project Structure

```
.
├── app.py                # Main Flask application
├── storage/
│   ├── __init__.py
│   └── storage.py        # Handles data storage and retrieval
├── config/
│   ├── __init__.py
│   └── config.py         # Application configuration variables
├── data/
│   └── data.json         # JSON file storing blog posts
├── templates/
│   ├── 404.html
│   ├── 500.html
│   ├── index.html        # Homepage displaying posts
│   ├── add.html          # Form to add new posts
│   └── update.html       # Form to edit existing posts
├── static/
│   └── style.css         # Stylesheet
├── requirements.txt      # Python dependencies
└── .env                  # Environment variables
```

---

Built with 💻 and ☕️ by Kristina Krauberger
