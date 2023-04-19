charge=5000
age=int(input('How old are you?'))
if age<8:
    print('0')
elif 8<=age<60:
    print('5000')
else:
    print(charge*0.5)