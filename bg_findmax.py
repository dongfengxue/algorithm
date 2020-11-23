

def FindMax(n,capacity,Value,w,v):  #动态规划

    #填表
    for j in range(capacity + 1):
        Value[0][j] = 0

    for i in range(1,n+1):
        # res[0][i] = 0
        for j in range(1,capacity+1):
            if(j<w[i-1]) :
                #包装不进
                Value[i][j]=Value[i-1][j]
            else:    #//能装

                if( Value[i-1][j] > Value[i-1][j-w[i-1]]+v[i-1]):   #//不装价值大
                    Value[i][j]=Value[i-1][j]
                else:
                    #//前i-1个物品的最优解与第i个物品的价值之和更大
                    Value[i][j]=Value[i-1][j-w[i-1]]+v[i-1]

def Findwhat(i,j):
    # j= capacity
    if i>=1:
        if Value[i][j] == Value[i-1][j]:
            item[i]=0
            Findwhat(i-1,j)
        elif (j-w[i-1]>=0) and (Value[i][j]==Value[i-1][j-w[i-1]]+v[i-1]):
            item[i]=1
            Findwhat(i-1,j-w[i-1])





if __name__ == '__main__':
    n = 4  #物品数量
    capacity = 8  #书包容量
    item=[0 for i in range(0,n+1)]
    w = [2, 3, 4, 5]   #每个物品重量
    v = [3, 4, 5, 6]   #每个物品价值
    Value=[[0 for i in range(8+1) ] for j in range(n+1)]  #5行4列二维矩阵
    # print(V)
    '''
    V[i][j]  表示当前背包容量为j，前i个物品的最佳组合值
    j<w(i),V[i][j]=V[i-1][j]
    j>w(i),V[i][j]=max{  V[i-1][j],V[i-1][j-w[i]]+v[i]}  
    '''

    res = FindMax(n, capacity,Value, w, v)
    print(Value)
    Findwhat(n,capacity)
    print (item)
    # show(n, c, w, res)
