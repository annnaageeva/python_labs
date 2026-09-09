fio = input()
parts = fio.split()
surname = parts[0]
name = parts[1]
patronymic = parts[2]
initials = (surname[0] + name[0] + patronymic[0]).upper()
name_clean = ' '.join(parts)
len_name_clean = len(name_clean)

print(f"ФИО: {name_clean}")
print(f"Инициалы: {initials}.")
print(f"Длина (символов) : {len_name_clean}")
