import sqlite3
import pandas as pd

# Создание базы данных SQLite
conn = sqlite3.connect('sql/salon_management.db')
cursor = conn.cursor()

# Чтение и выполнение SQL файла
with open('sql/create.sql', 'r') as file:
    sql_script = file.read()
cursor.executescript(sql_script)
conn.commit()

# Словарь файлов CSV и соответствующих имен таблиц
csv_files = {
    'Schedule_state.csv': 'Schedule_state',
    'Schedule.csv': 'Schedule',
    'Master_Service.csv': 'Master_Service',
    'Masters.csv': 'Master',
    'Positions.csv': 'Position',
    'Salons.csv': 'Salon',
    'Services.csv': 'Service'
}

# Загрузка данных из CSV файлов в соответствующие таблицы
for csv_file, table_name in csv_files.items():
    df = pd.read_csv(f'csv/{csv_file}')
    df.to_sql(table_name, conn, if_exists='append', index=False)

# Закрытие соединения с базой данных
conn.close()
