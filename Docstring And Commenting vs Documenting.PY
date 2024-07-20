# --------------------------------------------
# -- Doc String & Commenting vs Documenting --#معمول علشان افهم الاكواد المعقده او الكبيره
# --------------------------------------------
# [1] Documentation String For Class, Module or Function
# [2] Can Be Accessed From The Help and Doc Attributes
# [3] Made For Understanding The Functionality of The Complex Code#ده COMMETE
# [4] Theres One Line and Multiple Line Doc Strings
# -------------------------------------------------

def elzero_function(name):
  """
  Elzero Function
    It Say Hello From Elzero اما ده DOCUMENT
  Parameter:
    name => Person Name That Use Function
  Return:
    Return Hello Message To The Person
  """
  print(f"Hello {name} From Elzero")

elzero_function("Ahmed")

print(dir(elzero_function))

print(elzero_function.__doc__)#Iهيعرفك الفانكشن الي انا عاملها بتعمل ايه

#يعني مثلا هنا عيقولك It Say Hello From Elzero



help(elzero_function)#نفس كلام ال DOC ATTREBUTE