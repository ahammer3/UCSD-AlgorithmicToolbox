# Uses python3
import sys
import collections

def fast_count_segments(starts, ends, points):
    count = [0] * len(points)
    #write your code here
    left, point_label, right = (1,2,3)
    
    point_map = collections.defaultdict(set)
    
    pairs = []
    
    for i in starts:
        pairs.append((i, left))
    for i in ends:
        pairs.append((i, right))
    for i in range(len(points)):
        point = points[i]
        pairs.append((point, point_label))
        point_map[point].add(i)
                     
    sorted_ = sorted(pairs, key=lambda x: (x[0], x[1]))
                     
    cover = 0
    for pair in sorted_:
        if pair[1] == left:
            cover += 1
        elif pair[1] == right:
            cover -= 1
        elif pair[1] == point_label:
            indice = point_map[pair[0]]
            for i in indice:
                count[i] = cover
    
    return count
                     

def naive_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    for i in range(len(points)):
        for j in range(len(starts)):
            if starts[j] <= points[i] <= ends[j]:
                cnt[i] += 1
    return cnt
                     

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[1]
    starts = data[2:2 * n + 2:2]
    ends   = data[3:2 * n + 2:2]
    points = data[2 * n + 2:]
    #use fast_count_segments
    cnt = fast_count_segments(starts, ends, points)
    for x in cnt:
        print(x, end=' ')
