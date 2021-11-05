def calc_average(dictionary):
    sum = 0

    for mark in dictionary.values():
        sum += mark

    res = sum / len(dictionary)
    return res


myFinalMarks = {'CSF': 75, 'FunPro': 80, 'WT': 85}
print(calc_average(myFinalMarks))