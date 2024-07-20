# -----------------------------------
# -- Errors And Exceptions Raising --
# -----------------------------------
# [1] Exceptions Is A Runtime Error Reporting Mechanism
# [2] Exception Gives You The Message To Understand The Problem#اليه بتديك تقرير عن الاخطاء بتاعتك في الكود
# [3] Traceback Gives You The Line To Look For The Code in This Line
# [4] Exceptions Have Types (SyntaxError, IndexError, KeyError, Etc...)
# [5] Exceptions List https://docs.python.org/3/library/exceptions.html#فيه انوع error
# [6] raise Keyword Used To Raise Your Own Exceptions#ازاي احط exception بنفسي
# -----------------------------------------------------------------

x = -10

if x < 0:

  raise Exception(f"The Number {x} Is Less Than Zero")#هيوقف الكود هنا لو الرقم اصغر من  الصفر

  print("This Will Not Print Because The Error")

else:

  print(f"{x} Is Good Number and Ok")

print('Print Message After If Condition')

y = 10#مثال تاني 

if type(y) != int:

  raise ValueError("Only Numbers Allowed")

print('Print Message After If Condition')




# -----------------------------------
# --      Exceptions Handling      --
# -- Try | Except | Else | Finally --
# -----------------------------------
# Try     => Test The Code For Errors
# Except  => Handle The Errors
# ----------------------------
# Else    => If No Errors
# Finally => Run The Code
# ------------------------

number = int(input("Write Your Age: "))

print(number)
print(type(number))

try:  # Try The Code and Test Errors

  number = int(input("Write Your Age: "))

  print("Good, This Is Integer From Try")

except:  # Handle The Errors If Its Found

  print("Bad, This is Not Integer")

else:  # If Theres No Errors لو مفيش غلط

  print("Good, This Is Integer From Else")

finally:#بتطبع الكود مهما حصل

  print("Print From Finally Whatever Happens")


try:#بتختبر الكود 

  # print(10 / 0)
  # print(x)
  print(int("Hello"))
#تحت انا بحدد نوع ال ERROR
except ZeroDivisionError:#لازم تكون موجوده مع ال TRY علشان تهندل الكود بتاعك

  print("Cant Divide")

except NameError:

  print("Identifier Not Found")

except ValueError:

  print("Value Error Elzero")

except:

  print("Error Happens")



#فكره البرنامج ان انا لو عاوز اعمل عددمحاولات لشخص انه يفتح الملف و لو عرف يبفتحه هيقرء الي فيه
 # -----------------------------------
# --      Exceptions Handling      --
# -- Try | Except | Else | Finally -

# --       Advanced Example        --
# -----------------------------------

the_file = None

the_tries = 5

while the_tries > 0:

  try:  # Try To Open The File

    print("Enter The File Name With Absolute Path To Open")

    print(f"You Have {the_tries} Tries Left")

    print("Example: D:\Python\Files\yourfile.extension")

    file_name_and_path = input("File Name => : ").strip()

    the_file = open(file_name_and_path, 'r')

    print(the_file.read())

    break

  except FileNotFoundError:

    print("File Not Found Please Be Sure The Name is Valid")

    the_tries -= 1

  except:

    print("Error Happen")

  finally:

    if the_file is not None:

      the_file.close()

      print("File Closed.")

else:

  print("All Tries Is Done") 