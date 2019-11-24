month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

#year=int(input('Enter a year: '))

def is_leap(year):
    if year % 4 == 0:
        return '{} is Leap year'.format(year)
    else:
        return '{} in not Leap year'.format(year)

#print(is_leap(year))

def days_in_month(year, month):
    if year <= 9999:
        print(year)
    if month > 0 and month <= 12:
        print(month)
print(days_in_month(9999, 12))