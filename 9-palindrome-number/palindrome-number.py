class Solution:
    def isPalindrome(self, x: int) -> bool:
        b = str(x)
        palindrome = ''

        for i in range(len(b)-1,-1,-1):
            palindrome = palindrome + b[i]

        if palindrome == b:
            return True
        else:
            return False               

        