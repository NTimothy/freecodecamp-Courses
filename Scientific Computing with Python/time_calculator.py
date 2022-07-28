# https://replit.com/github/freeCodeCamp/boilerplate-time-calculator
def add_time(start, duration, weekday=""):
  _now = start.split(":")
  print(_now)
  current_time = {
    "day": "",
    "hour": int(_now[0]),
    "minute": int(_now[1][:2]),
  }
