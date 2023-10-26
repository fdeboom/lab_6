def encoder(password):  # encodes password by adding 3 to each digit
    for i in len(password):
        password[i] = str(int(password[i]) + 3)
    return password


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    encoder("123456")
