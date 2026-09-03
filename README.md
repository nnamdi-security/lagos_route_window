# Lagos Route Window

A small FastAPI service for looking up Lagos public transport routes, stops, fares, and buses (danfo, BRT, keke) from a local JSON dataset.

[![wakatime](https://wakatime.com/badge/user/55f2e7d8-e681-415e-ba87-93dc727f5023/project/1d6d491d-0982-4216-969c-3e23545835fe.svg)](https://wakatime.com/badge/user/55f2e7d8-e681-415e-ba87-93dc727f5023/project/1d6d491d-0982-4216-969c-3e23545835fe)

## Features

- Look up a route by number, with its stops and fare
- Paginate through a route's stops
- Look up a bus by plate number
- Filter buses by fleet type (BRT, danfo, keke)
- Search routes by destination stop, optionally capped by max fare

## Tech Stack

- Python 3.14+
- [FastAPI](https://fastapi.tiangolo.com/) (`fastapi[standard]`)
- Data served from a local `lagos_routes.json` file — no database required

## Getting Started

This project uses [uv](https://github.com/astral-sh/uv) for dependency management.

```bash
# Clone the repo
git clone https://github.com/nnamdi-security/lagos_route_window.git
cd lagos_route_window

# Install dependencies
uv sync

# Run the dev server
uv run fastapi dev main.py
```

The API will be available at `http://127.0.0.1:8000`, with interactive docs at `http://127.0.0.1:8000/docs`.

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/` | Welcome message with route/bus counts |
| `GET` | `/routes/{route_number}` | Get a single route by its number (1–200) |
| `GET` | `/route/{route_number}/stops` | Get a route's stops, with `limit` (1–10) and `skip` pagination |
| `GET` | `/buses/{plate}` | Get a bus by plate number, e.g. `WCA-881NF` |
| `GET` | `/fleet/{bus_type}` | Get all buses of a given type: `brt`, `danfo`, or `keke` |
| `GET` | `/search` | Search routes by `destination` stop, optionally filtered by `max_fare` |

### Example requests

```bash
curl http://127.0.0.1:8000/routes/14
curl "http://127.0.0.1:8000/route/14/stops?limit=3&skip=1"
curl http://127.0.0.1:8000/buses/WCA-881NF
curl http://127.0.0.1:8000/fleet/danfo
curl "http://127.0.0.1:8000/search?destination=Yaba&max_fare=800"
```

## Data

`lagos_routes.json` contains sample data for 28 routes and 60 buses across Lagos (e.g. Egbeda–Ketu, Oshodi–Ajah Express, Yaba–CMS), each with stops, fares in naira, and assigned vehicles.

## Project Structure

```
.
├── main.py             # FastAPI app and route handlers
├── data.py             # Loads routes/buses from the JSON dataset
├── lagos_routes.json   # Route and bus data
├── pyproject.toml      # Project metadata and dependencies
└── uv.lock             # Locked dependency versions
```
