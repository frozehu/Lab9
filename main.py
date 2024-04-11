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

def decode(encoded_password):
    numbers = "0123456789"
    og_password = []
    for num in encoded_password:
        new_index = (numbers.index(num) - 3) % len(numbers)
        og_password.append(numbers[new_index])
    return ''.join(og_password)



if __name__ == '__main__':
    while True:
        print("Menu  \n------------- \n1. Encode \n2. Decode \n3. Quit")
        print()
        option = input("Please enter an option: ")
        if option == '3':
            break
        elif option == '1':
            password = input("Please enter your password to encode: ")
            encode(password)
            print("Your password has been encoded and stored!")
        elif option == '2':
            new_password = encode(password)
            decoded_password = decode(new_password)
            print(f"The encoded password is {new_password}, and the original password is {decoded_password}")
