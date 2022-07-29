"""
failed 3 tests
def test(num):
    # Personal Tests
    if num == 0:
        add_time("00:00 AM", "00:00")
        add_time("00:00 AM", "11:59")
        add_time("00:00 AM", "12:01")
        add_time("00:00 AM", "23:59")
        add_time("00:00 AM", "24:01")
        add_time("00:00 AM", "49:01")

    # Test Cases
    if num == 1:
        add_time("3:00 PM", "3:10")
        print("Returns: 6:10 PM")

        add_time("11:30 AM", "2:32", "Monday")
        print("Returns: 2:02 PM, Monday")

        add_time("11:43 AM", "00:20")
        print("Returns: 12:03 PM")

        add_time("10:10 PM", "3:30")
        print("Returns: 1:40 AM (next day)")

        add_time("11:43 PM", "24:20", "tueSday")
        print("Returns: 12:03 AM, Thursday (2 days later)")

        add_time("6:30 PM", "205:12")
        print("Returns: 7:42 AM (9 days later)")
"""

def clock_display(clock, days="", weekday="", case=0):
    hour, minute, mer = clock[0], clock[1], clock[2]
    if minute == 0:
        minute = str("00")
    elif 10>minute>0:
        minute = str("0")+str(minute)


    # Formats clock to desired test outputs
    _output = {
        0: f"{hour}:{minute} {mer}",
        1: f"{hour}:{minute} {mer} (next day)",
        2: f"{hour}:{minute} {mer}, {weekday}",
        3: f"{hour}:{minute} {mer}, ({days} days later)",
        4: f"{hour}:{minute} {mer}, {weekday} ({days} days later)"
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
    meridiem = meridiem.upper()
    period = {
        "AM": 0,
        "PM": 1
    }
    if not periods:
        return period.get(meridiem, "")
    elif periods:
        for key, value in period.items():
            if meridiem == value:
                return key


def simplify(time):
    calc = True
    time_passed = [0, 0, 0, 0]
    while calc:
        if time >= 1440:
            time -= 1440
            time_passed[3] += 1
        elif time >= 720:
            time -= 720
            time_passed[2] += 1
        elif time >= 60:
            time -= 60
            time_passed[0] += 1
        else:
            time_passed[1] = time
            calc = False

    return time_passed


def add_time(start, duration, weekday=""):
    # Separates hours/minutes/period/weekday
    time_start = start.split(":")
    time_add = duration.split(":")
    current_display = [int(time_start[0]), int(time_start[1][:2]), time_start[1][3:], weekday]

    # Check Raw Input
    # print("INPUT:",time_start, "(", weekday.capitalize(), ") +", time_add)

    # meridiem = what_period(str(time_start[1][2:]))

    duration_total = int(time_add[0])*60 + int(time_add[1])

    # Calculate needed changes to clock
    duration_simplified = simplify(duration_total)
    # print("SIMPLIFIED (hh|mm|mer|dd):", duration_simplified)

    current_display[2] = what_period(current_display[2])
    new_clock = [
        (current_display[0]+duration_simplified[0]),
        current_display[1]+duration_simplified[1],
        current_display[2]+duration_simplified[2]
        ]

    if new_clock[1] >= 60:
        new_clock[0] += 1
        new_clock[1] -= 60
        new_clock[2] += 1

    # print(new_clock)
    # print(current_display)
    if new_clock[0]> 12:
        new_clock[0] = (new_clock[0]%12)
        if current_display[2]==1:
            new_clock[2] +=1


    if new_clock[2] == 2 or new_clock[2] == 0:
        if new_clock[2] ==2:
            duration_simplified[3] += 1
        new_clock[2] = "AM"
    elif new_clock[2] > 2 or new_clock[2]==1:
        if new_clock[2] >2:
            duration_simplified[3] +=1
        new_clock[2] = "PM"
    if new_clock[0] == 0:
        new_clock[0] = 12

    case = 0
    if duration_simplified[3]>1 and not weekday == "":
        case=4
    elif duration_simplified[3]>1 and weekday == "":
        case=3
    elif duration_simplified[3]<1 and not weekday == "":
        case=2
    elif duration_simplified[3] == 1:
        case=1

    if not weekday == "":
        weekday = (what_day(weekday) + duration_simplified[3])%7
        weekday = what_day(weekday, True)


    return clock_display(new_clock,duration_simplified[3],weekday,case)

