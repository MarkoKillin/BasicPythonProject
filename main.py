from Radnik import meniradnik
from Kupac import menikupac

korisnici=[]

def main():

    unos=input('Da li zelite da se registraciju(moguce samo kao kupac) ili login?')
    if unos=='login':
        titula=-1
        imekorisnika=''

        while titula==-1:
            korisnickoime=input('Korisnicko ime: ')
            lozinka=input('Lozinka: ')
            
            with open('podaci\Korisnici.txt') as fajl:
                podaci=fajl.readlines()

                for red in podaci:
                    korisnik=red.strip().split('|')
                    korisnici.append(korisnik)

                for red in korisnici:
                    if korisnickoime==red[5] and lozinka==red[6]:
                        titula=red[1]
                        imekorisnika=red[2]

            if titula==-1:
                print('Uneli ste pogresno korisnicno ime ili lozinku.')
                print('Pokusajte ponovo:')
            else:
                print('Login uspesan! Dobro dosao/la ' + imekorisnika)

        if titula=='0':
            meniradnik()
        elif titula=='1':
            menikupac()
        else:
            print('Doslo je do greske. Nepoznata titula.')
    elif unos=='registracija':
        kime=input('Unesite korisnicko ime: ')
        loz=input('unesite loziku:')

if __name__=='__main__':
    main()