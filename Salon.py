import pandas as pd

# Создание данных для таблицы Salon
salons_data = {
    'salon_id': [1, 2, 3],
    'address': ['ул. Ленина, д. 1', 'ул. Карла Маркса, д. 2', 'ул. Пушкина, д. 3'],
    'area': ['Центр', 'Юг', 'Север'],
    'opening_time': ['09:00', '09:00', '09:00'],
    'closing_time': ['21:00', '21:00', '21:00']
}

# Создание DataFrame
salons_df = pd.DataFrame(salons_data)

# Сохранение DataFrame в CSV файл
salons_df.to_csv('csv/Salons.csv', index=False)
