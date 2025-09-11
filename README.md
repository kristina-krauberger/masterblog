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
- python-dotenv

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
├── app.py
├── config/
│   └── config.py
├── data/
│   └── data.json
├── templates/
│   ├── index.html
│   ├── add.html
│   └── update.html
├── static/
│   └── (your CSS files)
├── requirements.txt
└── .env
```

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

Built with 💻 and ☕️ by Kristina Krauberger
