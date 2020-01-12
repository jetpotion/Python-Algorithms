class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        else:
            number = str(x)
            length  = len(number)
            half = length // 2
            if(length % 2 == 1):
                firsthalf = number[:half + 1]
                secondhalf = number[half : length]
                firsthalf = firsthalf [::-1]
                if firsthalf == secondhalf:
                    return True
                return False
            else:
                firsthalf = number[:half]
                secondhalf = number[half : length]
                firsthalf = firsthalf [::-1]
                if firsthalf == secondhalf:
                    return True
                return False
