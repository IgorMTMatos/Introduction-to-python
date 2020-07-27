def menu():
    print("\n\n\nMenu \n Choose an Option: \n1- Hello\n2-Goodbye\n0-Exit")
    optionChoosen = int(input("Opção: "))
    if optionChoosen == 1:
        print("Hello")
        menu()
    elif optionChoosen == 2:
        print("Goodbye")
        menu()
    elif optionChoosen == 0:
        print("Exiting...")


# menu()
