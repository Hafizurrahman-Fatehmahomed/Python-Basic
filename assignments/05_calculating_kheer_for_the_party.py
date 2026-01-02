# Channd Taara Khan is hosting a kheer (dessert) party at his institute.
# He needs your help to calculate the (total number of people attending).
# He also wants to know the amount of kheer (in grams and kg) he needs to prepare.


# Here is what we know

# - There are 12 faculty members
# - There are 4 administrative staff members
# - There are 100 students in the institute
# - There are 15 people absent
# - Per person 250g of kheer will be made

# What is the number of people attending
# How much kheer needs to be made in kg
# How much kheer needs to be made in grams


faculty = 12
admin_staff = 4
students = 100
absent = 15

total_people_present = faculty + admin_staff + students - absent
kheer_in_grams = total_people_present * 250
kheer_in_kg = kheer_in_grams / 1000

print(f"The total number of people that will be present at the party is {total_people_present}")

print(f"The amount of kheer that needs to be prepared in grams is {kheer_in_grams}g")


print(f"The amount of kheer that needs to be prepared in kg is {kheer_in_kg}kg")