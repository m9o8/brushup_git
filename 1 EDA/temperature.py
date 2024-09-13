def c_to_f(celsius: int) -> float:
    fahrenheit = celsius * 9/5 + 32
    return fahrenheit
cel=15
print(c_to_f(15))

def input_validation() -> float:
    """Checks whether the user input is a number and convertible to a float.

    Returns:
        float: representing Celsius.
    """    
    while True:
        try:
            u_input = float(input("Please input some celsius to be converted: "))
            break
        except ValueError:
            print("Not an int or float - try again")
    
    return u_input

def c_to_f_better() -> float:
    celsius = input_validation()
    fahrenheit = celsius * 9/5 + 32
    return fahrenheit

print(c_to_f_better())