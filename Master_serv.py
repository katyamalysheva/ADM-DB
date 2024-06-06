import pandas as pd
import itertools

# Загрузите ваши CSV файлы
masters_df = pd.read_csv('Masters.csv')
services_df = pd.read_csv('Services.csv')

# Определение услуг для каждой категории
manicure_pedicure_services = services_df[services_df['service_name'].str.contains('Маникюр|Педикюр')]['service_id']
makeup_lamination_correction_services = services_df[services_df['service_name'].str.contains('Макияж|Ламинирование|Коррекция')]['service_id']
haircut_services = services_df[services_df['service_name'].str.contains('Стрижка')]['service_id']
eyelash_extension_services = services_df[services_df['service_name'].str.contains('Наращивание ресниц')]['service_id']

# Назначение мастеров для каждой категории
manicure_pedicure_masters = masters_df.iloc[:9]['master_id']
makeup_lamination_correction_masters = masters_df.iloc[9:12]['master_id']
haircut_masters = masters_df.iloc[12:15]['master_id']
eyelash_extension_masters = masters_df.iloc[15:18]['master_id']

# Создание комбинаций для каждой категории
manicure_pedicure_combinations = list(itertools.product(manicure_pedicure_masters, manicure_pedicure_services))
makeup_lamination_correction_combinations = list(itertools.product(makeup_lamination_correction_masters, makeup_lamination_correction_services))
haircut_combinations = list(itertools.product(haircut_masters, haircut_services))
eyelash_extension_combinations = list(itertools.product(eyelash_extension_masters, eyelash_extension_services))

# Объединение всех комбинаций в один DataFrame
all_combinations = (manicure_pedicure_combinations + 
                    makeup_lamination_correction_combinations + 
                    haircut_combinations + 
                    eyelash_extension_combinations)

master_service_df = pd.DataFrame(all_combinations, columns=['master_id', 'service_id'])

# Сохранение DataFrame в новый CSV файл
master_service_df.to_csv('csv/Master_Service.csv', index=False)
