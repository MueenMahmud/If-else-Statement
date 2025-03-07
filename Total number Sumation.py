
total_input = int(input('How many number you want to Addition: '))

coutn = 1;
total = 0.0 ;
while coutn <= total_input:
    number = float(input("Enter number " + str(coutn) +": "))
    total += number
    coutn +=1
print('Summation is : ', total)
