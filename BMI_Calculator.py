def cal(uw,a,ow):
    bmi=(float(input("What is your weight in KG: ")))/(((int(input("What is your height in CM:  ")))/100)**2)
    print("Your BMI is",bmi)
    if bmi<uw:
        print("You are underweight")
    elif bmi<a:
        print("You are healthy")
    elif bmi<ow:
        print("You are overweight")
    else:
        print("you are obese")

age=input("Enter your age:")
while not age.isdigit():
    age=input("Re-enter your age:")
age=int(age)
if age>19:
    cal(19,25,30)
elif age<2:
    print("You are too young to measure your BMI")
else:
    gender=input("Enter whether you are a boy or a girl:")
    while not gender in ["boy","girl"]:
        gender=input("Invalid. Enter eighter 'boy' or 'girl'\nRe-enter whether you are a boy or a girl:")

    if gender=="boy":
        data=((14.7,18.1,19.3),(14.4,17.4,18.3),(14,17,17.8),(13.8,17.8,18.1),(14.3,17,18.4),(14.2,17.4,19.2),(13.7,18,20),(14,18.6,21),(14.3,19.4,22),(14.5,20.1,23.2),(15,21,24.2),(15.4,21.7,25.1),(16,22.6,26),(16.5,23.4,26.8),(17.1,24.2,27.5),(17.6,24.9,28.4),(18.3,25.6,29),(18.5,25,30))
    else:
        data=((14.2,18,19.1),(14,17.3,18.3),(13.7,16.8,18),(13.5,16.8,18.3),(13.5,17.1,18.7),(13.5,17.6,19.6),(13.5,18.3,20.6),(13.7,19,21.8),(14,20,23),(14.4,20.7,24),(14.8,21.7,25.2),(15.3,22.5,26.3),(15.8,23.4,27.3),(16.4,24,28),(16.8,24.6,28.9),(17.2,25.7,29.6),(17.5,25.7,30.3),(17.9,26.1,35))
    for i in range(len(data)):
        if i == age-2:
            cal(data[i][0],data[i][1],data[i][2])    