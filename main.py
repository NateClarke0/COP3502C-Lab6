# Nathaniel Austin-Clarke
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

    # encodes password by shifting all digits up by three
def main():
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
            try:
                print(f"The encoded password is {encoded_password}, and the original password is {password}.")
            except UnboundLocalError:
                print("Please enter a password to encode.\n")
                continue
        elif option == 3:
            break
        else:
            print("That is not an option.\n")
            continue


if __name__ == "__main__":
    main()
