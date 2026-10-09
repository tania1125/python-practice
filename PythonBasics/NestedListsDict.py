
# list in Dictionary_________________________________________
Travel_vlog ={
    "Jaipur": ["City Palace", "Amber fort", "gaitore ki chatriyan", "jaigarh fort"],
    "Udaipur": ["bahubali hills", "pichola lake", "gangaur ghat", "mansoon hill"]
}
print(f"{Travel_vlog['Jaipur'][0]}")

# Nested list __________________________________________
nested_list = ["1", "2",["3", "4"]]
print(nested_list[2][1])

# Nested dictionary and List inside dictionary____________________________________________
Travel_vlog2={
    "Jaipur": {
        "num_visted": "1", 
        "places_visited": ["City Palace", "Amber fort", "gaitore ki chatriyan", "jaigarh fort"]
    }
        ,
    "Udaipur": {
        "Budget": "5000", 
        "places_visited": ["bahubali hills", "pichola lake", "gangaur ghat", "mansoon hill"]
    }
    
}

print(f"The budget for udaipur trip is: {Travel_vlog2['Udaipur']["Budget"]}, the highest entry fee was for {Travel_vlog2['Udaipur']['places_visited'][1]} ride")

Personal_details ={"name": "Tania", "Place": "kerala", "Language": "Malayalam"}

for i, position in enumerate(Personal_details):
    print(i)
    print(Personal_details[position])
    
