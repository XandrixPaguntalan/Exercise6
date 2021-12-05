inputNumber = input("Enter a number or press Enter to quit: ")
sum = 0
countOfNumbersEntered = 0
while inputNumber != "":
    enteredNumber = float(inputNumber)
    sum += enteredNumber
    countOfNumbersEntered += 1
    average = sum / countOfNumbersEntered
    inputNumber = input("Enter a number or press Enter to quit: ")
print("The sum is", sum)
print("The average is", average)