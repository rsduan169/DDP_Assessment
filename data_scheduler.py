"""
Date Scheduler Function

Objective:
Write a function named 'date_passed' to determine the relationship between two dates.

Function Parameters:
1. todays_date (string): The current date in the format 'day Month'.
2. scheduled_date (string): The scheduled date to compare, in the same format.

Instructions:
- The function should compare todays_date and scheduled_date and print whether the scheduled date has passed, is yet to pass, or is today.
- Assume the dates are in the same year.
- The dates are in a format like '26th March'. Consider how to convert these for comparison.
- https://www.w3schools.com/python/python_datetime.asp

Example Test Cases:
1. date_passed('26th March', '25th March') should indicate that the scheduled date has passed.
2. date_passed('26th March', '26th March') should indicate that the scheduled date is today.
3. date_passed('26th March', '27th March') should indicate that the scheduled date is yet to pass.
"""

import re
from datetime import datetime

def date_passed(todays_date, scheduled_date):
    # Your code goes here
    # Implement the logic to compare the dates and print the appropriate message
    # pass  # Delete this after implementing some code inside this function


    # 将日期从 '26th March' 转换为 '26 March'
    def convert_date_format(date):
        return re.sub(r'(\d+)(st|nd|rd|th)', r'\1', date)

    # 转换日期格式以便比较
    todays_date = convert_date_format(todays_date)
    scheduled_date = convert_date_format(scheduled_date)

    # 定义日期格式
    date_format = "%d %B"

    # 将字符串日期转换为 datetime 对象进行比较
    todays_date = datetime.strptime(todays_date, date_format)
    scheduled_date = datetime.strptime(scheduled_date, date_format)

    # 比较日期并打印结果
    if todays_date > scheduled_date:
        return "The scheduled date has passed."
    elif todays_date < scheduled_date:
        return "The scheduled date is yet to pass."
    else:
        return "The scheduled date is today."

# Test cases
print(date_passed("26th March", "25th March"))  # Expected: Scheduled date has passed
print(date_passed("26th March", "26th March"))  # Expected: Scheduled date is today
print(date_passed("26th March", "27th March"))  # Expected: Scheduled date is yet to pass
