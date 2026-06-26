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

# Настройка раздачи картинок из папки frontend/images
current_dir = os.path.dirname(os.path.abspath(__file__))
images_path = os.path.join(current_dir, "../frontend/images")

app.mount("/static/images", StaticFiles(directory=images_path), name="images")

# Полная база данных меню со всеми твоими позициями
fake_db_menu = {
    "shashlychnaya_one": {
        "restaurant_name": "Шашлычный Двор №1",
        "categories": [
            {
                "category_name": "Фирменный Шашлык",
                "items": [
                    {
                        "id": 1,
                        "name": "Шашлык из баранины (Мякоть)",
                        "price": 2400,
                        "description": "Классическая нежная мякоть молодого барашка с дымком.",
                        "full_description": "Наш фирменный шашлык готовится из парной мякоти молодого ягненка, доставленного из экологически чистых предгорий Алматы. Маринуется по секретному рецепту с добавлением горных трав и лукового сока, а затем обжаривается на углях саксаула, что придает мясу неповторимый аромат.",
                        "image": "shashlyk.jpg"
                    },
                    {
                        "id": 2,
                        "name": "Антрекот из баранины",
                        "price": 2600,
                        "description": "Сочное мясо на ребрышке с прослойкой нежного жира.",
                        "full_description": "Отборный антрекот на кости. Мясо получается невероятно сочным благодаря тонкой прослойке жира, которая тает при запекании на углях. Подается с маринованным луком, зеленью и свежими зернами граната.",
                        "image": "antrekot.jpg"
                    },
                    {
                        "id": 3,
                        "name": "Люля-Кебаб из говядины",
                        "price": 1900,
                        "description": "Нежнейший рубленый фарш со специями.",
                        "full_description": "Традиционный люля-кебаб из мелко рубленой говядины с добавлением курдючного жира и восточных специй (зиры и кориандра). Тщательно отбивается вручную, чтобы фарш стал плотным и сочным.",
                        "image": "lyulya.jpg"
                    }
                ]
            },
            {
                "category_name": "Горячие блюда и Закуски",
                "items": [
                    {
                        "id": 4,
                        "name": "Фирменная утка",
                        "price": 4500,
                        "description": "Запеченная утка с золотистой корочкой и пряностями.",
                        "full_description": "Утка маринуется в фирменном маринаде со специями и запекается до хрустящей корочки. Подается горячей и идеально подходит для сытного ужина.",
                        "image": "duck.jpg"
                    },
                    {
                        "id": 5,
                        "name": "Свежий салат",
                        "price": 1200,
                        "description": "Легкий салат из спелых томатов и огурцов с зеленью.",
                        "full_description": "Классический легкий салат из свежих хрустящих огурцов, спелых томатов и сочного лука с добавлением свежей зелени. Отлично дополняет мясные блюда и освежает вкус.",
                        "image": "salad.jpg"
                    }
                ]
            },
            {
                "category_name": "Хлеб и Соусы",
                "items": [
                    {
                        "id": 6,
                        "name": "Свежий хлеб / Лепешка",
                        "price": 400,
                        "description": "Ароматная выпечка к вашему столу.",
                        "full_description": "Традиционный домашний хлеб, который выпекается ежедневно. Мягкий внутри, с хрустящей корочкой — идеальное дополнение к горячему шашлыку и соусам.",
                        "image": "bread.jpg"
                    },
                    {
                        "id": 7,
                        "name": "Фирменный соус",
                        "price": 300,
                        "description": "Пикантный соус на основе томатов и специй.",
                        "full_description": "Наш уникальный соус, приготовленный по особому рецепту из спелых томатов, свежей кинзы, чеснока и секретного набора кавказских пряностей. Превосходно раскрывает вкус любого мяса.",
                        "image": "sauce.jpg"
                    }
                ]
            }
        ]
    }
}

@app.get("/api/menu/{restaurant_id}")
async def get_menu(restaurant_id: str):
    return fake_db_menu.get(restaurant_id, {"error": "Restaurant not found"})