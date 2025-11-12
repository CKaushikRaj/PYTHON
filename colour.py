c = input("Enter the colour:")
match c :
   case "red":
      print("STOP!!!!!!")
   case "yellow":
      print("GET READY")
   case "green":
      print("GO")  
   case _:
      print("No status")
      