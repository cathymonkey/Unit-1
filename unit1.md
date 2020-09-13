
![](image)
# Unit 1: An Electronic hardware store
## Criteria A: Planning
### Context of the problem
There is a hardware store in Karuizawa. This store is quite old,like 1000 years old. The owner, Mr.Sakamoto, wants to upgrade his accounting moment is kept on paper.He would like to have a software application that replaces the accounting book. Mr.Sakamoto got a new mac PC from his nephew and we would like to use it.

### Justification of the solution 
**Here we will write the design statement: what we will do, how, by when**

## Criteria B: Design
### System Diagram
![SystemDiagram](https://github.com/cathymonkey/Unit-1/blob/master/SystemDiagram.png)

### Flow Diagram

```
	from datetime import datetime
	import pytz

	JST = pytz.timezone("Asia/Tokyo")
	datetimeJST = datetime.now(JST)
	date = datetimeJST.strftime("Date: %Y.%m.%d. Time: %H:%M")
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

	times = 0
	while times < len(Items)+1:
		option =  int(input())
	
		if 0<option<5:
			times += 1
			print("Here is good to go.")
	
		elif option > 4:
			times += 1
			if times < 4:
	    		print("option is not valid, Try again")

			else:
	    		print("You have used up all the chances. Please wait.")
	    		break





