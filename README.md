🤖 Telegram Shop Bot (aio_practice_bot) 🛒
**Бот-магазин для продажу товарів у Telegram з адмін-панеллю**  

## 📌 Основні функції  
### Для користувачів:  
- **Каталог товарів** з категоріями та детальними описам.  
- **Кошик**: Додавання/видалення товарів, зміна кількості.  
- **Оформлення замовлення** з підтвердженням адміністратором.  
- **Зворотній зв'язок** через команду `/sos`.  
- **Автоматичні сповіщення** про статус замовлення.  

### Для адміністраторів:  
- **Додавання/редагування товарів** та категорій.  
- **Перегляд замовлень** у реальному часі.  
- **Відповіді на запитання** користувачів через бота.  
- **Захищений доступ** за паролем.  

## 🛠 Технології  
- **Python 3.11** + **aiogram 2.25** (асинхронний фреймворк).  
- **SQLite** для зберігання даних (товари, замовлення, користувачі).  
- **FSM (Finite State Machine)** для керування станами (оформлення замовлення).  
- **Dotenv** для конфіденційних даних (токен бота, паролі).  

## 📦 Встановлення  
1. Клонуйте репозиторій:  
   ```bash
   git clone https://github.com/ваш-нік/aio_practice_bot.git
2. Встановіть залежності:
   pip install -r requirements.txt
3. Налаштуйте конфіг:
    Створіть файл .env у папці data/ на основі config.py:
   BOT_TOKEN=ваш_токен
   ADMIN_PASSWORD=ваш_пароль
4. Запустіть бота:
   python app.py

📂 Структура проекту (Діаграма архітектури)
graph TD
    A[Користувач Telegram] --> B[Telegram Bot]
    B --> C[Python Application]
    C --> D[SQLite Database]
    C --> E[Payment Gateway API]
    C --> F[Admin Panel]
    F --> G[Cloud Storage for Media]
    D --> H[(Backup System)]

Компоненти:

1. Python Application (aiogram)
2. SQLite Database (зберігання товарів/замовлень)
3. Telegram Bot API (інтерфейс користувача)
4. Admin Panel (Flask/Django для адміністраторів)
5. Cloud Storage (AWS S3 для зображень товарів)


📝 Інструкція для розробника
# Telegram Shop Bot - Документація розгортання

## 🛠 Вимоги до системи
- Python 3.10+
- SQLite 3
- Git
- Telegram Bot Token

## 🚀 Швидкий старт

1. Клонування репозиторію
   git clone https://github.com/SerHino/telegram-shop-bot.git
   cd telegram-shop-bot
2. Налаштування віртуального середовища
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
3. Встановлення залежностей
   pip install -r requirements.txt
4. Конфігурація
   Створіть файл .env у папці data/:
   BOT_TOKEN=ваш_токен
   ADMIN_ID=ваш_telegram_id
   DB_PATH=data/database.db
5. Ініціалізація БД
   python -c "from utils.db.storage import init_db; init_db()"
6. Запуск бота
   python app.py
   
🔧 Основні команди
Команда	      Опис
make migrate	Застосування міграцій БД
make test	   Запуск unit-тестів
make deploy	   Деплой на сервер

