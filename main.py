# This is Elizabeth's main.py file.

def encode(password):
    numbers = "0123456789"
    new_password = []
    for num in password:
        if num in numbers:
            new_index = (numbers.index(num) +3) % len(numbers)
            new_password.append(numbers[new_index])
        else:
            new_password.append()
    return ''.join(new_password)


if __name__ == '__main__':
    while True:
        print("Menu  \n------------- \n1. Encode \n2. Decode \n3. Quit")
        print()
        option = input("Please enter an option: ")
        if option == '3':
            break
        elif option == '1':
            password = input("Please enter your password to encode: ")
            print("Your password has been encoded and stored!")
