from faker import Faker
import pandas as pd
import random

# Инициализация генератора Faker с русской локалью
fake = Faker('ru_RU')

# Количество клиентов, которое нужно сгенерировать
num_clients = 20 * 3 * 14  # 18-20 * 3 * 14

# Функция для генерации клиента
def generate_client(client_id):
    gender = 'Ж' if random.random() < 0.85 else 'М'
    return {
        'client_id': client_id,
        'last_name': fake.last_name_female() if gender == 'Ж' else fake.last_name_male(),
        'first_name': fake.first_name_female() if gender == 'Ж' else fake.first_name_male(),
        'middle_name': fake.middle_name_female() if gender == 'Ж' else fake.middle_name_male(),
        'gender': gender,
        'phone_number': fake.phone_number(),
        'birth_date': fake.date_of_birth(minimum_age=18, maximum_age=70),
        'email': fake.email()
    }

# Генерация списка клиентов
clients = [generate_client(client_id) for client_id in range(1, num_clients + 1)]

# Преобразование в DataFrame
clients_df = pd.DataFrame(clients)

# Сохранение в CSV файл
clients_df.to_csv('csv/Clients.csv', index=False, encoding='utf-8')

print(f'Сгенерировано {num_clients} клиентов и сохранено в clients.csv')
