travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇
def add_new_country(country_visited, times, ListOfCities):
  new_log = {}
  new_log["country"] = country_visited
  new_log["visits"] = times
  new_log["cities"] = ListOfCities

  travel_log.append(new_log)

#🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)

order = {
  "starter": {1: "Salad", 2: "Soup"},
  "main": {1: ["Burger", "Fries"], 2: ["Steak"]},
  "dessert": {1: ["Ice Cream"], 2: []}
}

print(order["main"][2][0])