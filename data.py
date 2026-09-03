import json

with open("lagos_routes.json", "r") as file:
    data = json.load(file)

routes = data["routes"]
buses = data["buses"]