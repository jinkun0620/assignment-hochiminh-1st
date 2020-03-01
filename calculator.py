def sum(a,b) : 
    return a+b

def sub(a,b) : 
    return a-b

def mul(a,b) :
    return a*b

def div(a,b) :
    return a/b

while True:
    operation = int(input("Please selcect operation \n1. Add \n2. Subtract \n3. Multiply \n4. Divide \n\n Select Operations from 1,2,3,4 : "))
    if operation == 1: 
        print("You chose add cal")
        firstNum = int(input('Enter your first number: '))
        secondNum = int(input('Enter your second number: '))
        result = sum(firstNum,secondNum)
        print('The result is %f'%result)

    elif operation == 2: 
       print("You chose subtraction cal") 
       firstNum = int(input('Enter your first number: '))
       secondNum = int(input('Enter your second number: '))
       result = sub(firstNum,secondNum)
       print('The result is %f'%result)

    elif operation == 3:
       print("You chose multiplication cal") 
       firstNum = int(input('Enter your first number: '))
       secondNum = int(input('Enter your second number: '))
       result = mul(firstNum,secondNum)
       print('The result is %f'%result)

    elif operation == 4:
      print("You chose division cal") 
      firstNum = int(input('Enter your first number: '))
      secondNum = int(input('Enter your second number: '))
      result = div(firstNum,secondNum)
      print('The result is %f'%result)

    else:
      print("You typed wrong number! Please choose the number from 1 to 4.")