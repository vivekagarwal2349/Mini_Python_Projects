#Tower of hanoi problem - recursive solution
#start:A
#spare:c
#target:B
#smallest disk is called 1
#nth disk is the largest
import sys
def tower(n):
    """Input: n, an integer"""
    try:
        n = int(n)
    except:
        print("Invalid input, try again!")
        sys.exit()
    if n <= 0:
        print("Invalid input, try again!")
        sys.exit()
    def move(n, fr, to):
        print("Move disk", n, "from tower", fr ,"to tower", to)

    def hanoi(n,fr,to,spare):
        """Input: n, number of disks
                  fr, start tower  (represented by "A")
                  to, target tower (represented by "B")
                  spare, spare tower (represented by "C")
            Output:
                Returns steps(in the form of a string) that need to be taken to solve this problem
        """
        if n==1:   #if you've got only one disk, just move it to the target tower
            move(1,fr,to)
        else:
            hanoi(n-1, fr, spare, to)
            move(n, fr, to)
            hanoi(n-1, spare, to, fr)
    hanoi(n,"A","B","C")
n = input("Enter a positive integer:")
tower(n)
