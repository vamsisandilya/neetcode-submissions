class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        left = 0
        right = len(people) - 1
        count = 0
        people.sort()
        while left <= right:
            if left == right:
                count += 1
                break
            else:
                weight = people[left] + people[right]
                if weight <= limit:
                    count += 1
                    left += 1
                    right -= 1
                else:
                    right -= 1
                    count += 1
        return count