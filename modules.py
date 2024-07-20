# ---------------------------------
# -- Modules => Built In Modules --
# ---------------------------------
# [1] Module is A File Contain A Set Of Functions فايل فيه فانكشن كتيره بستخدمها
# [2] You Can Import Module in Your App To Help You
# [3] You Can Import Multiple Modules
# [4] You Can Create Your Own Modulesممكن اعملها انا
# [5] Modules Saves Your Time
# --------------------------------------------------

# Import Main Module
import random#بيطلع بيانات عشواءيه
print(random)
print(f"Print Random Float Number {random.random()}")# module . function

# Show All Functions Inside Module
print(dir(random))# بتجيب كل ال function الي موجوده في ال module

# Import One Or Two Functions From Module
from random import randint, random#لو مش عاوز استخدم كل الفانكشن الي موجوده في ال module
print(f"Print Random Float {random()}")
print(f"Print Random Integer {randint(100, 900)}")





# -----------------------------------
# -- Modules => Create Your Module --
# -----------------------------------

import sys#SYS .PATH بتدور علي المسارات بتاعة ال  MODULE
sys.path.append(r"D:\Games")
print(sys.path)

import elzero
print(dir(elzero))

elzero.sayHello("Ahmed")
elzero.sayHello("Osama")
elzero.sayHello("Mohamed")

elzero.sayHowAreYou("Ahmed")
elzero.sayHowAreYou("Osama")
elzero.sayHowAreYou("Mohamed")

# Alias

import elzero as ee#EE اسم مستعار لل ELZERO

ee.sayHello("Ahmed")
ee.sayHello("Osama")
ee.sayHello("Mohamed")

ee.sayHowAreYou("Ahmed")
ee.sayHowAreYou("Osama")
ee.sayHowAreYou("Mohamed")

from elzero import sayHello#كده عملت IMPOTR لل FUNCTION بتاعة ال SAYHELLO بس 

sayHello("Osama")

from elzero import sayHello as ss#SS اسم مستعار لل FUNCTION نفسها

ss("Osama")




#PART 3

# ------------------------------------------
# -- Modules => Install External Packages --
# ------------------------------------------
# [1] Module vs Package#ال PACKAGE عباره عن مجموعه من الMODULES
# [2] External Packages Downloaded From The Internet#لان هي حجمها كبير ف مش بتبقي موجوده في الللغه و بنطر ننزلها
# [3] You Can Install Packages With Python Package Manager PIP
# [4] PIP Install the Package and Its Dependenciesبينزل الحاجه وكل الحاجات الي معتمده عليها
# [5] Modules List "https://docs.python.org/3/py-modindex.html"#ده لينك لو عاوز اشوف ال MODULES الي موجوده
# [6] Packages and Modules Directory "https://pypi.org/"#موقع في PACKAGE الي موجوده في اللغه و اقدر ابحث عنها فيه
# [7] PIP Manual "https://pip.pypa.io/en/stable/reference/pip_install/"#PIP Manual
# ---------------------------------------------------------------------

#لو عاوز اشوف ال PACKAGE موجوده عندي باجي في لاال TERMENAL و اكتب (pip --version)

#لو عاوز اشوف الصدارات بتاعة ال package و ال package نفسها بكتب في ال terminal (pip list)
#لو عاوز اعمل install l package معينه بكتب  (pip install + اسم الحزمه)
import termcolor
import pyfiglet#بيلون الكلام

print(dir(pyfiglet))
print(pyfiglet.figlet_format("Elzero"))
print(termcolor.colored("Elzero", color="yellow"))

print(termcolor.colored(pyfiglet.figlet_format("Elzero"), color="yellow"))