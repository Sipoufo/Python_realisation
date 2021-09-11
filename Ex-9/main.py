# Nesting
travel_log = {
    "France": {"cities_visited": ["Paris", "Lille", "Dijon"]},
    "Germany": {
        "cities_visited": {
            0: "Paris", 1: "Lille", 2: "Dijon"
        },
        "total_visited": {
            "total": 12
        }
    },
}

print(travel_log["Germany"]["total_visited"]["total"])