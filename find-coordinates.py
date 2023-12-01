import re
# open coordinates.txt
f = open("input.txt","r")
num_list = []
line_num = 0
for line in f:
    # if string only has one number do not find second number
    num_of_nums = sum(c.isdigit() for c in line)
    #print('This is number of digits in string',num_of_nums)
    print('This is line',line_num+1,'total:')
    if num_of_nums > 1:
        # find the first number
        first_num = re.findall(r'\d',line)
        str_first_num = ''.join(first_num[0])
        # int_first_num = int(str_first_num)
        # find the second number
        last_num = re.findall(r'(\d)(?!.*\d)',line)
        str_last_num = ''.join(last_num[-1])
        # int_last_num = int(str_last_num)
        total_per_line = str_first_num + str_last_num
        tee_total = int(total_per_line)
    else:
        # find the first number
        first_num = re.findall(r'\d',line)
        str_first_num = ''.join(first_num[0])
        # int_first_num = int(str_first_num)
        total_per_line = str_first_num + str_first_num
        tee_total= int(total_per_line)

        print('Heres the numbers added up', tee_total)



    num_list .append(tee_total)
    print('This is num_list', num_list)

    line_num = line_num + 1

    total = sum(num_list)

    print(total)



