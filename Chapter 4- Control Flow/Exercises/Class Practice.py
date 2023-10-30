'''Price = float(input("Enter price : "))
item = 0
if Price > 1000 :
    item = "Expensive"
else:
    item = "Affordable"
print("Your item : "+str(item))'''

'''# Nested Decision Structure
price = int(input("Enter price of item : "))
calories = float(input("Enter calories of item : "))

if price <=1000:
 if calories <=500:
        print("The item is affordable and healthy.")
 else :
        print("The item is affordable but not healthy.")
else :
        print("The item is expensive.")'''

percentage = float (input("Enter the calories of your item : "))
if percentage >= 2000 :
    print("Your item is too heavy of a meal.")
elif percentage >= 1500 :
        print("Your item is a heavy meal")
elif percentage >= 1000 :
        print("Your item is a average meal.")
elif percentage >= 500 :
        print("Your item is a light meal.")
elif percentage >= 100 :
        print("Your item is a snack.")
else :
       print("Your item is too small.")