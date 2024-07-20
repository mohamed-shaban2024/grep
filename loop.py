# -------------------
# -- Loop => While --
# -------------------
# while condition_is_true
#   Code Will Run Until Condition Become False
# -----------------------

a = 0

while a < 15:

  print(a)

  a += 1  # a = a + 1

print("Loop is Done")  # True Become False

while False:#مش هيطبع حاجه علشان مفيش شرط هيتحقق

  print("Will Not Print")








# ----------------------------
# -- Loop => While Training --
# ----------------------------
# while condition_is_true
#   Code Will Run Until Condition Become False
# -----------------------

myF = ["Os", "Ah", "Ga", "Al", "Ra", "Sa", "Ta", "Ma", "Mo", "Wa"]

# print(len(myF))  # List Length [10]

a = 0

while a < len(myF):  # a < 10

  print(f"#{str(a + 1).zfill(3)} {myF[a]}")#.zfill بتزود اصفار قبل العدد زي منال عاوز

  a += 1  # a = a + 1

else:

  print("All Friends Printed To Screen.")

# print(myF[0])
# print(myF[1])
# print(myF[2])
# print(myF[3])
# print(myF[4])
# print(myF[5])
# print(myF[6])
# print(myF[7])
# print(myF[8])
# print(myF[9])






# ----------------------------
# -- Loop => While Training --
# -- Simple Bookmark Manage --
# ----------------------------

# Empty List To Fill Later
myFavouriteWebs = []

# Maximum Allowed Websites
maximumWebs = 5

while maximumWebs > 0:

  # Input The New Website
  web = input("Website Name Without https:// ")

  # Add The New Website To The List
  myFavouriteWebs.append(f"https://{web.strip().lower()}")

  # Decrease One Number From Allowed Websites
  maximumWebs -= 1  # maximumWebs = maximumWebs - 1

  # Print The Add Message
  print(f"Website Added, {maximumWebs} Places Left")

  # Print The List
  print(myFavouriteWebs)

else:

  print("Bookmark Is Full, You Cant Add More")

# Check If List Is Not Empty
if len(myFavouriteWebs) > 0:

  # Sort The List
  myFavouriteWebs.sort()

  index = 0

  print("Printing The List Of Websites in Your Bookmark")

  while index < len(myFavouriteWebs):

    print(myFavouriteWebs[index])

    index += 1  # index = index + 1





# ----------------------------
# -- Loop => While Training --
# -- Simple Password Guess --عاوز ادي الراجل الي بيدخل ال password عدد معين من المحاولات
# ----------------------------

tries = 4

mainPassword = "Osama@123"

inputPassword = input("Write Your Password: ")

while inputPassword != mainPassword:  # True

  tries -= 1  # tries = tries - 1

  print(f"Wrong Password, { 'Last' if tries == 0 else tries } Chance Left")

  inputPassword = input("Write Your Password: ")

  if tries == 0:

    print("All Tries Is Finished.")

    break

    print("Will Not Print")

else:

  print("Correct Password")


#===============================================================================================
#===============================================================================================
#===============================================================================================
#===============================================================================================


# -----------------
# -- Loop => For --
# -----------------
# for item in iterable_object :
#   Do Something With Item
# -----------------------------
# item Is A Vairable You Create and Call Whenever You Want
# item refer to the current position and will run and visit all items to the end
# iterable_object => Sequence [ list, tuples, set, dict, string of charcaters, etc ... ]
# ---------------------------------------------------------------

myNumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for number in myNumbers:

  # print(number * 17)

  if number % 2 == 0:  # Even

    print(f"The Number {number} Is Even.")

  else:

    print(f"The Number {number} Is Odd.")

else:

  print("The Loop Is Finished")

myName = "Osama"

for letter in myName:

  print(f" [ {letter.upper()} ] ")



# -----------------
# -- Loop => For --
# -- Nested Loop --
# -----------------

peoples = ["Osama", "Ahmed", "Sayed", "Ali"]

skills = ['Html', 'Css', 'Js']

for name in peoples:  # Outer Loop

  print(f"{name} Skills Is: ")

  for skill in skills:  # Inner Loop

    print(f"- {skill}")

# Dictionary

peoples = {
  "Osama": {
    "Html": "70%",
    "Css": "80%",
    "Js": "70%"
  },
  "Ahmed": {
    "Html": "90%",
    "Css": "80%",
    "Js": "90%"
  },
  "Sayed": {
    "Html": "70%",
    "Css": "60%",
    "Js": "90%"
  }
}

print(peoples["Osama"])
print(peoples["Ahmed"])
print(peoples["Sayed"])

print(peoples["Osama"]['Css'])
print(peoples["Ahmed"]['Css'])
print(peoples["Sayed"]['Css'])

for name in peoples:

  print(f"Skills and Progress For {name} Is: ")

  for skill in peoples[name]:

    print(f"{skill.upper()} => {peoples[name][skill]}")







# ---------------------------
# -- Break, Continue, Pass -- ممكن تستخدم في لاكذا حاجه غير ال loop
# ---------------------------

myNumbers = [1, 2, 3, 5, 7, 10, 13, 14, 15, 19]

# Continue  لو لما بتقف عند العنصر الي انا قيلها عليه بتسيبه و تكلمل اللوب 

for number in myNumbers:
# print(number)



  if number == 13:#



    continue#يعني هنا هتسي ال 13 و تكمل اللوب


  print(number)

print("#" * 50)

# Break بيوقف الللوب اول لما بقوله

for number in myNumbers:

  if number == 13:

    break# يعني هنا هيوقف اللوب عند ال13

  print(number)

print("#" * 50)

# Pass بستدخدمها لو فيه مثلا function فاضي و عاوز اعديه من غير ميطلعلي error

for number in myNumbers:

  if number == 13:

    pass

  print(number)





# ------------------------------
# -- Advanced Dictionary Loop --
# ------------------------------

mySkills = {
  "HTML": "80%",
  "CSS": "90%",
  "JS": "70%",
  "PHP": "80%"
}

print(mySkills.items())

#######################

for skill in mySkills:

  print(f"{skill} => {mySkills[skill]}")

#######################

for skill_key, skill_progress in mySkills.items():

  print(f"{skill_key} => {skill_progress}")
##################################################################

myUltimateSkills = {
  "HTML": {
    "Main": "80%",
    "Pugjs": "80%"
  },
  "CSS": {
    "Main": "90%",
    "Sass": "70%"
  }
}

for main_key, main_value in myUltimateSkills.items():

  print(f"{main_key} Progress Is: ")

  for child_key, child_value in main_value.items():

    print(f"- {child_key} => {child_value}")




