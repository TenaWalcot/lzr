a=input("enter your name:")
a=str(a)
print('\n'.join([''.join([(a[(x-y)%len(a)] if ((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3<=0 else ' ')for x in range(-30,30)])for y in range(30,-30,-1)]))
input()