import nltk
import random
from database import get_courses,get_fees

nltk.download('punkt')

def get_response(user_input)

    user_input = user_input.lower()

    if course in user_input

        courses = get_courses()

        return Available courses are  + , .join(courses)

    elif fee in user_input

        if bca in user_input
            fee = get_fees(BCA)
            return fBCA fees is {fee} per year

        if bba in user_input
            fee = get_fees(BBA)
            return fBBA fees is {fee} per year

    elif schedule in user_input or timing in user_input

        return Classes run Monday to Friday between 9 AM to 3 PM

    elif admission in user_input

        return Admission form is available on college website.

    elif hello in user_input or hi in user_input

        return Hello student, how can I help you

    else

        return Sorry I didn't understand. Please ask about courses or fees.