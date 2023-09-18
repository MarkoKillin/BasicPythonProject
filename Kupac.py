from matplotlib import pyplot as plt
from matplotlib import image as mpimg

korpa=[]

def menikupac():
    unos=input('Odaberite komandu("pomoc" za listu komandi): ')

    while unos!='zatvori':
        if unos=='pomoc':
            pomoc()
        elif unos=='sviproizvodi':
            sviproizvodi()
        elif unos=='pretrazi':
            unos1=input('Pretraga po brendu, broju zica, broju pragova ili ceni? ')
            if unos1=='brendu':
                pretrazibrend()
            elif unos1=='broju zica':
                pretrazibrojzica()
            elif unos1=='broju pragova':
                pretrazibrojpragova()
            elif unos1=='ceni':
                pretrazicena()
            else:
                print('Uneli ste pogresnu opciju, vracamo vas na odabir komandi. ')
                pass
        elif unos=='slikaproizvoda':
            slikaproizvoda()
        elif unos=='korpasadrzaj':
            korpasadrzaj()
        elif unos=='korpadodaj':
            korpadodaj()
        elif unos=='korpaobrisi':
            korpaobrisi()
        elif unos=='kupi':
            kupi()
        elif unos=='':
            pass
        else:
            print('Uneta komanda ne postoji')
        unos=input('Odaberite komandu("pomoc" za listu komandi): ')

def pomoc():
    print(' sviproizvodi    - Ispisuje listu svih proizvoda u prodavnici')
    print(' slikaproizvoda  - Prikazuje sliku zeljenog proizvoda')
    print(' pretrazi        - Omogucava vise razlicitih nacina pretrage')
    print(' korpasadrzaj    - Prikazuje koje proizvode imate u korpi')
    print(' korpadodaj      - Dodaje proizvod u korpu')
    print(' korpaobrisi     - Brise proizvod iz korpe')
    print(' kupi            - Izvrsava kupovinu i stampa racun')
    print(' pomoc           - Izbacuje listu dozvoljenih komandi')
    print(' zatvori         - Zatvara program\n')

def sviproizvodi():
    with open('podaci\Roba.txt') as roba:
        proizvodi=roba.readlines()
        print(f'{"id":2}|{"Proizvod":10}|{"Model":18}|{"Broj zica":9}|{"Broj pragova":12}|{"Cena":8}|')
        
        for red in proizvodi:
            proizvod=red.strip().split('|')
            print(f'{proizvod[0]:2}|{proizvod[1]:10}|{proizvod[2]:18}|{proizvod[3]:9}|{proizvod[4]:12}|{proizvod[5]:8}|')
        
        print(' ')

def korpasadrzaj():
    if len(korpa)==0:
        print('Korpa je prazna.')
    else:
        print(f'{"id":2}|{"Kolicina":8}|{"Proizvod":10}|{"Model":18}|{"Broj zica":9}|{"Broj pragova":12}|{"Cena":8}|')
        cena=0
        
        for i in korpa:
            print(f'{i[0]:2}|{i[8]:8}|{i[1]:10}|{i[2]:18}|{i[3]:9}|{i[4]:12}|{i[5]:8}|')
            cena=cena+int(i[5])*int(i[8])
        
        print('Ukupna cena je:', cena)
    
    print(' ')

def korpadodaj():
    print('Lista proizvoda: ')
    sviproizvodi()
    idpredmeta=input('Unesite id proizvoda koji zelite da dodate: ')
    kolicina=input('Unesite kolicinu proizvoda:')

    with open('podaci\Roba.txt') as roba:
        proizvodi=roba.readlines()
        
        for red in proizvodi:
            proizvod=red.strip().split('|')
            if int(idpredmeta)==int(proizvod[0]) and int(proizvod[6])>0:
                if int(proizvod[6])>=int(kolicina):
                    proizvod.append(kolicina)
                    korpa.append(proizvod)
                    print('Uspesno ste dodali ' + kolicina + ' x ' + proizvod[1] + ' ' + proizvod[2] + '.')
                else:
                    print('Nema dovoljno proizvoda na stanju.')
    
    print(' ')
                
def korpaobrisi():
    print('Koji proizvod zelite da obrisete?')
    korpasadrzaj()
    brisi=input('Unesite id proizvoda koji zelite da obrisete iz korpe:')
    
    for i in korpa:
        if(i[0]==brisi):
            korpa.remove(i)
            print('Proizvod je uspesno izbacen iz korpe.')
    
    print(' ')

def promenistanje(idx, kolicinax):
    postoji=False
    noviproizvodi=[]

    with open('podaci\Roba.txt') as roba:
        proizvodi=roba.readlines()

        for red in proizvodi:
            proizvod=red.strip().split('|')
            if int(idx)==int(proizvod[0]):
                postoji=True
                proizvod[6]=int(proizvod[6])-int(kolicinax)
                
            noviproizvod=proizvod[0]+'|'+proizvod[1]+'|'+proizvod[2]+'|'+proizvod[3]+'|'+proizvod[4]+'|'+proizvod[5]+'|'+str(proizvod[6])+'|'+proizvod[7]+'\n'
            noviproizvodi.append(noviproizvod)

    if postoji==True:
        with open('podaci\Roba.txt', 'w') as roba:
            for red in noviproizvodi:
                roba.write(red)

def belezistatistiku(idx, kolicinax):
    postoji=False
    noviproizvodi=[]

    with open('podaci\Statistika.txt') as roba:
        proizvodi=roba.readlines()

        for red in proizvodi:
            proizvod=red.strip().split('|')
            if int(idx)==int(proizvod[0]):
                postoji=True
                proizvod[3]=int(proizvod[3])+int(kolicinax)
                
            noviproizvod=proizvod[0]+'|'+proizvod[1]+'|'+proizvod[2]+'|'+str(proizvod[3])+'\n'
            noviproizvodi.append(noviproizvod)

    if postoji==True:
        with open('podaci\Statistika.txt', 'w') as roba:
            for red in noviproizvodi:
                roba.write(red)

def kupi():
    if len(korpa)!=0:
        cena=0
        
        with open('podaci\Racuni.txt', 'a') as racuni:
            racuni.write('--------------------------------------------------------------------------\n')
            
            for i in korpa:
                red1=f'{i[0]:2}|{i[8]:8}|{i[1]:10}|{i[2]:18}|{i[3]:9}|{i[4]:12}|{i[5]:8}|'
                racuni.write(red1)
                racuni.write('\n')
                cena=cena+int(i[5])*int(i[8])
            
            racuni.write('--------------------------------------------------------------------------\n')
            red2='Ukupna cena je:' + str(cena)
            racuni.write(red2)
            racuni.write('\n')
        
        for i in korpa:
            promenistanje(i[0], i[8])
            belezistatistiku(i[0], i[8])
        korpa.clear()
        print('Hvala na kupovini, racun je odstampan i korpa ispraznjena.')
    else:
        print('Korpa je prazna.')
    
    print(' ')

def pretrazibrend():
    brend=input('Unesite brend koji zelite da pretrazite: ')
    postoji=False

    with open('podaci\Roba.txt') as roba:
        proizvodi=roba.readlines()
        print(f'{"id":2}|{"Proizvod":10}|{"Model":18}|{"Broj zica":9}|{"Broj pragova":12}|{"Cena":8}|')
        
        for red in proizvodi:
            proizvod=red.strip().split('|')
            if brend.lower()==proizvod[1].lower():
                postoji=True
                print(f'{proizvod[0]:2}|{proizvod[1]:10}|{proizvod[2]:18}|{proizvod[3]:9}|{proizvod[4]:12}|{proizvod[5]:8}|')

    if postoji==False:
        print('Nemamo proizvode sa navedenim brendom.')
        
    print(' ')

def pretrazibrojzica():
    brzica=input('Unesite broj zica koji zelite: ')
    postoji=False

    with open('podaci\Roba.txt') as roba:
        proizvodi=roba.readlines()
        print(f'{"id":2}|{"Proizvod":10}|{"Model":18}|{"Broj zica":9}|{"Broj pragova":12}|{"Cena":8}|')
        
        for red in proizvodi:
            proizvod=red.strip().split('|')
            if int(brzica)==int(proizvod[3]):
                postoji=True
                print(f'{proizvod[0]:2}|{proizvod[1]:10}|{proizvod[2]:18}|{proizvod[3]:9}|{proizvod[4]:12}|{proizvod[5]:8}|')

    if postoji==False:
        print('Nemamo proizvode sa navedenim brojem zica.')
        
    print(' ')

def pretrazibrojpragova():
    brpragova=input('Unesite broj pragova koji zelite: ')
    postoji=False

    with open('podaci\Roba.txt') as roba:
        proizvodi=roba.readlines()
        print(f'{"id":2}|{"Proizvod":10}|{"Model":18}|{"Broj zica":9}|{"Broj pragova":12}|{"Cena":8}|')
        
        for red in proizvodi:
            proizvod=red.strip().split('|')
            if int(brpragova)==int(proizvod[4]):
                postoji=True
                print(f'{proizvod[0]:2}|{proizvod[1]:10}|{proizvod[2]:18}|{proizvod[3]:9}|{proizvod[4]:12}|{proizvod[5]:8}|')

    if postoji==False:
        print('Nemamo proizvode sa navedenim brojem pragova.')
        
    print(' ')

def pretrazicena():
    cena=input('Unesite maksimalnu cenu proizvoda: ')
    postoji=False

    with open('podaci\Roba.txt') as roba:
        proizvodi=roba.readlines()
        print(f'{"id":2}|{"Proizvod":10}|{"Model":18}|{"Broj zica":9}|{"Broj pragova":12}|{"Cena":8}|')
        
        for red in proizvodi:
            proizvod=red.strip().split('|')
            if int(cena)>=int(proizvod[5]):
                postoji=True
                print(f'{proizvod[0]:2}|{proizvod[1]:10}|{proizvod[2]:18}|{proizvod[3]:9}|{proizvod[4]:12}|{proizvod[5]:8}|')

    if postoji==False:
        print('Nemamo proizvode u tom cenovnom rangu.')
        
    print(' ')

def slikaproizvoda():
    print('Lista proizvoda: ')
    sviproizvodi()
    idx=input('Unesite id proizvoda ciju sliku zelite da vidite: ')
    postoji=False

    with open('podaci\Roba.txt') as roba:
        proizvodi=roba.readlines()

        for red in proizvodi:
            proizvod=red.strip().split('|')
            if idx==proizvod[0]:
                postoji=True
                brend=proizvod[1]
                model=proizvod[2]
                putanja=proizvod[7]

    if postoji==True:    
        plt.title(brend+' '+model)
        plt.xticks(color='w')
        plt.yticks(color='w')
        slika = mpimg.imread(putanja)
        plt.imshow(slika)
        plt.show()
    else:
        print('Proizvod ne postoji.')