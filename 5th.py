# Move all negative numbers to beginning and positive to end with constant extra space

def move(Arr):
    Arr.sort()
Arr=[-23,-43,32,4,2,-90,-65,10,-10]
move(Arr)
for e in Arr:
    print(e , end=" ")  # isse [ ] hat jayega !