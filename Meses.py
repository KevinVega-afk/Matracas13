import datetime

Dia = int(input("\nIngrese su dia de nacimiento: "))
Month = int(input("Ingrese su mes de nacimiento: "))
Year = int(input("Ingrese su año de nacimiento: "))

Bdia = datetime.datetime(Year, Month, Dia)
today = datetime.date.today()

Meses = (Bdia.year - today.year) * 12 + (Bdia.month - today.month)

print("\nHan pasado ", abs(Meses), " meses desde su fecha de nacimiento\n")