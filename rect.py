import random
import time

W = 10
H = 10

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

def make_random_arr(seed = False):
    r = [([0] * W) for i in range(0, H)]
    if seed:
        random.seed(seed)
    for i in range(1, H):
        for j in range(1, W):
            r[i][j] = int(random.random() * 2)
    return r

max_square_width = 0
def get_max_square(arr):
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

def get_max_rect_method1(arr, debug = False):
    max_square = get_max_square(arr)
    arr = max_square
    global max_rect_area
    global max_rect_width
    global max_rect_height
    max_rect = [([0] * W) for i in range(0, H)]
    for k in range(max_square_width, 0, -1):
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
                        if debug:
                            max_rect = [([0] * W) for __i in range(0, H)]
                            for _i in range(i - max_rect_height + 1, i+1):
                                for _j in range(j - max_rect_width + 1, j+1):
                                    max_rect[_i][_j]=6
                            max_rect[i][j] = 4
    return max_rect

def get_max_rect_method2(arr):
    global max_rect_area
    left = [([0] * W) for i in range(0, H)]
    top = [([0] * W) for i in range(0, H)]
    m = [([0] * W) for i in range(0,H)] # max area
    s = [([0] * W) for i in range(0,H)]
    for i in range(0, H):
        s[i][0] = [];
    for i in range(0, W):
        s[0][i] = [];
    def limit(queue, l, t, y, x):
        min_y = y - t + 1
        min_x = x - l + 1
        suspects = queue
        for i in suspects:
            if i[0] < min_y:
                i[0] = min_y
            if i[1] < min_x:
                i[1] = min_x
        suspects.append([min_y, x])
        if min_y != y or x != min_x :
            suspects.append([y, min_x])
        return suspects

    for i in range(1, H):
        for j in range(1, W):
            if arr[i][j]:
                left[i][j] = left[i][j - 1] + 1
                top[i][j] = top[i - 1][j] + 1
                s[i][j] = limit(s[i - 1][j - 1], left[i][j], top[i][j], i, j)
                for k in s[i][j]:
                    m[i][j] = max(m[i][j], (i - k[0] + 1) * (j - k[1] + 1))
                max_rect_area = max(m[i][j], max_rect_area);
            else:
                s[i][j] = []
    return m

random_arr = make_random_arr()

max_rect_width = 0
max_rect_height = 0
max_rect_area = 0

show(random_arr);

now = time.time()
result1 = get_max_rect_method1(random_arr)
print 'method1:' + str(time.time() - now)
print max_rect_area

now = time.time()
result2 = get_max_rect_method2(random_arr)
print 'method2:' + str(time.time() - now)

show(result2)
print max_rect_area
