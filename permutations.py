def permute(nums= [1,2,3]) :
    n = len(nums)
    l = []

    def func(first=0):
        if first == n:
            l.append(nums[:])
        for i in range(first, n):
            nums[first], nums[i] = nums[i], nums[first]
            func(first + 1)
            nums[i], nums[first] = nums[first], nums[i]

    func()
    return l
print(permute())