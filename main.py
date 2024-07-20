# Version 1
def colourPicker(color, word):
    if color == "red":
      print("\033[31m", word)
    elif color == "blue":
      print("\033[34m", word)
    elif color == "green":
      print("\033[32m", word)
    elif color == "yellow":
      print("\033[33m", word)
    elif color == "purple":
      print("\033[35m", word)
    elif color == "pink":
      print("\033[1;31m", word)
    elif color == "orange":
      print("\033[1;33m", word)

    else:
      print("\033[0m", word)
  
title = "🟥⬜🟦 Music App 🟦⬜🟥"
song = "Radio Gaga"
artist = "Queen"
emoji = "🔥▶"
prev = "PREV"
next = "NEXT"
pause = "PAUSE"
colourPicker("yellow",f"{title: ^35}")
print()
print(emoji, end = "")
colourPicker("white",f"{song:^18}")
colourPicker("yellow",f"{artist:^20}")
print()
colourPicker("white",f"{prev}")
colourPicker("green",f"{next:^18}")
colourPicker("purple",f"{pause:^33}")


title2 = "WELCOME TO"
subtitle = "--  ARMBOOK  --"
blurb = "Definitely not a rip off of"
blurb2 = "a certain other social"
blurb3 = "networking site."

honest = "Honest."
username = "Username: "
password = "Password: "

print()
colourPicker("white", f"{title2:^40}")
colourPicker("blue",f"{subtitle:^40}")
print()
colourPicker("yellow",f"{blurb:>40}")
colourPicker("yellow",f"{blurb2:>40}")
colourPicker("yellow",f"{blurb3:>40}")
print()
colourPicker("red",f"{honest:^40}")
print()
colourPicker("white",f"{username:^40}")
colourPicker("white",f"{password:^40}")


#Version 2
def colourPicker(color):
  if color=="red":
    return ("\033[31m")
  elif color=="white":
    return ("\033[0m")
  elif color=="blue":
    return ("\033[34m")
  elif color=="yellow":
    return ("\033[33m")
  elif color == "green":
    return ("\033[32m")
  elif color == "purple":
    return ("\033[35m")

#Create a dictionary to store colour
# def colourPicker(color):
#   color_codes = {
#       "red": "\033[31m",
#       "white": "\033[0m",
#       "blue": "\033[34m",
#       "yellow": "\033[33m",
#       "green": "\033[32m",
#       "purple": "\033[35m"
#   }
#   return color_codes.get(color, "\033[0m")  # Default to white if color is not found

# Example usage
print(colourPicker("red"))    # Output: \033[31m
print(colourPicker("green"))  # Output: \033[32m
print(colourPicker("unknown")) # Output: \033[0m (default to white)



title = f"{colourPicker('red')}={colourPicker('white')}={colourPicker('blue')}=Music App{colourPicker('blue')}={colourPicker('white')}={colourPicker('red')}="

print(f"        {title:^35}")
print(f"🔥▶\t{colourPicker('white')}Radio Gaga")
print(f"{colourPicker('yellow')}Queen")

prev = "PREV"
next = "NEXT"
pause = "PAUSE"

print(f"{colourPicker('white')}{prev:<35}")
print(f"{colourPicker('green')}{next:^35}")
print(f"{colourPicker('purple')}{pause:>35}")


print()
print()
text = "WELCOME TO"
print(f"{colourPicker('white')}{text:^35}")
text = "--  ARMBOOK  --"
print(f"{colourPicker('blue')}{text:^35}")
print()
text = "Definitely not a rip off of"
print(f"{colourPicker('yellow')}{text:>35}")
text = "a certain other social"
print(f"{colourPicker('yellow')}{text:>35}")
text = "networking site"
print(f"{colourPicker('yellow')}{text:>35}")
text = "Honest."
print(f"{colourPicker('red')}{text:^35}")
text = "Username:"
username = input(f"{colourPicker('white')}{text:^35}")
text = "Password: "
password = input(f"{colourPicker('white')}{text:^35}")
