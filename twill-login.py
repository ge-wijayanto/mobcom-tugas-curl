from twill.commands import *
go('http://localhost:3000')

fv("1", "username", "Gregorius_Evan")
fv("1", "password", "140810190040")

submit()

show()