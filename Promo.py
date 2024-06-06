import pandas as pd

# Данные для таблицы Promotion
promotions = [
    {"promotion_id": 1, "discount": 0, "promotion_name": "-"},
    {"promotion_id": 2, "discount": 5, "promotion_name": "LETO Sale"},
    {"promotion_id": 3, "discount": 10, "promotion_name": "Welcome Discount"}
]

# Создание DataFrame
promotions_df = pd.DataFrame(promotions)

# Сохранение таблицы в CSV файл
promotions_df.to_csv('csv/Promotion.csv', index=False)

print("Таблица Promotion сохранена в 'Promotion.csv'.")
