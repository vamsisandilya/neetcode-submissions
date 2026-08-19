class Solution:
    def calPoints(self, operations: List[str]) -> int:
        list1 = []
        result = 0
        for i in operations:
            if i == '+':
                result += list1[-1] + list1[-2]
                list1.append(list1[-1] + list1[-2])
            elif i == 'D':
                result += (2 * list1[-1])
                list1.append(2 * list1[-1])
            elif i == "C":
                result -= list1.pop()
            else:
                result += int(i)
                list1.append(int(i))
        return result
            