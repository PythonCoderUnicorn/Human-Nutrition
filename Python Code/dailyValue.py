
# -------------------------------------
# title: Nutritional Daily Value
# by: Zane Dax
# date: Jun 27, 2021 (original Jan 30, 2016)
# -------------------------------------



#-------------------------- required function
def divide(a,b):
	if b==0:
		print ("enter a value greater than 0")
	else:
		return float(a)/b
#-----------------------------------------------



print( " --------- Nutrition %DV --------------- \n ")

daily_value = float(input("  Enter % value of fat: " ))

num = divide(daily_value,100)
c = num * 65
print(f" .......... {daily_value} % = {c} grams")

# ----------------------
# food label: [2 bars] 
# per snack bar = 170 calories, fat 9g, %DV = 14%
#		9g * 9g / 170 * 100 = 48% is fat
# ----------------------
calories = float(input(" Enter the calories: "))
calories_from_fat = divide(c,calories)
Fats = (calories_from_fat * 100)
print(f" ............ {round(Fats,2)} % is fat ")



daily_value = float(input(" Enter % value Saturated fat : " ))
num = divide(daily_value,100)
c = num * 20
#print "  Sat fat value in mg: ", c
d = divide(c,10)
print(f" ..........{daily_value}%  = {c} grams")


daily_value = float(input(" Enter % value of Cholesterol: " ))
num = divide(daily_value,100)
c = num * 300
d = divide(c,10)
print(f" ..... cholesterol value {d} grams")
print(f" ..... {daily_value}% {c} mg")



daily_value = float(input("  Enter % value of sodium: " ))
num = divide(daily_value,100)
c = num * 2400
d = divide(c,10)
print(f" .......... {daily_value}% = {c} mg")



daily_value = float(input(" Enter % value of carbs: " ))
num = divide(daily_value,100)
c = num * 300
print(f" .......... {daily_value}% = {c} grams")



daily_value = float(input("  Enter % value of fibre: " ))
num = divide(daily_value,100)
c = num * 25
print(f" .......... {daily_value}% = {c} grams")


#--- 1 tsp of sugar = 4g 
daily_value = float(input(" Enter gram value of sugar: " ))
num = divide(daily_value,100)
c = num * 25
d = divide(c,10)
print(f" ..... value of sugar {c} in grams")








#-------------------- vitamins

daily_value = float(input("  Enter % value of vitamin A: " ))
num = divide(daily_value,100)
c = num * 1000
d = divide(c,10)
print(f" ..... value of vitamin A {d} grams")
print(f" ..........{daily_value}% = {c} mg")


daily_value = float(input("  Enter % value calcium: " ))
num = divide(daily_value,100)
c = num * 1100
d = divide(c,10)
print(f" ..........{daily_value} % = {c} mg")



daily_value = float(input("  Enter % value vitamin C: " ))
num = divide(daily_value,100)
c = num * 60
d = divide(c,10)
print(f" ..........{daily_value} % = {c} mg")


daily_value = float(input("  Enter % value iron: " ))
num = divide(daily_value,100)
c = num * 14
print(f" ..........{daily_value} % = {c} mg")
d = divide(c,10)

print("\n")














