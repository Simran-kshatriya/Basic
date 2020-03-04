import pandas as pd

abc = {'Day': [1, 2, 3, 4, 5, 6], "Visitors": [1000, 2000, 1000, 1500, 2000, 3000], 'Bonus_rate': [11, 12, 12, 13, 15, 16]}

df = pd.DataFrame(abc)

print(df)
