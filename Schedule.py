import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Загрузка данных
file_path = 'csv/Masters.csv'  # Обновите путь к вашему файлу
masters_df = pd.read_csv(file_path)

# Константы
num_days = 14
manicurists = masters_df.head(9)  # Первые 9 мастеров - маникюристы
other_masters = masters_df.iloc[9:]  # Остальные мастера
opening_time = "09:00:00"
closing_time = "21:00:00"
start_date = datetime.now().date()

# Статусы расписания
states_ru = {
    1: 'Рабочий день',
    2: 'Выходной',
    3: 'Больничный',
    4: 'Отпуск'
}

# Генерация базового расписания с шаблоном 2-1 для всех мастеров
def generate_base_schedule(num_masters):
    base_schedule = []
    for i in range(num_masters):
        schedule = []
        day_off_counter = 0
        for day in range(num_days):
            if day_off_counter == 2:
                schedule.append(2)  # Выходной день
                day_off_counter = 0
            else:
                schedule.append(1)  # Рабочий день
                day_off_counter += 1
        base_schedule.append(schedule)
    return np.array(base_schedule)

# Создание базового расписания для маникюристов и остальных мастеров
manicurist_schedule = generate_base_schedule(len(manicurists))
other_master_schedule = generate_base_schedule(len(other_masters))

# Корректировка расписания, чтобы обеспечить наличие хотя бы двух работающих маникюристов в одном салоне каждый день
for day in range(num_days):
    while np.sum(manicurist_schedule[:, day] == 1) < 2:
        off_indices = np.where(manicurist_schedule[:, day] == 2)[0]
        switch_index = np.random.choice(off_indices)
        manicurist_schedule[switch_index, day] = 1  # Переключение с выходного на рабочий день

# Случайное назначение больничных и отпусков
def assign_random_states(schedule, state_id, num_days=2):
    num_masters, total_days = schedule.shape
    for _ in range(num_days):
        master_index = np.random.randint(num_masters)
        day_index = np.random.randint(total_days)
        while schedule[master_index, day_index] != 1:  # Назначение только на рабочие дни
            master_index = np.random.randint(num_masters)
            day_index = np.random.randint(total_days)
        schedule[master_index, day_index] = state_id

# Назначение 2 больничных и 2 отпусков случайным образом
assign_random_states(manicurist_schedule, 3, 2)  # Больничный
assign_random_states(manicurist_schedule, 4, 2)  # Отпуск
assign_random_states(other_master_schedule, 3, 2)  # Больничный
assign_random_states(other_master_schedule, 4, 2)  # Отпуск

# Объединение расписаний
combined_schedule = np.vstack((manicurist_schedule, other_master_schedule))

# Создание итоговой DataFrame расписания
schedule_df = pd.DataFrame(combined_schedule, columns=[f'Day_{i+1}' for i in range(num_days)])
schedule_df.insert(0, 'master_id', masters_df['master_id'])

# Перевод значений статусов на русский
schedule_df_ru = schedule_df.copy()
for col in schedule_df.columns[1:]:
    schedule_df_ru[col] = schedule_df[col].map(states_ru)

# Создание таблицы состояния расписания
schedule_state_df = pd.DataFrame(list(states_ru.items()), columns=['state_id', 'state_name'])

# Генерация таблицы расписания с полями
shedule_entries = []
shedule_id_counter = 1
for day in range(num_days):
    current_date = start_date + timedelta(days=day)
    for master in masters_df.itertuples():
        shedule_id = shedule_id_counter
        state_id = schedule_df.iloc[master.Index, day+1]
        shedule_entries.append([
            shedule_id,
            state_id,
            master.master_id,
            closing_time,
            opening_time,
            current_date
        ])
        shedule_id_counter += 1

shedule_df = pd.DataFrame(shedule_entries, columns=[
    'schedule_id', 'state_id', 'master_id', 'closing_time', 'opening_time', 'date'
])

# Сохранение таблицы состояния расписания в CSV
schedule_state_csv_path = 'csv/Schedule_state.csv'  # Обновите путь по вашему усмотрению
schedule_state_df.to_csv(schedule_state_csv_path, index=False, encoding='utf-8')

# Сохранение таблицы расписания в CSV
shedule_csv_path = 'csv/Schedule.csv'  # Обновите путь по вашему усмотрению
shedule_df.to_csv(shedule_csv_path, index=False, encoding='utf-8')

print(f'CSV файл состояния расписания сохранен по пути: {schedule_state_csv_path}')
print(f'CSV файл расписания сохранен по пути: {shedule_csv_path}')
