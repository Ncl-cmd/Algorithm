class Solution(object):
    def add_two_numbers(self, la, lb) -> list:
        """
        :type la: List[int]
        :type lb: List[int]
        :type lr: List[int]
        """
        carry = 0
        lr = []
        for i in range(len(la)):
            if i>=len(lb):
                res = la[i] + carry
            else:
                res = la[i] + lb[i] + carry
            if res > 9:
                carry = 1
                res=res%10
            else:
                carry = 0
            lr.append(res)
        if carry == 1:
            lr.append(1)
        return (lr)


if __name__ == "__main__":
    s = Solution()
    la = [2, 4, 3]
    lb = [5, 6, 4]
    result = s.add_two_numbers(la, lb)
    print(f"Result : {result}")  # Should display [7,0,8]

    la = [9, 9]
    lb = [1]
    result = s.add_two_numbers(la, lb)
    print(f"Result : {result}")  # Should display [0,0,1]


    la = [0]
    lb = [0]
    result = s.add_two_numbers(la, lb)
    print(f"Result : {result}")  # Should display [0]

    la = [9,9,9,9,9,9,9]
    lb = [9,9,9,9]
    result = s.add_two_numbers(la, lb)
    print(f"Result : {result}")  # Should display [8,9,9,9,0,0,0,1]
