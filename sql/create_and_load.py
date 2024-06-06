import sqlite3
import pandas as pd

conn = sqlite3.connect('sql/salon_management.db')
cursor = conn.cursor()

with open('sql/create.sql', 'r') as file:
    sql_script = file.read()
cursor.executescript(sql_script)
conn.commit()

csv_files = {
    'Schedule_state.csv': 'Schedule_state',
    'Schedule.csv': 'Schedule',
    'Master_Service.csv': 'Master_Service',
    'Masters.csv': 'Master',
    'Positions.csv': 'Position',
    'Salons.csv': 'Salon',
    'Clients.csv': 'Client',
    'Promotion.csv': 'Promotion',
    'Registration.csv': 'Registration',
    'Receipts.csv': 'Receipt',
    'Service_Registration.csv': 'Service_Registration'
}

for csv_file, table_name in csv_files.items():
    df = pd.read_csv(f'csv/{csv_file}')
    df.to_sql(table_name, conn, if_exists='append', index=False)

conn.close()
