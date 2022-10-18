def main():
#asking to input values for varablies

    inch=int(input("Please enter your how many inches: "))
    foot=int(input("Please enter your how many feet: "))
    yard=int(input("Please enter your how many yards: "))
    mile=int(input("Please enter your how many mile: "))



    print("---------------------")

    #converting from imperial to metric

    centimeters_from_inch=float(inch*2.54)
    centimeters_from_foot=float(foot*30.48)
    meters_from_yard=float(yard*.914)
    kilometers_from_mile=float((mile*1.61))

    #printing the now values as metric

    print(centimeters_from_inch, "centimeters")
    print(centimeters_from_foot, "centimeters")
    print(meters_from_yard, "meters")
    print(kilometers_from_mile, "kilometers")

main()