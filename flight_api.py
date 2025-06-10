from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI(title="Flight Reservation API")


class Flight(BaseModel):
    id: int
    origin: str
    destination: str
    departure_time: str


class FlightIn(BaseModel):
    origin: str
    destination: str
    departure_time: str


class Reservation(BaseModel):
    id: int
    flight_id: int
    passenger_name: str


class ReservationIn(BaseModel):
    flight_id: int
    passenger_name: str


flights: List[Flight] = []
reservations: List[Reservation] = []


@app.post("/flights", response_model=Flight)
async def create_flight(flight: FlightIn):
    flight_id = len(flights) + 1
    new_flight = Flight(id=flight_id, **flight.dict())
    flights.append(new_flight)
    return new_flight


@app.get("/flights", response_model=List[Flight])
async def list_flights():
    return flights


@app.get("/flights/{flight_id}", response_model=Flight)
async def get_flight(flight_id: int):
    for f in flights:
        if f.id == flight_id:
            return f
    raise HTTPException(status_code=404, detail="Flight not found")


@app.post("/reservations", response_model=Reservation)
async def create_reservation(reservation: ReservationIn):
    # check flight exists
    for f in flights:
        if f.id == reservation.flight_id:
            reservation_id = len(reservations) + 1
            new_reservation = Reservation(id=reservation_id, **reservation.dict())
            reservations.append(new_reservation)
            return new_reservation
    raise HTTPException(status_code=404, detail="Flight not found")


@app.get("/reservations", response_model=List[Reservation])
async def list_reservations():
    return reservations


@app.get("/reservations/{reservation_id}", response_model=Reservation)
async def get_reservation(reservation_id: int):
    for r in reservations:
        if r.id == reservation_id:
            return r
    raise HTTPException(status_code=404, detail="Reservation not found")
