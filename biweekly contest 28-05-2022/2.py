"""
6084. Sender With Largest Word Count
"""
from typing import List


class Solution:
    def largestWordCount(self, messages: List[str], senders: List[str]) -> str:
        senders_dict = {}
        arr = []
        for i in range(len(senders)):
            senders_dict[senders[i]] = 0
        for i in range(len(messages)):
            word_list = messages[i].split()
            senders_dict[senders[i]] += len(word_list)
        max_value = max(senders_dict.values())
        for key, value in senders_dict.items():
            if value == max_value:
                arr.append(key)
        return max(arr)


messages = ["Hello userTwooo", "Hi userThree", "Wonderful day Alice", "Nice day userThree"]
senders = ["Alice", "userTwo", "userThree", "Alice"]
# messages = ["How is leetcode for everyone","Leetcode is useful for practice"]
# senders = ["Bob","Charlie"]

s = Solution()
print(s.largestWordCount(messages, senders))
