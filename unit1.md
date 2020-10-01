
![](image)
# Unit 1: An Electronic hardware store
## Criteria A: Planning
### Context of the problem
There is a hardware store in Karuizawa. This store is quite old,like 1000 years old. The owner, Mr.Sakamoto, wants to upgrade his accounting moment is kept on paper.He would like to have a software application that replaces the accounting book. Mr.Sakamoto got a new mac PC from his nephew and we would like to use it.

### Justification of the solution 
**Here we will write the design statement: what we will do, how, by when**

we want to create a text based application that runs on a computer, which provides the functionality for the hardware store. The app should provide actions such as record of purchases, categorization of items, record of inventory, calculation of totals, billing. We will develop this app using python. We will use python because it is the software we are using in class at the moment. In comparison to C++ or C, python has a lean and simple syntax. In addition, python has become the most poplar programming language over the last years.[1] Similarly, python has a large repository of libaries and documentation.

T.E.L.O.S study

[1] "The 10 Most Popular Programming Languages To Learn In 2020". Northeastern University Graduate Programs, 2020, https://www.northeastern.edu/graduate/blog/most-popular-programming-languages/. 

## Criteria for Success
1. Provides clear feedback to the user
2.**There are no bugs in the application**
3. The application should allow to calculate the total and billing
4. Secure application: it allows user login/authentication


## Criteria B: Design
### System Diagram
![SystemDiagram](https://github.com/cathymonkey/Unit-1/blob/master/SystemDiagram.png)

### Flow Diagram
![FlowDiagram](https://github.com/cathymonkey/Unit-1/blob/master/FlowDiagram.png)


```.py
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
```

**Tax and total bills**
```.py

while True:
    bill = int(input("Please enter the total amount of(BTC): "))
    if bill< 0:
        print("The total cannot be negative. Try again.")
        break
    else:
        break
for i in range(4):
    if 250*i<bill<=250*(i+1):
        tax = 0.20 - 0.05 * i
    if bill > 1000:
        tax = 0.25
total = bill*(1+tax)
total = round(total,2)


row = 5
column = 50
def rect_draw(row,column):
    for i in range(row):
        for j in range(column):
            if i == 0 or i == row-1 or j == 0 or j == column-1:
                print("x",end = "")

            else:
                print(" ",end ="" )
        print()
rect_draw(row,column)

```
### Flow Chart for Encrytion
![encryption_flow](https://github.com/cathymonkey/Unit-1/blob/master/encryption_flow.png)
```
all_lines_db = open("database","r").readlines()

for line in all_lines_db:
    encrypted_line = ""
    shift = 2
    len_line = len(line)
    
    for L in range(len_line):
    	new_L = chr(ord(line[L]) + shift)
        encrypted_line += new_L
	
    print(encrypted_line)
    with open("encrypted_file","a") as wfile:
        wfile.write(encrypted_line+"\n")
	
```
### Figure 1. Computer  
![Computer](https://github.com/cathymonkey/Unit-1/blob/master/computer.jpg). *by Cathy, Isabel,Kien and Timur*

The computer we design consumes 1000w per hour which is much higher than usual. 



### Record for tasks


| Task No. | Planned Action                                                                                        | Planned outcome                       | Time finished  | Target Completion date | Criterion |
|----------|-------------------------------------------------------------------------------------------------------|---------------------------------------|----------------|------------------------|-----------|
| 1        | Planning: Discuss the context of the situation.(Ideally this is the first interview with your client) | Write the context of  the problem     | 15min          | Sep 11th               | A         |
| 2        | Development: Coded a text-based menu system for some parts in the hardware store                      | A working program that shows the menu | 80min          | Sep 18th               | D         |
| 3        | Design: Created a system-diagram and a flow-diagram for the menu system                               | An easy-to-follow flow diagram        | 20min          | Sep 15th               | B         |

## Criteria D: Functionality

## Criteria E: Evaluation
