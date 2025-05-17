from datetime import datetime
koltsegek = []
koltseg = {}

with open('data.txt','r',encoding='utf-8') as file_rd:
    for sor in file_rd:
        data = sor.strip().split(';')
        koltseg['költség_neve'] = data[0]
        koltseg['költség_dátuma'] = data[1]
        koltseg['költség_ára'] = int(data[2])
        koltsegek.append(koltseg)
        koltseg = {}
    
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
                print(f'A költség leírása: {koltseg['költség_neve']} dátum: {koltseg['költség_dátuma']} {koltseg['költség_ára']}')
                print()
    elif muvelet == '+':
        print()
        adat_bevitel_leiras = input('Kérem adja meg a költség leírását (pl. telefon, repjegy): ').strip()
        print()
        adat_bevitel_datum = input('Kérem adja meg a dátumot (minta: 2025-05-14) (Mai dátum: ENTER): ').strip()

        if adat_bevitel_datum == '':
            now = datetime.now()
            adat_bevitel_datum = now.strftime('%Y-%m-%d')
            print('\nA mai dátum sikeresen el lett mentve!\n')

        adat_bevitel_ar = int(input('Kérem adja meg a(z) árat forintban: '))     

        with open('data.txt','a',encoding='utf-8') as file_add:
            print(f'{adat_bevitel_leiras};{adat_bevitel_datum};{adat_bevitel_ar}', file=file_add)

    elif muvelet == 'eszközök':
        print()
        print('Eddigi költségek kiírása: költségek')
        print()
        eszkoz = input('Kérem válasszon műveletet (kilépés: exit): ').strip().lower()
        while eszkoz not in ['költségek','']:
            print(f'')
            print(f'Nem megfelelő művelet!')
            print(f'')
            eszkoz = input('Kérem válasszon műveletet (kilépés: exit): ').strip().lower()
            print(f'')
        if eszkoz == '':
            print(f'Sikeres kilépés!')
            print()
            break
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
                        continue
                break