from flask import Flask, render_template, request, redirect, url_for
import json


app = Flask(__name__)

@app.route('/')
def index():
    """
    Render the homepage with a list of blog posts loaded from the JSON file.

    Returns:
        Rendered HTML template with the list of blog posts.
    """
    with open("data.json", "r", encoding="UTF-8") as fileobj:
        blog_posts = json.load(fileobj)

    return render_template('index.html', posts=blog_posts)


@app.route('/add', methods=['GET', 'POST'])
def add():
    """
    Handle GET and POST requests to add a new blog post.

    GET: Render the form to create a new blog post.
    POST: Receive form data, append new post to JSON file, and redirect to homepage.

    Returns:
        Redirect or rendered HTML template depending on request method.
    """
    if request.method == 'POST':
        title = request.form.get("title", "--")
        author = request.form.get("author", "--")
        content = request.form.get("content", "--")

        with open("data.json", "r", encoding="UTF-8") as fileobj:
            blog_posts = json.load(fileobj)

        existing_ids = {post["id"] for post in blog_posts}
        new_id = 1
        while new_id in existing_ids:
            new_id += 1

        new_post = {
            "id": new_id,
            "author": author,
            "title": title,
            "content": content
        }

        blog_posts.append(new_post)

        with open("data.json", "w", encoding="UTF-8") as fileobj:
            json.dump(blog_posts, fileobj, indent=4, ensure_ascii=False)

        return redirect(url_for('index'))
    return render_template('add.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001, debug=True)