number=[1,2,4,11,8,6]
max_number=max(number)
print("max",max_number)



class Number:
    def __init__(self, Maximum):
        self.Maximum = Maximum
        self.max_Maximum = max(Maximum)
        print("Max san:", self.max_Maximum)

Maximum = (1, 3, 5, 2, 9, 8)
number = Number(Maximum)



def find_max(list1):
    return max(list1)
a = find_max([2,3,1,8,4,6])
print("Max:", a)