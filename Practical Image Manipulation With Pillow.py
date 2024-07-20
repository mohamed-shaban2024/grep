# -------------------------------------------------
# -- Practical => Image Manipulation With Pillow --#pillow مكتبه بتعمل اي حاجه انا عاوز اعملها في الصور
# -------------------------------------------------

from PIL import Image#لازم اعملها انستول عن طريق انا باجي في الترمنل و اكتب pip install + اسم المكتبه الي هي pillow
# PIL دي الميثود الي في الباكدج الي بتتعامل مع الصور
# Open The Image
myImage = Image.open(r"C:\Users\Dell\Desktop\صوري\.thumbnails")

# Show The Image
myImage.show()

# My Cropped Image
myBox = (300, 300, 800, 800)#الجزء الي انا هقطعه من الصور(LIFT, UPPER ,LOWER ,RIGHT)
myNewImage = myImage.crop(myBox)# اعمل حاجات كتير غير دي ممكن

# Show The New Image
myNewImage.show()

# My Converted Mode Image
myConverted = myImage.convert("L")#بتحول الصوره لابيض و اسود
myConverted.show()

