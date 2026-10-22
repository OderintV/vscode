# dictionary, take brand(key) input from user and print the models
car_models = {
"Toyota": ["Corolla", "Camry", "RAV4", "Prius"],
"Honda": ["Civic", "Accord", "CR-V", "Pilot"],
"Ford": ["Mustang", "F-150", "Explorer", "Focus"], 
"Bmw": ["3 Series", "5 Series", "X5", "i8"] }

brand = input("Enter a car brand: ").strip().lower().title()
if brand in car_models:
    print(f"Models available for {brand}: {', '.join(car_models[brand])}")
else:
    print("Brand not found in the dictionary.")

