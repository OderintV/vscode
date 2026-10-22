from pyfiglet import Figlet
import random
import sys
figlet = Figlet()

if len(sys.argv) == 1:
    fontn = random.choice(figlet.getFonts())
elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font") and (sys.argv[2] in figlet.getFonts()):
    fontn = sys.argv[2]
else:
    sys.exit("Invalid usage")


text = input("Input: ")
figlet.setFont(font=fontn)
print("Output:", figlet.renderText(text))
