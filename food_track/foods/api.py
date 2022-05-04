import ast
import string
usda_key = '0arBG94hGw3XyzanWdsZ4I6dTCmsT1aj7QWSJkGf'

nutrient_dict = {
    "Alanine": "",
    "Alcohol, ethyl": "",
    "Arginine": "",
    "Ash": "",
    "Aspartic acid": "",
    "Beta-sitosterol": "",
    "Betaine": "",
    "Caffeine": "",
    "Calcium, Ca": "",
    "Campesterol": "",
    "Carbohydrate, by difference": "",
    "Carotene, alpha": "",
    "Carotene, beta": "",
    "Cholesterol": "",
    "Choline, total": "",
    "Copper, Cu": "",
    "Cryptoxanthin, beta": "",
    "Cystine": "",
    "Energy": "",
    "Fatty acids, total monounsaturated": "",
    "Fatty acids, total polyunsaturated": "",
    "Fatty acids, total saturated": "",
    "Fatty acids, total trans": "",
    "Fatty acids, total trans-monoenoic": "",
    "Fatty acids, total trans-polyenoic": "",
    "Fiber, total dietary": "",
    "Fluoride, F": "",
    "Folate, DFE": "",
    "Folate, food": "",
    "Folate, total": "",
    "Folic acid": "",
    "Fructose": "",
    "Galactose": "",
    "Glucose (dextrose)": "",
    "Glutamic acid": "",
    "Glycine": "",
    "Histidine": "",
    "Hydroxyproline": "",
    "Iron, Fe": "",
    "Isoleucine": "",
    "Lactose": "",
    "Leucine": "",
    "Lutein + zeaxanthin": "",
    "Lycopene": "",
    "Lysine": "",
    "MUFA 14:1": "",
    "MUFA 15:1": "",
    "MUFA 16:1": "",
    "MUFA 16:1 c": "",
    "MUFA 17:1": "",
    "MUFA 18:1": "",
    "MUFA 18:1 c": "",
    "MUFA 18:1-11 t (18:1t n-7)": "",
    "MUFA 20:1": "",
    "MUFA 22:1": "",
    "MUFA 22:1 c": "",
    "MUFA 24:1 c": "",
    "Magnesium, Mg": "",
    "Maltose": "",
    "Manganese, Mn": "",
    "Methionine": "",
    "Niacin": "",
    "PUFA 18:2": "",
    "PUFA 18:2 CLAs": "",
    "PUFA 18:2 i": "",
    "PUFA 18:2 n-6 c,c": "",
    "PUFA 18:3": "",
    "PUFA 18:3 n-3 c,c,c (ALA)": "",
    "PUFA 18:3 n-6 c,c,c": "",
    "PUFA 18:3i": "",
    "PUFA 18:4": "",
    "PUFA 20:2 n-6 c,c": "",
    "PUFA 20:3": "",
    "PUFA 20:3 n-3": "",
    "PUFA 20:3 n-6": "",
    "PUFA 20:4": "",
    "PUFA 21:5": "",
    "PUFA 22:4": "",
    "PUFA 22:5 n-3 (DPA)": "",
    "PUFA 22:6 n-3 (DHA)": "",
    "PUFA 2:4 n-6": "",
    "PUFA 2:5 n-3 (EPA)": "",
    "Pantothenic acid": "",
    "Phenylalanine": "",
    "Phosphorus, P": "",
    "Phytosterols": "",
    "Potassium, K": "",
    "Proline": "",
    "Protein": "",
    "Retinol": "",
    "Riboflavin": "",
    "SFA 10:0": "",
    "SFA 12:0": "",
    "SFA 13:0": "",
    "SFA 14:0": "",
    "SFA 15:0": "",
    "SFA 16:0": "",
    "SFA 17:0": "",
    "SFA 18:0": "",
    "SFA 20:0": "",
    "SFA 22:0": "",
    "SFA 24:0": "",
    "SFA 4:0": "",
    "SFA 6:0": "",
    "SFA 8:0": "",
    "Selenium, Se": "",
    "Serine": "",
    "Sodium, Na": "",
    "Starch": "",
    "Stigmasterol": "",
    "Sucrose": "",
    "Sugars, total including NLEA": "",
    "TFA 16:1 t": "",
    "TFA 18:1 t": "",
    "TFA 18:2 t not further defined": "",
    "TFA 18:2 t,t": "",
    "TFA 22:1 t": "",
    "Theobromine": "",
    "Thiamin": "",
    "Threonine": "",
    "Tocopherol, beta": "",
    "Tocopherol, delta": "",
    "Tocopherol, gamma": "",
    "Tocotrienol, alpha": "",
    "Tocotrienol, beta": "",
    "Tocotrienol, delta": "",
    "Tocotrienol, gamma": "",
    "Total lipid (fat)": "",
    "Tryptophan": "",
    "Tyrosine": "",
    "Valine": "",
    "Vitamin A, IU": "",
    "Vitamin A, RAE": "",
    "Vitamin B-12": "",
    "Vitamin B-12, added": "",
    "Vitamin B-6": "",
    "Vitamin C, total ascorbic acid": "",
    "Vitamin D (D2 + D3)": "",
    "Vitamin D (D2 + D3), International Units": "",
    "Vitamin D2 (ergocalciferol)": "",
    "Vitamin D3 (cholecalciferol)": "",
    "Vitamin E (alpha-tocopherol)": "",
    "Vitamin E, added": "",
    "Vitamin K (Dihydrophylloquinone)": "",
    "Vitamin K (Menaquinone-4)": "",
    "Vitamin K (phylloquinone)": "",
    "Water": "",
    "Zinc, Zn": ""
}
nutrients = [
    "['Protein: 10.6G', 'Total lipid (fat): 12.9G', 'Carbohydrate, by difference: 35.3G', 'Energy: 306KCAL', 'Sugars, total including NLEA: 4.71G', 'Fiber, total dietary: 1.2G', 'Calcium, Ca: 176MG', 'Iron, Fe: 1.69MG', 'Sodium, Na: 847MG', 'Vitamin A, IU: 0.0IU', 'Vitamin C, total ascorbic acid: 0.0MG', 'Cholesterol: 29.0MG', 'Fatty acids, total trans: 0.0G', 'Fatty acids, total saturated: 5.29G']",
    "['Protein: 7.89G', 'Total lipid (fat): 0.0G', 'Carbohydrate, by difference: 55.3G', 'Energy: 263KCAL', 'Sugars, total including NLEA: 0.0G', 'Fiber, total dietary: 2.6G', 'Calcium, Ca: 0.0MG', 'Iron, Fe: 0.95MG', 'Sodium, Na: 553MG', 'Vitamin A, IU: 0.0IU', 'Vitamin C, total ascorbic acid: 0.0MG', 'Cholesterol: 0.0MG', 'Fatty acids, total trans: 0.0G', 'Fatty acids, total saturated: 0.0G']",
    "['Protein: 21.4G', 'Total lipid (fat): 25.0G', 'Carbohydrate, by difference: 0.0G', 'Energy: 346KCAL', 'Sugars, total including NLEA: 0.0G', 'Fiber, total dietary: 0.0G', 'Calcium, Ca: 714MG', 'Iron, Fe: 0.0MG', 'Sodium, Na: 536MG', 'Vitamin A, IU: 714IU', 'Vitamin C, total ascorbic acid: 0.0MG', 'Cholesterol: 146MG', 'Fatty acids, total trans: 0.0G', 'Fatty acids, total saturated: 14.3G']",
    "['Protein: 10.4G', 'Total lipid (fat): 20.8G', 'Carbohydrate, by difference: 44.8G', 'Energy: 408KCAL', 'Alcohol, ethyl: 0.0G', 'Water: 21.1G', 'Caffeine: 0.0MG', 'Theobromine: 0.0MG', 'Sugars, total including NLEA: 2.08G', 'Fiber, total dietary: 2.1G', 'Calcium, Ca: 90.0MG', 'Iron, Fe: 2.49MG', 'Magnesium, Mg: 17.0MG', 'Phosphorus, P: 120MG', 'Potassium, K: 84.0MG', 'Sodium, Na: 750MG', 'Zinc, Zn: 0.96MG', 'Copper, Cu: 0.086MG', 'Selenium, Se: 19.8UG', 'Retinol: 23.0UG', 'Vitamin A, RAE: 24.0UG', 'Carotene, beta: 9.0UG', 'Carotene, alpha: 1.0UG', 'Vitamin E (alpha-tocopherol): 1.49MG', 'Vitamin D (D2 + D3): 0.1UG', 'Cryptoxanthin, beta: 0.0UG', 'Lycopene: 0.0UG', 'Lutein + zeaxanthin: 45.0UG', 'Vitamin C, total ascorbic acid: 0.0MG', 'Thiamin: 0.433MG', 'Riboflavin: 0.303MG', 'Niacin: 3.28MG', 'Vitamin B-6: 0.048MG', 'Folate, total: 107UG', 'Vitamin B-12: 0.24UG', 'Choline, total: 8.5MG', 'Vitamin K (phylloquinone): 32.4UG', 'Folic acid: 75.0UG', 'Folate, food: 32.0UG', 'Folate, DFE: 159UG', 'Vitamin E, added: 0.0MG', 'Vitamin B-12, added: 0.0UG', 'Cholesterol: 10.0MG', 'Fatty acids, total saturated: 6.25G', 'SFA 4:0: 0.153G', 'SFA 6:0: 0.073G', 'SFA 8:0: 0.043G', 'SFA 10:0: 0.096G', 'SFA 12:0: 0.111G', 'SFA 14:0: 0.401G', 'SFA 16:0: 3.62G', 'SFA 18:0: 1.48G', 'MUFA 18:1: 4.17G', 'PUFA 18:2: 8.1G', 'PUFA 18:3: 1.1G', 'PUFA 20:4: 0.0G', 'PUFA 22:6 n-3 (DHA): 0.0G', 'MUFA 16:1: 0.076G', 'PUFA 18:4: 0.0G', 'MUFA 20:1: 0.039G', 'PUFA 2:5 n-3 (EPA): 0.0G', 'MUFA 22:1: 0.0G', 'PUFA 22:5 n-3 (DPA): 0.0G', 'Fatty acids, total monounsaturated: 4.34G', 'Fatty acids, total polyunsaturated: 9.2G']"
    ]

for n in nutrients:
    a = ast.literal_eval(n)
    # print(a)

names = list((nutrient.split(':') for nutrient in nutrients))
for name in names:
    nutrient = name[0]
    amount = name[1].strip(" ")
    # print(nutrient, amount)
new_dict = {}
for k, v in nutrient_dict.items():
    if k == None:
        new_dict.update({k: '55'})

res = [list(filter(lambda ele: ele in sub, nutrient_dict)) for sub in nutrients]
nutrient_balance = {}
for nutrient_list in nutrients:
    nutrient_list = ast.literal_eval(nutrient_list) # convert to actual list
    for nutrient in nutrient_list:
        nutrient = nutrient.split(": ") # [nutrient, amount]
        # Get int value
        for i, char in enumerate(nutrient[1]):
            if char not in string.ascii_uppercase:
                nutrient_amount = float(nutrient[1][:i+1])
        # Add to balance
        if nutrient_balance.get(nutrient[0]):
            nutrient_balance[nutrient[0]] += nutrient_amount
        else:
            nutrient_balance[nutrient[0]] = nutrient_amount

# print(nutrient_balance)