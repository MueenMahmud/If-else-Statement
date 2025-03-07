rows = int(input('Enter your Rows: '))

# looping  in inputs add one is ruls
for i in range(1, rows + 1):
    print(" "*(rows - i),end="")
  
    print("*"*(2 * i - 1))
