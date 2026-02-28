
import requests
from bs4 import BeautifulSoup
from typing import List, Optional

def fetch_url(url: str) -> Optional[BeautifulSoup]:

    """
    Fetch the url of the page
    """

    try:
        
        headers = {
    "User-Agent": (
        "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) "
        "AppleWebKit/605.1.15 (KHTML, like Gecko) "
        "Version/17.0 Mobile/15E148 Safari/604.1"
    ),
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1"
    }
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return BeautifulSoup(response.content, 'lxml')
    
    except requests.RequestException as e:
        print(f"Http Error: {e}")
        return None
    
def get_comments(body: BeautifulSoup) -> List[str]:

    """
    Get the elements of the page and return the comments
    """

    elements = body.find_all(class_="ind", indent="0")
    return [e.find_next(class_="comment") for e in elements if e.find_next(class_="comment")]
    

def get_keywords(comments: List[BeautifulSoup], keywords: dict[str, int]) -> List[str]:

    """
    Updates Keywrod counts and return python related comments
    """

    python_comments = []

    for c in comments:
        comment_text = c.get_text().lower()
        words = comment_text.split()
        words = {w.strip(".,/!@|-$") for w in words}

        for k in keywords:
            if k in words:
                keywords[k] += 1

        if "python" in comment_text:
            python_comments.append(comment_text)

    return python_comments

def main() -> None:
    
    """
    Main program flow: fetch, extract, count keywords, and print results.
    """

    url = "https://news.ycombinator.com/item?id=46466074"
    soup = fetch_url(url)

    if not soup:
        print("Failed to fetch URL")
        return
    
    body = soup.find('body')
    if not body:
        print("No body found in the page")
        return
    
    python_comments = []
    keywords = {
                "python": 0,
                "javascript": 0,
                "typescript":0,
                "devops": 0,
                "ruby": 0,
                "java": 0
            }
    
    comments = get_comments(body)
    python_comments = get_keywords(comments, keywords)

    print(keywords, "\n")
    print(f"found {len(python_comments)} python related comments\n")

    for idx, comment in enumerate(python_comments, start=1):
        print(f"{idx}., {comment}")
        print("-" * 80, "\n")
   

if __name__ == "__main__":
    main()
