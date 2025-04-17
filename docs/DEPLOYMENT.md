# Інструкція розгортання

## 1. Передумови
- Ubuntu 22.04 LTS
- Docker 24.0+
- PostgreSQL 15
- Python 3.10

## 2. Налаштування сервера
```bash
# Оновлення системи
sudo apt update && sudo apt upgrade -y

# Встановлення залежностей
sudo apt install -y git python3-pip postgresql

# Клонування репозиторію
git clone https://github.com/your-username/telegram-shop-bot.git
cd telegram-shop-bot