#Uses python3
import sys
import math

def minimum_distance(x, y):
    #write your code here
    points = sorted(list(zip(x,y)), key=lambda x: x[0])
   
    return math.sqrt(minimum(points))
   
   
def minimum(points):
    n = len(points)
    if n <= 3:
        x, y = [list(t) for t in zip(*points)]
     
        return minimum_small(x, y)
     
    mid = n // 2
    
    d1 = minimum(points[:mid])
    d2 = minimum(points[mid:])
    d12 = min(d1,d2)
    
    midpoint = [p for p in points if abs(points[mid][0] - p[0]) < d12]
    d = check_mid(midpoint, d12)
    
    return d
   
   
def check_mid(points, d):
    min_dist = d
    n = len(points)
    points = sorted(points, key=lambda x: x[1])
    for i in range(n-1):
        p1 = points[i]
        for j in range(i+1, min(i+9, n)):
            p2 = points[j]
            dist = (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2
          
            if dist < min_dist:
                min_dist = dist
             
    return min_dist
   
   
def minimum_small(x, y):
    points = list(zip(x, y))
    min_dist = 10 ** 18
    for i in range(len(points) - 1):
        p1 = points[i]
        for j in range(i+1, len(points)):
            p2 = points[j]
            dist = (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2
            
            if dist < min_dist:
                min_dist = dist
              
    return min_dist       
     

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(minimum_distance(x, y)))
