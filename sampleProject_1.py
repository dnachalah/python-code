print("Hello and welcome to an interface that'll print both the odd and even numbers in any range you give for you")
start = int(input("Enter the starting range: "))
end = int(input("Enter the ending range: "))


while True:
    option = str(input("Enter the letter 'o' if you would like to print odd numbers or enter the letter 'e' if you would like to print even numbers or enter the letter 'x' to end: "))
    if option == 'o' or option == 'O' or option == 'e' or option == 'E' or option == 'x' or option == 'X':
        if option == 'o' or option == 'O':
            print("The odd numbers between " + str(start) + " and " + str(end) + " are:")

            for num in range(start, end + 1):
                if num % 2 != 0:
                    print(num)

        elif option == 'e' or option == 'E':
            print("The even numbers between " + str(start) + " and " + str(end) + " are:")
            
            for num in range(start, end + 1):
                if num % 2 == 0:
                    print(num)
        elif option == 'x' or option == 'X':
            break
                        
    else:
        option = str(input("Enter the letter 'o' if you would like to print odd numbers or enter the letter 'e' if you would like to print even numbers or enter the letter 'x' to end: "))
