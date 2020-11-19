
list1 = [49,38,65,97,76,13,27,49]
def simple_select_sort(arr):
    '''
    简单选择排序，每轮找出一个最小值，每轮将一个未排序位置上的数交换成已排序数，即每轮选一个最值
    :param arr:
    :return:
    '''

    for i in range(0,len(arr)):
        min_index = i
        for j in range(i+1,len(arr)): #此循环找出最小的值
            if arr[j] < arr[min_index]:
               min_index = j
        if i!= min_index:     #交换最小值到i的位置
            tmp = arr[i]
            arr[i]=arr[min_index]
            arr[min_index]=tmp

        print(arr)



if __name__=='__main__':
    print("初始序列：",list1)  #输出初始序列
    simple_select_sort(list1)