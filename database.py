import snowflake.connector

def connect_snowflake():

    conn = snowflake.connector.connect(
        user='Anchal',
        password='Anchalgothwal@1234',
        account='https://app.snowflake.com/vvbadpg/le30326',
        warehouse='COMPUTE_WH',
	ROLE = 'AI_CHATBOT_USER',
        database='COLLEGE_DB',
        schema='COLLEGE_SCHEMA'
    )

    return conn


def get_courses():

    conn = connect_snowflake()
    cur = conn.cursor()

    cur.execute("SELECT course_name FROM courses")

    rows = cur.fetchall()

    courses = [row[0] for row in rows]

    return courses


def get_fees(course):

    conn = connect_snowflake()
    cur = conn.cursor()

    cur.execute(f"SELECT fees FROM courses WHERE course_name='{course}'")

    result = cur.fetchone()

    if result:
        return result[0]

    return None