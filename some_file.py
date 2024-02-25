print('This is a file from GitHub repository')


print('These are new local changes')

def another_some_function(number: int | float | complex = 0) -> None:
    return number * 5

print(another_some_function(3))