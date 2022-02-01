"""
Given a time in

-hour AM/PM format, convert it to military (24-hour) time.

Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
- 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock. 
""" 

def time_conversion(s):
    # First check if AM or Pm
    if s[-2:] == 'AM' and s[:2] == '12':
        return "00" +  s[2:-2]
    elif s[-2:] == 'AM':
        return s[:-2]
    elif s[-2:] == 'PM' and s[:2] == '12':
        return s[:-2]
    else:
        return str(int(s[:2]) + 12) + s[2:8]


def main():
    print(time_conversion("12:01:00PM")) # Expected 12:01
    print(time_conversion("12:01:00AM")) # Expected 00:01
    print(time_conversion("00:33:00PM"))  # Expected 17:33


if __name__ == "__main__":
    main()