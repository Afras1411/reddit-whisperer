import os
from datetime import datetime, timedelta
from dotenv import load_dotenv

import praw
from google import genai

load_dotenv()

# Instantiate the Gen AI client for the Gemini Developer API
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))  # :contentReference[oaicite:0]{index=0}

# Reddit client remains the same
reddit = praw.Reddit(
    client_id=os.getenv("REDDIT_CLIENT_ID"),
    client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
    user_agent=os.getenv("REDDIT_USER_AGENT"),
)

KEYWORDS = [
    "travel esim", "international roaming", "travel sim",
    "BNESIM", "airalo", "gigsky", "connectivity issues",
    "roaming charges"
]

def search_posts(subreddits, limit=100):
    results = []
    cutoff = datetime.utcnow() - timedelta(days=7)
    for subreddit_name in subreddits:
        for post in reddit.subreddit(subreddit_name).new(limit=limit):
            text = post.title + " " + post.selftext
            if any(kw.lower() in text.lower() for kw in KEYWORDS):
                if datetime.utcfromtimestamp(post.created_utc) > cutoff:
                    results.append({
                        'title': post.title,
                        'content': post.selftext,
                        'url': post.url,
                        'score': post.score,
                        'comments': post.num_comments,
                        'subreddit': post.subreddit.display_name
                    })
    return results

def generate_response(post):
    prompt = f"""
Reddit Post:
Title: {post['title']}
Content: {post['content']}

Write a friendly, helpful response from a BNESIM rep that:
- Addresses the issue
- Offers travel advice
- Suggests BNESIM naturally (no hard sell)
"""
    try:
        # use the text‐generation endpoint with Gemini Flash
        resp = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )
        return resp.text.strip()
    except Exception as e:
        print(f"Error generating response: {e}")
        return "Sorry, I couldn't generate a response at this time."

if __name__ == "__main__":
    subreddits = ["travel", "digitalnomad", "solotravel"]
    posts = search_posts(subreddits, limit=50)

    for i, post in enumerate(posts[:5]):
        print(f"\nPost #{i+1} — r/{post['subreddit']}")
        print("Title:", post['title'])
        print("URL:", post['url'])
        print("Content:", post['content'][:200], "...")
        print("\nSuggested Reply:\n", generate_response(post))
        print("=" * 80)
