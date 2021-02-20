#Singlton Class
print("***************Singlton class***************")
import functools
def singleton(cls):
    @functools.wraps(cls)
    def wrapper(*args,**kwargs):
        if not wrapper.instance:
            wrapper.instance=cls(*args,**kwargs)
        return wrapper.instance
    wrapper.instance=None
    return wrapper
@singleton
class one:
    pass
first=one()
second=one()
print(first is second)

#**************Passin ARgument in Decorater****************
print("\n **************Passin ARgument in Decorater****************")
import functools
def repeat(num):
    def decorator_repeat(fun):
        @functools.wraps(fun)
        def wrapper(*args, **kwargs):
            for _ in range(num):
                value=fun(*args, **kwargs)
            return value
        return wrapper
    return decorator_repeat
@repeat(num=5)
def function(name):
    print(f"{name}")
function("Shubham")
