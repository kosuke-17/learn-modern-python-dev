unm :int = 0
name :str = "John"
is_student :bool = True

def add_numbers(a: int, b: int) -> int:
    return a + b

def greet(name: str) -> str:
    return f"Hello, {name}!"

print(add_numbers("1", 2))
print(greet("John"))