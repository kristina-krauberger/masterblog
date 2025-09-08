from flask import Flask, render_template
import json


app = Flask(__name__)

@app.route('/')
def index():

    with open("data.json", "r", encoding="UTF-8") as fileobj:
        #fileobj.read()
        blog_posts = json.load(fileobj)

    return render_template('index.html', posts=blog_posts)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001, debug=True)