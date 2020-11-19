


list1 = [49,38,65,97,76,13,27,49]

def insert_sort(list1):
    '''
    直接插入排序算法，每次将一个数据插入到已经拍好序的数据中，算法复杂的O(n^2)
    :param list1:
    :return:
    '''
    i=0
    j=i+1
    while j<len(list1):
        temp=list1[j]
        while j>=1:
            if temp< list1[j-1]:   #如果比前面的数小，交换位置
                list1[j] =list1[j-1]
                j=j-1
            else:
                break
        list1[j]=temp
        print(list1)     #打印输出每次排序结果
        i=i+1
        j=i+1

if __name__=='__main__':
    print(list1)  #输出初始序列
    insert_sort(list1)