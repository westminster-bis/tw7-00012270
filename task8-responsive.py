def get_input():
    new_dict = dict()

    n = 0
    value_flag = False
    while not value_flag:
        n = int(input("Number of exams: "))
        if n > 0 and n <= 8:
            value_flag = True
            print("You inserted " + str(n) + " modules")
        else:
            print("Incorrect! Try again...")

    for i in range(n):
        print("\n*** Module " + str(i+1) + " ***")
        new_key = input("Name of Module: ")
        new_dict[new_key] = final_mark()
    return new_dict

def final_mark():
    marks = []
    weights = []
    new_value = 0

    iterator_flag = False
    while not iterator_flag:
        iterator = int(input("Number of Components (1-3): "))
        if iterator >= 1 and iterator <= 3:
            iterator_flag = True
        else:
            print("Incorrect! Try again...")

    for i in range(iterator):
        print("Component " + str(i+1) + ": ")
        input("Name of Component: ")

        mark_flag = False
        while not mark_flag:
            marks.append(int(input("Your mark (0-100): ")))
            if marks[i] >= 0 and marks[i] <= 100:
                mark_flag = True
            else:
                print("Incorrect! Try again...")

        weight_flag = False
        while not weight_flag:
            weights.append(int(input("Weight (1%-100%): ")))
            if weights[i] >= 0 and weights[i] <= 100:
                weight_flag = True
            else:
                print("Incorrect! Try again...")

    for i in range(iterator):
        new_value += marks[i] * weights[i] / 100
    return new_value

def calc_average(dictionary):
    sum = 0

    for mark in dictionary.values():
        sum += mark

    res = sum / len(dictionary)
    return "\nYour total average: " + str(round(res,1))


myFinalMarks = get_input()
print(calc_average(myFinalMarks))