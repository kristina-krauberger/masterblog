from flask import Flask, render_template, request, redirect, url_for, flash
from config.config import Config
from storage.storage import loads_posts, save_posts

app = Flask(__name__)
app.secret_key = Config.SECRET_KEY


@app.route('/')
def index():
    """
    Show homepage with blog posts using loads_posts.

    Returns: Rendered template with posts.
    """
    blog_posts = loads_posts(Config.DATA_FILE)

    if not blog_posts:
        flash("Error while loading file. File is empty or damaged.", "error")
        return render_template("index.html", posts=[])
    else:
        return render_template("index.html", posts=blog_posts)


@app.route('/add', methods=['GET', 'POST'])
def add():
    """
    Add a new blog post.

    Returns: Redirect or rendered HTML template depending on request method.
    """
    if request.method == 'POST':
        title = request.form.get("title", "--")
        author = request.form.get("author", "--")
        content = request.form.get("content", "--")

        blog_posts = loads_posts(Config.DATA_FILE)

        if not blog_posts:
            flash("Error while loading file. File is empty or damaged.", "error")
            return render_template("index.html", posts=[])

        else:
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

            if save_posts(Config.DATA_FILE, blog_posts):
                return redirect(url_for('index'))
            else:
                flash("Error while saving posts.", "error")
                return render_template("index.html", posts=blog_posts)

    else:
        return render_template('add.html')


@app.route('/delete/<int:post_id>')
def delete(post_id):
    """
    Delete a blog post by its ID. Removes the blog post from data.json. Stores a success message using flash.

    Args:
        post_id (int): The ID of the blog post to be deleted.

    Returns:
        Response: Redirect to the homepage after deletion.
    """

    blog_posts = loads_posts(Config.DATA_FILE)

    if not blog_posts:
        flash("Error while loading file. File is empty or damaged.", "error")
        return render_template("index.html", posts=[])

    else:
        for index, blog_post in enumerate(blog_posts):
            print(index)
            if post_id == blog_post["id"]:
                del blog_posts[index]
                flash(f"The post '{blog_post['title']}' was successfully deleted.", "success")
                break

        if save_posts(Config.DATA_FILE, blog_posts):
            return redirect(url_for('index'))
        else:
            flash("Error while saving posts.", "error")
            return render_template("index.html", posts=blog_posts)


def fetch_post_by_id(post_id):
    """
    Fetch a blog post by its ID.

    Args:
        post_id (int): ID of the blog post.

    Returns:
        dict or None: Post dictionary if found, else None.
    """

    blog_posts = loads_posts(Config.DATA_FILE)

    if not blog_posts:
        flash("Error while loading file. File is empty or damaged.", "error")
        return None

    else:
        for blog_post in blog_posts:
            if post_id == blog_post["id"]:
                return blog_post
        return None


@app.route('/update/<int:post_id>', methods=['GET', 'POST'])
def update(post_id):
    """
    Handle GET and POST requests to update an existing blog post.
    GET: Load the existing blog post data by ID and render the update form.
    POST: Receive updated form data, modify the post in data.json,
    flash a success message, and redirect to the homepage.

    Args:
        post_id (int): The ID of the blog post to update.

    Returns:
        Response: Rendered update form (GET) or redirect to index page (POST).
    """

    searched_blog_post = fetch_post_by_id(post_id)
    if searched_blog_post is None:
        return "Post not found", 404

    if request.method == 'POST':
        title = request.form.get("title", "--")
        author = request.form.get("author", "--")
        content = request.form.get("content", "--")

        blog_posts = loads_posts(Config.DATA_FILE)

        if not blog_posts:
            flash("Error while loading file. File is empty or damaged.", "error")
            return render_template("index.html", posts=[])

        for post in blog_posts:
            if searched_blog_post["id"] == post["id"]:
                post["title"] = title
                post["author"] = author
                post["content"] = content
                flash(f"The post '{post['title']}' was successfully updated.", "success")
                break

        if save_posts(Config.DATA_FILE, blog_posts):
            return redirect(url_for("index"))
        else:
            flash("Error while saving posts.", "error")
            return render_template('update.html', post=searched_blog_post)

    return render_template('update.html', post=searched_blog_post)


@app.route('/update_like/<int:post_id>', methods=['POST'])
def update_like(post_id):
    """
    Increment likes for a blog post and redirect to index.

    Args:
        post_id (int): ID of the post to like.

    Returns:
        Response: Redirect to the homepage.
    """

    blog_posts = loads_posts(Config.DATA_FILE)

    if not blog_posts:
        flash("Error while loading file. File is empty or damaged.", "error")
        return render_template("index.html", posts=[])

    else:
        for blog_post in blog_posts:
            if post_id == blog_post['id']:
                blog_post['likes'] = blog_post.get('likes', 0) + 1
                break

        if save_posts(Config.DATA_FILE, blog_posts):
            return redirect(url_for("index"))
        else:
            flash("Error while saving posts.", "error")
            return render_template("index.html", posts=blog_posts)


@app.errorhandler(404)
def page_not_found(error):
    """
    Render the 404 error page.

    Args:
        error: The raised error object.

    Returns:
        Response: Rendered 404 error template.
    """
    return render_template("404.html"), 404


@app.errorhandler(500)
def internal_server_error(error):
    """
    Render the 500 error page.

    Args:
        error: The raised error object.

    Returns:
        Response: Rendered 500 error template.
    """
    return render_template("500.html"), 500


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001, debug=True)