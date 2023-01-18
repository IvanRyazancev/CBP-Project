print("           Calculation of Bridge Parameters. CBP.         ")
print("                  Расчет параметров моста.                ")

print("")
print("")


# Модуль ввода исходных данных

class Objekt:  # Создание объекта "Мост"

    Name_Class = "Мост"

    def __init__(self, name_objekt, dlina_objekt, gabarit_objekt, kol_proletov):
        self.name_objekt = name_objekt
        self.dlina_objekt = dlina_objekt
        self.gabarit_objekt = gabarit_objekt
        self.kol_proletov = kol_proletov


class Prolet:  # Создание и описание класса "Пролет"

    Name_Class = "Пролет "

    #     Характеристика пролетного строения

    def __init__(self, dlina_proleta, shirina_proleta, nomer_proleta):  # Создание объекта "Пролет"
        self.dlina_proleta = dlina_proleta
        self.shirina_proleta = shirina_proleta
        self.nomer_proleta = nomer_proleta


class Balka:  # Создание объекта "Балка"

    Name_Class = "Балка"

    def __init__(self, dlina_balka, visota_balka, shirina_balka, nomer_balka, naimenovanie_balka, massa_balka,
                 material_balka):
        self.dlina_balka = dlina_balka
        self.visota_balka = visota_balka
        self.shirina_balka = shirina_balka
        self.nomer_balka = nomer_balka
        self.naimenovanie_balka = naimenovanie_balka
        self.massa_balka = massa_balka
        self.material_balka = material_balka


# Модуль расчета параметров моста

# Модуль ввода исходных данных

bridge = Objekt(input("Введите название проекта: "), float(input("Введите длину сооружения, м: ")),
                input("Введите габарит сооружения, м: "), int(input("Введите желательное количество пролетов, шт.: ")))

# Модуль вывода исходных данных

print("Расчет выполнен для проекта: ", bridge.name_objekt)
print("Исходные данные: ")
print("_________________")
print("Габарит моста Г -", bridge.gabarit_objekt)
print("Длина сооружения: ", bridge.dlina_objekt, "м.")

# Модуль вывода расчетных данных

for i in range(int(bridge.kol_proletov)):
    span = Prolet((bridge.dlina_objekt - 0.1) / bridge.kol_proletov, int(bridge.gabarit_objekt), i + 1)
    print("Номер пролетного строения: №", span.nomer_proleta)
    print("Исходные данные пролетного строения: ")
    print("Длина пролета: ", round(span.dlina_proleta, 2),
          "м.")  # округление значения длины пролета до 2-го знака после запятой
    print("Ширина пролетного строения: ", span.shirina_proleta, "м.")