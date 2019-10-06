def tower_of_hanoi(height,left='left',right='right',middle='middle'):
    if height:
        tower_of_hanoi(height-1,left,middle,right)
        print("{} => {} ".format(left,right))
        tower_of_hanoi(height-1,middle,right,left)

tower_of_hanoi(3)