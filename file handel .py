#part 1
# -------------------
# -- File Handling --
# -------------------
# "a" Append  Open File For Appending Values, Create File If Not Exists
# "r" Read    [Default Value] Open File For Read and Give Error If File is Not Exists
# "w" Write   Open File For Writing, Create File If Not Exists
# "x" Create  Create File, Give Error If File Exists
# --------------------------------------------------

import os

# Main Current Working Directory
print(os.getcwd()) #بستخدمها لو انا عاوز اعرف المسار بتاع الفايل

# Directory For The Opened File
print(os.path.dirname(os.path.abspath(__file__)))

# Change Current Working Directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))

print(os.getcwd())

print(os.path.abspath(__file__))

file = open(r"D:\Python\Files\nfiles\osama.txt")#)حرف ال r يعني ملكش دعوه بكل امر جوه القوس زي \n


file = open("D:\Python\Files\osama.txt")


#part 2
# --------------------------------
# -- File Handling => Read File --
# --------------------------------

myFile = open("D:\Python\Files\osama.txt", "r")#الr هنا قصدها ان المبف readable

print(myFile)  # File Data Object بيانات الفيل مش محتوي الفايل 
print(myFile.name)#لو انا عاوز بيانات معينه من الفايل
print(myFile.mode)#لو انا عاوز بيانات معينه من الفايل
print(myFile.encoding)#لو انا عاوز بيانات معينه من الفايل

print(myFile.read())#بحدد بيه عدد العناصر الفي انا عاوز اقرءها
print(myFile.read(5))#بحدد بيه عدد العناصر الفي انا عاوز اقرءها

print(myFile.readline(5))#بيقرء سطر من ال لاfile
print(myFile.readline())
print(myFile.readline())

print(myFile.readlines())# بترجع برضو سطور بس بتبقي نوع البيانات list
print(myFile.readlines(50))
print(type(myFile.readlines()))


#لو انا عاوز اعمل loop علي الفايل 
for line in myFile:

  print(line)

  if line.startswith("07"):# لو انا عاوز اعمل loop  السطورعلي عدد معين من

    break

# Close The File

myFile.close()#بيقفل الفايل


#part 3
# -----------------------------------------------
# -- File Handling => Write and Append In File --لو عاوز افتح ملف و اضيف ليه حاجات من الايديتور
# -----------------------------------------------

myFile = open("D:\Python\Files\osama.txt", "w")
myFile.write("Hello\n")
myFile.write("Third Line")

myFile = open(r"D:\Python\Files\fun.txt", "w")
myFile.write("Elzero Web School\n" * 1000)

myList = ["Oasma\n", "Ahmed\n", "Sayed\n"]

myFile = open("D:\Python\Files\osama.txt", "w")
myFile.writelines(myList)#بيلوب علي ال list و ويطبعها

myFile = open("D:\Python\Files\osama.txt", "a")#Append In File 
myFile.write("Elzero")




#part 4
# -------------------------------------
# -- File Handling => Important Info --
# -------------------------------------

import os#تبع ال remove الي تحت

myFile = open("D:\Python\Files\osama.txt", "a")
myFile.truncate(5)#اقتطاع       باخد 5 حروف بس

myFile = open("D:\Python\Files\osama.txt", "a")
print(myFile.tell())#بتقولي علي مكان الموس ولو عملت انتر و رن هيطلعلي  زايد حلرفين مش حرف علشان \n

myFile = open("D:\Python\Files\osama.txt", "r")
myFile.seek(11) #بيحطلي ال الموس علي المكان الي انا عاوزه علشان لو حبيت اعمل اي append لل file من مكان معين
print(myFile.read())

os.remove("D:\Python\Files\osama.txt")#لما اعوز احزف ملف






