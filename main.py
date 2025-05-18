from datetime import datetime
koltsegek = []
koltseg = {}

kategoriak = ['utazás','élelmiszer','hobbi']  

with open('data.txt','r',encoding='utf-8') as file_rd:
    for sor in file_rd:
        data = sor.strip().split(';')
        koltseg['költség_neve'] = data[0]
        koltseg['költség_dátuma'] = data[1]
        koltseg['költség_ára'] = int(data[2])
        koltseg['költség_kategoria'] = data[3]
        koltsegek.append(koltseg)
        koltseg = {}

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
print(f'Üdvözöljük A költség vezető alkalmazásunkban, lehetőségek kiírása: (eszközök) (készítette: Szabó Tamás ©)')
print()

if len(koltsegek) == 0:
    print(f'Jelenleg nincsenek költségei!')
    print()
while True:
    muvelet = input('Kérem válasszon! (Új költség felvétele +) (Meglévő költség kivonása -) (Meglévő költségek kiírása ENTER) (eszközök) (kilépés: exit): ').strip()
    while muvelet not in ['+','-','','eszközök','exit']:
        print(f'')
        print(f'Nem megfelelő művelet!')
        print(f'')
        muvelet = input('Kérem válasszon! (Új költség felvétele +) (Meglévő költség kivonása -) (Meglévő költségek kiírása ENTER) (kilépés: exit): ').strip()
    if muvelet == 'exit':
        print()
        print('Sikeres kilépés!')
        break
    elif muvelet == '':
        if len(koltsegek) == 0:
            print()
            print(f'Még nem lett költség felvéve!')
            print()
        else:
            for koltseg in koltsegek:
                print()
                print(f'A költség leírása: {koltseg['költség_neve']} | dátum: {koltseg['költség_dátuma']} | Ár: {koltseg['költség_ára']} | kategória: {koltseg['költség_kategoria']}')
                print()
    elif muvelet == '+':
        print()
        adat_bevitel_leiras = input('Kérem adja meg a költség leírását (pl. telefon, repjegy): ').strip()
        print()
        while True:
            adat_bevital_kategoria = input('Kérem adja meg a költség kategóriáját (meglévő kategóriák: kategoria): ').strip().lower()
            
            if adat_bevital_kategoria == 'kategoria':
                print('\nElérhető kategóriák:')
                for kategoria in kategoriak:
                    print(f'{kategoria}')
                print()
                continue 
            
            while adat_bevital_kategoria in kategoriak:
                print('A kategória már létezik')
                adat_bevital_kategoria = input('Kérem adja meg a költség kategóriáját (meglévő kategóriák: kategoria): ').strip().lower()
                break
            else:
                print(f'Új kategória létrehozva: {adat_bevital_kategoria}')
                kategoriak.append(adat_bevital_kategoria)
                break

                ## nincs kész

        adat_bevitel_datum = input('Kérem adja meg a dátumot (minta: 2025-05-14) (Mai dátum: ENTER): ').strip()

        if adat_bevitel_datum == '':
            now = datetime.now()
            adat_bevitel_datum = now.strftime('%Y-%m-%d')
            print('\nA mai dátum sikeresen el lett mentve!\n')

        adat_bevitel_ar = int(input('Kérem adja meg a(z) árat forintban: '))   
        uj_koltseg = {
            'költség_neve': adat_bevitel_leiras,
            'költség_dátuma': adat_bevitel_datum,
            'költség_ára': adat_bevitel_ar,
            'költség_kategoria': adat_bevitel_ar
        }           
        koltsegek.append(uj_koltseg)
        uj_koltseg = {}
        with open('data.txt','a',encoding='utf-8') as file_add:
            print(f'{adat_bevitel_leiras};{adat_bevitel_datum};{adat_bevitel_ar}', file=file_add)

    elif muvelet == 'eszközök':
        print()
        print('Eddigi költségek kiírása: költségek')
        print()
        print(f'Meglévő költség keresése: keres')
        print()
        print('Eddigi legdrágább vásárlás kiírása: legdrágább')
        print()
        print('Egy adott napra való keresés: kereső')
        print()
        print()
        print('Az átlag költség kiszámítása: átlag')
        print()
        print()
        print('Az havi költség keresése: hónap')
        print()
        eszkoz = input('Kérem válasszon műveletet (kilépés: exit): ').strip().lower()
        print()
        while eszkoz not in ['költségek','','legdrágább','kereső','átlag','hónap','keres']:
            print(f'')
            print(f'Nem megfelelő művelet!')
            print(f'')
            eszkoz = input('Kérem válasszon műveletet (kilépés: exit): ').strip().lower()
            print(f'')
        if eszkoz == '':
            print(f'Sikeres kilépés!')
            print()
            break
        elif eszkoz == 'keres':
            keresett_vasarlas = input('Kérem adja meg a vásrás nevét: ').lower().strip()
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
            print(f'Az átlag költsége: {round((osz_koltseg / db),2)}')
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
            print(f'Összesen: {ossz_koltes}Ft.')
            print()
        elif eszkoz == 'kereső':
            now = datetime.now()
            adat_bevitel_datum = now.strftime('%Y-%m-%d')
            datum_kereso = input(f'Kérem a keresett dátumot (minta: {adat_bevitel_datum}): ')
            for elem in koltsegek:
                if elem['költség_dátuma'] == datum_kereso:
                    print()
                    print(f'Erre költött ezen a napon: {datum_kereso} | {elem['költség_neve']} {elem['költség_ára']}Ft.')
                    print()
        elif eszkoz == 'legdrágább':
            print()
            ledragabb_dolog = -100
            ledragabb_dict = {}
            for elem in koltsegek:
                if elem['költség_ára'] > ledragabb_dolog:
                    ledragabb_dolog = elem['költség_ára']
                    ledragabb_dict = elem
            print(f'Legdrágább költekezés: {ledragabb_dict['költség_neve']} - {ledragabb_dict['költség_ára']}Ft.')
            print()
        else:
            eddigi_koltesegek = 0
            for elem in koltsegek:
                eddigi_koltesegek += elem['költség_ára']
            print(f'Eddig költött pénz: {eddigi_koltesegek}Ft.')
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
                        print(f'{elem['költség_neve']};{elem['költség_dátuma']};{elem['költség_ára']}')
                        y_or_n = input('Ezt az elemet szertné törlni? (igen / nem): ').lower().strip()
                        while y_or_n not in ['igen','nem']:
                            print()
                            print(f'nem megfelelő formátum!')
                            print()
                            y_or_n = input('Ezt az elemet szertné törlni? (igen / nem): ').lower().strip()
                            print()
                        if y_or_n == 'igen':
                            continue
                        else:
                            print(f'{elem['költség_neve']};{elem['költség_dátuma']};{elem['költség_ára']}',file=file_remove)
                break