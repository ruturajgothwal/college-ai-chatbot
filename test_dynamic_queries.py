#!/usr/bin/env python3
"""
Test script to demonstrate the dynamic Snowflake query builder functionality
"""

from chatbot import get_dynamic_response, identify_query_type, extract_course_name, build_snowflake_query

def test_dynamic_queries():
    """Test the dynamic query building functionality"""

    test_questions = [
        "What courses do you offer?",
        "How much is BCA fee?",
        "What are the timings?",
        "How long is MBA?",
        "When are BBA classes?",
        "Tell me about fees",
        "Show me all courses",
        "What is the schedule for BCA?"
    ]

    print("🎯 Dynamic Snowflake Query Builder Test")
    print("=" * 50)

    for question in test_questions:
        print(f"\n❓ Question: {question}")

        # Show what the chatbot identifies
        query_type = identify_query_type(question)
        course_name = extract_course_name(question)
        query = build_snowflake_query(query_type, course_name)

        print(f"📋 Query Type: {query_type}")
        print(f"🏫 Course Name: {course_name}")
        print(f"🔍 SQL Query: {query}")

        # Show the response
        response = get_dynamic_response(question)
        print(f"💬 Response: {response[:100]}..." if len(response) > 100 else f"💬 Response: {response}")

        print("-" * 30)

if __name__ == "__main__":
    test_dynamic_queries()