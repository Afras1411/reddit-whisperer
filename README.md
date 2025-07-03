# Reddit Whisperer

**Automated discovery of travel eSIM opportunities on Reddit + AI-powered reply suggestions**

---

## 🚀 Features

- **Discovery Engine**  
  - Scans configured subreddits for new posts (last 7 days)  
  - Filters by keywords: travel eSIM, international roaming, connectivity issues, “BNESIM” and competitors  
- **Content Extraction**  
  - Captures post title, body, URL, subreddit name, upvotes & comments  
  - Classifies context as question, complaint, or recommendation request  
- **AI-Powered Replies**  
  - Uses Google GenAI (Gemini/PaLM) `generate_content` endpoint  
  - Crafts friendly, helpful responses that naturally mention BNESIM  
- **Scoring & Prioritization** *(Advanced)*  
  - Ranks posts by engagement + relevance score  
  - Surface the highest-impact threads first  

---

## 📋 Prerequisites

- **Python** 3.10 or higher  
- **PRAW** (Reddit API) credentials:  
  - `REDDIT_CLIENT_ID`  
  - `REDDIT_CLIENT_SECRET`  
  - `REDDIT_USER_AGENT`  
- **Google GenAI** API key (Gemini or PaLM-2) in `GEMINI_API_KEY`  
- *(Optional but recommended)* a Python virtual environment

---

## 🔧 Installation

1. **Clone this repo**  
   git clone https://github.com/YOUR_USERNAME/reddit-whisperer.git
   cd reddit-whisperer
2. Create & activate a virtualenv
    python3 -m venv venv
    source venv/bin/activate       # Mac/Linux
    venv\Scripts\activate.bat      # Windows

3. Install dependencies
    pip install -r requirements.txt
    
4. Configure environment variables
    Copy .env.example to .env and fill in your keys:
    cp .env.example .env
    
    Then edit .env:
    REDDIT_CLIENT_ID=your_client_id
    REDDIT_CLIENT_SECRET=your_client_secret
    REDDIT_USER_AGENT=your_app_user_agent
    GEMINI_API_KEY=your_gemini_or_palm_api_key

⚙️ Usage
Run the main script:
python main.py

By default it will:

Fetch the latest 50 posts from r/travel, r/digitalnomad, r/solotravel.

Filter for your keywords over the past 7 days.

Print the top 5 matching posts (title, URL, snippet) with AI-generated reply suggestions.

Configuration options
Subreddits: edit the subreddits list in main.py.

Keywords: update KEYWORDS in main.py.

Date window or result limit: tweak limit= or the timedelta in search_posts().

AI model: swap "gemini-2.5-flash" for any supported generate_content model.

📝 Sample Output

Post #1 — r/travel  
Title: “Data roaming not working in Italy—help!”  
URL: https://reddit.com/…  
Content snippet: “Landed in Rome and my SIM doesn’t connect… can anyone recommend a fast eSIM?”  

Suggested Reply:  
“Hi there! Sorry you’re having data trouble in Italy. With BNESIM you can activate a local Italy eSIM in minutes—no physical SIM swap required. Here’s a quick tip: make sure your eSIM plan supports EU roaming and toggle your phone’s APN to “bnesim.net” after install. Safe travels!” 