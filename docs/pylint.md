# Налаштування Pylint

## Правила для нашого проєкту

### Важливі відключені правила
- `missing-docstring` - Не вимагаємо докстрінгів для кожного методу
- `too-few-public-methods` - Дозволяємо класи-менеджери
- `import-error` - Ігноруємо помилки імпортів AIOgram

### Ключові обмеження
| Параметр            | Значення | Пояснення               |
|---------------------|----------|-------------------------|
| `max-line-length`   | 120      | Макс. довжина рядка     |
| `max-args`          | 6        | Аргументи функції       |
| `max-locals`        | 15       | Локальні змінні         |

## Інтеграція з PyCharm
1. `File > Settings > Tools > External Tools`
2. Додайте нову конфігурацію:
   - Program: `pylint`
   - Arguments: `--rcfile=.pylintrc $FilePath$`
   - Working dir: `$ProjectFileDir$`

## Приклади запуску
```bash
# Перевірити всю папку handlers
pylint handlers/ --rcfile=.pylintrc

# Перевірити з HTML-звітом
pylint app.py --rcfile=.pylintrc --output-format=html > report.html