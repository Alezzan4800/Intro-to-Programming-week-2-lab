#asking to input values for varablies

inch=int(input("Please enter your how many inches: "))
foot=int(input("Please enter your how many feet: "))
yard=int(input("Please enter your how many yards: "))
mile=int(input("Please enter your how many mile: "))



print("---------------------")

#converting from imperial to metric

centimeters_per_inch=float(inch*2.54)
centimeters_per_foot=float(foot*30.48)
meters_per_yard=float(yard*.914)
kilometers_per_mile=float((mile*1.61))

#printing the now values as metric

print(centimeters_per_inch, "centimeters")
print(centimeters_per_foot, "centimeters")
print(meters_per_yard, "meters")
print(kilometers_per_mile, "kilometers")