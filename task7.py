myFinalMarks = {'CSF': 75, 'FunPro': 80, 'WT': 85}
sum = 0

for mark in myFinalMarks.values():
    sum += mark

res = sum / len(myFinalMarks)
print("Your average mark: " + str(res))