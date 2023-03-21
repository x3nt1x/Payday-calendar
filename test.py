from app import *

holidays = list(Estonia(2023).keys())


def test__get_paydays__correct_size():
    """Check if returns correct size."""
    assert len(get_paydays(2023, holidays)) == 12


def test__get_paydays__workday():
    """Check if returns 10th day when it's workday."""
    paydays = get_paydays(2023, holidays)

    assert paydays[0] == date(2023, 1, 10)  # Tuesday
    assert paydays[2] == date(2023, 3, 10)  # Friday
    assert paydays[3] == date(2023, 4, 10)  # Monday


def test__get_paydays__weekend():
    """Check if returns last day of work when weekend."""
    paydays = get_paydays(2023, holidays)

    assert paydays[5] == date(2023, 6, 9)  # Saturday
    assert paydays[8] == date(2023, 9, 8)  # Sunday


def test__get_paydays__holiday():
    """Check if returns last day of work when holiday."""
    paydays = get_paydays(2020, list(Estonia(2020).keys()))

    assert paydays[3] == date(2020, 4, 9)  # Good Friday


def test__get_reminder__mid_week():
    """Check if returns reminder 3 workdays in advance."""
    assert get_reminder(date(2023, 8, 10), holidays) == date(2023, 8, 7)
    assert get_reminder(date(2023, 3, 10), holidays) == date(2023, 3, 7)


def test__get_reminder__weekend_between():
    """Check if returns reminder 3 workdays in advance when weekend is in between."""
    assert get_reminder(date(2023, 1, 10), holidays) == date(2023, 1, 5)
    assert get_reminder(date(2023, 5, 10), holidays) == date(2023, 5, 5)


def test__get_reminder__holiday_between():
    """Check if returns reminder 3 workdays in advance when holiday is between."""
    assert get_reminder(date(2023, 4, 10), holidays) == date(2023, 4, 4)
    assert get_reminder(date(1977, 4, 10), list(Estonia(1977).keys())) == date(1977, 4, 4)


def test__get_combined__correct_size():
    """Check if returns correct size including header."""
    assert len(get_combined(2023)) == 13


def test__get_combined__has_header():
    """Check if first row is header."""
    data = get_combined(2023)

    assert data[0] == 'payday,reminder'


def test__get_combined__is_correct():
    """Check if combined data is correct."""
    data = get_combined(2023)

    assert data[1] == '2023-01-10,2023-01-05'
    assert data[3] == '2023-03-10,2023-03-07'
    assert data[4] == '2023-04-10,2023-04-04'


def test__export_csv__creates_folder_file():
    """Check if folder and file are created."""
    export_csv('2023', get_combined(2023))

    with open('output/2023.csv'):
        assert True


def test__export_csv__is_correct():
    """Check if outputted csv is correct."""
    export_csv('2023', get_combined(2023))

    with open('output/2023.csv') as file:
        assert file.read() == r"""payday,reminder
2023-01-10,2023-01-05
2023-02-10,2023-02-07
2023-03-10,2023-03-07
2023-04-10,2023-04-04
2023-05-10,2023-05-05
2023-06-09,2023-06-06
2023-07-10,2023-07-05
2023-08-10,2023-08-07
2023-09-08,2023-09-05
2023-10-10,2023-10-05
2023-11-10,2023-11-07
2023-12-08,2023-12-05"""


def test__run__invalid_input(monkeypatch):
    """Check if returns error when invalid input."""
    monkeypatch.setattr('builtins.input', lambda _: "test")

    assert run() == 'Input must be number!'


def test__run__correct_input(monkeypatch):
    """Check if returns success when correct input."""
    monkeypatch.setattr('builtins.input', lambda _: "2023")

    assert run() == 'Success! Result stored in output/2023.csv'
