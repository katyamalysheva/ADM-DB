import pandas as pd
import random
from datetime import datetime

# Загрузка данных
promotions_df = pd.read_csv('csv/Promotion.csv')
registrations_df = pd.read_csv('csv/Registration.csv')
service_registrations_df = pd.read_csv('csv/Service_Registration.csv')
services_df = pd.read_csv('csv/Services.csv')

# Фильтрация регистраций до 14 июня
filtered_registrations = registrations_df[pd.to_datetime(registrations_df['date']) <= pd.to_datetime('2024-06-14')]

# Объединение регистраций с услугами
merged_data = pd.merge(filtered_registrations, service_registrations_df, on='registration_id')
merged_data = pd.merge(merged_data, services_df, on='service_id')

# Инициализация списка для чеков
receipts = []

# Присвоение случайных скидок и расчет суммы
for index, row in merged_data.iterrows():
    promotion = promotions_df.sample(1).iloc[0]
    discount_amount = row['price'] * (promotion['discount'] / 100)
    total_sum = row['price'] - discount_amount
    
    receipt = {
        'receipt_id': len(receipts) + 1,
        'registration_id': row['registration_id'],
        'promotion_id': promotion['promotion_id'],
        'payment_method': random.choice(['cash', 'card']),
        'creation_date': row['date'],  # Использование даты процедуры как даты создания чека
        'total_sum': round(total_sum, 2)
    }
    receipts.append(receipt)

# Конвертация списка словарей в DataFrame
receipts_df = pd.DataFrame(receipts)

# Сохранение данных чеков в CSV файл
receipts_df.to_csv('csv/Receipts.csv', index=False)

print("Чеки сохранены в 'csv/Receipts.csv'.")
