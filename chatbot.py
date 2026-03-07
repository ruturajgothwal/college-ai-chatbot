from database import get_courses, get_fee

def get_response(user_input):

    text = user_input.lower()

    if "course" in text:

        courses = get_courses()

        return "Available courses: " + ", ".join(courses)

    elif "fee" in text:

        if "bca" in text:
            fee = get_fee("BCA")
            return f"BCA fees is {fee} per year"

        elif "bba" in text:
            fee = get_fee("BBA")
            return f"BBA fees is {fee} per year"

        elif "mba" in text:
            fee = get_fee("MBA")
            return f"MBA fees is {fee} per year"

        else:
            return "Please specify course name"

    elif "schedule" in text or "timing" in text:

        return "Classes run Monday to Friday between 9 AM and 3 PM."

    elif "admission" in text:

        return "You can apply through the college admission portal."

    elif "hello" in text or "hi" in text:

        return "Hello student, how can I help you?"

    else:

        return "Sorry I didn't understand. Ask about courses, fees, or admission."