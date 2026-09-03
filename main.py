from fastapi import FastAPI, Path, Query, HTTPException
from enum import Enum
from data import routes, buses




class BusType(str, Enum):
    Fashola_bus = "brt"
    danfo_driver = "danfo"
    keke_napep = "keke"
    okada = "danfo"



app = FastAPI()

@app.get("/")
def home() -> dict:
    return {
        "message": "Welcome to the Lagos Route Window",
        "routes": len(routes),
        "buses": len(buses)
        }


@app.get("/routes/{route_number}")
def get_route(route_number: int = Path(ge=1, le=200)) -> dict:
    for route in routes:
        if route["route_number"] == route_number:
            return route

    raise HTTPException(status_code=404, detail="Route not found")



@app.get("/route/{route_number}/stops")
def get_route_stops(
    route_number: int = Path(ge=1, le=200),
    limit: int = Query(default=5, ge=1, le=10),
    skip: int = Query(default=0, ge=0)
):
    for route in routes:
        if route["route_number"] == route_number:
            stops = route["stops"]
            return stops[skip:skip + limit]

    raise HTTPException(status_code=404, detail="Route not found")



@app.get("/buses/{plate}")
def get_bus(plate: str = Path(pattern=r"^[A-Z]{3}-[0-9]{3}[A-Z]{2}$")):
    for bus in buses:
        if bus["plate"] == plate:
            return bus

    raise HTTPException(status_code=404, detail="Bus not found")





@app.get("/fleet/{bus_type}")
def get_fleet(bus_type: BusType):

    fleet = []

    for bus in buses:
        if bus["bus_type"] == bus_type:
            fleet.append(bus)

    return fleet


@app.get("/search")
def search_routes(
    destination: str = Query(min_length=3, max_length=30), 
    max_fare: int | None = Query(default=None, gt=0)):

    results = []

    for route in routes:
       
        if destination in route["stops"]:
            
            if max_fare is None or route["fare_naira"] <= max_fare:
                results.append(route)

    return results