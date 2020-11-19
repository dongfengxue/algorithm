



list1 = [49,38,65,97,76,13,27,49]
def heap_max_sort(arr):
    '''
    堆排序,构造堆
    :param arr:
    :return:
    '''
    n = len(arr)

    for start in range(n,-1,-1):         #循环每个父节点构造大根堆
        a=max_heapify(arr,n,start)
        # print("构建大根堆：",a)
    for end in range(n-1,0,-1):
        arr[end],arr[0]=arr[0],arr[end]
        max_heapify(arr, end,0)


    print(arr)

def max_heapify(arr,n,i):   #构造大根堆
    largest = i
    l=2*i+1        #左子节点
    r=2*i+2        #右子节点

    if l<n and arr[i] <arr[l]:    #左子节点在范围内且  小于左子节点
        largest= l          #标记为左子节点序号
    if r<n and arr[largest] <arr[r]:     #右子节点在范围内且 当前最大小于右子节点
        largest=r                     #标记为右子节点
    if largest!=i:              #根节点不是最大的节点
        arr[i],arr[largest]=arr[largest],arr[i]     #交换
        max_heapify(arr,n,largest)
    return arr



if __name__=='__main__':
    print("初始序列：",list1)  #输出初始序列
    heap_max_sort(list1)
    #
    # for i in range (10,0,-1):
    #     print (i)