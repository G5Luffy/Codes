from datetime import date , time , datetime

today = date.today()
now = datetime.now()
print("today's date is", today)
print("\nCurrent date and time is ", now)
print("n\Date cumponents", today.year , today.month , today.day)
