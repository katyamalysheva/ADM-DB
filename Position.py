import pandas as pd

position_names = [
    "Топ-мастер маникюра и педикюра", "Мастер маникюра и педикюра",
    "Мастер макияжа, ламинирования ресниц и коррекции бровей",
    "Топ-мастер по волосам", "Мастер по волосам",
    "Мастер по наращиванию ресниц"
]

rates = [2500, 1500, 2000, 3000, 1800, 2200]

df_positions = pd.DataFrame({
    'position_id': range(1, len(position_names) + 1),
    'rate': rates,
    'position_name': position_names
})

df_positions.to_csv('csv/Positions.csv', index=False)

