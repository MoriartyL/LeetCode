import operator
def twoSum(nums, target):
    # list = []
    # nums_tup = [(i,nums[i]) for i in range(len(nums))]
    # i = 0
    # j = len(nums_tup)-1
    # nums_tup.sort(key=operator.itemgetter(1))
    # while True:
    #     if i == j:
    #         print("Not found")
    #         break
    #     sum = nums_tup[i][1] + nums_tup[j][1]
    #     if sum == target:
    #         list.append(nums_tup[i][0])
    #         list.append(nums_tup[j][0])
    #         break
    #     elif sum > target:
    #         j -= 1
    #     else:
    #         i += 1
    # print(list)
    hash = {}
    for i,num in enumerate(nums):
        if num in hash:
            print([hash[num],i])
        hash[target-num] = i

def main():
    twoSum([2,5,4,5,1,7,8],10)


if __name__ == "__main__":
    main()