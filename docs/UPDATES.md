# Процедура оновлення продакшен-середовища

## 1. Підготовка до оновлення
### Передумови
- [ ] Перевірити changelog (містить breaking changes?)
- [ ] Запланувати вікно оновлення (найменша активність: 03:00-04:00 EEST)
- [ ] Сповістити користувачів про запланований даунтайм

### Інструменти
```bash
# Встановити утиліти для бекапів
sudo apt install postgresql-client-15 pgbackrest
```

### Створення резервних копій
База даних
```bash
# PostgreSQL
pg_dump -U botuser -d shopbot -F c -f /backups/shopbot_$(date +%Y%m%d).dump

# SQLite (якщо використовується)
sqlite3 data/database.db ".backup '/backups/db_$(date +%Y%m%d).bak'"
```

Код та конфігурація
```bash
# Архівувати поточну версію
tar -czvf /backups/bot_v$(cat VERSION).tar.gz --exclude='venv' .
```

### Перевірка сумісності
```bash
# Тест на staging-середовищі
docker-compose -f docker-compose.staging.yml up --build -d
# Перевірити:
# 1. Відповідь на /start
# 2. Міграції БД
# 3. Логи помилок
```

## 2. Процес оновлення
### Зупинка служб
```bash
# Зупинити бота
docker stop shopbot
# Зупинити Celery workers (якщо є)
supervisorctl stop celery_worker
```

### Розгортання коду
```bash
# Отримати останню версію
git fetch --tags
git checkout vX.Y.Z

# Оновити залежності
pip install -r requirements.txt --upgrade

# Застосувати міграції БД (якщо потрібно)
alembic upgrade head
```

### Конфігурація
```bash
# Оновити змінні середовища
cp .env.prod .env.prod.bak
nano .env.prod  # Внести зміни

# Перевірити конфіг
python -m configtest
```

### Запуск після оновлення
```bash
# Запустити бота
docker-compose -f docker-compose.prod.yml up -d --build

# Перевірка здоров'я
curl -X GET http://localhost:8000/healthcheck
```

### Відкат (rollback) у разі збою
```bash
# Відновити БД
pg_restore -U botuser -d shopbot -c /backups/shopbot_YYYYMMDD.dump

# Відновити код
tar -xzvf /backups/bot_vOLD.tar.gz -C /opt/bot
```

