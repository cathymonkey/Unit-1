**Task3: Operative System**
🤔 In this task, you will expand your understanding of Operating systems. The resources needed are:
[Operating Systems: Crash Course Computer Science #18](https://www.youtube.com/watch?v=26QPDBe-NB8&t=26s)

[Evolution of market dominion by most popular operating systems](https://www.youtube.com/watch?v=eJuvKn5j_kE)

**Question 1: Describe four roles of the Operating systems in a computer.**

   Intermediaries: Operating system is an interface between software  and hardware. Also it develops a software abstraction  through APIs called device drivers to    handle input and output and control the peripherals. 

   Multitasking: It allows one big batch to have many programs running simultaneously on a single computer.
   Memory management: OS system can  allocate each program its own  block of memory by using the method of “virtual memory”. Virtual memory allows programs to        have flexible memory sizes that appear to be continuous to them. It simplifies everything and offers tremendous flexibility to the OS in running multiple 
   programs simultaneously.

   Memory protection:  Operating systems  can protect memory from malwares or viruses, which means other processes who are not allocated to  before can’t access 
   the memory. 

**Question 2:  What did you find surprising from the video about the Operating systems (#1) Describe below your point:**
Surprising thing:
Virtual memory: Since the OS allows the computer to run multiple programs simultaneously on a single CPU, these programs then need to share time and memory of the 
computer, which can cause a problem when you want to extract specific memory as all the memory from different programs are mixed together. So, here comes  a 
solution -- “virtual memory”. This can make the memory that belongs to the same program in random sequence appear to be continuous, much easier to read the       
memory under the same program.Clever!

**Question 3: Watch the video showing the market share for the most popular Operating Systems during the last years (#2). Describe the trends shown in the graph.

   
```.py
    # Create a program that prints n numbers of the Fibonacci Series, where n is an integer entered by the user.
    n = int(input("Please enter a postive integer: "))
    start = 1
    fibonacci = []
    for i in range(n):
        while i < 2:
            fibonacci.append(1)
            break
        while i > 1:
            num = fibonacci[i-1]+fibonacci[i-2]
            fibonacci.append(num)
            break
    print(fibonacci)
```
