def Roman_to_integer(string):
    Num_lib = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    string = 'MDLXX'
    result = 0
    numbers = []

    for i in range(len(string)):
        numbers.append(Num_lib[string[i]])

    print(numbers)

    for i in range(len(numbers)):
        if i == len(numbers) - 1:
            result += numbers[i]
        else:
            if numbers[i] >= numbers[i + 1]:
                result += numbers[i]
            else:
                result -= numbers[i]
    return result


if __name__ == '__main__':

    string = 'LVIII'
    result = Roman_to_integer(string)

    num = 1954
    string = str(num)
    numbers = []
    Num_lib = {1:'I',5: 'V',10: 'X',50: 'L',100: 'C',500: 'D',1000: 'M'}

    for i in range(len(string)-1, -1, -1):
        diff = num // 10**i
        latter = Num_lib[10**i]







