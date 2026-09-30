def format_record(rec):
    if not isinstance(rec, tuple) or len(rec) != 3:
        raise TypeError
    fio, group, gpa = rec
    if not isinstance(fio, str):
        raise TypeError ("ФИО должно быть строкой")
    if not isinstance(group, str):
        raise TypeError ("Группа должна быть строкой")
    if not isinstance(gpa, (int, float)):
        raise TypeError ("gpa должен быть числом") 
    fio = " ".join(fio.strip().split())
    group = group.strip()
    if not fio:
        raise ValueError("ФИО не может быть пустым")
    if len(fio.split()) < 2:
        raise ValueError("ФИО должно содержать как минимум фамилию и имя")
    if not group:
        raise ValueError("Группа не может быть пустым")
    if not 0.0 <= gpa <= 5.0:
        raise ValueError("GPA должен быть от 0.0 до 5.0")
    parts = fio.split()
    surname = parts[0][0].upper() + parts[0][1:].lower()
    names = parts[1:]
    initials = "".join(name[0].upper() + "." for name in names)
    return f"{surname} {initials}, гр. {group}, GPA {gpa:.2f}"


inf1 = ("Иванов Иван Иванович", "BIVT-25", 4.6)
inf2 = ("Петров Пётр", "IKBO-12", 5.0)
inf3 = ("  сидорова  анна   сергеевна ", "ABB-01", 3.999)
inf4 = ("  ПЕТРОВ ПЕТР", "ABB-01", 3.999)
print(format_record(inf1))
print(format_record(inf2))
print(format_record(inf4))

