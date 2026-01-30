class Solution(object):
    def letterCombinations(self, digits):
        if not digits:
            return []
        phone={
            2:"abc",
            3:"def",
            4:"ghi",
            5:"jkl",
            6:"mno",
            7:"pqrs",
            8:"tuv",
            9:"wxyz"
        }
        result=[""]
        for d in digits:
            new_result=[]
            letters=phone[int(d)]
            for combo in result:
                for ch in letters:
                    new_result.append(combo+ch)
            result=new_result
        return result
