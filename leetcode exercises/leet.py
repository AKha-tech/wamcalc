x = [9, 1, 0, 0, 2, 1, 0, 4]


def canjump(nums):
    n = len(nums)
    zeros = [0]  # list of indices with 0
    if nums[0] == 0:
        return False
    for i in range(n):
        if nums[i] == 0:
            zeros.append(i)
            for j in range(zeros[-1]-1, -1, -1):
                away = i-j
                if nums[j] <= away and j == 0:
                    print(j, away)
                    return False
                if nums[j] == away:
                    continue
                elif nums[j] > away:
                    break
    return True


# print([1][-1])
print(canjump(x))
