import snowflake.connector

def connect_db():
    """Create a connection to Snowflake database"""
    conn = snowflake.connector.connect(
        user='Anchal',
        password='Anchalgothwal@1234',
        account='vvbadpg-le30326',  # Correct format: VVBADPG-LE30326
        warehouse='COMPUTE_WH',
        role='AI_CHATBOT_USER',
        database='COLLEGE_DB',
        schema='COLLEGE_SCHEMA'
    )
    return conn

def get_courses():
    """Fetch all available courses from Snowflake COURSES table"""
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("SELECT COURSE_NAME FROM COURSES ORDER BY COURSE_NAME")
    rows = cur.fetchall()
    courses = [row[0] for row in rows]
    cur.close()
    conn.close()
    return courses

def get_fee(course):
    """Fetch fees for a specific course from Snowflake COURSES table"""
    conn = connect_db()
    cur = conn.cursor()
    cur.execute(f"SELECT FEES FROM COURSES WHERE UPPER(COURSE_NAME) = '{course.upper()}'")
    row = cur.fetchone()
    cur.close()
    conn.close()
    
    if row:
        return f"₹{row[0]:,}"
    else:
        return "Fee information not available"

def get_duration(course):
    """Fetch course duration from Snowflake COURSES table"""
    conn = connect_db()
    cur = conn.cursor()
    cur.execute(f"SELECT DURATION FROM COURSES WHERE UPPER(COURSE_NAME) = '{course.upper()}'")
    row = cur.fetchone()
    cur.close()
    conn.close()
    
    if row and row[0]:
        return str(row[0])
    else:
        return "Duration not specified"

def get_schedule(course):
    """Fetch class schedule for a specific course from Snowflake SCHEDULE table"""
    conn = connect_db()
    cur = conn.cursor()
    cur.execute(f"SELECT CLASS_TIME FROM SCHEDULE WHERE UPPER(COURSE_NAME) = '{course.upper()}'")
    row = cur.fetchone()
    cur.close()
    conn.close()
    
    if row and row[0]:
        return str(row[0])
    else:
        return "Schedule not available"

def get_course_details():
    """Fetch all course details from COURSES table"""
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("SELECT COURSE_NAME, FEES, DURATION FROM COURSES ORDER BY COURSE_NAME")
    rows = cur.fetchall()
    
    course_details = []
    for row in rows:
        course_details.append({
            "name": row[0],
            "fees": f"₹{row[1]:,}",
            "duration": str(row[2]) if row[2] else "Not specified"
        })
    
    cur.close()
    conn.close()
    return course_details

def get_all_schedules():
    """Fetch all course schedules from SCHEDULE table"""
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("SELECT COURSE_NAME, CLASS_TIME FROM SCHEDULE ORDER BY COURSE_NAME")
    rows = cur.fetchall()
    
    schedules = {}
    for row in rows:
        schedules[row[0]] = str(row[1])
    
    cur.close()
    conn.close()
    return schedules

def get_all_courses_info():
    """Get formatted string of all courses with fees, duration, and schedule"""
    courses = get_course_details()
    schedules = get_all_schedules()
    
    if not courses:
        return "No course information available"
    
    info = "Here are all our courses:\n\n"
    for course in courses:
        schedule = schedules.get(course['name'], "Not specified")
        info += f"📚 {course['name']}\n"
        info += f"   💰 Fees: {course['fees']}\n"
        info += f"   📖 Duration: {course['duration']}\n"
        info += f"   🕐 Timing: {schedule}\n\n"
    
    return info