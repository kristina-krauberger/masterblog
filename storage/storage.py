import json


def loads_posts(data_file):
    """
    Load posts from a JSON file.

    Args:
        data_file (str): Path to the JSON file.

    Returns:
        list: List of blog posts.
    """
    try:
        with open(data_file, "r", encoding="UTF-8") as fileobj:
            blog_posts = json.load(fileobj)
            return blog_posts

    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error loading posts: {e}")
        blog_posts = []
        return blog_posts


def save_posts(data_file, new_blog_posts):
    """
    Save posts to a JSON file.

    Args:
        data_file (str): Path to the JSON file.
        new_blog_posts (list): Posts to save.

    Returns:
        bool: True if successful, False otherwise.
    """
    try:
        with open(data_file, "w", encoding="UTF-8") as fileobj:
            json.dump(new_blog_posts, fileobj, indent=4, ensure_ascii=False)

    except (PermissionError, OSError, TypeError) as e:
        print(f"Error saving posts: {e}")
        return False
    return True
