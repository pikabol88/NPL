from calls_counter import CountCalls


@CountCalls
def puk():
    print("puk")


@CountCalls
def time_to_say(isGoodMood=True):
    if isGoodMood:
        print("Hello, world!")
    else:
        print("Goodbye, world!")


@CountCalls
def useless_function(isGoodMood=True):
    pass


if __name__ == '__main__':
    for i in range(5):
        puk()
    for i in range(2):
        time_to_say(True)
    for i in range(10):
        time_to_say(False)
    for i in range(255):
        useless_function()

    result = CountCalls.get_all_decorated_functions_calls()

    for key in result:
        print(f"The function {key} was called for {result[key]} times")
