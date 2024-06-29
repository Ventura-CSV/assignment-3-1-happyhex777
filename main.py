import random


def main():
    number1 = random.randint(0, 100)
    number2 = random.randint(0, 100)
    number3 = random.randint(0, 100)
    """
    ########################################
    Code Your Program here
    ########################################
    """
    if number1<number2:
        if number1<number3:
            min_value=number1
        else:
            min_value=number3
    else:
        if number2<number3:
            min_value=number2
        else:
            min_value=number3
            
    print(number1,number2,number3)
    print(min_value)

    ########################################
    # Do not delete the return statement
    ########################################
    return number1, number2, number3, min_value


if __name__ == '__main__':
    main()
