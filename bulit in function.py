# ------------------------
# -- Built In Functions --
# ------------------------
# all()#ال functioin هنا اكناها ترجمه حرفيه يعني معناها لو ةكل العناصر موجوده في x تنفذ الشرط
# any()#لو فيه اي عنصر من عناصر الليست true اكتبلي انها true
# bin()#بترجعلي ال binary number
# id()الايدي بتاع العناصر الي متخزنه في لاالميموري
# ------------------------

x = [1, 2, 3, 4, []]

if all(x):#ال functioin هنا اكناها ترجمه حرفيه يعني معناها لو ةكل العناصر موجوده في x تنفذ الشرط

  print("All Elements Is True")

else:

  print("Theres At Least One Element Is False")

x = [0, 0, []]

if any(x):

  print("There's At Least One Element is True")

else:

  print("Theres No Any True Elements")

print(bin(100))

a = 1
b = 2

print(id(a))
print(id(b))


# ------------------------
# -- Built In Functions --
# ------------------------
# sum()
# round()
# range()
# print()
# ------------------------

# sum(iterable, start)
a = [1, 10, 19, 40]
print(sum(a))#جمع العناصر الي في ال list
print(sum(a, 40))#ضاف علي العناصر 40

# round(number, numofdigits)#بيطلب الرقم و عاوز اقرب ركام لرقم بعد العلامه العشريه
print(round(150.501))#بتقرب الرقم
print(round(150.554, 2))#بيطلب الرقم و عاوز اقرب ركام لرقم بعد العلامه العشريه                           

# range(start, end, step)
print(list(range(0)))
print(list(range(10))) #من 0 الي 9
print(list(range(0, 20, 2)))

# print()
print("Hello @ Osama @ How @ Are @ You")
print("Hello", "Osama", "How", "Are", "You", sep=" | ")#stringبضيف العلامه الي انا عاوزها بعد كل

print("First Line", end=" ")
print("Second Line")
print("Third Line")




#part 3
# ------------------------
# -- Built In Functions --
# ------------------------
# abs()#absulat value بترجع الرقم من غير سالب 
# pow()#لاس ** 
# min()الاصغر
# max()الاكبر
# slice()#بيطلب ال stop اجباري
# ------------------------

# abs()#absulat value بترجع الرقم من غير سالب 
print(abs(100))
print(abs(-100))
print(abs(10.19))
print(abs(-10.19))

print("#" * 50)

# pow(base, exp, mod) => Power#لاس ** 
print(pow(2, 5))  # 2 * 2 * 2 * 2 * 2
print(pow(2, 5, 10))  # (2 * 2 * 2 * 2 * 2) % 10#العشره الي هي ال modulas مش لازم اكتبه

print("#" * 50)

# min(item, item , item, or iterator)
myNumbers = (1, 20, -50, -100, 100)
print(min(1, 10, -50, 20, 30))
print(min("X", "Z", "Osama"))
print(min(myNumbers))

print("#" * 50)

# max(item, item , item, or iterator)
myNumbers = (1, 20, -50, -100, 100)
print(max(1, 10, -50, 20, 30))
print(max("X", "Z", "Osama"))
print(max(myNumbers))

print("#" * 50)

# slice(start, end, step)بيطلب ال stop اجباري
a = ["A", "B", "C", "D", "E", "F"]
print(a[:5])
print(a[slice(5)])
print(a[slice(2, 5)])




# -------------------------------
# -- Built In Functions => Map --
# -------------------------------
# [1] Map Take A Function + Iterator
# [2] Map Called Map Because It Map The Function On Every Element
# [3] The Function Can Be Pre-Defined Function or Lambda Function
# ---------------------------------------------------------------

# Use Map With Predefined Function

def formatText(text):

  return f"- {text.strip().capitalize()} -"

myTexts = [" OSama ", "AHMED", "  sAYed  "]

myFormatedData = map(formatText, myTexts)#map function

print(myFormatedData)

for name in list(map(formatText, myTexts)):

  print(name)

print("#" * 50)
#PART 4
# Use Map With Lambda Function

def formatText(text):

  return f"- {text.strip().capitalize()} -"

myTexts = [" OSama ", "AHMED", "  sAYed  "]

for name in list(map((lambda text: f"- {text.strip().capitalize()} -"), myTexts)):

  print(name)

#PART 5



# ----------------------------------
# -- Built In Functions => Filter --
# ----------------------------------
# [1] Filter Take A Function + Iterator
# [2] Filter Run A Function On Every Element
# [3] The Function Can Be Pre-Defined Function or Lambda Function#من 1 الي 3 زي ال MAP
# [4] Filter Out All Elements For Which The Function Return True#بيرجع البايانات الي الشرط بتاعها بيتحقق
# [5] The Function Need To Return Boolean Value
# ---------------------------------------------------------------

# Example 1

def checkNumber(num):

  return num > 10

myNumbers = [0, 0, 1, 19, 10, 20, 100, 5, 0]

myResult = filter(checkNumber, myNumbers)

for number in myResult:

  print(number)

print("#" * 50)

# Example 2

def checkName(name):

  return name.startswith("O")

myTexts = ["Osama", "Omer", "Omar", "Ahmed", "Sayed", "Othman"]

myReturnedData = filter(checkName, myTexts)

for person in myReturnedData:

  print(person)

print("#" * 50)

# Example 3#     lamda function # بكتبها علطول علشان هي مش ببتعرف الاول زي ال فانكشن العاديه

myNames = ["Osama", "Omer", "Omar", "Ahmed", "Sayed", "Othman", "Ameer"]

for p in filter(lambda name: name.startswith("A"), myNames):#مش لازم اخزنها في متغير ممكن اللوب عليها علطول

  print(p)







  #PART 6


  # ----------------------------------
# -- Built In Functions => Reduce --
# ----------------------------------
# [1] Reduce Take A Function + Iterator
# [2] Reduce Run A Function On FIrst and Second Element And Give Result
# [3] Then Run Function On Result And Third Element
# [4] Then Run Function On Rsult And Fourth Element And So On
# [5] Till One ELement is Left And This is The Result of The Reduce
# [6] The Function Can Be Pre-Defined Function or Lambda Function
# ---------------------------------------------------------------

from functools import reduce#عملتهلها import

def sumAll(num1, num2):

  return num1 + num2

numbers = [1, 8, 2, 9, 100]

result = reduce(sumAll, numbers)#بال FUNCTION العاديه

result = reduce(lambda num1, num2: num1 + num2, numbers) #LAMBDA FONCTION

print(result)# ((((1 + 8) + 2) + 9) + 100)






#PART 7


# ------------------------
# -- Built In Functions --
# ------------------------
# enumerate()#بتعد يعني علي اول عنصر في ال LIST بتحط 0 و هكاذا ولو عاوزها تبدا من عدد معين ممكن اعمل كده بالSTART
# help()# بيخليني لو فيه اي methods او اي function مش عارف بتعمل ايه ممكن استخدم ال help
# reversed() بيطلب iterable وبيعكس العناصر
# ------------------------

# enumerate(iterable, start=0) ال START اختياري 

mySkills = ["Html", "Css", "Js", "PHP"]

mySkillsWithCounter = enumerate(mySkills, 20)

print(type(mySkillsWithCounter))#نو البيانات ENUMERATE

for counter, skill in mySkillsWithCounter:#هنا ال enumerate خلتني اعرف اللوب علي عنصرينة جنب بعض

  print(f"{counter} - {skill}")

print("#" * 50)

# help()

print(help(print))

print("#" * 50)

# reversed(iterable)

myString = "Elzero"

print(reversed(myString))

for letter in reversed(myString):

  print(letter)

for s in reversed(mySkills):

  print(s)