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

**Question 3: Watch the video showing the market share for the most popular Operating Systems during the last years (#2). Describe the trends shown in the graph**
The most popular OS during the last years:

Windows(different versions):
Win XP: 2003.11 - 2011.07 
Win 7: 2011.07 - 2017.04
Win 10: 2017.04 - 2019.07(or maybe till now)

Windows OS has been the most popular operating system in the market for many years and it’s about 60%-80% of the total market. According to the data now, windows 
will still remain the first for a long time unless there are new and better operating systems entering the market.  Mac OS is now the most potential operating 
system to catch up with windows. Also, when there is an updated version of windows, people will usually gradually forgo the previous one and use the new one, which 
makes sense.

**Question 4: Identify the original creators of the Operating Systems in video #2. Add the citations for your sources.**
Mac OS: Steve Job 
("Macintosh By Apple - Complete History Of Mac Computers". History-Computer.Com, 2020, https://history-computer.com/ModernComputer/Personal/Macintosh.html. Accessed 2 Oct 2020.)

Linux: Linux Torvalds 
("TECHNOLOGY; Creator Of Linux Defends Its Originality". Nytimes.Com, 2020, https://www.nytimes.com/2003/12/23/business/technology-creator-of-linux-defends-its-
originality.html#:~:text=Linus%20Torvalds%2C%20creator%20of%20the,a%20Utah%20company%20has%20contended. Accessed 2 Oct 2020.)

Windows: Bill Gates
("From Windows 1 To Windows 10: 29 Years Of Windows Evolution". The Guardian, 2020, https://www.theguardian.com/technology/2014/oct/02/from-windows-1-to-windows-
10-29-years-of-windows-evolution. Accessed 2 Oct 2020.)

Chrome OS: Jeff Nelson
(Vaughan-Nichols, Steven. "The Secret Origins Of Google's Chrome OS | Zdnet". Zdnet, 2020, https://www.zdnet.com/article/the-secret-origins-of-googles-chrome-
os/#:~:text=Jeff%20Nelson%2C%20a%20former%20Google,%2C%20granted%20later%2C%20for%20network%2D. Accessed 2 Oct 2020.)
**programming task**  
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
**[HL] Task: Pick one of the OS in the list above (or any other you find which is open source), download it, and install it in your computer using a Virtual 
Machine (Tutorial Here). Prepare 3 Slides with your experience, plus you will show us the operating system running and some interesting software applications 
included, check the games and office applications. Enjoy!**


