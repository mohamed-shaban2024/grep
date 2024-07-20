# #103
# # ------------------------------------------
# # -- Object Oriented Programming => Intro --
# # ------------------------------------------
# # [1] Python Support Object Oriented Programming
# # [2] OOP Is A Paradigm Or Coding Style
# #     OOP Paradigm =>
# #       Means Structuring Program So The Methods[Functions] and Attributes[Data]
# #       Are Bundled Into Objects
# # [3] Methods => Act As Function That Use The Information Of The Object
# # [4] Python Is Multi-Paradigm Programming Language [Procedural, OOP, Functional]
# #     - Procedural => Structure App Like Recipe, Sets Of Steps To Make The Task
# #     - Functional => Built On the Concept of Mathematical Functions
# # [5] OOP Allow You To Organize Your Code and Make It Readable and Reusable
# # [6] Everything in Python is Object
# # [7] If Man Is Object
# #     - Attributes => Name, Age, Address, Phone Number, Info [Can Be Differnet]
# #     - Methods[Behaviors] => Walking, Eating, Singing, Playing
# # [8] If Car Is Object
# #     - Attributes => Model, Colour, Price
# #     - Methods[Behaviors] => Walking, Stopping
# # [9] Class Is The Template For Creating Objects [Object Constructor | Blueprint]
# #     - Class Car Can Create Many Cars Object
# # ---------------------------------------------


# #104
# # ----------------------------------------------------------
# # -- Object Orie1nted Programming => Class Syntax and Info --
# # ----------------------------------------------------------
# # [01] Class is The Blueprint Or Construtor Of The Object
# # [02] Class Instantiate Means Create Instance of A Class
# # [03] Instance => Object Created From Class And Have Their Methods and Attributes
# # [04] Class Defined With Keyword class
# # [05] Class Name Written With PascalCase [UpperCamelCase] Style
# # [06] Class May Contains Methods and Attributes
# # [07] When Creating Object Python Look For The Built In __init__ Method
# # [08] __init__ Method Called Every Time You Create Object From Class
# # [09] __init__ Method Is Initialize The Data For The Object
# # [10] Any Method With Two Underscore in The Start and End Called Dunder or Magic Method
# # [11] self Refer To The Current Instance Created From The Class And Must Be First Param
# # [12] self Can Be Named Anything
# # [13] In Python You Dont Need To Call new() Keyword To Create Object
# # -------------------------------------------------------------------

# # Syntax
# # class Name:
# #     Constructor => Do Instantiation [ Create Instance From A Class ]
# #     Each Instance Is Separate Object
# #     def __init__(self, other_data)
# #         Body Of Function


# class Member:         #this is keywords 


#   def __init__(self):

#     print("A New Member Has Been Added")

# member_one = Member()
# member_two = Member()
# member_three = Member()

# print(member_one.__class__)#بعمل كده لو عاوز اعرف ال CLASS بتاعي بيعمل ايه الي هو هنا مثلا بيطبع "A New Member Has Been Added"

# my_dictionary = {
#   'name': "Osama",
#   'age': 36,
#   'monthly_salary': 5000,
#   'yearly_salary': ''  # Something
# }





# #105
# # --------------------------------------------------------------------
# # -- Object Oriented Programming => Instance Attributes and Methods --
# # --------------------------------------------------------------------
# # Self: Point To Instance Created From Class
# # Instance Attributes: Instance Attributes Defined Inside The Constructor
# # -----------------------------------------------------------------------
# # Instance Methods: Take Self Parameter Which Point To Instance Created From Class
# # Instance Methods Can Have More Than One Parameter Like Any Function
# # Instance Methods Can Freely Access Attributes And Methods On The Same Object
# # Instance Methods Can Access The Class Itself
# # -----------------------------------------------------------

# class Member:
#   def __init__(self, first_name, middle_name, last_name):
#     self.fname = first_name
#     self.mname = middle_name
#     self.lname = last_name

# member_one = Member("Osama", "Mohamed", "Elsayed")
# member_two = Member("Ahmed", "Ali", "Mahmoud")
# member_three = Member("Mona", "Ali", "Mahmoud")

# # print(dir(member_one))

# print(member_one.fname, member_one.mname, member_one.lname)
# print(member_two.fname)
# print(member_three.fname)





# #106
# # --------------------------------------------------------------------
# # -- Object Oriented Programming => Instance Attributes and Methods --
# # --------------------------------------------------------------------
# # Self: Point To Instance Created From Class
# # Instance Attributes: Instance Attributes Defined Inside The Constructor
# # -----------------------------------------------------------------------
# # Instance Methods: Take Self Parameter Which Point To Instance Created From Class
# # Instance Methods Can Have More Than One Parameter Like Any Function
# # Instance Methods Can Freely Access Attributes And Methods On The Same Object
# # Instance Methods Can Access The Class Itself
# # -----------------------------------------------------------

# class Member:
#   def __init__(self, first_name, middle_name, last_name, gender):
#     self.fname = first_name
#     self.mname = middle_name
#     self.lname = last_name
#     self.gender = gender

#   def full_name(self):
#     return f"{self.fname} {self.mname} {self.lname}"

#   def name_with_title(self):
#     if self.gender == "Male":
#       return f"Hello Mr {self.fname}"
#     elif self.gender == "Female":
#       return f"Hello Miss {self.fname}"
#     else:
#       return f"Hello {self.fname}"

#   def get_all_info(self):
#     return f"{self.name_with_title()}, Your Full Name Is: {self.full_name()}"


# member_one = Member("Osama", "Mohamed", "Elsayed", "Male")
# member_two = Member("Ahmed", "Ali", "Mahmoud", "Male")
# member_three = Member("Mona", "Ali", "Mahmoud", "Female")

# # print(dir(member_one))

# # print(member_one.fname, member_one.mname, member_one.lname)
# # print(member_two.fname)
# # print(member_three.fname)

# # print(member_two.full_name())
# # print(member_two.name_with_title())

# print(member_one.get_all_info())






# #107
# # -----------------------------------------------------
# # -- Object Oriented Programming => Class Attributes --
# # -----------------------------------------------------
# # Class Attributes: Attributes Defined Outside The Constructor
# # -----------------------------------------------------------

# class Member:

#   not_allowed_names = ["Hell", "Shit", "Baloot"]

#   users_num = 0

#   def __init__(self, first_name, middle_name, last_name, gender):

#     self.fname = first_name

#     self.mname = middle_name

#     self.lname = last_name

#     self.gender = gender

#     Member.users_num += 1  # Member.users_num = Member.users_num + 1

#   def full_name(self):

#     if self.fname in Member.not_allowed_names:

#       raise ValueError("Name Not Allowed")

#     else:

#       return f"{self.fname} {self.mname} {self.lname}"

#   def name_with_title(self):

#     if self.gender == "Male":

#       return f"Hello Mr {self.fname}"

#     elif self.gender == "Female":

#       return f"Hello Miss {self.fname}"

#     else:

#       return f"Hello {self.fname}"

#   def get_all_info(self):

#     return f"{self.name_with_title()}, Your Full Name Is: {self.full_name()}"

#   def delete_user(self):

#     Member.users_num -= 1  # Member.users_num = Member.users_num -1

#     return f"User {self.fname} Is Deleted."


# print(Member.users_num)




# member_one = Member("Osama", "Mohamed", "Elsayed", "Male")
# member_two = Member("Ahmed", "Ali", "Mahmoud", "Male")
# member_three = Member("Mona", "Ali", "Mahmoud", "Female")
# member_four = Member("Shit", "Hell", "Metal", "DD")

# print(Member.users_num)

# print(member_four.delete_user())
            
# print(Member.users_num)

# print(dir(member_one))

# print(member_one.fname, member_one.mname, member_one.lname)
# print(member_two.fname)
# print(member_three.fname)

# print(member_two.full_name())
# print(member_two.name_with_title())

# print(member_three.get_all_info())

# print(dir(Member))







# #108
# # -------------------------------------------------------------------
# # -- Object Oriented Programming => Class Methods & Static Methods --
# # -------------------------------------------------------------------
# # Class Methods:
# # - Marked With @classmethod Decorator To Flag It As Class Method
# # - It Take Cls Parameter Not Self To Point To The Class not The Instance   # ال pramiter الي فيها مش self زي ال instancemethod لا بيضاف ليها cls
# # - It Doesn't Require Creation of a Class Instance
# # - Used When You Want To Do Something With The Class Itself
# # Static Methods:#مش بحطلها pramiter 
# # - It Takes No Parameters
# # - Its Bound To The Class Not Instance
# # - Used When Doing Something Doesnt Have Access To Object Or Class But Related To Class
# # -----------------------------------------------------------

# class Member:

#   not_allowed_names = ["Hell", "Shit", "Baloot"]

#   users_num = 0

#   @classmethod
#   def show_users_count(cls):

#     print(f"We Have {cls.users_num} Users In Our System.")

#   @staticmethod
#   def say_hello():

#     print("Hello From Static Method")

#   def __init__(self, first_name, middle_name, last_name, gender):

#     self.fname = first_name

#     self.mname = middle_name

#     self.lname = last_name

#     self.gender = gender

#     Member.users_num += 1  # Member.users_num = Member.users_num + 1

#   def full_name(self):

#     if self.fname in Member.not_allowed_names:

#       raise ValueError("Name Not Allowed")

#     else:

#       return f"{self.fname} {self.mname} {self.lname}"

#   def name_with_title(self):

#     if self.gender == "Male":

#       return f"Hello Mr {self.fname}"

#     elif self.gender == "Female":

#       return f"Hello Miss {self.fname}"

#     else:

#       return f"Hello {self.fname}"

#   def get_all_info(self):

#     return f"{self.name_with_title()}, Your Full Name Is: {self.full_name()}"

#   def delete_user(self):

#     Member.users_num -= 1  # Member.users_num = Member.users_num -1

#     return f"User {self.fname} Is Deleted."



# print(Member.users_num)

# member_one = Member("Osama", "Mohamed", "Elsayed", "Male")
# member_two = Member("Ahmed", "Ali", "Mahmoud", "Male")
# member_three = Member("Mona", "Ali", "Mahmoud", "Female")
# member_four = Member("Shit", "Hell", "Metal", "DD")

# print(Member.users_num)
# print(member_four.delete_user())
# print(Member.users_num)

# print("#" * 50)

# Member.show_users_count()

# print("#" * 50)

# print(member_one.full_name())
# print(Member.full_name(member_one))

# Member.say_hello()


# class food :#based class
#   def __init__ (self,name,price):
#       self.name = name
#       self.price = price
#       print (f"{self.name}is created from base class")

#   def eat (self):#derived class
#     print ("eat method from base class")
    

#     class apple: #(food) :
#       def __init__ (self,name,price):
#         print ("apple is created from derived class")
#     food_one = food () 
#     food_two = apple () 
#     food_two.eat  ()  






