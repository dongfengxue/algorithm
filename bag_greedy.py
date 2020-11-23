

class goods:
    def __init__(self,id,weight=0,value=0,status=0):
        self.id = id     #物品id
        self.weight = weight   #物品重量
        self.value = value       #物品价值
        self.value_per_weight = value/weight   #物品单位价值
        self.status = status  #status表示是否放入背包

    def __str__(self):
        return "('%s',%d,%.0f,%.1f)" % (self.id, self.weight, self.value,self.status)

    # def get_value_per_weight(self):
    #     return self.value_per_weight

def value_per_weight_greedy(capacity=0,goods_set=[]):    #最大价值贪婪算法
    goods_set.sort(key=lambda x:x.value_per_weight,reverse=True)
    # for good in goods_set:
    #     print (good)

    result = []
    the_cost = 0
    for good in goods_set:
        if capacity < good.weight:

            if len(result) < len(goods_set) and capacity != 0:
                good.status=capacity/good.weight
                result.append(goods(good.id, good.weight, good.value* (capacity/good.weight),capacity/good.weight))
                print('放入商品：%d，剩余容量 %d' % (good.id, 0))
                break
        else:
            good.status=1
            result.append(good)
            capacity = capacity - good.weight
            print('放入商品：%d，剩余容量 %d：'%(good.id,capacity))

    for x in result:
        the_cost = the_cost+x.value
        print(x)
    # print(result)
    return result,the_cost

if __name__ == '__main__':
    some_goods = [goods(0, 35, 10,0), goods(1, 30, 40,0), goods(2, 60, 30,0), goods(3, 50, 50,0), goods(4, 10, 40,0)]
    result = value_per_weight_greedy(140,some_goods)
    # for i in result:
    #     print (i)