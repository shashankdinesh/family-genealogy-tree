def partition(child_num,total_child,seq):
    if child_num-1 >= total_child // 2:
        total_child = total_child // 2
        child_num=child_num-total_child
        return 1,total_child,child_num
    else:

        total_child = total_child // 2
        return 0,total_child,child_num

def child_gender(sequence,gender=None):
    for i in sequence:
        if i == 0 and gender == None:
            gender = "M"
        elif i == 0 and gender == "F":
            gender = "F"
        elif i == 0 and gender == "M":
            gender = "M"
        elif i == 1 and gender == None:
            gender = "F"
        elif i == 1 and gender == "F":
            gender = "M"
        elif i == 1 and gender == "M":
            gender = "F"
    return gender







import time

test_case_num = int(input().strip())
#test_case_num = 1
st = time.time()
if not (1 <= test_case_num <= 600):
    exit()
result = []

for i in range(test_case_num):

    sequence = []
    generation, child_num = map(int, input().strip().split())
    #generation, child_num = 5,16
    print(generation,child_num)
    if not (1 <= generation <= 11000):

        exit()
    if not (1 <= child_num <= min(10 ** 15, 2 ** (generation - 1))):

        exit()

    if generation == 1 or child_num == 1:
        result.append("M")
    elif generation == 1 or child_num == 2:
        result.append("F")
    else:
        total_child = 2 ** (generation-1)
        while total_child>1:
            part,total_child,child_num=partition(child_num, total_child,sequence)
            sequence.append(part)
            #print(sequence)
        result.append(child_gender(sequence))
et = time.time()

print("\n".join(result),result,sep='\n')



