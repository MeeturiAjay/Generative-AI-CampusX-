from typing import TypedDict, Annotated
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

load_dotenv()

model = ChatGroq(model = "llama-3.3-70b-versatile")

class TripPlanner(TypedDict):
    spots: list[str]
    cost: float
    days: int
    persons_suitable: int
    detailed_trip_explanation: Annotated[str, "Give the detailed explanation to start and proceed with the trip"]

model_ = model.with_structured_output(TripPlanner)
response = model_.invoke("Give me the trip plan for the visit of Hyderabad.")

print(response)