#Noah Lunberry COP3502C
def encode(unencoded):
    # Noah Lunberry COP3502C
    templist = list(unencoded)
    newlist = []
    for i in templist:
        encoded_char = str((int(i) + 3) % 10)  # ensure the result is within the digit range (0-9)
        newlist.append(encoded_char)

    return ''.join(newlist)

# August McDaniel COP3502C
def decode(encoded_password):
    templist = list(encoded_password)
    newlist = []
    for i in templist:
        encoded_char = str((int(i) - 3) % 10)
        newlist.append(encoded_char)
    return ''.join(newlist)


def main():
    x = True
    encoded_password = None
    while x:
        print('Menu')
        print('-------------')
        print('1. Encode')
        print('2. Decode')
        print('3. Quit')
        print()
        choice = int(input('Please enter an option: '))

        if choice == 1:
            unencoded = input('Please enter your password to encode: ')
            encoded_password = encode(unencoded)
            print('Your password has been encoded and stored!')
            print()
        elif choice == 2:
            decoded_password = decode(str(encoded_password))
            print(f'The encoded password is {encoded_password}, and the original password is {decoded_password}.')
        elif choice == 3:
            x = False


if __name__ == '__main__':
    main()