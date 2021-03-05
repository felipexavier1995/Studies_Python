##### This calculator is for Studies on Language in Python #####
#####                Only simple calcculator               #####
def welcome():
    print('Welcome Calculator')

def finished():
    print('Tranks for user my aplication')

welcome()
number1 = int(input('Enter your first number:')) 
number2 = int(input('Enter your second number:'))

def calculate():
    operation = str(input('Please type in the math operation you would like to complete' 
                    ' [+] for addition'
                    ' [-] for subtraction'
                    ' [*] for multiplication'
                    ' [/] for division: ')
                    )
    if operation == '+':
        print('{} + {} = ' .format(number1,number2))
        print(number1 + number2)
    elif operation == '-':
        print('{} - {} = ' .format(number1,number2))
        print(number1 - number2)
    elif operation == '/':
        print('{} / {} = ' .format(number1,number2))
        print(number1 / number2)
    elif operation == '*':
        print('{} * {} = ' .format(number1,number2))
        print(number1 * number2)
    else:
        print('Operation invalid !')
    again()    
                
    
def again():
    calc_again = input('Do you to calculate again ? Please type Y or N: ')
    if calc_again.upper() == 'Y':
        calculate()
    elif calc_again.upper() == 'N':
        print('See you Later')
    else:
        again()       

calculate()  

finished()

  