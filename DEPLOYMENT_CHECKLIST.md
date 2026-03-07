# DEPLOYMENT CHECKLIST FOR RENDER

## Files to COMMIT and PUSH to GitHub ✅

### Essential Files (Must Include)
```
app.py                    # Flask application
chatbot.py                # NLP logic
database.py               # Snowflake connection
requirements.txt          # Dependencies (NEW - with versions)
Procfile                  # Render configuration (NEW)
runtime.txt               # Python version (NEW)
README.md                 # Documentation (UPDATED)
.gitignore                # Git ignore file (NEW)
templates/index.html      # Web interface
static/style.css          # Styling
```

### Total: 10 files to push

---

## Files to DELETE (Do NOT push) ❌

```
virtualENV/               # Virtual environment directory
venv/                     # Alternative venv directory  
test_database.py          # Test file
test_dynamic_queries.py   # Test file
voice_bot.py              # Not used in chatbot
requirements_local.txt    # Use requirements.txt instead
requirements_render.txt   # Use requirements.txt instead
__pycache__/              # Python cache (auto-ignored by .gitignore)
*.pyc                     # Compiled Python files (auto-ignored by .gitignore)
.env                      # Environment variables (auto-ignored by .gitignore)
```

---

## Git Commands for Deployment

```bash
# Navigate to project directory
cd C:\Ruturaj\PROJECT\college-ai-chatbot

# Check git status
git status

# Add all necessary files
git add .

# Commit changes
git commit -m "Deploy college AI chatbot to Render

- Remove all static/fallback responses
- Use only Snowflake database
- Add production-ready configuration
- Include Procfile and runtime.txt for Render"

# Push to GitHub
git push origin main
```

---

## Render Deployment Steps

1. Go to https://render.com
2. Click "New +" → "Web Service"
3. Connect your GitHub repository
4. Fill in deployment details:
   - **Name**: college-ai-chatbot
   - **Environment**: Python 3
   - **Build Command**: pip install -r requirements.txt
   - **Start Command**: gunicorn app:app

5. Add Environment Variables:
   - SNOWFLAKE_USER=Anchal
   - SNOWFLAKE_PASSWORD=Anchalgothwal@1234
   - SNOWFLAKE_ACCOUNT=vvbadpg-le30326
   - SNOWFLAKE_WAREHOUSE=COMPUTE_WH
   - SNOWFLAKE_ROLE=AI_CHATBOT_USER
   - SNOWFLAKE_DATABASE=COLLEGE_DB
   - SNOWFLAKE_SCHEMA=COLLEGE_SCHEMA

6. Click "Deploy"

---

## What's Ready

✅ app.py - Production configured
✅ chatbot.py - No hardcoded data
✅ database.py - Direct Snowflake queries
✅ requirements.txt - All dependencies with versions
✅ Procfile - For Render
✅ runtime.txt - Python 3.12.0
✅ .gitignore - Excludes virtual environment
✅ README.md - Complete documentation
✅ templates/index.html - Web interface
✅ static/style.css - Styling
