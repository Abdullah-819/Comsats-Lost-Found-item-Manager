def get_lost_items():
    return [
        {"name": "Wallet", "location": "Library", "status": "Unresolved"},
        {"name": "Keys", "location": "Cafeteria", "status": "Resolved"},
        {"name": "Laptop Charger", "location": "Classroom 2B", "status": "Unresolved"},
    ]

def get_found_items():
    return [
        {"name": "Phone", "location": "Lab", "status": "Unresolved"},
        {"name": "Bag", "location": "Gym", "status": "Resolved"},
        {"name": "Water Bottle", "location": "Auditorium", "status": "Unclaimed"},
    ]
