# -----------------------------------
# -- Date and Time => Introduction --
# -----------------------------------

import datetime

# print(dir(datetime))
# print(dir(datetime.datetime))#datetimeعباره عن module جوه ال package

# Print The Current Date and Time
print(datetime.datetime.now())#هترجع توقيت جرينتش

print("#" * 40)

# Print The Current Year#ده لو عاوز اعمل السنه لو حدها
print(datetime.datetime.now().year)

# Print The Current Month
print(datetime.datetime.now().month)

# Print The Current Day
print(datetime.datetime.now().day)

print("#" * 40)

# Print Start and End Of Date
print(datetime.datetime.min)#بتجيب البدايه للتوقيت
print(datetime.datetime.max)#بتجيب النهايه بتاعة التوقيت

print("#" * 40)

# print(dir(datetime.datetime.now()))

# Print The Current Time
print(datetime.datetime.now().time())#return part time

print("#" * 40)

# Print The Current Time Hour
print(datetime.datetime.now().time().hour)

# Print The Current Time Minute
print(datetime.datetime.now().time().minute)

# Print The Current Time Second
print(datetime.datetime.now().time().second)

print("#" * 40)

# Print Start and End Of Time
print(datetime.time.min)
print(datetime.time.max)

print("#" * 40)

# Print Specific Date
print(datetime.datetime(1982, 10, 25))#لو انا عاوز اطبع تريخ بنفسي
print(datetime.datetime(1982, 10, 25, 10, 45, 55, 150364))

print("#" * 40)

myBirthDay = datetime.datetime(1982, 10, 25)
dateNow = datetime.datetime.now()

print(f"My Birthday is {myBirthDay} And ", end="")
print(f"Date Now Is {dateNow}")

print(f" I Lived For {dateNow - myBirthDay}")
print(f" I Lived For {(dateNow - myBirthDay).days} Days.")#برجع الايام بس






# ----------------------------------
# -- Date and Time => Format Date --
# ----------------------------------
# https://strftime.org/
# ---------------------

import datetime

myBirthday = datetime.datetime(1982, 10, 25)#strfteim بتحول الوقت الي انا عاوزه من رقم الي STRINGوممكن ابحث عنها في جوجل تجيبلي كل ال FORMATING الي انا عوزها

print(myBirthday)
print(myBirthday.strftime("%a"))# a بطلع الايام او الشهور بالاختصار
print(myBirthday.strftime("%A"))#Aبطلع ال الايام او الشهور من غير اختصار
print(myBirthday.strftime("%b"))
print(myBirthday.strftime("%B"))#الشهر

print(myBirthday.strftime("%d %B %Y"))#السنه والشهر و الايام 
print(myBirthday.strftime("%d, %B, %Y"))
print(myBirthday.strftime("%d/%B/%Y"))
print(myBirthday.strftime("%d - %B - %Y"))
print(myBirthday.strftime("%B - %Y"))