inventory = ['butter' , 'tomato' , 'green beans' , 'chicken' , 'italian herbs' , 'garlic']
print("Welcome to inventory program")
item = input('Enter the item you want to check')
if item in inventory :
	print("Yes we fucking have that")
else:
	print("no , we don't have ",item)
