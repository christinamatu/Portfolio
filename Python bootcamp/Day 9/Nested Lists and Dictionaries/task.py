capitals = {
    "France": "Paris",
    "Germany": "Berlin"
}

## nested List in a dictionary
# travel_log = {
  #  "France": ["Paris", "Lille", "Dijon"],
  #  "Germany": ["Stuttgart", "Berlin"]
#}

# print Lille
# print(travel_log["France"][1])

# print D from the nested list
nested_list = ["A", "B", ["C", "D"]]
print(nested_list[2][1])

travel_log = {
    "France": {
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12
    },
    "Germany": {
        "cities_visited": ["Berlin", "Hamburg", "Stuttgard"],
        "total_visits": 5
    }
}

# print "Stuttgard" from the travel_log
print(travel_log["Germany"]["cities_visited"][2])