''' The code calculates how many USB sticks a girl can purchase with a budget of £50, where each USB stick costs £6.
It then determines the amount of money she will have remaining and prints this information. '''

budget = 50
usb_stick_cost = 6
num_usb_sticks = budget // usb_stick_cost
money_left = budget % usb_stick_cost
print(f"She can buy {num_usb_sticks} USB sticks and will have £{money_left} left.")