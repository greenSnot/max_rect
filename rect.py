import random

W = 20
H = 20

W = W + 1
H = H + 1

def show(arr):
    for i in range(1, H):
        for j in range(1,W):
            if arr[i][j]:
                print '\33['+str(30+arr[i][j])+'m#',
            else:
                print '\33[0m0',
        print('')
    print ''

def min(a, b):
    if a < b:
        return a
    return b

def max(a, b):
    if a > b:
        return a
    return b

def gen_random(arr):
    for i in range(1, H):
        for j in range(1, W):
            arr[i][j] = int(random.random() * 4)

max_square_width = 0
def gen_max_square(arr):
    left = [([0] * W) for i in range(0, H)]
    top = [([0] * W) for i in range(0, H)]
    max_square = [([0] * W) for i in range(0,H)]

    global max_square_width
    for i in range(1, H):
        for j in range(1, W):
            if arr[i][j]:
                left[i][j] = left[i][j - 1] + 1
                top[i][j] = top[i - 1][j] + 1
                max_square[i][j] = min(max_square[i - 1][j - 1] + 1,min(left[i][j], top[i][j]))
                max_square_width = max(max_square_width, max_square[i][j]);
    return max_square

def gen_max_rect(arr):
    max_square = gen_max_square(arr)
    show(max_square)
    arr = max_square
    global max_rect_area
    global max_rect_width
    global max_rect_height
    max_rect = [([0] * W) for i in range(0, H)]
    for k in range(max_square_width, 1, -1):
        max_ = 0
        left = [([0] * W) for i in range(0, H)]
        top = [([0] * W) for i in range(0, H)]
        for i in range(1, H):
            for j in range(1, W):
                if arr[i][j] >= k :
                    left[i][j] = left[i][j - 1] + 1
                    top[i][j] = top[i - 1][j] + 1
                    area = (max(left[i][j], top[i][j]) + k - 1) * k
                    if area > max_rect_area :
                        max_rect_area = area
                        if left[i][j] > top[i][j]:
                            max_rect_width = left[i][j] + k - 1
                            max_rect_height = k
                        else:
                            max_rect_width = k
                            max_rect_height = top[i][j] + k - 1
                        max_rect = [([0] * W) for __i in range(0, H)]
                        for _i in range(i - max_rect_height + 1, i+1):
                            for _j in range(j - max_rect_width + 1, j+1):
                                max_rect[_i][_j]=6
                        max_rect[i][j] = 4

        #show(left)
        #show(top)
        print '---------------' + str(k)
    return max_rect

random_arr = [([0] * W) for i in range(0, H)]
gen_random(random_arr)

max_rect_width = 0
max_rect_height = 0
max_rect_area = 0

show(gen_max_rect(random_arr))
print max_rect_width
print max_rect_height
