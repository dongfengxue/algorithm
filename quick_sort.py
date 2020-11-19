



list1 = [49,38,65,97,76,13,27,49]

def quick_sort(arr,start,end):
    '''
    快速排序，重新排序数列，所有元素比基准值小的摆放在基准前面，所有元素比基准值大的摆在基准的后面（相同的数可以到任一边）。
    在这个分区结束之后，该基准就处于数列的中间位置。这个称为分区（partition）操作
    :param arr:
    :return:
    '''

    if start>=end:  #递归结束条件
        return
    mid = arr[start]     #起始基准元素
    low=start            #low为序列左边开始的从左往右的游标
    high=end             #high为序列右边开始的从右往左的游标
    while low<high:        #如果low与high未重合，high(右边)指向的元素大于等于基准元素，则high向左移动
        while low<high and arr[high]>=mid:
            high=high-1
        arr[low]=arr[high]  #走到此位置时high指向一个比基准元素小的元素,将high指向的元素放到low的位置上,此时high指向的位置空着,接下来移动low找到符合条件的元素放在此处
        while low<high and arr[low]<mid:
            low=low+1
        arr[high]=arr[low]   # 此时low指向一个比基准元素大的元素,将low指向的元素放到high空着的位置上,此时low指向的位置空着,之后进行下一次循环,将high找到符合条件的元素填到此处
    arr[low] = mid   #对基准元素左边的子序列进行快速排序
    quick_sort(arr,start,low-1)  # start :0  low -1 原基准元素靠左边一位
    quick_sort(arr,low+1,end)    # low+1 : 原基准元素靠右一位  end: 最后



if __name__=='__main__':
    print("初始序列：",list1)  #输出初始序列
    quick_sort(list1,0,len(list1)-1)
    print(list1)
    #
    # for i in range (10,0,-1):
    #     print (i)