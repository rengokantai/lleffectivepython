__author__ = 'Hernan Y.Ke'
def safe_division(number,divisior, *, ignore_overflow=False, ignore_zero_devision=False):
    try:
        return number/divisior
    except OverflowError:
        if ignore_overflow:
            return 0
        else:
            raise
    except ZeroDivisionError:
        if ignore_zero_devision:
            return float('inf')
        else:
            raise

print(safe_division(1.0,0,ignore_overflow=True, ignore_zero_devision=False))