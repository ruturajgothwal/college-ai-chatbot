#!/usr/bin/env python3
"""
Test script for database functions
"""

from database import connect_db, get_courses, get_fee, get_schedule, get_duration

print('=== Testing Database Functions ===')
print()

# Test database connection (will fail but should handle gracefully)
try:
    conn = connect_db()
    print('✅ Database connection successful')
    conn.close()
except Exception as e:
    print(f'⚠️  Database connection failed (expected): {str(e)[:50]}...')

print()

# Test individual functions (should return mock data)
print('Testing get_courses():')
try:
    courses = get_courses()
    print(f'✅ Courses: {courses}')
except Exception as e:
    print(f'❌ Error: {e}')

print()
print('Testing get_fee("BCA"):')
try:
    fee = get_fee('BCA')
    print(f'✅ BCA Fee: {fee}')
except Exception as e:
    print(f'❌ Error: {e}')

print()
print('Testing get_schedule("MBA"):')
try:
    schedule = get_schedule('MBA')
    print(f'✅ MBA Schedule: {schedule}')
except Exception as e:
    print(f'❌ Error: {e}')

print()
print('Testing get_duration("BBA"):')
try:
    duration = get_duration('BBA')
    print(f'✅ BBA Duration: {duration}')
except Exception as e:
    print(f'❌ Error: {e}')

print()
print('=== All Tests Completed ===')