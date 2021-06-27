# ----------------------------------------------
# title: BMI Calculator 
# by: Zane Dax
# Date: June 27, 2021. [original:Dec 13, 2016]
# Note: This code tries to be inclusive despite Kinesiology/ Nutrition not being.
# ----------------------------------------------



# conversions
# --------------------------
print("`````````` Conversions for BMR formulas ````````")
weight_lbs_to_kg = float(input("Enter weight in pounds: "))
kg_from_lbs =  weight_lbs_to_kg/2.205
print(f"Weight in kg: {kg_from_lbs}")

height_ft = float(input(" Enter your height in m: "))    # metres !
height_cm_from_ft = height_ft * 30.48
print(f"Height in cm: {height_cm_from_ft}")

#------------------------------------------------------------------------------- user input
print( "------------------- all BMR & EER ------------------------ \n")
#------------ kg
weight_kg = float(input(" Enter your weight in kg : "))  
age = float(input(" Enter your age : "))
# ----------- cm
height_cm = float(input(" Enter your height in cm: "))    

#-------------------------------------------------------------------------------


# ------------------------- basic  Basal Metabolic Rate (BMR)
# BMR = kg * 24  (male)      
# BMR = kg *22   (female)
m_BMR = (weight_kg * 24)
w_BMR = (weight_kg * 22)
#---------------------------

# ------------------------------ Harris-Benedict formula
#- formula for males
# BMR = 88.362 + (13.397 * kg) + (4.799 * cm) - (5.677 * age)   
# EER = BMR * AF
male_BMR = 88.362 + (13.397 * weight_kg) + (4.799 * height_cm) - (5.677 * age)

#- formula for females
# BMR = 447.593 + (9.247 * kg) + (3.098 * cm) - (4.330 * age)  
# EER = BMR * AF
female_BMR = 447.593 + (9.247 * weight_kg) + (3.098 * height_cm) - (4.330 * age)
#--------------------------------


#--------------------------------- Mifflin-Jeor formula
#- formula for males
# BMR = (10 * kg) + (6.25 * cm) -(5 * age) + 5	
# EER = BMR * AF
male_miff_BMR = (10 * weight_kg) + (6.25 * height_cm) -(5 * age) + 5

#- formula for females
# BMR = (10 * kg) + (6.25 * cm) -(5 * age) - 16	
# EER = BMR * AF
female_miff_BMR = (10 * weight_kg) + (6.25 * height_cm) -(5 * age)
#----------------------------------


#---------------------------------- EER FORMULAS

#---------- PHYSICAL ACTIVITY 
print( " _____ Physical Activity values used in EER (ADULTS 19+) _______")
print( " sedentary: daily living + walking ..................... = 1.00 ")
print( " low active: 30 - 60 min. moderate ..................... = 1.12 ")
print( " active: 60 min. of activity ........................... = 1.27 ")
print( " very active: 60 min. activity / 60 + min. ............. = 1.45 ")
PA = float(input("\n Enter Physical activity # : ")) 



# -------------------------------------------- Health Canada EER
# HEALTH CANADA EER          PA # 				
EER_m = 662 - (9.53 * age) + (PA) * ((15.91 * weight_kg)+(539.6*height_m))  # male
EER_w = 354 - (6.91 * age) + (PA) * ((9.36 * weight_kg)+(726*height_m))     # female


#--------------------------------------------- activity levels % [textbook]
print( "__________ activity levels ___________________________")
print( " sedentary/inactive .............. (range: .25 to .40)")
print( " light activity     .............. (range: .40 to .70)")
print( " moderate activity  .............. (range: .50 to .80)")
print( " heavily active     .............. (range: .80 to 1.20)")
print( " very active        .............. (range: 1.3 to 1.45)")


#------- user input
AL_1 = float(input(" Enter Activity low-Level value : "))
AL_2 = float(input(" Enter Activity high-Level value : "))		

#------- EER = BMR + (BMR * AL)   [textbook]	AL * BMR 
male_EER1 = (m_BMR + (m_BMR * AL_1))
male_EER2 = (m_BMR + (m_BMR * AL_2))
female_EER1 = (w_BMR +(w_BMR * AL_1))
female_EER2 = (w_BMR +(w_BMR * AL_2))



print("\n ---------------------------------------------------------------")
print("....... basic BMR range = ",round(m_BMR,2), " to = ",round(w_BMR,2))
print("....... [Harris-Benedict] BMR range = ",round(male_BMR,2), "to = ",round(female_BMR,2))
print("....... [Mifflin-Jeor] BMR range = ",round(male_miff_BMR,2)," female = ",round(female_miff_BMR,2))
print("\n") # health canada PA levels
print("...... [Health Canada] EER range = ", round(EER_m,2), "to = ",round(EER_w,2))  
#---- EER = BMR * AL
print("...... Activity Level EER range (male)   = ",round(male_EER1,2)," to ",round(male_EER2,2)) 
print("...... Activity Level EER range (female) = ",round(female_EER1,2)," to ",round(female_EER2,2) )
#---- BMR 
print( " [textbook] BMR range = ",m_BMR,"to = ",w_BMR)	
print( "\n")











