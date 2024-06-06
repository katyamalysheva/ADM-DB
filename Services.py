import csv
import random
from datetime import datetime, timedelta

# Услуги
service_data = [
    {"service_id": "1", "service_name": "Маникюр", "price_decimal": "1000", "duration": "45"},
    {"service_id": "2", "service_name": "Маникюр с покрытием", "price_decimal": "1500", "duration": "60"},
    {"service_id": "3", "service_name": "Педикюр", "price_decimal": "2000", "duration": "60"},
    {"service_id": "4", "service_name": "Педикюр с покрытием", "price_decimal": "2500", "duration": "75"},
    {"service_id": "5", "service_name": "Стрижка", "price_decimal": "2000", "duration": "60"},
    {"service_id": "6", "service_name": "Макияж", "price_decimal": "3000", "duration": "90"},
    {"service_id": "7", "service_name": "Коррекция бровей", "price_decimal": "800", "duration": "30"},
    {"service_id": "8", "service_name": "Ламинирование ресниц", "price_decimal": "2500", "duration": "120"},
    {"service_id": "9", "service_name": "Наращивание ресниц", "price_decimal": "4000", "duration": "150"}
]

csv_services_recreated_path = 'csv/Services.csv'
with open(csv_services_recreated_path, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=service_data[0].keys())
    writer.writeheader()
    writer.writerows(service_data)
