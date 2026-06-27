from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

current_dir = os.path.dirname(os.path.abspath(__file__))
# Убедись, что путь к папке картинок верный для твоего проекта
images_path = os.path.join(current_dir, "../frontend/images")
app.mount("/static/images", StaticFiles(directory=images_path), name="images")

fake_db_menu = {
    "shashlychnaya_one": {
        "restaurant_name": "Шашлычный Двор №1",
        "categories": [
            {
                "category_name": "Фирменный Шашлык",
                "items": [
                    {"id": 1, "name": "Шашлык из баранины (Мякоть)", "price": 2400, "image": "shashlyk.jpg"},
                    {"id": 2, "name": "Антрекот из баранины", "price": 2600, "image": "antrekot.jpg"},
                    {"id": 3, "name": "Люля-Кебаб из говядины", "price": 1900, "image": "lyulya.jpg"}
                ]
            }
        ]
    }
}

@app.get("/api/menu/{restaurant_id}")
async def get_menu(restaurant_id: str):
    return fake_db_menu.get(restaurant_id, {"error": "Restaurant not found"})

@app.put("/api/menu/{restaurant_id}/item/{dish_id}")
async def update_price(restaurant_id: str, dish_id: int, new_price: dict):
    restaurant = fake_db_menu.get(restaurant_id)
    if not restaurant: return {"error": "Restaurant not found"}
    for category in restaurant["categories"]:
        for item in category["items"]:
            if item["id"] == dish_id:
                item["price"] = new_price["price"]
                return {"message": "Success", "new_price": item["price"]}
    return {"error": "Dish not found"}
