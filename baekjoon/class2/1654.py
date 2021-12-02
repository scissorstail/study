k, n = map(int, input().split(' '))
# print(k, n)

values = [int(input()) for _ in range(k)]

# print(values)

start = 1
end = max(values)
# count = 0
# mid_priv = None
while True:
    # 2) ~~인 값 중 최대
    # mid=(start+end+1)/2 (올림)
    # - 오른쪽 가야함 -> start=mid
    # (hi 고정, lo가 근소하게 오른쪽)
    # - 왼쪽 가야함 -> end=mid-1
    
    mid = (start + end + 1) // 2

    if(start == end):
        print(mid)
        break

    mid_count = sum([ x // mid for x in values])
    
    left_mid = (start + mid + 1) // 2
    left_count = sum([ x // left_mid for x in values])

    right_mid = (mid + end + 1) // 2
    right_count = sum([ x // right_mid for x in values])

    left_avail = None
    right_avail = None

    # print('start:', start, 'end:', end)
    # print('mid', mid_count, ' => mid:', mid)
    # print('left', left_count, ' => mid:', left_mid)
    # print('right', right_count, ' => mid:', right_mid)


    if(mid_count < n):
        if(left_count >= right_count):
            left_avail = True
        else:
            right_avail = True
    else:
        if(left_mid <= right_mid):
            right_avail = True
        else:
            left_avail = True
    

    # print(left_avail, right_avail)
    # print('=======')
    
    if(left_avail):
        # to left
        end = mid - 1
    elif(right_avail):
        # to right
        start = mid
    else:
        if(left_mid == right_mid):
            print(mid)
            break
    
    # count += 1
    # if(count > 10):
    #     break