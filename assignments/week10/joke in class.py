import cowsay
import pyjokes
import helper

print(helper.vari) #access variable from other file
helper.greet("Timo") #access def from other file

joke = pyjokes.get_joke()

(cowsay.milk(joke))

