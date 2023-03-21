import os
from numpy import busday_offset
from holidays import Estonia
from datetime import date

PAYDAY = 10
REMINDER = 3
OUTPUT_FOLDER = 'output'


def export_csv(filename: str, data: list) -> None:
    """Write data into .csv file."""
    if not os.path.exists(OUTPUT_FOLDER):
        os.makedirs(OUTPUT_FOLDER)

    with open(f'{OUTPUT_FOLDER}/{filename}.csv', 'w') as file:
        file.write('\n'.join(data))


def get_paydays(year: int, holidays: list) -> list:
    """
    Return all paydays in specified year.
    If the payday falls on a weekend or holiday, the last day of work is returned.
    """
    paydays = [date(year, month, PAYDAY) for month in range(1, 13)]

    return busday_offset(paydays, 0, roll='backward', holidays=holidays)


def get_reminder(payday: date, holidays: list) -> date:
    """Return the date of the reminder set specified workdays in advance."""
    return busday_offset(payday, -REMINDER, roll='backward', holidays=holidays)


def get_combined(year: int) -> list:
    """Return the list with paydays and their respective reminder dates."""
    holidays = list(Estonia(year).keys())

    data = ['payday,reminder']  # table header

    for payday in get_paydays(year, holidays):
        data.append(f'{payday},{get_reminder(payday, holidays)}')

    return data


def run() -> str:
    """Main program."""
    year = input('Enter year: ')

    if not year.isnumeric():
        return 'Input must be number!'

    export_csv(year, get_combined(int(year)))
    return f'Success! Result stored in {OUTPUT_FOLDER}/{year}.csv'


if __name__ == '__main__':
    print(run())
