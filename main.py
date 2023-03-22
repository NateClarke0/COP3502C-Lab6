def encoder(password):
    encoded_password_list = []
    for number in password:
        number = int(number)
        if number >= 7:
            encoded_password_list.append((number + 3) % 10)
        else:
            encoded_password_list.append(number + 3)
    encoded_password = "".join(str(num) for num in encoded_password_list)
    return encoded_password


def decode(encoded_password):
    password = ''
    for digit in encoded_password:
        new_digit = int(digit) - 3
        if new_digit < 0:
            new_digit += 10
        password += str(new_digit)
    return password


def main():  # encodes password by shifting all digits up by three
    password = 'none'
    encoded_password = 'none'
    while True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")

        option = int(input("\nPlease enter an option: "))

        if option == 1:
            password = int(input("Please enter your password to encode: "))
            encoded_password = encoder(str(password))
            print("Your password has been encoded and stored!\n")
        elif option == 2:
            if encoded_password != 'none':
                password = decode(str(encoded_password))
            print(f'The encoded password is {encoded_password}, and the original password is {password}.')
            print()
        elif option == 3:
            break
        else:
            print("That is not an option.\n")
            continue


if __name__ == "__main__":
    main()
