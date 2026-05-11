import time

while True:
    try:
        a = int(input('Enter first number: '))
        b = int(input('Enter second number: '))
        c = input('Enter operation: ')

        if c == '+':
            answer = a + b
        elif c == '-':
            answer = a - b
        elif c == '/':
            if b != 0:
                answer = a / b
            else:
                print('Error: Cannot divide by 0!')
                break
        elif c == '*':
            answer = a * b
        elif c == '**':
            answer = a ** b
        else:
            print('Invalid Syntax!')
            break
        print("Calculating...")
        time.sleep(1)
        print(f'Result: {answer}')

        z = input('Type [q] to quit or enter to continue: ').lower()

        if z == 'q':
            print('Bye! Shutting down!')
            time.sleep(1)
            break
        else:
            continue
    except ValueError:
        print('Please enter valid inputs!')