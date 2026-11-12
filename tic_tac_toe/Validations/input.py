def input_number(message="entr a number:"):
    while True:
        try:
            input_num=input(message)

            input_number=int(input_num)
            if input_number < 10 and input_number > 0:
                return input_number
            print("The number must be between 1 and 9!")

        except ValueError:
            print("Please enter a number!")




