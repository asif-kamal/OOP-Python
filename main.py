# import turtle
import veryprettytable
#
# sally = turtle.Turtle()
# sally.shape("turtle")
# sally.color("red")
#
# sally.forward(100)
#
# my_screen = turtle.Screen()
# my_screen.bgcolor("teal")
# my_screen.exitonclick()

table = veryprettytable.VeryPrettyTable()

table.add_column("City Names", ["Adelaide", "Sydney", "Melbourne", "Darwin", "Perth"])
table.add_column("City Pokemon", ["Pikachu", "Raichu", "Onix", "Spinarak", "Hoothoot"])
#table.align = 'l'
table.align["City Names"] = "l"
table.align["City Pokemon"] = "r"
print(table)