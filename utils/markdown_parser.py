import markdown
import os

def load_posts(directory):
    posts = []
    for filename in sorted(os.listdir(directory), reverse=True):
        if filename.endswith(".md"):
            path = os.path.join(directory, filename)
            with open(path, "r") as f:
                content = f.read()
            html = markdown.markdown(content)
            slug = filename.replace(".md", "")
            posts.append({"slug": slug, "html": html})
    return posts
