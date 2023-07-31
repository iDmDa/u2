#Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, 
# а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть, 
# чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть

import random

coins = []
coin_count = int(input("Введите число монет: "))
for i in range(coin_count):
    number = random.randint(0, 1)
    coins.append(number)
print(coins)
print("Необходимо перевернуть монет:", coins.count(0) if coins.count(0) < coins.count(1) else coins.count(1))