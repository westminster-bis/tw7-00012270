csf = {
'cw1-weight': 0.4,
'cw1-mark':79,
'exam-weight':0.6,
'exam-mark':65
}

cw1 = csf.get('cw1-weight') * csf.get('cw1-mark')
exam = csf.get('exam-weight') * csf.get('exam-mark')

res = cw1 + exam
print("Your average mark: " + str(res))