import turtle
name=turtle.textinput("name","what is your name:")
name=name.lower()
if name.startswith("mr"):
    print("hello sir,how are you?")
elif name.startswith("miss") or name.startswith("mrs") or name.startwith("ms"):
    print("hello medam,how are you?")
else:
    name=name.capitalize()
    str="Hi"+name+"! how are you?"
    print(str)
turtle.exitonclick()
