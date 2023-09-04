import time

def countdown_decorator(func):
    def wrapper(*args, **kwargs):
        for i in range(3, 0, -1):
            print(i)
            time.sleep(1)
        return func(*args, **kwargs)
    return wrapper

@countdown_decorator
def what_time_is_it_now():
    return time.strftime('%H:%M')

result = what_time_is_it_now()
print(result)