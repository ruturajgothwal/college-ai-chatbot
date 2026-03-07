# College AI Chatbot

A modern AI-powered chatbot for college inquiries with NLP capabilities and Snowflake database integration.

## Features

- 🤖 **Natural Language Processing** - Understands user queries using NLTK and scikit-learn
- 🗄️ **Snowflake Integration** - Fetches real-time data from Snowflake database
- 💬 **Dynamic Query Building** - Automatically constructs SQL queries based on user input
- 🌐 **Modern Web Interface** - Responsive design with real-time chat functionality
- 📚 **Course Information** - Provides courses, fees, schedules, and duration

## Tech Stack

- **Backend**: Python 3.12, Flask
- **NLP**: NLTK, scikit-learn
- **Database**: Snowflake
- **Frontend**: HTML5, CSS3, JavaScript
- **Deployment**: Gunicorn, Render

## Project Structure

```
college-ai-chatbot/
├── app.py                 # Flask application entry point
├── chatbot.py             # NLP logic and response generation
├── database.py            # Snowflake database functions
├── requirements.txt       # Python dependencies
├── Procfile               # Render deployment configuration
├── runtime.txt            # Python version specification
├── templates/
│   └── index.html         # Web interface
└── static/
    └── style.css          # Styling
```

## Installation

### Local Development

1. Clone the repository:
```bash
git clone <repository-url>
cd college-ai-chatbot
```

2. Create and activate virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the application:
```bash
python app.py
```

Visit `http://localhost:5000` in your browser.

## Deployment on Render

### Prerequisites
- GitHub repository
- Render account
- Snowflake database with appropriate tables

### Quick Steps

1. **Push to GitHub**:
```bash
git add .
git commit -m "Deploy college AI chatbot"
git push origin main
```

2. **Connect on Render**:
   - Go to [render.com](https://render.com)
   - Click "New +" → "Web Service"
   - Select your GitHub repository
   - Configure:
     - **Name**: college-ai-chatbot
     - **Environment**: Python 3
     - **Build Command**: `pip install -r requirements.txt`
     - **Start Command**: `gunicorn app:app`

3. **Set Environment Variables** in Render dashboard:
   - `SNOWFLAKE_USER`
   - `SNOWFLAKE_PASSWORD`
   - `SNOWFLAKE_ACCOUNT`
   - `SNOWFLAKE_WAREHOUSE`
   - `SNOWFLAKE_ROLE`
   - `SNOWFLAKE_DATABASE`
   - `SNOWFLAKE_SCHEMA`

## Database Schema

### COURSES Table
```sql
CREATE TABLE COURSES (
    COURSE_NAME VARCHAR(100),
    FEES NUMBER,
    DURATION VARCHAR(50)
);
```

### SCHEDULE Table
```sql
CREATE TABLE SCHEDULE (
    COURSE_NAME VARCHAR(100),
    CLASS_TIME VARCHAR(100)
);
```

## Usage

Users can ask:
- "What courses do you offer?"
- "How much is BCA fee?"
- "What are the class timings?"
- "How long is MBA?"

## Core Files

| File | Purpose |
|------|---------|
| `app.py` | Flask application |
| `chatbot.py` | NLP & response generation |
| `database.py` | Snowflake connection |
| `requirements.txt` | Dependencies |
| `Procfile` | Render config |
| `templates/index.html` | Web UI |
| `static/style.css` | Styling |

## Notes

- All data from Snowflake database only
- No hardcoded fallback data
- Dynamic SQL query generation
- NLP-based intent recognition
