import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from difflib import SequenceMatcher
import numpy as np
import re

# Download required NLTK data
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')

try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords')

try:
    nltk.data.find('corpora/wordnet')
except LookupError:
    nltk.download('wordnet')

# Try to download punkt_tab if available (for newer NLTK versions)
try:
    nltk.data.find('tokenizers/punkt_tab')
except LookupError:
    try:
        nltk.download('punkt_tab')
    except:
        pass  # Ignore if download fails

from database import get_courses, get_fee, get_schedule, get_course_details, get_all_courses_info, get_all_schedules, get_duration, connect_db

# Initialize NLP components
lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('english'))

# Keywords for different query types
COURSE_KEYWORDS = ['course', 'courses', 'program', 'programs', 'subject', 'subjects', 'study', 'learn', 'offer', 'available']
FEE_KEYWORDS = ['fee', 'fees', 'cost', 'costs', 'price', 'prices', 'tuition', 'money', 'pay', 'payment', 'amount']
SCHEDULE_KEYWORDS = ['schedule', 'schedules', 'timing', 'timings', 'time', 'times', 'class', 'classes', 'when', 'hour', 'hours']
DURATION_KEYWORDS = ['duration', 'durations', 'long', 'length', 'period', 'year', 'years', 'month', 'months']
COURSE_NAMES = ['BCA', 'BBA', 'MBA']

def preprocess_text(text):
    """Preprocess text using NLTK with fallback"""
    # Convert to lowercase
    text = text.lower()

    try:
        # Try NLTK tokenization
        tokens = word_tokenize(text)
    except LookupError:
        # Fallback to simple splitting if NLTK data not available
        tokens = text.split()

    # Remove stopwords and punctuation
    tokens = [word for word in tokens if word.isalnum() and word not in stop_words]

    # Lemmatize
    try:
        tokens = [lemmatizer.lemmatize(word) for word in tokens]
    except:
        # Fallback if lemmatization fails
        pass

    return tokens

def extract_course_name(text):
    """Extract course name from user input"""
    text_upper = text.upper()

    for course in COURSE_NAMES:
        if course in text_upper:
            return course

    return None

def identify_query_type(text):
    """Identify what type of information the user is asking for"""
    text_lower = text.lower()
    tokens = preprocess_text(text)

    # Check for course-related queries
    if any(keyword in text_lower for keyword in COURSE_KEYWORDS):
        return "courses"

    # Check for fee-related queries
    if any(keyword in text_lower for keyword in FEE_KEYWORDS):
        return "fees"

    # Check for schedule-related queries
    if any(keyword in text_lower for keyword in SCHEDULE_KEYWORDS):
        return "schedule"

    # Check for duration-related queries
    if any(keyword in text_lower for keyword in DURATION_KEYWORDS):
        return "duration"

    return "unknown"

def build_snowflake_query(query_type, course_name=None):
    """Build appropriate Snowflake SQL query based on query type"""
    if query_type == "courses":
        return "SELECT COURSE_NAME, FEES, DURATION FROM COURSES ORDER BY COURSE_NAME"

    elif query_type == "fees" and course_name:
        return f"SELECT COURSE_NAME, FEES FROM COURSES WHERE UPPER(COURSE_NAME) = '{course_name}'"

    elif query_type == "schedule" and course_name:
        return f"SELECT COURSE_NAME, CLASS_TIME FROM SCHEDULE WHERE UPPER(COURSE_NAME) = '{course_name}'"

    elif query_type == "schedule":
        return "SELECT COURSE_NAME, CLASS_TIME FROM SCHEDULE ORDER BY COURSE_NAME"

    elif query_type == "duration" and course_name:
        return f"SELECT COURSE_NAME, DURATION FROM COURSES WHERE UPPER(COURSE_NAME) = '{course_name}'"

    return None

def execute_snowflake_query(query):
    """Execute a Snowflake query and return results"""
    try:
        conn = connect_db()
        cur = conn.cursor()
        cur.execute(query)
        rows = cur.fetchall()
        cur.close()
        conn.close()
        return rows
    except Exception as e:
        print(f"Error executing query: {e}")
        return None

def format_query_results(query_type, results, course_name=None):
    """Format query results into readable text"""
    if not results:
        return "No information found."

    if query_type == "courses":
        response = "📚 Available Courses:\n\n"
        for row in results:
            course_name, fees, duration = row
            response += f"• {course_name}\n"
            response += f"  💰 Fees: ₹{fees:,}\n"
            response += f"  📖 Duration: {duration}\n\n"
        return response.strip()

    elif query_type == "fees" and course_name:
        course_name, fees = results[0]
        return f"💰 {course_name} Fees: ₹{fees:,}"

    elif query_type == "schedule" and course_name:
        course_name, class_time = results[0]
        return f"🕐 {course_name} Class Schedule: {class_time}"

    elif query_type == "schedule":
        response = "📅 Class Schedules:\n\n"
        for row in results:
            course_name, class_time = row
            response += f"• {course_name}: {class_time}\n"
        return response.strip()

    elif query_type == "duration" and course_name:
        course_name, duration = results[0]
        return f"📖 {course_name} Duration: {duration}"

    return "Information retrieved successfully."

def get_dynamic_response(user_input):
    """Generate response by dynamically building and executing Snowflake queries"""
    # Identify what the user is asking for
    query_type = identify_query_type(user_input)

    # Extract course name if mentioned
    course_name = extract_course_name(user_input)

    # Build appropriate query
    query = build_snowflake_query(query_type, course_name)

    if query:
        # Execute query
        results = execute_snowflake_query(query)

        if results:
            # Format and return results
            return format_query_results(query_type, results, course_name)
        else:
            return "No information found in the database."

    # If no specific query type identified, return general help
    return "I'm not sure what you're asking. You can ask about:\n• 📚 Available courses\n• 💰 Course fees\n• 🕐 Class schedules\n• 📖 Course duration"
