def convert_to_24_hour(hour, minute, period):
    # Check if it's in the AM period
    if period.lower() == "am":
        # If it's 12:00 AM, convert to 24-hour as 00:00
        if hour == 12:
            hour = 0
    elif hour != 12:
        hour += 12

    return f"{hour:02d}{minute:02d}"

# Real time Example 
time_1 = convert_to_24_hour(12, 30, "am")
time_2 = convert_to_24_hour(22, 30, "pm")

# Display the results
print(time_1)  
print(time_2)  
