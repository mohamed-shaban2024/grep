
# # -------------------------
# # -- Function And Return --
# # -------------------------
# # [1] A Function is A Reusable Block Of Code Do A Task
# # [2] A Function Run When You Call It
# # [3] A Function Accept Element To Deal With Called [Parameters]
# # [4] A Function Can Do The Task Without Returning Data
# # [5] A Function Can Return Data After Job is Finished
# # [6] A Function Create To Prevent DRY
# # [7] A Function Accept Elements When You Call It Called [Arguments]
# # [8] There's A Built-In Functions and User Defined Functions
# # [9] A Function Is For All Team and All Apps
# # ----------------------------------------

# def function_name():

#   return "Hello Python From Inside Function"

# dataFromFunction = function_name()

# print(dataFromFunction)




# # ---------------------------------------
# # -- Function Parameters And Arguments --
# # ---------------------------------------

# a, b, c = "Osama", "Ahmed", "Sayed"

# print(f"Hello {a}")
# print(f"Hello {b}")
# print(f"Hello {c}")

# # def                     => Function Keyword [Define]
# # say_hello()             => Function Name
# # name                    => Parameter
# # print(f"Hello {name}")  => Task
# # say_hello("Ahmed")      => Ahmed is The Argument

# def say_hello(n):

#   print(f"Hello {n}")

# say_hello(a)
# say_hello(b)
# say_hello(c)

# def addition(n1, n2):

#   print(n1 + n2)

# addition(100, 300)
# addition(-50, 100)


# def addition(n1, n2):

#   if type(n1) != int or type(n2) != int:

#     print("Only Integers Allowed")

#   else:

#     print(n1 + n2)

# addition(100, 500)

# def full_name(first, middle, last):

#   print(f"Hello {first.strip().capitalize()} {middle.upper():.1s} {last.capitalize()}")

# full_name("   osama   ", 'mohamed', "elsayed")








# # -------------------------------------------------
# # -- Function Packing, Unpacking Arguments *Args --
# # -------------------------------------------------

# print(1, 2, 3, 4)

# myList = [1, 2, 3, 5]

# print(myList)
# print(*myList)

# def say_hello(*peoples):  # n1, n2, n3, n4بالعلامه دي اكني بقوله ان ال peoples هي الي هتتكتب تحت

#   for name in peoples:

#     print(f"Hello {name}")

# say_hello("Osama", "Ahmed", "Sayed", "Mahmoud")

# def show_details(name, *skills):

#   print(f"Hello {name} Your Skills Is: ")

#   for skill in skills:

#     print(skill)

# show_details("Osama", "Html", "CSS", "JS")
# show_details("Ahmed", "Html", "CSS", "JS", "Python", "PHP", "MySQL")




# # ---------------------------------
# # -- Function Default Parameters --
# # ---------------------------------

# def say_hello(name="Unknown", age="Unknown", country="Unknown"):#بستخدمها لما ال user ميدخلش حاجه

#   print(f"Hello {name} Your Age is {age} and Your Country Is {country}")

# say_hello("Osama", 36, "Egypt\n")
# say_hello("Mahmoud", 28, "KSA\n")
# say_hello("Sameh", 38)
# say_hello("Ramy")
# say_hello()

# # ----------------------------------------------------
# # -- Function Packing, Unpacking Arguments **KWArgs --
# # ----------------------------------------------------

# def show_skills(*skills):

#   print(type(skills))

#   for skill in skills:

#     print(f"{skill}")

# show_skills("Html", "CSS", "JS")

# mySkills = {
#   'Html': "80%",
#   'Css': "70%",
#   'Js': "50%",
#   'Python': "80%",
#   "Go": "40%"
# }

# def show_skills(**skills):# **العلامه دي بتفك اللعناصر بتاعت ال dectionary اول لما اعمله run

#   print(type(skills))

#   for skill, value in skills.items():

#     print(f"{skill} => {value}")

# show_skills(**mySkills)




# # -----------------------------------------------------
# # -- Function Packing, Unpacking Arguments Trainings --
# # -----------------------------------------------------

# myTuple = ("Html", "CSS", "JS")

# mySkills = {
#   'Go': "80%",
#   'Python': "50%",
#   'MySQL': "80%"
# }

# def show_skills(name, *skills, **skillsWithProgres):

#   print(f"Hello {name} \nSkills Without Progress Is: ")

#   for skill in skills:

#     print(f"- {skill}")

#   print("Skills With Progress Is: ")

#   for skill_key, skill_value in skillsWithProgres.items():

#     print(f"- {skill_key} => {skill_value}")

# show_skills("Osama", *myTuple, **mySkills)


# #**لل dectionary 
# #* للباقي


# # --------------------
# # -- Function Scope --
# # --------------------

# x = 1  # Global Scope

# def one():

#   global x

#   x = 2

#   print(f"Print Variable From Function Scope {x}")

# def two():

#   x = 10

#   print(f"Print Variable From Function Scope {x}")

# one()
# print(f"Print Variable From Global Scope {x}")
# two()
# print(f"Print Variable From Global Scope After One Function Is Called {x}")










# # ------------------------
# # -- Function Recursion --
# # ------------------------
# # ---------------------------------------------------------------------
# # -- To Understand Recursion, You Need to First Understand Recursion --
# # ---------------------------------------------------------------------

# # Test Word [ WWWoooorrrldd ] # print(x[1:])

# def cleanWord(word):

#   if len(word) == 1:

#     return word

#   print(f"Print Start Function {word}")

#   if word[0] == word[1]:

#     print(f"Print Before Condition {word}")

#     return cleanWord(word[1:])

#   print(f"Print Before Return {word}")

#   return word[0] + cleanWord(word[1:])

#   # Stash [ World ]

# print(cleanWord("WWWoooorrrldd"))





# ------------------------
# -- Function => lambda --
# -- Anonymous Function --#الوظيفة المجهوله
# ------------------------
# [1] It Has No Name
# [2] You Can Call It Inline Without Defining It
# [3] You Can Use It In Return Data From Another Function في ال gerafecal muser inter face
# [4] Lambda Used For Simple Functions and Def Handle The Large Tasks
# [5] Lambda is One Single Expression not Block Of Code
# [6] Lambda Type is Function
# -------------------------------------------------------------------

def say_hello(name, age) : return f"Hello {name} your Age Is: {age}"#this is a normal function syntax

hello = lambda name, age : f"Hello {name} your Age Is: {age}"# this is a Anonymous Function syntax

print(say_hello("Ahmed", 36))
print(hello("Ahmed", 36))

print(say_hello.__name__)# كلمة name بتخليني اعرف اسم ال funct ion
print(hello.__name__)

print(type(hello))









