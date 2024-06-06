import pandas as pd
import random
from faker import Faker

def generate_patronymic(name, gender):
    if gender == 'M':
        return name + 'ович'
    else:
        return name + 'овна'

fake = Faker('ru_RU')

total_masters = 18
male_count = 3
female_count = total_masters - male_count

columns = ['master_id', 'last_name', 'first_name', 'middle_name', 'gender', 'phone_number', 'birth_date', 'position_id']

df_masters = pd.DataFrame(columns=columns)

for i in range(total_masters):
    gender = 'M' if i < male_count else 'F'
    first_name = fake.first_name_male() if gender == 'M' else fake.first_name_female()
    father_name = fake.first_name_male()
    middle_name = generate_patronymic(father_name, gender)
    last_name = fake.last_name_male() if gender == 'M' else fake.last_name_female()
    phone_number = fake.phone_number()
    birth_date = fake.date_of_birth(minimum_age=18, maximum_age=65).isoformat()
    position_id = random.randint(1, 6)

    new_row = pd.DataFrame({
        'master_id': [i + 1],
        'last_name': [last_name],
        'first_name': [first_name],
        'middle_name': [middle_name],
        'gender': [gender],
        'phone_number': [phone_number],
        'birth_date': [birth_date],
        'position_id': [position_id],
    })
    df_masters = pd.concat([df_masters, new_row], ignore_index=True)

df_masters.to_csv('csv/Masters.csv', index=False)