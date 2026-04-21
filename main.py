from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import json

app = FastAPI(title="Supply Chain API")

# Simple In-Memory Data
inventory = [
    {"id": 1, "name": "Standard Widget", "quantity": 150, "location": "Warehouse-East"},
    {"id": 2, "name": "Premium Gadget", "quantity": 85, "location": "Warehouse-West"},
    {"id": 3, "name": "Legacy Tool", "quantity": 20, "location": "Warehouse-North"},
]

shipments = [ {
    "item_id": 1,
    "destination": "sjmdnjs",
    "quantity": 2,
    "priority": "Normal",
    "id": 6,
    "status": "Pending"
  }
]

# Models
class Shipment(BaseModel):
    item_id: int
    destination: str
    quantity: int
    priority: Optional[str] = "Normal"

@app.get("/")
def read_root():
    """Health check endpoint."""
    return {"message": "Supply Chain System is Online"}

@app.get("/inventory")
def get_inventory():
    """Returns the full list of supply chain items."""
    return inventory

@app.get("/inventory/{item_id}")
def get_item(item_id: int):
    """Returns details for a specific item id."""
    for item in inventory:
        if item["id"] == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")

@app.post("/shipments")
def create_shipment(shipment: Shipment):
    """
    Creates a new shipment request.
    Validates that the item exists in inventory.
    """
    # Check if item exists
    item_exists = any(item["id"] == shipment.item_id for item in inventory)
    if not item_exists:
        raise HTTPException(status_code=400, detail="Invalid item_id: Item does not exist in inventory")
    
    # Simple logic: add to shipments list
    new_shipment = shipment.model_dump()
    new_shipment["id"] = len(shipments) + 1
    new_shipment["status"] = "Pending"
    shipments.append(new_shipment)
    
    return {"message": "Shipment created successfully", "shipment": new_shipment}

@app.get("/shipments")
def get_shipments():
    return shipments
