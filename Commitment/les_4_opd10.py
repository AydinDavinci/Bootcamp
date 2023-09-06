
seconden_per_minuut = 60
seconden_per_uur = 60 * seconden_per_minuut


uren_per_dag = 24


dagen_per_week = 7
dagen_per_jaar = 365

seconden_per_dag = uren_per_dag * seconden_per_uur
seconden_per_week = dagen_per_week * seconden_per_dag
seconden_per_jaar = dagen_per_jaar * seconden_per_dag


print(f"Aantal seconden in een dag: {seconden_per_dag}")
print(f"Aantal seconden in een week: {seconden_per_week}")
print(f"Aantal seconden in een jaar (zonder schrikkeljaar): {seconden_per_jaar}")