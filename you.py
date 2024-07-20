# #11
# import re

# def validate_password(pass_value):
#     if len(pass_value) < 8:
#         return False
#     if not re.search(r"[a-z]", pass_value):
#         return False
#     if not re.search(r"[A-Z]", pass_value):
#         return False
#     if not re.search(r"[0-9]", pass_value):
#         return False
#     if not re.search(r"[_@$]", pass_value):
#         return False
#     return True

# password = "sr@m@_f0rtu9e$._2023"
# print(validate_password(password))

# #12
# def reverse_words(statement):
#     words = statement.split()
#     reversed_statement = ' '.join(words[::-1])
#     return reversed_statement

# statement = "i like this program very much"
# result = reverse_words(statement)
# print(result)  

# #13
# statement = 'A computer science portal for portal'
# word = 'portal'


# words_list = statement.split()
# count_occur = 0
# for item in words_list:
#     if item == word:
#         count_occur = count_occur + 1

# print('word occur times : ', count_occur)

# #14
# def remove_special_characters(statement):
#     result = ''.join(char for char in statement if char.isalnum())
#     return result

# ini_string = "123abcjw:, .@! eiw"
# cleaned_string = remove_special_characters(ini_string)
# print(cleaned_string)  

# #15
# ips_List = [
#     ('192.168.0.15', 'y'),
#     ('192.168.0.22', 'y'),
#     ('192.168.0.14', 'y'),
#     ('192.168.0.24', 'n'),
#     ('192.168.0.15', 'y'),
#     ('192.168.0.11', 'y')
# ]
# unique_list = []
# for ip in ips_List:
#     if ip not in unique_list:
#         unique_list.append(ip)

# print(unique_list)



# # 16
# company_employees = [
# (101, 'Hayam Esam', 10000.0, 'Engineer', 'F'),
# (102, 'Ibrahim Ahmed', 9000.0, 'Accountant', 'M'),
# (103, 'Adham Aly', 5000.0, 'Engineer','M'),
# (104, 'Islam Hassan', 7000.0, 'Sales','M'),
# (105, 'Marwa Esam', 7000.0, 'Marketer','F'),
# (106, 'Ola Hassan', 7000.0, 'Engineer','F')
# ]
# count_male, count_female = 0, 0
# for employee in company_employees:
#     if employee[4] == 'M':
#         count_male = count_male + 1
#     elif employee[4] == 'F':
#         count_female = count_female + 1

# print('Count Male = ', count_male)
# print('Count Female = ', count_female)



# # 17
# shopping_cart_dict = {'milk': 20.0, 'bread': 10.0, 'eggs': 145.0}

# print('Original Dict : ', shopping_cart_dict)

# total_order = 0
# for item, value in shopping_cart_dict.items():
#     shopping_cart_dict[item] = value + value * 0.1
#     total_order = total_order + shopping_cart_dict[item]

# print('After 10% raise : ', shopping_cart_dict)
# print('Total order : ', total_order)


# order_net_salary = total_order + total_order * 0.14
# print('After vat - net salary = ', order_net_salary)

# #18
# num1 = 4
# num2 = 7 
# print(num1, num2)

# num1, num2 = num2, num1 

# print(num1, num2)


# #19
# ips_list = [
#     ('192.168.0.15', 'y'),
#     ('192.168.0.22', 'y'),
#     ('192.168.0.14', 'y'),
#     ('192.168.0.24', 'n'),
#     ('192.168.0.81', 'n'),
#     ('192.168.0.11', 'y')
# ]

# for i, state in ips_list:
#     if state == 'y':
#         print(i, '>' , i.split('.')[-1] )

# #20
# statement = input(str ("put on your string"))
# word = input(str ("put on your word"))


# words_list = statement.split()
# count_occur = 0
# for item in words_list:
#     if item == word:
#         count_occur = count_occur + 1

# print('word occur times : ', count_occur)
 




str = "i like this program very much"

def rev (str):
    for i in str:
        print (i)



