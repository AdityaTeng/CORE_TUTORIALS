def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    nums_set = set(nums)
    count_dict = dict()
    return_list = list()
    for i in nums_set:
        count_dict[i] = nums.count(i)
    for key , value in count_dict.items():
        if value >= 2:
            for i in range(2):
                return_list.append(key)
        else:
            return_list.append(key)
    print(return_list)
    nums = list()
    for i in return_list:
        nums.append(i)
    print(nums)
    return len(nums)

removeDuplicates([1,1,1,2,2,3])
