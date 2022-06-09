

if __name__ == '__main__':

    # Num_lib = {'I': 1, }
    Roman_numbers = ['I', 'V', 'X', 'L', 'C', 'D', 'M']

    string = 'LVIII'
    result = 0

    for item in Roman_numbers:
        pass

    while len(string) > 0:
        if string[0] == 'M':
            if string[1] != 'M':
                result += 1000
                string = string[1:]
            elif string[1] == 'M':
                if string[2] == 'M':
                    result += 3000
                    string = string[3:]
                else:
                    result += 2000
                    string = string[2:]
        elif string[0] == 'D':
            if string[1] != 'C':
                result += 500
                string = string[1:]
            elif string[1] == 'C':
                if string[2] == 'C':
                    if string[3] == 'C':
                        result += 800
                        string = string[4:]
                    else:
                        result += 700
                        string = string[3:]
                else:
                    result += 600
                    string = string[2:]
        elif string[0] == 'C':
            pass



