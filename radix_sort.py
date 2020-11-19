
list1 = [4,38,65,97,76,13,27,498]

def radix_sort(arr):
    '''
    基数排序，按照元素位数排序
    :param arr:
    :return:
    '''

    i=0  #记录当前正在排的一位，最低位为1
    max_num = max(arr)
    j = len(str(max_num))  #记录最大值位数
    while i<j:
        bucket_list = [[] for _ in range(10)]    #初始化桶数组，即下面等价
        # bucket_list = [[],[],[],[],[],[],[],[],[],[]]
        for x in arr:
            bucket_list[(int(x/10**i)) %10].append(x)   #找到位置放入相应的桶数组

        print(bucket_list)
        arr.clear()
        for x in bucket_list:       #重新放回原序列
            for y in x:
                arr.append(y)
        i =i+1





if __name__ == '__main__':
    print("初始序列：", list1)  # 输出初始序列
    radix_sort(list1)
    print(list1)


