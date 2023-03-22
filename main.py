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

def menu():
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")

if __name__ == "__main__":
    while True:
        menu()
        option = int(input("\nPlease enter an option: "))
        if option == 1:
            password = int(input("Please enter your password to encode: "))
            password = encoder(str(password))
            print("Your password has been encoded and stored!\n")
        elif option == 2:
            #FIXME: Add decoder option.
            raise NotImplementedError
        elif option == 3:
            break