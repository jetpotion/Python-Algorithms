class Solution:
    def intToRoman(self, num: int) -> str:
        switcher = {1 :    "I",
                    5 :    "V",
                    10 :   "X",
                    50 :   "L",
                    100 :  "C",
                    500 :  "D",
                    1000: "M",
                    4  :   "IV",
                    9 :    "IX",
                    40 :   "XL",
                    90:    "XC",
                    900 :  "CM",
                    400:   "CD"}
        output = ""
        conversion = str(num)
        powersoften = pow(10,len(conversion) - 1)
        for x in conversion:
            character = x
            basedigits = int(character) * powersoften
            if basedigits in switcher:
                output += switcher[basedigits]
                powersoften = powersoften//10
                continue
            else:
                substring = ""
            #If this number is not a ones digits or ten it self but this will never happen because 10 will be located before it all began
            #Keep substracting nearest local power 600 then becomes 600 - 100 = 500 From which 500 will be located. This will reduce the problem down to the 5,500.,500
                while basedigits is not 0 :
                    basedigits = basedigits - powersoften
                    substring += switcher[powersoften]
                    #Check as we reduce  it 
                    if basedigits in switcher:
                     substring += switcher[basedigits]
                     basedigits = 0
            powersoften = powersoften // 10
            output += substring[::-1]
        return output
