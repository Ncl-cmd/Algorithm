class Solution(object):
    def two_sum(self, nums, target) -> list:
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(len(nums)-1,i,-1):
                if nums[i]+nums[j] == target:
                    return ([i,j])
        return None

if __name__ == "__main__":
    s = Solution()
    nums = [2, 7, 11, 15]
    target = 9
    result = s.two_sum(nums, target)
    print(f"Result : {result}")  # Should display [0, 1]

    nums = [3,2,4]
    target = 6
    result = s.two_sum(nums, target)
    print(f"Result : {result}")  # Should display [1, 2]

    nums = [3,3]
    target = 6
    result = s.two_sum(nums, target)
    print(f"Result : {result}")  # Should display [0, 1]

    assert s.two_sum([2, 7, 11, 15], 9) == [0, 1]

    # Cas avec des nombres négatifs
    assert s.two_sum([-3, 4, 3, 90], 0) == [0, 2]

    # Cas où aucun doublon n'existe
    assert s.two_sum([1, 2, 3], 10) is None

    print("Tous les tests ont réussi avec succès !")