from datetime import timedelta,datetime
def add(moment):
    delta = timedelta(seconds=1_000_000_000)
    result = moment + delta
    return result
