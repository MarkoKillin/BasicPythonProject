from matplotlib import pyplot as plt
from matplotlib import image as mpimg

def meniradnik():
    unos=input('Odaberite komandu("pomoc" za listu komandi): ')

    while unos!='zatvori':
        if unos=='pomoc':
            pomoc()
        elif unos=='sviproizvodi':
            sviproizvodi()
        elif unos=='prikazikupce':
            prikazikupce()
        elif unos=='promenicenu':
            promenicenu()
        elif unos=='dodajproizvod':
            dodajproizvod()
        elif unos=='promenistanje':
            promenistanje()
        elif unos=='prikazigraf':
            prikazigraf()
        elif unos=='slikaproizvoda':
            slikaproizvoda()
        elif unos=='':
            pass
        else:
            print('Uneta komanda ne postoji')
        unos=input('Odaberite komandu("pomoc" za listu komandi): ')

def pomoc():
    print(' sviproizvodi    - Ispisuje listu svih proizvoda u prodavnici')
    print(' slikaproizvoda  - Prikazuje sliku zeljenog proizvoda')
    print(' prikazikupce    - Ispisuje listu registrovanih kupaca')
    print(' promenicenu     - Menja cenu proizvoda')
    print(' dodajproizvod   - Dodaje proizvod u izbor')
    print(' promenistanje   - Promeni stanje nekog proizvoda u magacinu')
    print(' prikazigraf     - Prikazuje graf prodaje')
    print(' pomoc           - Izbacuje listu dozvoljenih komandi')
    print(' zatvori         - Zavrsava kupovinu\n')

def sviproizvodi():
    with open('podaci\Roba.txt') as roba:
        proizvodi=roba.readlines()
        print(f'{"id":2}|{"Proizvod":10}|{"Model":18}|{"Broj zica":9}|{"Broj pragova":12}|{"Cena":8}|{"Kolicina":8}|')
        
        for red in proizvodi:
            proizvod=red.strip().split('|')
            print(f'{proizvod[0]:2}|{proizvod[1]:10}|{proizvod[2]:18}|{proizvod[3]:9}|{proizvod[4]:12}|{proizvod[5]:8}|{proizvod[6]:8}|')
        
    print(' ')

def prikazikupce():
    with open('podaci\Korisnici.txt') as nalozi:
        kupci=nalozi.readlines()
        print(f'{"Ime":12}|{"Prezime":15}|{"Broj telefona":14}|')

        for red in kupci:
            kupac=red.strip().split('|')
            if kupac[1]=='1':
                print(f'{kupac[2]:12}|{kupac[3]:15}|{kupac[4]:14}|')
            else:
                pass

    print(' ')

def promenicenu():
    print('Lista proizvoda: ')
    sviproizvodi()
    idpredmeta=input('Unesite id proizvoda ciju cenu zelite da promenite: ')
    novacena=input('Unesite novu cenu proizvoda: ')
    postoji=False
    noviproizvodi=[]

    with open('podaci\Roba.txt') as roba:
        proizvodi=roba.readlines()

        for red in proizvodi:
            proizvod=red.strip().split('|')
            if int(idpredmeta)==int(proizvod[0]):
                postoji=True
                proizvod[5]=novacena
            noviproizvod=proizvod[0]+'|'+proizvod[1]+'|'+proizvod[2]+'|'+proizvod[3]+'|'+proizvod[4]+'|'+proizvod[5]+'|'+proizvod[6]+'|'+proizvod[7]+'\n'
            noviproizvodi.append(noviproizvod)

    if postoji==True:
        with open('podaci\Roba.txt', 'w') as roba:
            for red in noviproizvodi:
                roba.write(red)

        print('Uspesno ste promenili cenu.\n')
    else:
        print('Proizvod ne postoji.\n')

def dodajproizvod():
    brend=input('Unesite brend proizvoda: ')
    model=input('Unesite model proizvoda: ')
    brzica=input('Unesite broj zica proizvoda: ')
    brpragova=input('Unesite broj pragova proizvoda: ')
    cena=input('Unesite cenu proizvoda: ')
    kolicina=input('Unesite kolicinu proizvoda u magacinu: ')
    putanja=input('Unesite putanju do slike proizvoda: ')
    id=int(0)
    postoji=False

    with open('podaci\Roba.txt') as roba:
        proizvodi=roba.readlines()
        
        for red in proizvodi:
            id=id+1
            proizvod=red.strip().split('|')
            if brend==proizvod[1] and model==proizvod[2]:
                postoji=True
                print('Proizvod vec postoji.')
                return
    
    if postoji==False:
        with open('podaci\Roba.txt','a') as roba:
            id=id+1
            noviproizvod=str(id)+'|'+brend+'|'+model+'|'+brzica+'|'+brpragova+'|'+cena+'|'+kolicina+'|'+putanja+'\n'
            roba.write(noviproizvod)
            print('Uspesno ste dodali nov proizvod. \n')
            
def promenistanje():
    print('Lista proizvoda: ')
    sviproizvodi()
    idpredmeta=input('Unesite id proizvoda cije stanje zelite da promenite: ')
    novostanje=input('Unesite novo stanje proizvoda: ')
    postoji=False
    noviproizvodi=[]

    with open('podaci\Roba.txt') as roba:
        proizvodi=roba.readlines()

        for red in proizvodi:
            proizvod=red.strip().split('|')
            if int(idpredmeta)==int(proizvod[0]):
                postoji=True
                proizvod[6]=novostanje
            noviproizvod=proizvod[0]+'|'+proizvod[1]+'|'+proizvod[2]+'|'+proizvod[3]+'|'+proizvod[4]+'|'+proizvod[5]+'|'+proizvod[6]+'|'+proizvod[7]+'\n'
            noviproizvodi.append(noviproizvod)

    if postoji==True:
        with open('podaci\Roba.txt', 'w') as roba:
            for red in noviproizvodi:
                roba.write(red)

        print('Uspesno ste promenili stanje.\n')
    else:
        print('Proizvod ne postoji.\n')

def prikazigraf():
    labels=[]
    sizes=[]
    with open('podaci\Statistika.txt') as roba:
        proizvodi=roba.readlines()

        for red in proizvodi:
            proizvod=red.strip().split('|')
            if proizvod[3]!='0':
                labels.append(proizvod[1]+' '+proizvod[2])
                sizes.append(proizvod[3])
        
        fig1, ax1 = plt.subplots()
        ax1.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True)
        ax1.axis('equal')
        plt.show()

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