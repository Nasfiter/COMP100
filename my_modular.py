def greet(name):
    return f'Hello, {name}!'

PI = 3.14159

class Calculator:
    def add(self, a, b):
        return a + b


cal = Calculator()


print(cal.add(a=5, b=6))

print(dir(cal))

help(Calculator)