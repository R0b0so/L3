text = int(input("enter the temprature (degrees)"))
if text >= 15:
   print("Wear a t shirt")
elif text <= 14 and text >= 8:
   print("Wear a sweater")
elif text <= 7 and text >= -1:
   print("Wear a light jacket")
elif text <= -2:
   print("Wear a thick jacket")
