
def format_answer(clock, days=0, day_given=False, case=0):
    hour, minute, mer, weekday = clock[0], clock[1], clock[2], clock[3]

    # Format Minutes Hand to String
    if minute == 0:
        minute = str("00")
    elif 10 > minute > 0:
        minute = str("0")+str(minute)

    if day_given:
        case += 3

    # Formats clock to desired test outputs
    _output = {
        0: f"{hour}:{minute} {mer}",
        1: f"{hour}:{minute} {mer} (next day)",
        2: f"{hour}:{minute} {mer} ({days} days later)",
        3: f"{hour}:{minute} {mer}, {weekday}",
        4: f"{hour}:{minute} {mer}, {weekday} (next day)",
        5: f"{hour}:{minute} {mer}, {weekday} ({days} days later)"
    }
    return _output.get(case, "")


def what_day(day, weekday=False):
    week = {
        "Sunday": 0,
        "Monday": 1,
        "Tuesday": 2,
        "Wednesday": 3,
        "Thursday": 4,
        "Friday": 5,
        "Saturday": 6,
        "": ""
    }
    if not weekday:
        day = day.lower().capitalize()
        return week.get(day, "")
    elif weekday:
        for key, value in week.items():
            if day == value:
                return key


def what_period(meridiem, periods=False):
    period = {
        "AM": 0,
        "PM": 1
    }
    if not periods:
        meridiem = meridiem.upper()
        return period.get(meridiem, "")
    elif periods:
        for key, value in period.items():
            if meridiem == value:
                return key


def military_time(clock, reverse=False):
    time = [0, 0]
    # Converts Standard Time into a Military Time and returns list in format [Hour, Minute]
    if not reverse:
        if clock[1] < 10:
            time = [str(clock[0] % 12 + what_period(clock[2]) * 12), "0" + str(clock[1])]
        else:
            time = [str(clock[0] % 12 + what_period(clock[2]) * 12), str(clock[1])]
    return time


def simplify(time):
    # Resets absolute time after 1 week (10080 minutes) has passed
    time = time % 10080

    # Determines what day of the week
    day = what_day(int(time/1440), True)

    # Determines clock values (Hour, Minute, Ante Meridiem)
    hour = int((time % 1440)/60)
    minute = time % 60
    meridiem = int(hour/12) % 2
    meridiem_txt = what_period(meridiem, True)
    if meridiem == 1:
        hour -= 12
        if hour == 0:
            hour += 12
    elif meridiem == 0 and hour == 0:
        hour += 12

    # print(f"{hour}:{minute} {meridiem_txt} on {day}")
    return [hour, minute, meridiem_txt, day]


def add_time(start, duration, weekday=""):
    case = 0
    # Separates hours/minutes/period/weekday
    time_start = start.split(":")
    time_add = duration.split(":")

    # Format current time into list [Hour, Minute, Ante meridiem]
    clock = [int(time_start[0]), int(time_start[1][:2]), time_start[1][3:], weekday]

    # Format time into military time [Hour, Minute, Ante meridiem]
    clock_military = military_time(clock)

    # FOR TESTING | print(f"CLOCK (Military): {clock_military[0]}{clock_military[1]} {weekday}")
    inputs = [int(clock_military[0]), int(clock_military[1]), weekday, int(time_add[0]), int(time_add[1])]

    # Absolute Time is a representational number for the exact Day/Hour/Time in any given week
    # Absolute Time = Current Hour + Current Minutes + Current Day
    # Absolute Time New = Current Hour + Current Minutes + Current Day + Added Hours + Added Minutes
    if not weekday == "":
        absolute_time = \
            (inputs[0]*60) \
            + (inputs[1]) \
            + (what_day(weekday)*1440)

        absolute_time_new = \
            (inputs[0]*60) \
            + (inputs[1]) \
            + (inputs[3]*60) \
            + (inputs[4]) \
            + (what_day(weekday)*1440)
        day_given = True
    else:
        absolute_time = \
            (inputs[0]*60) \
            + (inputs[1]) \

        absolute_time_new = \
            (inputs[0]*60) \
            + (inputs[1]) \
            + (inputs[3]*60) \
            + (inputs[4])
        day_given = False
        # weekday = "Sunday"

    clock_new = simplify(absolute_time_new)

    # Calculates total days passed from input
    days_passed = int(inputs[3]/24)

    # if PM -> AM, change format
    if ((absolute_time % 1440) >= 720 and (absolute_time_new % 1440 < 720)) or (days_passed == 1):
        case = 1

    # if PM -> AM and >1 day transition
    if inputs[3] >= 24 and inputs[4] > 0:
        case += 1
        days_passed += 1

    ans = format_answer(clock_new, days_passed, day_given, case)
    return ans
