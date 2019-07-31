user_input = input()
try:
   if "." in user_input :
     val = float(user_input)
     print("yes")
   else:
      val = int(user_input)
      print("yes")
except ValueError:
   print("No")
   
