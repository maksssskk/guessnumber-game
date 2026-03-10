import datetime

def czy_poprawny(pesel):
    if len(pesel) != 11 or not pesel.isdigit():
        return False
    
    wagi = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
    suma = sum(int(pesel[i]) * wagi[i] for i in range(10)) 
    kontrolna = (10 - (suma % 10)) % 10
    
    if kontrolna != int(pesel[10]):
        return False

    try:
        r_short = int(pesel[0:2])
        m_raw = int(pesel[2:4])
        dzien = int(pesel[4:6])

        if 81 <= m_raw <= 92:
            rok, miesiac = 1800 + r_short, m_raw - 80
        elif 1 <= m_raw <= 12:
            rok, miesiac = 1900 + r_short, m_raw
        elif 21 <= m_raw <= 32:
            rok, miesiac = 2000 + r_short, m_raw - 20
        elif 41 <= m_raw <= 52:
            rok, miesiac = 2100 + r_short, m_raw - 40
        elif 61 <= m_raw <= 72:
            rok, miesiac = 2200 + r_short, m_raw - 60
        else:
            return False
        
        datetime.date(rok, miesiac, dzien)
        return True
    except ValueError:
        return False

def presort_lista(pesel):
    r_short = int(pesel[0:2])
    m_raw = int(pesel[2:4])
    dz = int(pesel[4:6])
    p = int(pesel[9])

    if 81 <= m_raw <= 92:
        rok, miesiac = 1800 + r_short, m_raw - 80
    elif 1 <= m_raw <= 12:
        rok, miesiac = 1900 + r_short, m_raw
    elif 21 <= m_raw <= 32:
        rok, miesiac = 2000 + r_short, m_raw - 20
    elif 41 <= m_raw <= 52:
        rok, miesiac = 2100 + r_short, m_raw - 40
    else:
        rok, miesiac = 2200 + r_short, m_raw - 60

    plec = 'K' if p % 2 == 0 else 'M'
    data = datetime.date(rok, miesiac, dz)
    return data, plec

def dopisz_lista(pesel, lista):
    if czy_poprawny(pesel) and pesel not in lista:
        lista.append(pesel)
        return True
    return False

def sort_lista(lista, kryterium):
    if kryterium == '1':
        return sorted(lista, key=lambda p: presort_lista(p)[0])
    elif kryterium == '2':
        return sorted(lista, key=lambda p: presort_lista(p)[1])
    elif kryterium == '3':
        return sorted(lista, key=lambda p: (presort_lista(p)[1], presort_lista(p)[0]))
    else:
        return lista

peseli = []
dopisz_lista('58101143531', peseli) 
dopisz_lista('86111812725', peseli) 
print("Sorted by data:", sort_lista(peseli, '1'))
print("Sorted by gender:", sort_lista(peseli, '2'))
print("Sorted by gender and data:", sort_lista(peseli, '3'))