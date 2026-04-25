from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel, Field
from typing import Optional, List

app = FastAPI(title="Supply Chain Management API")

# -------------------------------
# In-Memory Database
# -------------------------------
inventory = [
    {"id": 1, "name": "Standard Widget", "quantity": 150, "location": "Warehouse-East"},
    {"id": 2, "name": "Premium Gadget", "quantity": 85, "location": "Warehouse-West"},
    {"id": 3, "name": "Legacy Tool", "quantity": 20, "location": "Warehouse-North"},
]

shipments = []

# -------------------------------
# Models
# -------------------------------
class InventoryItem(BaseModel):
    name: str
    quantity: int = Field(gt=0)
    location: str

class Shipment(BaseModel):
    item_id: int
    destination: str
    quantity: int = Field(gt=0)
    priority: Optional[str] = "Normal"

class ShipmentUpdate(BaseModel):
    status: str

# -------------------------------
# Helper Functions
# -------------------------------
def find_item(item_id: int):
    for item in inventory:
        if item["id"] == item_id:
            return item
    return None

def find_shipment(shipment_id: int):
    for shipment in shipments:
        if shipment["id"] == shipment_id:
            return shipment
    return None

# -------------------------------
# Root
# -------------------------------
@app.get("/")
def read_root():
    return {"message": "Supply Chain API Running"}

# -------------------------------
# Inventory APIs
# -------------------------------

# Get all inventory (with optional search)
@app.get("/inventory")
def get_inventory(search: Optional[str] = Query(None)):
    if search:
        return [item for item in inventory if search.lower() in item["name"].lower()]
    return inventory

# Get single item
@app.get("/inventory/{item_id}")
def get_item(item_id: int):
    item = find_item(item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

# Add new inventory item
@app.post("/inventory")
def add_item(item: InventoryItem):
    new_item = item.dict()
    new_item["id"] = len(inventory) + 1
    inventory.append(new_item)
    return {"message": "Item added", "item": new_item}

# Update inventory item
@app.put("/inventory/{item_id}")
def update_item(item_id: int, updated: InventoryItem):
    item = find_item(item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")

    item.update(updated.dict())
    return {"message": "Item updated", "item": item}

# Delete inventory item
@app.delete("/inventory/{item_id}")
def delete_item(item_id: int):
    item = find_item(item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")

    inventory.remove(item)
    return {"message": "Item deleted"}

# -------------------------------
# Shipment APIs
# -------------------------------

# Create shipment
@app.post("/shipments")
def create_shipment(shipment: Shipment):
    item = find_item(shipment.item_id)
    if not item:
        raise HTTPException(status_code=400, detail="Item not found")

    if item["quantity"] < shipment.quantity:
        raise HTTPException(status_code=400, detail="Not enough stock")

    # Reduce stock
    item["quantity"] -= shipment.quantity

    new_shipment = shipment.dict()
    new_shipment["id"] = len(shipments) + 1
    new_shipment["status"] = "Pending"

    shipments.append(new_shipment)

    return {"message": "Shipment created", "shipment": new_shipment}

# Get all shipments (filter by status)
@app.get("/shipments")
def get_shipments(status: Optional[str] = Query(None)):
    if status:
        return [s for s in shipments if s["status"].lower() == status.lower()]
    return shipments

# Get single shipment
@app.get("/shipments/{shipment_id}")
def get_shipment(shipment_id: int):
    shipment = find_shipment(shipment_id)
    if not shipment:
        raise HTTPException(status_code=404, detail="Shipment not found")
    return shipment

# Update shipment status
@app.put("/shipments/{shipment_id}")
def update_shipment(shipment_id: int, update: ShipmentUpdate):
    shipment = find_shipment(shipment_id)
    if not shipment:
        raise HTTPException(status_code=404, detail="Shipment not found")

    shipment["status"] = update.status
    return {"message": "Shipment updated", "shipment": shipment}

# Delete shipment
@app.delete("/shipments/{shipment_id}")
def delete_shipment(shipment_id: int):
    shipment = find_shipment(shipment_id)
    if not shipment:
        raise HTTPException(status_code=404, detail="Shipment not found")

    shipments.remove(shipment)
    return {"message": "Shipment deleted"}
