'''Price = float(input("Enter price : "))
item = 0
if Price > 1000 :
    item = "Expensive"
else:
    item = "Affordable"
print("Your item : "+str(item))'''

# Nested Decision Structure
price = int(input("Enter price of item : "))
calories = float(input("Enter calories of item : "))

if price <=1000:
 if calories <=500:
        print("The item is affordable and healthy.")
 else :
        print("The item is affordable but not healthy.")
else :
        print("The item is expensive.")