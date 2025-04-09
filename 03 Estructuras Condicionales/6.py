import random
from statistics import mode, median, mean

nums = [random.randint(1, 100) for i in range(50)]
moda = mode(nums)
mediana = median(nums)
media = mean(nums)

sesgo: str = "Sin sesgo"

if media > mediana and mediana > moda:
  sesgo = "Positivo"
if media < mediana and mediana < moda:
  sesgo = "Negativo"

print(f"Sesgo: {sesgo}")