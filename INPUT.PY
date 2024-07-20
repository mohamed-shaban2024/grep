# ----------------
# -- User Input --
# ----------------

fName = input('What\'s Is Your First Name?')
mName = input('What\'s Is Your Middle Name?')
lName = input('What\'s Is Your Last Name?')

fName = fName.strip().capitalize()#STRIP بتعمل ازاله للمسافات
mName = mName.strip().capitalize()#capitalize بتخلي اول حرف من ال input capetal
lName = lName.strip().capitalize()

print(f"Hello {fName} {mName:.1s} {lName} Happy To See You.")#.1S بتخليني اخد اول حرف من ال MNAME


  
# ---------------------------
# -- Practical Slice Email -- اني عاوز المستخدم يدخلي الاميل و انا بفصصهوله
# ---------------------------

theName = input('What\'s Your Name ?').strip().capitalize()
theEmail = input('What\'s Your Email ?').strip()

theUsername = theEmail[:theEmail.index("@")]  #هنا بقوله اقف لغاية ال العالمه دي @
theWebsite = theEmail[theEmail.index("@") + 1:]#المفروض من غير ال +1 دي انه يبدا من عند العلامه@

print(f"Hello {theName} Your Email Is {theEmail}")
print(f"Your Username Is {theUsername} \nYour Website Is {theWebsite}")

# email = "Osama@elzero.org"
# print(email[:email.index("@")])











