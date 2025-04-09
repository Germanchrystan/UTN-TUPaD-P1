DAYS_BY_MONTH = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def isValidMonth(monthInput: str) -> bool:
  try:
    int(monthInput)
  except ValueError:
    return False
  
  return int(monthInput) > 0 and int(monthInput) < 13

def isValidDay(dayInput: str, month: int) -> bool:
  try:
    int(dayInput)
  except ValueError:
    return False
  return int(dayInput) > 0 and int(dayInput) <= DAYS_BY_MONTH[month - 1]

def convertToYearDay(month: int, day: int) -> int:
  result = 0
  for i in range(0, month - 1):
    result += DAYS_BY_MONTH[i]
  result += day
  return result

day: int
month: int
season: str

dayInputStr: str
monthInputStr: str

validMonth = False
validDay = False
validHemisphere = False

while not validHemisphere:
  hemisphere = input("Ingrese el hemisferio (N/S): ")
  if hemisphere.upper() in ["N", "S"]:
    hemisphere = hemisphere.upper()
    validHemisphere = True
  else:
    print("Hemisferio no válido")


while not validMonth:
  monthInputStr = input("Ingrese el número del mes: ")
  if isValidMonth(monthInputStr):
    month = int(monthInputStr)
    validMonth = True
  else:
    print("Mes no válido")

while not validDay:
  dayInputStr = input("Ingrese el número del día: ")
  if isValidDay(dayInputStr, month):
    day = int(dayInputStr)
    validDay = True
  else:
    print("Día not válido")

yearDay = convertToYearDay(month, day)
season: str

if yearDay >= 81 and yearDay <= 172:
  if (hemisphere == "S"):
    season = "Otoño"
  else:
    season = "Primavera"
elif yearDay >= 173 and yearDay <= 263:
  if (hemisphere == "S"):
    season = "Invierno"
  else:
    season = "Verano"
elif yearDay >= 264 and yearDay <= 355:
  if (hemisphere == "S"):
    season = "Primavera"
  else:
    season = "Otoño"
else:
  if (hemisphere == "S"):
    season = "Verano"
  else:
    season = "Invierno"

print(f"Estación: {season}")