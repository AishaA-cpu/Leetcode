class Solution:
    def minMaxDifference(self, num: int) -> int:
   
        num_string = str(num)
        ind_to_num = {}
        flipped = False
        to_flip = 0
        for n in num_string:
            if n != '9' and flipped == False:
                flipped = True
                to_flip = n
           
        new_string = ''

        for i in enumerate(num_string):
            idx, num = i
            ind_to_num[idx] = num
            if num == to_flip:
                new_string += '9'
            else:
                new_string += num

        
        min_string = ''
        for k, v in ind_to_num.items():
            if k == 0:
               min_string += '0'
            elif v == ind_to_num[0]:
                min_string += '0'
            else:
                min_string += v

        # print(new_string)
        # print(min_string)

        return int(new_string) - int(min_string)
        
        




        # whats the smallest number?
        # when we find that number, replace all its occurences with 9
        # replace the first number with a 0, note what the number is 
        # and replace all occurneces with 0
        
        # by taking the lowest number, and converting it to 9, do we get the highest
        # possible number?


        # turing the begining of any number to 0, will always reduce the value?

        