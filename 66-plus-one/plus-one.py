class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        
        n = len(digits)
        string = ''
        outputNumbers = []
        for i in range (n):
            string = string + str(digits[i])    

        string = int(string)+1
        convertedString = str(string)
        for char in convertedString:
            
            outputNumbers.append(int(char))

        return outputNumbers    