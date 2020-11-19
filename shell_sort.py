



list1 = [49,38,65,97,76,13,27,49]

# def shell_sort1(arr):
#     '''
#     希尔排序
#     :param arr: 待排序列
#     :return:
#
#     step：步长值
#     '''
#     step = len(arr) // 2  #步长取整数，逐步缩短
#     while step > 0:
#         for i in range(step, len(arr)):  #
#             for j in range(i,step-1,-step):  #从i到step-1，每次增加-step
#                 if arr[j] < arr[j-step]:
#                     temp = arr[j]
#                     arr[j] = arr[j-step]
#                     arr[j-step] = temp
#                 else:
#                     break
#
#         step = step//2
#         print(arr)

def shell_sort2(arr):
    '''
    希尔排序
    :param arr: 待排序列
    :return:

    step：步长值
    '''
    step = len(arr) // 2  #步长取整数，逐步缩短
    while step > 0:
        for i in range(step,len(arr)):
            for j in range(i,0,-step):  #从i到step-1，每次增加-step
                if arr[j] < arr[j-step]:   #后面的比前面的小就交换
                    temp = arr[j]
                    arr[j] = arr[j-step]
                    arr[j-step] = temp
                else:
                    break

        step = step//2
        print(arr)


if __name__=='__main__':
    print("初始序列：",list1)  #输出初始序列
    shell_sort2(list1)