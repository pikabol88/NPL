import functools


class CountCalls:
    decorated_functions_list = []

    def __init__(self, func):
        functools.update_wrapper(self, func)
        self.func = func
        self.num_calls = 0
        CountCalls.decorated_functions_list.append(self)

    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        #print(f"{self.num_calls} вызов функции {self.func.__name__!r}")
        return self.func(*args, **kwargs)

    @staticmethod
    def get_all_decorated_functions_calls():
        result = {}
        for el in CountCalls.decorated_functions_list:
            result[el.__name__] = el.num_calls
        return result