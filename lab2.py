#COMP1127
#Lab 2
#Joel Wilson
#620091836
#October 31, 2022

# -----------------------------------------------------------------------------------------------
# Question 1
# -----------------------------------------------------------------------------------------------
def days_in_month(name_of_month):
    """Function  takes a month as an argument and finds the
    corresponding month in the month_days list and returns the list with the number of days
    associated with that month."""
    month_days = [('January', [31]), ('February', [28, 29]), ('March', [31]),
                  ('April', [30]), ('May', [31]), ('June', [30]), ('July', [31]), ('August', [31]),
                  ('September', [30]), ('October', [31]), ('November', [30]), ('December', [31])]

    for n in month_days:
        if n[0] == name_of_month:
            return n[1]

# -----------------------------------------------------------------------------------------------
# Question 2
# -----------------------------------------------------------------------------------------------
def day_of_week(d, m, y):
    """Function  which displays the day name for a given date supplied
        in the form (day,month,year). """

    day_names = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    if m < 3:
        m += 12
        y -=1

    return day_names[int((((13 * m + 3) // 5 + d + y + (y / 4) - (y // 100) + (y // 400)) % 7))]

# -----------------------------------------------------------------------------------------------
# Question 3
# -----------------------------------------------------------------------------------------------
def unlucky(y):
    """Function which returns all the days in a
    given year which have the date Friday 13th"""

    return [(d,m,y) for m in range(1,13) for d in range(1,32)  if (d == 13) and day_of_week(d, m, y) == 'Friday']


# -----------------------------------------------------------------------------------------------
# Question 4
# -----------------------------------------------------------------------------------------------
def mostUnlucky(start, end):
    """Function which lists all the years between a given start year and
        end year e.g. years 0 and 2010 which have 3 unlucky days"""

    unlucky_years = []

    for i in range(start, end+1):
        if len(unlucky(i)) >= 3:
            unlucky_years += [i]
    return unlucky_years

