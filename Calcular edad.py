
Day = int(input("Inserete el día de nacimiento: "))
Month = int(input("Inserte el mes de nacimiento: "))
Year = int(input("Inserte el año de nacimiento: " ))
print("Usted nacio el día", Day, "del mes", Month, "del año", Year )
Present_Year = 2025
Present_Day = 11
Present_Month = 5
Actual_Day = (30*Month)
Actual_Month = (12+(Present_Month-Month))
if Day >= Present_Day:
   Actual_Year = (Present_Year-1)
print("Usted actualmente tiene", Actual_Day, "dias con", Actual_Month, "meses y", Actual_Year, "años")