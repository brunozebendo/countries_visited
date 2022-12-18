travel_log = [
{  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]

def add_new_country(country_visited, times_visited, cities_visited):
  new_country = {}
  new_country["country"] = country_visited
  new_country["visits"] = times_visited
  new_country["cities"] = cities_visited
  travel_log.append(new_country)

#escrevi uma função que cria um novo dicionário e relaciona cada item do dicionário já existente com o item
# da nova entrada, depois usa a função append para incluir o novo dicionário no já existente assim que
# a função é chamada

add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)