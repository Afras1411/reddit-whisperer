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
   ```bash
   git clone https://github.com/YOUR_USERNAME/reddit-whisperer.git
   cd reddit-whisperer
