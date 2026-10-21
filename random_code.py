user_input_number = input("What number do you want to convert to binary: ") 
divider = 2
reminder = 0
binary = ""

while int(user_input_number) > 0 :
    user_input_number = int(user_input_number) // divider
    reminder = int(user_input_number) % divider
    binary = str(reminder) + binary

print(f"Your number  in binary is {binary}")