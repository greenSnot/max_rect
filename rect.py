import random

w=20
h=10

w=w+1
h=h+1

def show(arr):
    for i in range(1,h):
        for j in range(1,w):
            if arr[i][j]:
                print '\33['+str(30+arr[i][j])+'m#',
            else:
                print '\33[0m0',
        print('')

def min(a,b):
    if a<b:
        return a
    return b

def max(a,b):
    if a>b:
        return a
    return b

def gen_random(arr):
    for i in range(1,h):
        for j in range(1,w):
            arr[i][j]=int(random.random()*4)

def gen_max_square(arr):
    left=[([0]*w) for i in range(0,h)]
    top=[([0]*w) for i in range(0,h)]
    max_square=[([0]*w) for i in range(0,h)]

    for i in range(1,h):
        for j in range(1,w):
            if arr[i][j]:
                left[i][j]=left[i][j-1]+1
                top[i][j]=top[i-1][j]+1
                max_square[i][j]=min(max_square[i-1][j-1]+1,min(left[i][j],top[i][j]))
    return max_square

m=[([0]*w) for i in range(0,h)]
gen_random(m)

def gen_max_rect(arr):
    max_rect=[([0]*w) for i in range(0,h)]
    for i in range(h,0,-1):
        for j in range(w,0,-1):
            if arr[i][j]:
                max_rect[i][j]=9
    return max_rect

max_square=gen_max_square(m)
show(max_square)
print ''
show(gen_max_rect(max_square))
