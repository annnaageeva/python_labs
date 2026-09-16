m = int(input("Минуты: "))
hours = (m // 60) % 24
minut = m % 60 
print(f"{hours:02d}:{minut:02d}")