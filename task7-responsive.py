def get_input():
    new_dict = dict()
    n = int(input("Number of exams: "))

    for i in range(n):
        print("\n*** Iteration " + str(i+1) + " ***")
        new_key = input("Name of Module: ")

        value_flag = False
        while not value_flag:
            new_value = int(input("Your mark (0-100): "))
            if new_value >= 0 and new_value <= 100:
                value_flag = True
            else:
                print("Incorrect! Try again...")

        new_dict[new_key] = new_value

    return new_dict

def calc_average(dictionary):
    sum = 0

    for mark in dictionary.values():
        sum += mark

    res = sum / len(dictionary)
    return "\nYour total average: " + str(round(res,1))


myFinalMarks = get_input()
print(calc_average(myFinalMarks))