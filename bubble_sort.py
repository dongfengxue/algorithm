



list1 = [49,38,65,97,76,13,27,49]

def bubble_sort(arr):
    '''
    冒泡排序，相邻的两个数依次进行比较和调整，让较大的数往下沉，较小的往上冒
    :param arr:
    :return:
    '''
    n = len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]   #交换
    print(arr)



if __name__=='__main__':
    print("初始序列：",list1)  #输出初始序列
    bubble_sort(list1)
    #
    # for i in range (10,0,-1):
    #     print (i)