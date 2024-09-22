import praw
import requests
import re
import os
import hashlib
from bs4 import BeautifulSoup
from datetime import datetime
from urllib.parse import urlparse

# PRAW configuration
CLIENT_ID = 'ADD_YOUR_REDDIT_API_CLIENT_ID'
CLIENT_SECRET = 'ADD_YOUR_REDDIT_API_CLIENT_SECRET'
USER_AGENT = 'ADD_A_VALID_USER_AGENT'
reddit = praw.Reddit(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, user_agent=USER_AGENT)

# Directories to save images and posts
CACHE_DIR = '.'
IMAGES_DIR = os.path.join(CACHE_DIR, 'images')
POSTS_DIR = os.path.join(CACHE_DIR, 'posts')
os.makedirs(IMAGES_DIR, exist_ok=True)
os.makedirs(POSTS_DIR, exist_ok=True)

def fetch_image(img_url):
    img_hash = hashlib.md5(img_url.encode()).hexdigest()  # Generate a unique filename based on URL
    img_ext = os.path.splitext(urlparse(img_url).path)[1]  # Get the file extension
    img_path = os.path.join(IMAGES_DIR, img_hash + img_ext)
    if not os.path.exists(img_path):
        img_url = img_url.strip().rstrip(')')  # Clean URL
        response = requests.get(img_url)
        if response.status_code == 200:
            with open(img_path, 'wb') as f:
                f.write(response.content)
        else:
            print(f"Error downloading image {img_url}, Status code: {response.status_code}")
    return img_path

def handle_images(content):
    # Find all image URLs with preview.redd.it
    image_urls = re.findall(r'https://preview\.redd\.it/[^\s\'"]+', content)
    for url in image_urls:
        url = url.strip().rstrip(')')
        local_path = fetch_image(url)
        if local_path:
            # Replace the URL with the <img> tag using the local path
            content = content.replace(url, f'<img src="{local_path}" alt="Reddit Image">')
    return content

def fetch_post_content(url):
    parts = url.rstrip('/').split('/')
    slug = parts[-1]  # Post title
    post_id = parts[-2]  # Post ID
    filename = f"{slug}_{post_id}"
    post_path = os.path.join(POSTS_DIR, filename + '.md')

    if not os.path.exists(post_path):
        if 'reddit.com' in url:
            submission = reddit.submission(url=url)
            content = f"**Author**: u/{submission.author}\n\n"
            content += f"**Posted on**: {datetime.utcfromtimestamp(submission.created_utc).strftime('%Y-%m-%d')}\n\n"
            content += f"Original post: [{url}]({url})\n\n"
            # Remove extraneous H1 tags "\n\n #" (they always start with two newlines due to the create_epub_structure function)
            selftext = re.sub(
                r'\n\n# ',
                r'\n\n#### ',
                submission.selftext
            )
            content += selftext
            content = handle_images(content)
            with open(post_path, 'w', encoding='utf-8') as f:
                f.write(content)
        else:
            content = fetch_external_content(url)
            with open(post_path, 'w', encoding='utf-8') as f:
                f.write(content)
    else:
        with open(post_path, 'r', encoding='utf-8') as f:
            content = f.read()

    return content

def fetch_external_content(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        content = soup.get_text()
        return content
    return "Could not fetch the content."

def process_bullet_links(content):
    lines = content.splitlines()
    sub_chapters = []
    lingo_section = False
    for line in lines:
        match = re.search(r'\d{2}-[a-zA-Z]{3}-\d{4} - (.+) - (.+)\((https?://[^\)]+)\)', line)
        # chapter_title = re.search(r'^# .+\b', line)
        # heading_1 = re.search(r'^\* ', line)
        # heading_2 = re.search(r'^  \* ', line)
        # heading_3 = re.search(r'^    \* ', line)
        note = re.search(r'\*\*Note:\*\*', line)
        title = re.search(r'\[(.+)]\(', line)
        url = re.search(r'\[[^][]+]\((https?:\/\/[^()]+)\)', line)
        user = re.search(r'`u\/(.+)`', line)
        date_of_post = re.search(r'\* (\d{1,2}-(?:[a-zA-Z]{3,4}|\d{2})-\d{4})', line)  # long expression as matches e.g. 10-Oct-2022 OR 10-10-2022
        post_no_date = re.search(r'(\* \[)', line)
        lingo = re.search(r'(\* [a-zA-Z*(]+)', line)
        # style = None
        # if heading_1:
        #     style = "heading_1"
        # elif heading_2:
        #     style = "heading_2"
        # elif heading_3:
        #     style = "heading_3"
        # elif chapter_title:
        #     style = "chapter_title"
        # elif note:
        #     style = "note"
        try: # download reddit posts
            if "reddit" in url.group(1):
                if post_no_date or date_of_post:
                    title = title.group(1)
                    if "](" in title: # need this because the markdown text for some posts is incorrect in the wiki such as the one for ""$30K Challenge - Complete!""
                        title = title.split("](")[0]  # Remove everything after "]("
                    post_content = fetch_post_content(url.group(1))
                    sub_chapters.append(f"### {title}\n\n{post_content}\n")
        except:
            pass # TODO this is things like twitter posts and other URLs
        if line == "# Lingo/Jargon":
            lingo_section = True
        try:
            if lingo_section and lingo:
                sub_chapters.append(f"{line}\n")
        except:
            pass
    return sub_chapters

def create_epub_structure(wiki_content):
    chapters = re.split(r'______________________________________________________________________', wiki_content)
    epub_content = ""
    for chapter in chapters:
        lines = chapter.strip().splitlines()
        if lines:
            chapter_title = lines[2].strip()
            epub_content += f"{chapter_title}\n\n"
            sub_chapter_content = process_bullet_links('\n'.join(lines[1:]))
            epub_content += '\n'.join(sub_chapter_content)
            epub_content += "\n\n"
    return epub_content

def convert_markdown_to_html(markdown_content):
    import markdown
    from markdown.extensions.extra import ExtraExtension
    from markdown.extensions.codehilite import CodeHiliteExtension
    from markdown.extensions.toc import TocExtension

    md = markdown.Markdown(extensions=[ExtraExtension(), CodeHiliteExtension(), TocExtension()])
    html_content = md.convert(markdown_content)
    # Remove unwanted <h1> tags
    html_content = re.sub(r'<h1 id="_\d+">`</h1>', '', html_content)

    # Replace URLs with <img> tags for local images
    html_content = re.sub(
        r'(https://preview\.redd\.it/[^\s\'"]+)',
        r'<img src="\1" alt="Reddit Image">',
        html_content
    )

    # Fix cases where <a> wraps an <img>, replacing the <a> tag entirely
    html_content = re.sub(
        r'<a href="img src=&quot;([^&]+)&quot; alt=&quot;Reddit Image&quot;">',
        r'<img src="\1" alt="Reddit Image">',
        html_content
    )

    # Ensure text after image is placed on a new line
    html_content = re.sub(
        r'(<img[^>]+>)',
        r'\1<br>',  # Add a line break after the <img> tag
        html_content
    )

    # Fix paths for locally cached images
    html_content = re.sub(
        r'<img src="images/([a-zA-Z0-9_]+\.(png|jpg|webp|jpeg|gif))"',
        r'<img src="./images/\1"',
        html_content
    )

    return html_content

def fetch_wiki_content(subreddit_name, wiki_page):
    subreddit = reddit.subreddit(subreddit_name)
    wiki = subreddit.wiki[wiki_page]
    return wiki.content_md

def main():
    wiki_content = fetch_wiki_content('RealDayTrading', 'index')
    epub_content = create_epub_structure(wiki_content)
    epub_html = convert_markdown_to_html(epub_content)

    with open('wiki_output.html', 'w', encoding='utf-8') as f:
        f.write(epub_html)

    print("EPUB content saved to wiki_output.html. Convert this HTML file to EPUB using a tool like Calibre or Pandoc.")

if __name__ == "__main__":
    main()
