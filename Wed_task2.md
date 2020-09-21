**Question 1: Describe the four core computational thinking skills?**

1.Decomposition is to  break difficult problems into simple and easy-to-manage parts.

2.Pattern recognition is to find out the similarities between the problems you solved before and you are solving, coming up with the similar solutions to immediately solve the problems now.

3. Abstraction is to recognize the core of the problems.

4. Algorithmic thinking is to create a set of rules for the problems so that others can also solve them by following these rules.

**Question 2: What is the most powerful computer? Glad you asked. Watch this video about Sierra Computer. Describe below points that surprised you the most.**

Summit built by IBM in the U.S. is the most powerful computer in the world. Sierra is the second powerful one in the world.

Surprising points:
   i.  The supercomputer plays a significant role in the military than in other areas. It can model the changes and run the simulations to predict whether anything could break in a real-world detonation. People would like to  test the reliability of the stockpile of weapons by using this and expect the old weapons to be improved and become new weapons. “As long as there are nuclear weapons, we need supercomputers.”

   ii. Sierra will be “air gapped”, which means it will be completely cut off by any network and will be turning into a little island of processing power  while its operations will be classified.

**Question 3: Supercomputers are currently used to investigate solutions to real life problems from cancer research, Ai, economics, or brain simulation. Military uses are also one major force behind the development of these machines. Analyze the benefits and possible drawbacks of developing supercomputers in our modern world? Should we do it?**

Pros:
Can help ensure the reliability and safety of people’s life as supercomputers will simulate the possible activities of the weapons in the future.
Can reduce the waste of old weapons and reuse resources as supercomputers can do a lot of calculations and experiments in a short time to provide information that can help improve the old weapons and turn them into new ones.
Can strengthen the power of the weapons as supercomputers can model the  attacks to be more precisely and efficiently to attack the targets.

Cons:
Will create a certain amount of social panic as supercomputers are really useful and necessary to build the advanced weapons.

Cannot be commonly used by people because they take up a lot of space and require a lot of cost and a large amount of knowledge to build and operate.

**Question 4: Identify the most advanced computer in Japan (What, specs, location, uses). We might go and visit it :-)**

Fugaku supercomputer is located in Kobe, Japan. So far, it is the fastest computer in the world and its speed is 415 PFLOPS. The memory of it is HBM2 32GiB and its total bandwidth is up to 163PB/s.

“Our guiding strategy was to build a science-driven, low-powered machine that was easy to use and could run science and engineering applications efficiently,” says Toshiyuki Shimizu, principal engineer of Fujitsu’s Platform Development Unit. 
"Full Page Reload". IEEE Spectrum: Technology, Engineering, And Science News, 2020, https://spectrum.ieee.org/tech-talk/computing/hardware/japans-fugaku-supercomputer-is-first-in-the-world-to-simultaneously-top-all-high-performance-benchmarks.

Fugaku is scheduled to start fully  operating in 2021. Although it hasn’t been installed completely, it has run the simulations of coronavirus and predictions in environmental changes. 

In a school there are 2400 students and each student uses one locker. Each locker has a unique number from 1 to 2400. The lockers are to be painted in four colours: red, white, yellow and blue, in order of locker numbers, as shown in the following [table](https://docs.google.com/document/d/1_bGPdvLZNzLIBHB2IduZxIlA2ecajslQJBbAT0tsx-c/edit)

The pattern of colours continues in this manner. For example, locker number 15 will be painted yellow.
**Task 1: Create a program that shows the colors of all the lockers from 1 to 2400**
```.py
color = ["red","white","yellow","blue"]
for i in range(1, 2401):
   print(i,color[i%4-1])
 ```

**Task 2: Using the program above, create another program that allows the user to enter a number and the program outputs the color that should be used in the locker.**
```.py
n = int(input("Please enter a number of the locker: "))
for i in range(4):
    if (n-1) % 4 == i:
        print(f"The color is {color[i]}.")
 ```
 **Task 3: Create a program that receives a color from the user, validates the input,  and outputs the numbers of the lockers of the color provided.**
 ```.py
 while col in color:
    numbers = []
    for n in range(1,5):
        if color.index(col)+1 == n:
            while 0 < n < 601:
                for n in range(n,2401,4):
                    numbers.append(n)
                print(f"The {col} locker numbers are {numbers}")

    break
```










