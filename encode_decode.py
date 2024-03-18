'''Rachel Baryol
Lab 6: Software Engineering'''


# Rachel: function that asks user for password to encode and stores the encoded password to a new variable
def encode(password):
    encoded_password = ''

    # Encode password
    for char in password:
        new_char_int = int(char) + 3
        if new_char_int >= 10:
            new_char_int -= 10
        encoded_password += str(new_char_int)

    return encoded_password


def decode(password):
    # TODO: Blas writes decode function
    pass


def main():
    # Ask user for menu choice
    while True:
        print('\nMenu')
        print('-------------')
        print('1. Encode')
        print('2. Decode')
        print('3. Quit')

        try:
            choice = int(input('\nPlease enter an option: '))

            # 1. Encode
            if choice == 1:
                password = input("Please enter your password to encode: ")
                encoded_password = encode(password)
                print('Your password has been encoded and stored!')

            # 2. Decode
            elif choice == 2:
                decoded_password = decode(encoded_password)
                print(f'The encoded password is {encoded_password}, and the original password is {decoded_password}.')

            # 3. Quit
            elif choice == 3:
                break

            else:
                raise ValueError

        except ValueError:
            print('Invalid entry')
            continue



if __name__ == '__main__':
    main()