from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Разрешаем доступ с WebApp
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # позднее можно указать домен твоего WebApp
    allow_methods=["*"],
    allow_headers=["*"],
)

# Тестовый endpoint профиля
@app.get("/profile")
def get_profile():
    return {
        "telegram_id": 123456,
        "name": "Пользователь",
        "balance": 0.0,
        "level": 1
    }

# Тестовый endpoint для сигналов
@app.get("/signals")
def get_signals():
    return [
        {"symbol": "BTCUSDT", "type": "buy", "price": 50000, "status": "new"}
    ]
