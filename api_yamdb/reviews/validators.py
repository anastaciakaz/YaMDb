import datetime as dt


def max_year_title(year):
    now_year = dt.date.today()
    if year > now_year.year:
        raise ValueError('Год не может быть больше текущего')
