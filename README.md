# 📦 Supply Chain Management API

A RESTful API built using FastAPI to manage supply chain operations such as inventory tracking and shipment processing. This project demonstrates backend development skills including API design, data validation, and system structuring.

---

## 🚀 Features

* 📋 View complete inventory
* 🔍 Retrieve details of a specific item
* 📦 Create shipment requests
* 🚚 Track all shipments
* ✅ Input validation using Pydantic
* ⚡ Fast and lightweight API using FastAPI

---

## 🛠️ Tech Stack

* **Backend Framework:** FastAPI
* **Language:** Python
* **Data Validation:** Pydantic
* **Server:** Uvicorn

---

## 📂 Project Structure

```
supply-chain-api/
│
├── main.py              # Main application file
├── requirements.txt     # Project dependencies
├── README.md            # Project documentation
└── .gitignore           # Ignored files
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

```
git clone https://github.com/your-username/supply-chain-api.git
cd supply-chain-api
```

### 2️⃣ Install dependencies

```
pip install -r requirements.txt
```

### 3️⃣ Run the application

```
uvicorn main:app --reload
```

### 4️⃣ Open in browser

* API Docs (Swagger UI): http://127.0.0.1:8000/docs
* Alternative Docs: http://127.0.0.1:8000/redoc

---

## 📡 API Endpoints

### 🔹 Root

* `GET /`

  * Health check endpoint

---

### 🔹 Inventory

* `GET /inventory`

  * Returns all inventory items

* `GET /inventory/{item_id}`

  * Returns details of a specific item

---

### 🔹 Shipments

* `POST /shipments`

  * Create a new shipment

**Request Body Example:**

```
{
  "item_id": 1,
  "destination": "New York",
  "quantity": 10,
  "priority": "High"
}
```

---

* `GET /shipments`

  * Returns all shipment records

---

## 🧪 Sample Response

```
{
  "message": "Shipment created successfully",
  "shipment": {
    "item_id": 1,
    "destination": "New York",
    "quantity": 10,
    "priority": "High",
    "id": 2,
    "status": "Pending"
  }
}
```

---

## ⚠️ Limitations

* Uses in-memory data (no persistent database)
* No authentication or user management
* Not production-ready (for academic/demo purposes)

---

## 🔮 Future Improvements

* 🔐 Add authentication (JWT-based login system)
* 🗄️ Integrate database (MySQL / PostgreSQL)
* ✏️ Add update & delete endpoints
* 📊 Build frontend dashboard
* 📦 Add shipment tracking status updates

---

## 👨‍🎓 Academic Context

This project was developed as part of a final year academic submission to demonstrate backend API development and system design concepts.

---

## 📜 License

This project is for educational purposes only.

---

## 🙌 Acknowledgements

* FastAPI Documentation
* Python Community

---
