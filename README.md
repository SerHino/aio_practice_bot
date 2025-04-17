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
   git clone https://github.com/SerHino/aio_practice_bot.git
2. Встановіть залежності:
   ```bash
   pip install -r requirements.txt
4. Налаштуйте конфіг:
    Створіть файл .env у папці data/ на основі config.py:
   ```bash
   BOT_TOKEN=ваш_токен
   ADMIN_PASSWORD=ваш_пароль
5. Запустіть бота:
   ```bash
   python app.py

📂 Структура проекту (Діаграма архітектури)
```bash
aio_practice_bot/
│
├── data/                   # Папка з даними та конфігурацією
│   ├── config.py           # Налаштування бота (токен, паролі адмінів)
│   ├── database.db         # База даних SQLite
│   └── .env                # Чутливі дані (у .gitignore)
│
├── filters/                # Фільтри для обробки повідомлень
│   ├── __init__.py         # Ініціалізація фільтрів
│   ├── is_admin.py         # Перевірка прав адміністратора
│   └── is_user.py          # Перевірка статусу користувача
│
├── handlers/               # Обробники подій
│   ├── admin/              # Логіка для адміністратора
│   │   ├── __init__.py
│   │   ├── add_product.py  # Додавання товарів
│   │   └── orders.py       # Управління замовленнями
│   │
│   └── user/              # Логіка для користувачів
│       ├── __init__.py
│       ├── cart.py         # Робота з кошиком
│       ├── catalog.py      # Перегляд каталогу
│       └── menu.py         # Головне меню
│
├── keyboards/              # Клавіатури та кнопки
│   ├── default/            # Звичайні кнопки
│   │   └── markup.py       # Готові шаблони кнопок
│   │
│   └── inline/             # Інлайн-клавіатури
│       ├── catalog.py      # Кнопки для каталогу
│       └── cart.py         # Кнопки для кошика
│
├── states/                 # Машини станів (FSM)
│   ├── __init__.py
│   ├── checkout.py         # Стан оформлення замовлення
│   └── product.py          # Стан додавання товару
│
├── utils/                  # Додаткові утиліти
│   └── db/                 # Робота з базою даних
│       ├── __init__.py
│       └── storage.py      # Функції для роботи з SQLite
│
├── .gitignore             # Список ігнорованих файлів
├── LICENSE                # Ліцензія MIT
├── README.md              # Документація проекту
├── app.py                 # Вхідний файл (запуск бота)
├── loader.py              # Ініціалізація бота
└── requirements.txt       # Залежності (aiogram, python-dotenv тощо)
```

Компоненти:

1. Python Application (aiogram)
2. SQLite Database (зберігання товарів/замовлень)
3. Telegram Bot API (інтерфейс користувача)
4. Admin Panel (Flask/Django для адміністраторів)
5. Cloud Storage (AWS S3 для зображень товарів)


# Telegram Shop Bot - Документація розгортання

## 🛠 Вимоги до системи
- Python 3.10+
- SQLite 3
- Git
- Telegram Bot Token

## 🚀 Швидкий старт

1. Клонування репозиторію
   ```bash
   git clone https://github.com/SerHino/telegram-shop-bot.git
   cd telegram-shop-bot
3. Налаштування віртуального середовища
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
5. Встановлення залежностей
   ```bash
   pip install -r requirements.txt
7. Конфігурація
   - Створіть файл .env у папці data/:
     ```bash
     BOT_TOKEN=ваш_токен
     ADMIN_ID=ваш_telegram_id
     DB_PATH=data/database.db
8. Ініціалізація БД
   ```bash
   python -c "from utils.db.storage import init_db; init_db()"
10. Запуск бота
   ```bash
   python app.py
   ```
🔧 Основні команди

1. make migrate - Застосування міграцій БД
2. make test - Запуск unit-тестів
3. make deploy - Деплой на сервер

# 📝 Інструкція для розробника
## 1. Встановлення Python та залежностей
```bash
# Для Ubuntu/Debian
sudo apt update
sudo apt install python3.10 python3.10-venv sqlite3

# Для Windows (Python installer з python.org)
```

## 2. Налаштування IDE (PyCharm)
1. Відкрийте папку проекту
2. Встановіть інтерпретатор:
   File > Settings > Project > Python Interpreter → виберіть venv

## 3. Конфігурація бази даних
Створіть міграцію для нових таблиць:
```bash
# utils/db/migrations/001_initial.py
def upgrade():
    op.create_table(
        'products',
        Column('id', Integer, primary_key=True),
        Column('name', String(100)),
        Column('price', Numeric(10,2))
    )
```

## 4. Тестові дані
Додайте фіктивні товари через Python shell:
```bash
python -c """
from utils.db.storage import add_product
add_product('iPhone 15', 999.99)
"""
```

## 5. Перевірка роботи
1. Запустіть бота
2. Відправте /start у Telegram
3. Перевірте логі:
   ```bash
   tail -f bot.log  # Linux
   Get-Content bot.log -Wait  # Windows PowerShell
   ```

## 📚 Документування коду

### Стандарти:
1. **Класи/Методи**: Google Style Docstrings
2. **Типи**: Обов'язкові type hints
3. **Модулі**: Короткий опис у `__doc__`

### Приклад:
```python
def calculate_total(items: list[dict]) -> float:
    """Розраховує підсумкову суму замовлення.

    Args:
        items: Список товарів у форматі {'price': float, 'quantity': int}

    Returns:
        Загальна сума без урахування доставки
    """
```

### Генерація документації:
```bash
# Встановити pdoc
pip install pdoc3

# Згенерувати HTML
pdoc --html --output-dir docs aiogram_shop_bot
```
