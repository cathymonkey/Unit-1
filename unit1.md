# Unit 1: An Electronic hardware store
## Criteria A: Planning
### Context of the problem
There is a hardware store in Karuizawa. This store is quite old,like 1000 years old. The owner, Mr.Sakamoto, wants to upgrade his accounting moment is kept on paper.He would like to have a software application that replaces the accounting book. Mr.Sakamoto got a new mac PC from his nephew and we would like to use it.

### Justification of the solution 
**Here we will write the design statement: what we will do, how, by when**

	from datetime import datetime

	date = datetime.today()
	print(f"Welcome to Mr.Sakamoto's store {date}")
	name = input("Hello user. Please enter your name: ")
	print(f"{name}")

	# basic menu of items
	print("\nThis is the basic menu.")
	print("\nItems")
	print("=" * 35)

	Items = list(["1.RAM", "2.CPU", "3.Motherboard", "4.GPU"])
	NumberOfItems = len(Items)
	Price = [1, 5, 5, 2]

	for i in range(NumberOfItems):
	
	    print(f"\n{Items[i]}".ljust(25, "."), f"{Price[i]} bitcoin")

	print(f"\nPlease enter your option[1-{NumberOfItems}]:")

	option = input()
	option = int(option)


	def inRange(x: int):  # check if the selection number is in range

	    if x > 0 and option < NumberOfItems + 1:
	    
		print("Yes,thank you. Please wait.")


	    else:
	    
		print("Try again. Your selection doesn't exist.")


	inRange(option)





































	




