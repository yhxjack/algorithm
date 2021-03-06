# -*- coding: utf-8 -*-

# 位运算: 相同位位1, 相异位为0, 3&5=1 -> 011&101=001
# 异或算: 相同位为0, 相异位为1, 1^3=2 -> 001^011=010

def aa(array):
    if len(array) < 3:
        return array

    a=b=sums=0
    for i in array:
        sums ^= i
    mask = sums & (-sums)  #负数二进制为, 整数全部反转为0 + 1
    
    # 位运算, 将0分为1组, 1分为1组; 异或相同会抵消0, 最终剩下那个数
    for i in array:
        if i&mask:
            a ^= i
        else:
            b ^= i
    return [a,b]


def bb(nums):
    x, y, n, m = 0, 0, 0, 1
    for num in nums:         # 1. 遍历异或
        n ^= num
    while n & m == 0:        # 2. 循环左移，计算 m
        m <<= 1       
    for num in nums:         # 3. 遍历 nums 分组
        if num & m: x ^= num # 4. 当 num & m != 0
        else: y ^= num       # 4. 当 num & m == 0
    return x, y


if __name__ == "__main__":
    array = [4,1,4,6]
    print aa(array)
    print aa([3,4])
