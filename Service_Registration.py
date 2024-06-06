import pandas as pd
import random
from datetime import datetime, timedelta

# Загрузка данных
clients_df = pd.read_csv('csv/Clients.csv')
master_service_df = pd.read_csv('csv/Master_Service.csv')
masters_df = pd.read_csv('csv/Masters.csv')
salons_df = pd.read_csv('csv/Salons.csv')
schedule_df = pd.read_csv('csv/Schedule.csv')
schedule_state_df = pd.read_csv('csv/Schedule_state.csv')
services_df = pd.read_csv('csv/Services.csv')

# Определение вместимости на основе типа мастера
master_capacities = {}
for idx, master in masters_df.iterrows():
    if idx < 9:
        master_capacities[master['master_id']] = (5, 6)  # Маникюр
    elif idx < 12:
        master_capacities[master['master_id']] = (4, 5)  # Макияж
    elif idx < 15:
        master_capacities[master['master_id']] = (3, 6)  # Волосы
    else:
        master_capacities[master['master_id']] = (2, 3)  # Наращивание ресниц

# Фильтрация рабочих дней
working_schedule = schedule_df[schedule_df['state_id'] == 1]

# Получение списка работающих мастеров
working_masters = working_schedule['master_id'].unique()

# Функция для конвертации строки в объект времени
def str_to_time(t):
    return datetime.strptime(t, '%H:%M:%S').time()

# Функция для комбинирования даты и времени
def combine_date_time(date, time):
    return datetime.combine(date, time)

# Получение длительности услуг
service_durations = services_df.set_index('service_id')['duration'].to_dict()

# Инициализация списка для хранения обновленных регистраций с временами
registrations = []
service_registrations = []

# Определение рабочих часов
work_start_time = str_to_time('09:00:00')
work_end_time = str_to_time('21:00:00')

# Вспомогательная функция для добавления минут к объекту времени
def add_minutes_to_time(time_obj, minutes):
    full_datetime = combine_date_time(datetime.today(), time_obj)
    new_datetime = full_datetime + timedelta(minutes=minutes)
    return new_datetime.time()

# Конвертация строковой даты в объект datetime.date
working_schedule['date'] = pd.to_datetime(working_schedule['date']).dt.date

# Планирование регистраций с обновленной конвертацией даты
for master_id in working_masters:
    master_schedule = working_schedule[working_schedule['master_id'] == master_id]
    
    for _, row in master_schedule.iterrows():
        date = row['date']
        current_time = work_start_time
        
        # Получение услуг, которые может выполнять мастер
        master_services = master_service_df[master_service_df['master_id'] == master_id]['service_id'].tolist()
        if not master_services:
            continue
        
        # Случайное перемешивание услуг
        random.shuffle(master_services)
        
        # Получение вместимости для мастера
        service_capacity = master_capacities[master_id]
        num_clients = random.randint(service_capacity[0], service_capacity[1])
        clients = clients_df.sample(num_clients)
        
        # Рандомизация начального времени ближе к вечеру
        random_shift_minutes = random.randint(0, 360)  # до 6 часов сдвига
        current_time = add_minutes_to_time(work_start_time, random_shift_minutes)
        
        for client in clients.itertuples():
            # Обеспечение различных услуг для каждого клиента в течение дня
            service_id = random.choice(master_services)
            service_duration = int(service_durations[service_id])
            start_time = current_time
            end_time = add_minutes_to_time(current_time, service_duration)
            
            # Обеспечение окончания встречи в рабочее время
            if combine_date_time(date, end_time) > combine_date_time(date, work_end_time):
                break
            
            registration = {
                'registration_id': len(registrations) + 1,
                'client_id': client.client_id,
                'date': date,
                'opening_time': start_time,
                'closing_time': end_time,
                'master_id': master_id
            }
            registrations.append(registration)

            service_registration = {
                'service_id': service_id,
                'registration_id': registration['registration_id']
            }
            service_registrations.append(service_registration)
            
            # Обновление текущего времени для следующей встречи, включая 15-минутный перерыв
            current_time = add_minutes_to_time(current_time, service_duration + 15 + 15)  # Добавление 15-минутного буфера и 15-минутного перерыва

# Конвертация списка словарей в DataFrame
registrations_df = pd.DataFrame(registrations)
service_registrations_df = pd.DataFrame(service_registrations)

# Сохранение обновленных данных о регистрации в CSV файлы
registrations_df.to_csv('csv/Registration.csv', index=False)
service_registrations_df.to_csv('csv/Service_Registration.csv', index=False)

print("Регистрации клиентов сохранены в 'Registration.csv'.")
print("Связи регистраций с услугами сохранены в 'Service_Registration.csv'.")
