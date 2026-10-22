car_models = {
"Toyota": ["Corolla", "Camry", "RAV4", "Prius"],
"Honda": ["Civic", "Accord", "CR-V", "Pilot"],
"Ford": ["Mustang", "F-150", "Explorer", "Focus"], 
"BMW": ["3 Series", "5 Series", "X5", "i8"] }
brandname = input("enter brandname")
if brandname in car_models:
    print("brandmodels:", car_models[brandname])
else:
    print("brand not found")    