def get_month(date): ...
def get_quarter_number(date): ...
def get_quarter(date): ...
def get_fiscal_year(date, day: int = ..., month: int = ...): ...
def get_timedelta(qty, granularity): ...
def start_of(value, granularity): ...
def end_of(value, granularity): ...
def add(value, *args, **kwargs): ...
def subtract(value, *args, **kwargs): ...
def json_default(obj): ...
def date_range(start, end, step=...): ...
