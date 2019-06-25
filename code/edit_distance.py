# Uses python3
def edit_distance(s, t):
    #write your code here
    res = [[x for x in range(len(s) + 1)] for y in range(len(t) + 1)]
   
    for y in range(len(t) + 1):
        res[y][0] = y
      
    for i in range(1, len(s) + 1):
        for j in range(1, len(t) + 1):
            insert = res[j-1][i] + 1
            delete = res[j][i-1] + 1
            match = res[j-1][i-1]
            mismatch = res[j-1][i-1] + 1
            
            if s[i-1] == t[j-1]:
                res[j][i] = min(insert, delete, match)
            else:
                res[j][i] = min(insert, delete, mismatch)
              
    return res[len(t)][len(s)]

   
if __name__ == "__main__":
    print(edit_distance(input(), input()))
