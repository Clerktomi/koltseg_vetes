import random
import bcrypt
import getpass
import pwinput
from datetime import datetime
import csv
koltsegek = []
koltseg = {}
valuta = ''
with open('valuta.txt','r',encoding='utf-8') as file_r:
    for sor in file_r:
        valuta = sor
kategoriak = []  
kategoria = {}

abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

fiok = {}

with open('fiok.txt', 'r', encoding='utf-8') as file_rd:
    for sor in file_rd:
        data = sor.strip().split(';')
        if len(data) >= 2:
            fiok['username'] = data[0]
            fiok['password'] = data[1]

if len(fiok) == 0:
    print()
    print('Kérjük regisztráljon! 🔥')
    print()
    username = input('Felhasználónév: ')
    print()
    password = pwinput.pwinput(prompt='Jelszó: ', mask='*')
    password_again = pwinput.pwinput(prompt='Jelszó ismét: ', mask='*')
    while password != password_again:
        print()
        print('A jelszavak nem eggyeznek!')
        print()
        password = pwinput.pwinput(prompt='Jelszó: ', mask='*')
        password_again = pwinput.pwinput(prompt='Jelszó ismét: ', mask='*')
    print()
    password_bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password_bytes, salt)
    with open('fiok.txt', 'w', encoding='utf-8') as f:
        f.write(f"{username};{hashed.decode('utf-8')}\n")
    print("Regisztráció sikeres!")

else:
    while True:
        print()
        print('Kérjük jelentkezzen be! 🔥')
        print()
        username_log = input('Felhasználónév: ')
        print()
        password_log = pwinput.pwinput(prompt='Jelszó: ', mask='*')
        password_log_bytes = password_log.encode('utf-8')

        if username_log == fiok.get('username') and bcrypt.checkpw(password_log_bytes, fiok.get('password').encode('utf-8')):
            print()
            print('Sikeres bejelentkezés! 🔥')
            print()
            break
        else:
            print()
            print('Hibás felhasználónév vagy jelszó! 🚫')
            print()

with open('data.txt','r',encoding='utf-8') as file_rd:
    for sor in file_rd:
        data = sor.strip().split(';')
        koltseg['költség_neve'] = data[0]
        koltseg['költség_dátuma'] = data[1]
        koltseg['költség_ára'] = int(data[2])
        koltseg['költség_kategoria'] = data[3]
        koltsegek.append(koltseg)
        koltseg = {}

with open('koltseg.csv','w',encoding='utf-8-sig') as file_write:
    print('Költség neve;Dátum;Ár;Kategoria',file=file_write)
    for elem in koltsegek:
        date_rem = elem['költség_dátuma'].replace('-','.')
        print(f'{elem['költség_neve']};{date_rem};{int(elem['költség_ára'])};{elem['költség_kategoria']}',file=file_write)

with open('kategoriak.txt','r',encoding='utf-8') as file_rd:
    for sor in file_rd:
        data = sor.split('\n')
        kategoriak.append(data[0])
        
honapok = [
    "január", "február", "március", "április", "május", "június",
    "július", "augusztus", "szeptember", "október", "november", "december"
]

honapok_szam = []
for i in range(1,13):
    egesz = '0'
    egesz += f'{i}'
    honapok_szam.append(egesz)

# print([honapok[1]],honapok_szam[1])    

print()
print(f'Üdvözöljük A költség vezető alkalmazásunkban, lehetőségek kiírása: (eszközök) (minen lehetőség megtekintéséhez: Beálítások ⚙️) (készítette: 👑 Szabó Tamás 👑 ©)')
print()

if len(koltsegek) == 0:
    print(f'Jelenleg nincsenek költségei!')
    print()
while True:
    muvelet = input('Kérem válasszon! (Új költség felvétele +)🟢 (Meglévő költség kivonása -)🔴 (meglévő költség szerkesztése: szerkesztés) (Meglévő költségek kiírása ENTER)↩️ (kilépés: exit)🔚: ').strip()
    while muvelet not in ['+','-','','eszközök','exit','szerkesztés','Beálítások','törlés','valuta']:
        print(f'')
        print(f'Nem megfelelő művelet!')
        print(f'')
        muvelet = input('Kérem válasszon! (Új költség felvétele +)🟢 (Meglévő költség kivonása -)🔴 (Meglévő költségek kiírása ENTER)↩️ (kilépés: exit)🔚: ').strip()
    if muvelet == 'exit':
        print()
        print('Sikeres kilépés!')
        break
    elif muvelet == 'valuta':
        print()
        new_valta = input(f'Kérem adja meg az új valutát (A régi: {valuta}): ')
        valuta = new_valta
        with open('valuta.txt','w',encoding='utf-8') as file_wr:
            print(new_valta,file=file_wr)
        print()
    elif muvelet == 'törlés':
        print()
        delete = input('Bizosan szeretne minden elemet törölni (igen / nem)(kilépés: exit) ? 🚧: ').lower().strip()
        while delete not in ['igen','nem','exit']:
            print('nem megfelelő művelet!💥')
            delete = input('Bizosan szeretne minden elemet törölni (igen / nem)(kilépés: exit) ? 🚧: ').lower().strip()
        if delete == 'exit':
            print()
            print(f'Sikeres kilépés ✅!')
            print()
            break
        elif delete == 'nem':
            print()
            print(f'Sikeres kilépés ✅!')
            print()
            break
        else:
            random_karakterek = ''
            while len(random_karakterek) < 5:
                karakter = random.choice(abc)
                if karakter not in random_karakterek:
                    random_karakterek += karakter
            print()
            bot = input(f'Kérem erősitse meg ezt a kódot: {random_karakterek}: ')
            while random_karakterek != bot:
                print()
                print('hiba történt!❌')
                print()
                bot = input(f'Kérem erősitse meg ezt a kódot: {random_karakterek}: ')
            with open('data.txt','w',encoding='utf-8') as file_del:
                continue
            with open('koltseg.csv','w',encoding='utf-8') as file_del:
                continue
            with open('kategoriak.txt','w',encoding='utf-8') as file_del:
                continue
            print()
            print('A Minden elem törölve lett! ✅')
            print()
    elif muvelet == 'Beálítások':
        print()
        print(f'A műveletek leírása ⬇️:')
        print()
        print('Gyors törlés (minden elemet töröl⚠️): (törlés)')
        print()
        print('Valuta át álítása: (valuta)💰')
        print()
    elif muvelet == 'szerkesztés':
        print()
        print('A költségek 💰:')
        print()
        
        for i in range(len(koltsegek)):
            print(f'    A költség leírása: {koltsegek[i]["költség_neve"]:<9} | dátum: {koltsegek[i]["költség_dátuma"]:<9} | Ár: {koltsegek[i]["költség_ára"]:<7} | kategória: {koltsegek[i]["költség_kategoria"]:<12} | sorszám: {i}')
        
        print()
        valaszt = int(input('Kérem adja meg a szerkeszteni kívánt elem sorszámát (kilépés = -1): '))
        
        if valaszt == -1:
            print('\nSikeres kilépés!\n')
            break
        
        if valaszt < 0 or valaszt >= len(koltsegek):
            print(f'\nHibás sorszám! Max sorszám: {len(koltsegek) - 1}\n')
            continue
        print()
        print(f'    A költség leírása: {koltsegek[valaszt]["költség_neve"]:<9} | dátum: {koltsegek[valaszt]["költség_dátuma"]:<9} | Ár: {koltsegek[valaszt]["költség_ára"]:<7} | kategória: {koltsegek[valaszt]["költség_kategoria"]:<12} | sorszám: {valaszt}')
        
        print()
        for_sure = input('Biztosan ezt az elemet szeretné szerkeszteni? (igen / nem): ').lower().strip()
        print()
        
        while for_sure not in ['igen', 'nem']:
            print('\nNem megfelelő művelet (igen / nem)\n')
            print()
            for_sure = input('Biztosan ezt az elemet szeretné szerkeszteni? (igen / nem): ').lower().strip()
            print()
        
        if for_sure == 'igen':
            koltsegek.pop(valaszt)
            print()

            adat_bevitel_leiras = input('Kérem adja meg a(z) (új) költség leírását (pl. telefon, repjegy)📊: ').strip()
            print()
            
            adat_bevital_kategoria = input('Kérem adja meg a költség kategóriáját (meglévő kategóriák kiíratása: kategoria)🏷️: ').strip().lower()
            print()

            if adat_bevital_kategoria in kategoriak:
                print('A kategória sikeresen kiválasztva✅! (már létezik)')
                print()
            else:
                print('A kategória sikeresen létrehozva✅!')
                print()
                kategoriak.append(adat_bevital_kategoria)
                with open('kategoriak.txt', 'a', encoding='utf-8') as file_add:
                    print(f'{adat_bevital_kategoria}', end='\n', file=file_add)

            adat_bevitel_datum = input('Kérem adja meg a dátumot (minta: 2025-05-14) (Mai dátum: ENTER)📆: ').strip()
            
            if adat_bevitel_datum == '':
                now = datetime.now()
                adat_bevitel_datum = now.strftime('%Y-%m-%d')
                print('\nA mai dátum sikeresen el lett mentve✅!\n')

            while True:
                try:
                    adat_bevitel_ar = int(input(f'Kérem adja meg a(z) árat {valuta} ban/ben💰: '))
                    print()
                    break
                except ValueError:
                    print('\nHibás formátum! Kérem egész számot adjon meg!💥\n')

            uj_koltseg = {
                'költség_neve': adat_bevitel_leiras,
                'költség_dátuma': adat_bevitel_datum,
                'költség_ára': adat_bevitel_ar,
                'költség_kategoria': adat_bevital_kategoria
            }
            
            koltsegek.append(uj_koltseg)

            #ujra iras
            with open('data.txt','w',encoding='utf-8') as file_wr:
                for elem in koltsegek:
                    print(f'{elem['költség_neve']};{elem['költség_dátuma']};{elem["költség_ára"]};{elem['költség_kategoria']}', file=file_wr)

    elif muvelet == '':
        if len(koltsegek) == 0:
            print()
            print(f'Még nem lett költség felvéve! 💡')
            print()
        else:
            for koltseg in koltsegek:
                print()
                print(f'A költség leírása: {koltseg['költség_neve']:<17} | dátum: {koltseg['költség_dátuma']:<10} | Ár: {koltseg['költség_ára']:<6} | kategória: {koltseg['költség_kategoria']:<15}')
                print()
    elif muvelet == '+':
        print()
        adat_bevitel_leiras = input('Kérem adja meg a költség leírását (pl. telefon, repjegy)📊: ').strip()
        print()
        adat_bevital_kategoria = input('Kérem adja meg a költség kategóriáját (meglévő kategóriák: kategoria)🏷️: ').strip().lower()
        print()
        while True:
            if adat_bevital_kategoria in kategoriak:
                print('A kategória sikeresen ki választva✅! (már létezik)')
                print()
                break
            else:
                print('A kategóra sikeresen létrehozva✅!')
                print()
                kategoriak.append(adat_bevital_kategoria)
                with open ('kategoriak.txt','a',encoding='utf-8') as file_add:
                    print(f'{adat_bevital_kategoria}',end='\n',file=file_add)
                break

                ## nincs kész

        adat_bevitel_datum = input('Kérem adja meg a dátumot (minta: 2025-05-14) (Mai dátum: ENTER)📆: ').strip()

        if adat_bevitel_datum == '':
            now = datetime.now()
            adat_bevitel_datum = now.strftime('%Y-%m-%d')
            print('\nA mai dátum sikeresen el lett mentve!✅\n')

        while True:
            try:
                adat_bevitel_ar = int(input(f'Kérem adja meg a(z) árat {valuta} ban/ben💰: '))
                break
            except ValueError:
                print()
                print(f'Hibás formátum! kérem egész számot adjon meg!💥')
                print()
                adat_bevitel_ar = int(input(f'Kérem adja meg a(z) árat {valuta} ban/ben💰: '))
        print()   
        uj_koltseg = {
            'költség_neve': adat_bevitel_leiras,
            'költség_dátuma': adat_bevitel_datum,
            'költség_ára': adat_bevitel_ar,
            'költség_kategoria': adat_bevital_kategoria
        }           
        koltsegek.append(uj_koltseg)
        uj_koltseg = {}
        with open('data.txt','a',encoding='utf-8') as file_add:
            print(f'{adat_bevitel_leiras};{adat_bevitel_datum};{adat_bevitel_ar};{adat_bevital_kategoria}', file=file_add)

    elif muvelet == 'eszközök':
        print()
        print('Eddigi költségek kiírása: (költségek)💵')
        print()
        print(f'Meglévő költség keresése: (keres)🔎')
        print()
        print('Eddigi legdrágább vásárlás kiírása: (legdrágább💎')
        print()
        print('Egy adott napra való keresés: (kereső)🔎')
        print()
        print('Az átlag költség kiszámítása: (átlag)📐')
        print()
        print('Az havi költség keresése: (hónap)🎯')
        print()
        eszkoz = input('Kérem válasszon műveletet (kilépés: exit)📱: ').strip().lower()
        print()
        while eszkoz not in ['költségek','','legdrágább','kereső','átlag','hónap','keres']:
            print(f'')
            print(f'Nem megfelelő művelet!')
            print(f'')
            eszkoz = input('Kérem válasszon műveletet (kilépés: exit)💥: ').strip().lower()
            print(f'')
        if eszkoz == '':
            print(f'Sikeres kilépés✅!')
            print()
            break
        elif eszkoz == 'keres':
            keresett_vasarlas = input('Kérem adja meg a vásrás nevét🛒: ').lower().strip()
            for elem in koltsegek:
                if elem['költség_neve'] == keresett_vasarlas:
                    print(f'A költség leírása: {elem['költség_neve']} dátum: {elem['költség_dátuma']} {elem['költség_ára']}')
                    print()
        elif eszkoz == 'átlag':
            print()
            osz_koltseg = 0
            db = 0
            for elem in koltsegek:
                osz_koltseg += elem['költség_ára']
                db += 1
            print(f'Az átlag költsége: {round((osz_koltseg / db),2)} 💸')
            print()
        elif eszkoz == 'hónap':
            print()
            keresett_honap = input('Kérem adja meg a keresett hónapot (pl: 05): ').lower().strip()
            ossz_koltes = 0
            for elem in koltsegek:
                honap = elem['költség_dátuma'].split('-')
                if honap[1] == keresett_honap:
                    ossz_koltes += elem['költség_ára']
                    print()
                    print(f'A költség leírása: {elem['költség_neve']} dátum: {elem['költség_dátuma']} {elem['költség_ára']}')
            print('- '*15)
            print(f'Összesen: {ossz_koltes}{valuta}.')
            print()
        elif eszkoz == 'kereső':
            now = datetime.now()
            adat_bevitel_datum = now.strftime('%Y-%m-%d')
            datum_kereso = input(f'Kérem a keresett dátumot (minta: {adat_bevitel_datum}): ')
            for elem in koltsegek:
                if elem['költség_dátuma'] == datum_kereso:
                    print()
                    print(f'Erre költött ezen a napon: {datum_kereso} | {elem['költség_neve']} {elem['költség_ára']}{valuta}.')
                    print()
        elif eszkoz == 'exit':
            print()
            print(f"Sikeres kilépés!✅")
            print()
            break
        elif eszkoz == 'legdrágább':
            print()
            ledragabb_dolog = -100
            ledragabb_dict = {}
            for elem in koltsegek:
                if elem['költség_ára'] > ledragabb_dolog:
                    ledragabb_dolog = elem['költség_ára']
                    ledragabb_dict = elem
            print(f'Legdrágább költekezés: {ledragabb_dict['költség_neve']} - {ledragabb_dict['költség_ára']}{valuta}.')
            print()
        else:
            eddigi_koltesegek = 0
            for elem in koltsegek:
                eddigi_koltesegek += elem['költség_ára']
            print(f'Eddig költött pénz: {eddigi_koltesegek}{valuta}. 💳')
            print()
    else:
        for koltseg in koltsegek:
            print(f'A költség leírása: {koltseg['költség_neve']} dátum: {koltseg['költség_dátuma']} {koltseg['költség_ára']}')
            print()
        torles = input('Kérem adja meg melyeik elemet szertné törlni (A költség leírásnevét adja meg): ').lower()
        print()
        while True:
            with open('data.txt','w',encoding='utf-8') as file_remove:
                for elem in koltsegek:
                    if elem['költség_neve'] != torles:
                        print(f'{elem['költség_neve']};{elem['költség_dátuma']};{elem['költség_ára']}',file=file_remove)
                    else:
                        print(f'{elem['költség_neve']} {elem['költség_dátuma']} {elem['költség_ára']}')
                        y_or_n = input('Ezt az elemet szertné törlni? (igen / nem) 🗳️: ').lower().strip()
                        while y_or_n not in ['igen','nem']:
                            print()
                            print(f'nem megfelelő formátum!❌')
                            print()
                            y_or_n = input('Ezt az elemet szertné törlni? (igen / nem) 🗳️: ').lower().strip()
                            print()
                        if y_or_n == 'igen':
                            continue
                        else:
                            print(f'{elem['költség_neve']};{elem['költség_dátuma']};{elem['költség_ára']}',file=file_remove)
                break
print()
print(F'köszönjük hogy minket választott! 👑')