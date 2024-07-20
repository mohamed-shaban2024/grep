# print("i love python")
# print("i love programmrng")
# print(type([1,5,8,]))
# p=10
# print(p)
# help("keywords")

# a , b, c = 10,20,32
# print(b)



# p="kvfok"
# o="bfcudh"
# print (p + " 4" +o)

#===========================LIST===================================================
#===========================LIST===================================================
#===========================LIST===================================================
#===========================LIST===================================================


#list is mutable "يعني مكن اعدل عليه"   
#string is immutable "مينفعش اعدل عليها"


# List1 =[1,2,3,4,5] 
# List2 =[6,7,8,9,10]
# List3 = List1+List2
# Print (List3) 

# list= "samir"
# print(list.upper())

# print (type(5+6j))
# print (120//20)
# print("i love python")
# print (len("mdvfkflda))

myFriends = ["Osama", "Ahmed", "Sayed"]
myOldFriends = ["Haytham", "Samah", "Ali"]

myFriends.append("Alaa")#بستخدم append لما اعوز اضيف عنصر لي list
myFriends.append(100)
myFriends.append(150.200)
myFriends.append(True)
myFriends.append(myOldFriends)

print(myFriends)
print(myFriends[2])
print(myFriends[6])
print(myFriends[7])
print(myFriends[7][2])#هنا لو عاوز ادخل علي عنصر موجود في list و list موجوده برضو جوه list

# extend() بضيف list جوه list

a = [1, 2, 3, 4]
b = ["A", "B", "C"]
c = ["One", "Two"]

a.extend(b)
a.extend(c)

print(a)

# remove() بتمسح العنصر الي انا عاوزه من list

x = [1, 2, 3, 4, 5, "Osama", True, "Osama", "Osama"]
x.remove("Osama")
print(x)

# sort()برتب الlist بس بالعكس يعني من الكبير للصغير ولازم كل العناصر الي فيها يكون من نفس لاال data type

y = [1, 2, 100, 120, -10, 17, 29]
# y = ["A", "Z", "C"]
y.sort(reverse=True)
print(y)

# reverse() بتعكس ال list بس مش بالترتيب و مش شرط فيها يكون العنصر الي جوه الlist من نفس ال data type

z = [10, 1, 9, 80, 100, "Osama", 100]
z.reverse()
print(z)

# clear() بتمسح العناصر الي في ال list

a = [1, 2, 3, 4]
a.clear()
print(a)

# copy() بتاخد نسخه من ال list

b = [1, 2, 3, 4]
c = b.copy()

print(b)  # Main List
print(c)  # Copied List

b.append(5) #هنل لو انا عاوز اضيف عنصر علي الlist بيضاف علي ا list الاصليه بس 

print(b)  # Main List
print(c)  # Copied List

# count() و هيا بتشوف موجود كام مره في ال listبديها عنصر 

d = [1, 2, 3, 4, 3, 9, 10, 1, 2, 1]
print(d.count(1))

# index() بتجيب ال index بتاع عنصر في ال list

e = ["Osama", "Ahmed", "Sayed", "Ramy", "Ahmed", "Ramy"]
print(e.index("Ramy"))

# insert()بضيف عنصر قبل ال index الي انا مدهولها 

f = [1, 2, 3, 4, 5, "A", "B"]
f.insert(0, "Test")
f.insert(-1, "Test")

print(f)

# pop() بتطبع العنصر بالانديكس بتاعه

g = [1, 2, 3, 4, 5, "A", "B"]
print(g.pop(-3))
#=======================================TUPLE======================================================================
#=======================================TUPLE======================================================================
#=======================================TUPLE======================================================================
#=======================================TUPLE======================================================================


# Tuple Syntax & Type Test

myAwesomeTupleOne = ("Osama", "Ahmed")
myAwesomeTupleTwo = "Osama", "Ahmed"

print(myAwesomeTupleOne)#TUPLE
print(myAwesomeTupleTwo)#STRING

print(type(myAwesomeTupleOne))
print(type(myAwesomeTupleTwo))

# Tuple Indexing

myAwesomeTupleThree = (1, 2, 3, 4, 5)
print(myAwesomeTupleThree[0])
print(myAwesomeTupleThree[-1])
print(myAwesomeTupleThree[-3])

# Tuple Assign Values هنا مش ةزي ال list يعني مش بقدر اعدل عنصر جوه القوس

myAwesomeTupleFour = (1, 2, 3, 4, 5)
# myAwesomeTupleFour[2] = "Three"
# print(myAwesomeTupleFour)  # 'tuple' object does not support item assignment

# Tuple Data ممكن عادي العناصر الي جوه القواس مش نفس ال data type

myAwesomeTupleFive = ("Osama", "Osama", 1, 2, 3, 100.5, True)
print(myAwesomeTupleFive[1])
print(myAwesomeTupleFive[-1])



# Tuple With One Element 

myTuple1 = ("Osama",)# بحط الكومه هنا علشان اعرفه انها tuple مش string
myTuple2 = "Osama", #بحط الكومه هنا علشان اعرفه انها tuple مش string

print(myTuple1)
print(myTuple2)

print(type(myTuple1))
print(type(myTuple2))

print(len(myTuple1))
print(len(myTuple2))

# Tuple Concatenation

a = (1, 2, 3, 4)
b = (5, 6)

c = a + b
d = a + ("A", "B", True) + b

print(c)
print(d)

# Tuple, List, String Repeat (*)  بستخدم العلامه بتاعة الضرب علشان لو عاوز اكرر العناصر الي موجوده في ال تلاته دول بعدد معين

myString = "Osama"
myList = [1, 2]
myTuple = ("A", "B")

print(myString * 6)
print(myList * 6)
print(myTuple * 6)

# Methods => count()  بتعد العناصر الي لاجوه ال tuple

a = (1, 3, 7, 8, 2, 6, 5, 8)
print(a.count(8))

# Methods => index()

b = (1, 3, 7, 8, 2, 6, 5)
# print("The Position of Index Is: " + b.index(7))  # Error
print("The Position of Index Is: {:d}".format(b.index(7)))
print(f"The Position of Index Is: {b.index(7)}")

# Tuple Destruct

a = ("A", "B", 4, "C") #   نا باسين القيمه لكل متغير  ال x=A و هكذا و لو عاوز اكنسل عنصر بحط اندر سكور مكانه

x, y, _, z = a

print(x)
print(y)
print(z)

#===================================================SIT======================================================
#===================================================SIT======================================================
#===================================================SIT======================================================
#===================================================SIT======================================================
# [1] Set Items Are Enclosed in Curly Braces بتتعمل في القواس دي{}
# [2] Set Items Are Not Ordered And Not Indexed ملهاش انديكس لان العناصر فيها مش مرتبه
# [3] Set Indexing and Slicing Cant Be Done مينعش اعملها slicing لان الاندكس مش موجود
# [4] Set Has Only Immutable Data Types (Numbers, Strings, Tuples) List and Dict Are Not  مينعش احط جواها ال list او tuple
# [5] Set Items Is Unique مينفعش عنصر يتقرر فيها
# -----------------------------

# Not Ordered And Not Indexed

mySetOne = {"Osama", "Ahmed", 100}
print(mySetOne)
# print(mySetOne[0])

# Slicing Cant Be Done

mySetTwo = {1, 2, 3, 4, 5, 6}
# print(mySetTwo[0:3])

# Has Only Immutable Data Types

# mySetThree = {"Osama", 100, 100.5, True, [1, 2, 3]} # unhashable type: 'list'
mySetThree = {"Osama", 100, 100.5, True, (1, 2, 3)}

print(mySetThree)

# Items Is Unique

mySetFour = {1, 2, "Osama", "One", "Osama", 1}
print(mySetFour)

# -----------------
# -- Set Methods --
# -----------------

# clear() بتمسح العناصر الي في ال sit 

a = {1, 2, 3}
a.clear()
print(a)

# union() بتعمل اتحاد لكذا sit مع بعض

b = {"One", "Two", "Three"}
c = {"1", "2", "3"}
x = {"Zero", "Cool"}

print(b | c)
print(b.union(c, x))

# add() بضيف عنصر للsit بتاعتي

d = {1, 2, 3, 4}
d.add(5)
d.add(6)
print(d)

# copy() بتنسخ عنصر ال sit بس لو ضيفت عنصر جديد بيضاف علي الاصل مش عالي النسخه

e = {1, 2, 3, 4}
f = e.copy()

print(e)
print(f)

e.add(6)

print(e)
print(f)

# remove() بتمسح عنصر معين

g = {1, 2, 3, 4}
g.remove(1)
# g.remove(7) لان العنصر مش موجود
print(g)

# discard() زي ال remve بس مش بطلع error لو تلقت العنصر الي انا طالب منها تمسحه مش موجود

h = {1, 2, 3, 4}
h.discard(1)
h.discard(7)
print(h)

# pop() بقدر اطلع بيها عنصر من sit زي ال tuple و list بس الفرق ان دي مش بتاخد انديكس فكل مره بطلع عنصر مختلف من sit

i = {"A", True, 1, 2, 3, 4, 5}
print(i.pop())

# update() زي ال union بضبف ال sit علي الي قبلها 

j = {1, 2, 3}
k = {1, "A", "B", 2}
j.update(['Html', "Css"])
j.update(k)

print(j)


# -----------------
# -- Set Methods --
# -----------------

# difference() بطلع العناصر الي موجوده في sit الا,له مش موجوده في الباقي

a = {1, 2, 3, 4}
b = {1, 2, 3, "Osama", "Ahmed"}
print(a)
print(a.difference(b))  # a - b is other syntax 
print(a)

print("=" * 40)  # Separator

# difference_update() بتعمل updata للنتيجه في ال oragnal sit

c = {1, 2, 3, 4}
d = {1, 2, "Osama", "Ahmed"}
print(c)
c.difference_update(d)  # c - d
print(c)

print("=" * 40)  # Separator

# intersection()بتجيب العناصر ىفي متكرره في sits


e = {1, 2, 3, 4, "X", "Osama"}
f = {"Osama", "X", 2}
print(e)
print(e.intersection(f))  # e & f
print(e)

# print("=" * 40)  # Separator

# intersection_update() طبعلي العناصر المتشابها و ساب الباقي

g = {1, 2, 3, 4, "X", "Osama"}
h = {"Osama", "X", 2}
print(g)
g.intersection_update(h)  # g & h
print(g)

print("=" * 40)  # Separator

# symmetric_difference() بيطلع الحاجات الي مش موجوده في الاتنين

i = {1, 2, 3, 4, 5, "X"}
j = {"Osama", "Zero", 1, 2, 4, "X"}
print(i)
print(i.symmetric_difference(j))  # i ^ j
print(i)

print("=" * 40)  # Separator

# symmetric_difference_update() 

k = {1, 2, 3, 4, 5, "X"}
l = {"Osama", "Zero", 1, 2, 4, "X"}
print(k)
k.symmetric_difference_update(l)  # k ^ l
print(k)





# issuperset()لو عاوز اعرف كل العناصر الي في ال sit التانيه موجودف في الاوله

a = {1, 2, 3, 4}
b = {1, 2, 3}
c = {1, 2, 3, 4, 5}

print(a.issuperset(b))  # Trueيعني كده كل العناصر الي في B موجوده في A
print(a.issuperset(c))  # False

print("=" * 50)

# issubset() يعني لازم الاوله تكون هي الي نفس التانيه issupersetعكس ال  

d = {1, 2, 3, 4}
e = {1, 2, 3}
f = {1, 2, 3, 4, 5}

print(d.issubset(e))  # False
print(d.issubset(f))  # True

print("=" * 50)

# isdisjoint() بتعرف لو الSITS فيهم ارقام ةمتشابهه ولا لاء

g = {1, 2, 3, 4}
h = {1, 2, 3}
i = {10, 11, 12}

print(g.isdisjoint(h))  # False مش منفصلين 
print(g.isdisjoint(i))  # True منفصلين 

#=============================================Dictionary===========================================================
#=============================================Dictionary===========================================================
#=============================================Dictionary===========================================================

#[1] Dict Items Are Enclosed in Curly Braces
# [2] Dict Items Are Contains Key : Value
# [3] Dict Key Need To Be Immutable => (Number, String, Tuple) List Not Allowed
# [4] Dict Value Can Have Any Data Types
# [5] Dict Key Need To Be Unique
# [6] Dict Is Not Ordered You Access Its Element With Key
# ----------------------------

# Dictionary
#syntax
user = {
  "name": "Osama",
  "age": 36,
  "country": "Egypt",
  "skills": ["Html", "Css", "JS"],
  "rating": 10.5
}

print(user)
print(user['country'])
print(user.get("country")) #OTHER METHOD

print(user.keys())#countryb is name key #and egypt is name value
print(user.values())#countryb is name key #and egypt is name value

# Two-Dimensional Dictionary    INSTED DICTIONARY

languages = {#IS A SYNTAX FOR  INSTED DICTIONARY

  "One": {
    "name": "Html",
    "progress": "80%"
  },
  "Two": {
    "name": "Css",
    "progress": "90%"
  },
  "Three": {
    "name": "Js",
    "progress": "90%"
  }
}
# WHEN I WANT ACCES TO INSTED DICTIONARY
print(languages)
print(languages['One'])
print(languages['Three']['name'])

# Dictionary Length

print(len(languages))# COUNT THE DICTIONARY
print(len(languages["Two"]))

# Create Dictionary From Variables

frameworkOne = {
  "name": "Vuejs",
  "progress": "80%"
}

frameworkTwo = {
  "name": "ReactJs",
  "progress": "80%"
}

frameworkThree = {
  "name": "Angular",
  "progress": "80%"
}

allFramework = {
  "one": frameworkOne,
  "two": frameworkTwo,
  "three": frameworkThree
}

print(allFramework)

# ------------------------
# -- Dictionary Methods --
# ------------------------

# clear() Dictionary بتفضي العناصر الي في ال 

user = {
  "name": "Osama"
}
print(user)
user.clear()
print(user)

print("=" * 50)

# update()   Dictionaryبتخليني اضيف عناصر جديده في ال 

member = {
  "name": "Osama"
}
print(member)
member["age"] = 36 #FIRST METHOD FOR ADDING NEW ITIME IN Dictionary
member["age"] = 36 
print(member)
member.update({"country": "Egypt"})#SECAND METHOD FOR ADDING NEW ITIME IN Dictionary
print(member)

print("=" * 50)

# copy() COPY ITEMS IN Dictionary

main = {
  "name": "Osama"
}

b = main.copy()
print(b)
main.update({"skills": "Fighting"})
print(main)
print(b)

# keys() + values()

print(main.keys())
print(main.values())


# setdefault()هنا بحط اسم  جديد لو اتلقاه في الاصل مش بيغيره اما لو متلقهوش بيضيف الي انا مدهولوه

user = {
  "name": "Osama"
}
print(user)
print(user.setdefault("age", 36))
print(user)

print("=" * 40)

# popitem() بيطلع اخر عنصر انا ضيفته في ال ديكشيناري

member = {
  "name": "Osama",
  "skill": "PS4"
}
print(member)
member.update({"age": 36})
print(member.popitem())

print("=" * 40)

# items() بيحتفظ في البيانات الي انا ضيفتها حتي لو مسحتها

view = {
  "name": "Osama",
  "skill": "XBox"
}

allItems = view.items()
print(view)
view["age"] = 36

print(allItems)

print("=" * 40)

# fromkeys() بينشأ ديكشيناري فاضي من الديكشيناري الي انا مدهالوه

a = ('MyKeyOne', 'MyKeyTwo', 'MyKeyThree')

b = "X"

print(dict.fromkeys(a, b))









