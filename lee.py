import re

class Solution:
    def numberToWords(self, num: int) -> str:
        def threeNumberToWords(str_num: str, unit: str) -> str:
            if str_num.strip() == "": return ""
            num = int(str_num)
            # All dictionary
            result_str = []
            singles_words = ['Zero', 'One', "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
            ten_to_twenty_words = [
                "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen",
                "Sixteen", "Seventeen", "Eighteen", "Nineteen"
            ]
            abv_twenty_words = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
            tri_words = ["Hundred"]
            if num == 0: return singles_words[0]
            # Hundred position
            hundred_pos = num//100
            if hundred_pos > 0:
                result_str.append(f"{singles_words[hundred_pos]} Hundred")
            num = num%100
            # Ten position
            if num != 0:      # Still have remaining at ten position
                ten_pos = num//10
                if ten_pos == 1:
                    result_str.append(f"{ten_to_twenty_words[num%10]}")
                else:
                    last_pos = num%10
                    if ten_pos >= 2 and last_pos == 0:
                        result_str.append(f"{abv_twenty_words[ten_pos]}")
                    else:
                        result_str.append(f"{abv_twenty_words[ten_pos]} {singles_words[last_pos]}")
            return f"{' '.join(result_str)} {unit}"

        ret = []
        k_unites = [
            'Nonllion', 'Octillion', 'Septillion', 'Sextilliion',
            'Quintillion', 'Quadrillion', 'Quadrillion', 'Trillion',
            'Billion', 'Million', 'Thousand' , ''
        ]   # Empty for hundred
        str_num = f"{num}"[::-1]
        chunks = len(str_num)//3 + 1
        for i in range(chunks):
            ret.insert(0, threeNumberToWords(
                str_num[i*3:i*3+3][::-1],
                k_unites[-i-1]
            ))
            # print(f"{i}: {str_num[i*3:i*3+3][::-1]}, {k_unites[-i-1]}")

        # Remove continus Zero
        if len(ret) > 1:
            ret = [chunk for chunk in ret if chunk!="Zero"]

        return re.sub(r"\s+", " ", " ".join(ret).strip())
        

if __name__ == "__main__":
    sol = Solution()
    print(sol.numberToWords(1000010))