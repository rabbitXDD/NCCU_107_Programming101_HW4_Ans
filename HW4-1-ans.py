import datetime

# player name
name = input()

# player birthday
birth = input()

# player NBA beginning year
begin_year = int(input())

# player record achieving year
record_year = input()

# player average score rate
score = float(input())


def is_leap_year(year):
    """
    Check if given A.D. year is leap year or not.

    Args:
        year (int): The year we want to know whether is leap year.

    Returns:
        bool: The return value. True if year is leap year, False otherwise.

    """

    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0


def count_leap_year(from_year, to_year):
    """
    Check how many leap years are there between from_year and to_year(not contains to_year).

    Args:
        from_year (int): The begin year of the counting range.
        to_year (int): The end year of the counting range.

    Returns:
        int: The return value. Leap year counts between from_year and to_year.

    """

    count = 0
    for ele in range(from_year, to_year):
        if is_leap_year(ele):
            count += 1
    return count


# Change begin_year and birth into datetime objects
datetime_record = datetime.datetime.strptime(record_year, '%Y/%m/%d')
datetime_birth = datetime.datetime.strptime(birth, '%Y/%m/%d')

# Calculate days between two datetime object
total_days = (datetime_record - datetime_birth).days
# Count how many leap year between birthday date and record date
# Note the last year(record year) shouldn't count into the leap days.
leap_days = count_leap_year(datetime_birth.year, datetime_record.year)

# count total days without leap days
total_days = total_days - leap_days

# Note that if birthday year is leap year, but birthday month is after March,
# should not count into the leap days.
if datetime_birth.month > 3 and is_leap_year(datetime_birth.year):
    total_days += 1

# Total days
days = int(total_days % 365)
# Total years
years = int((total_days - days) / 365)

scores = score * 82 * (datetime_record.year - begin_year)
if 20000 <= scores < 25000:
    scores = '20,000'
elif 25000 <= scores < 30000:
    scores = '25,000'
elif 30000 <= scores < 35000:
    scores = '30,000'
else:
    scores = '35,000'
print(
    '{} became the player with {} career points at {} years and {} days.'.
    format(name, scores, years, days)
)
