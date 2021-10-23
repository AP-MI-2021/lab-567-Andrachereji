from Logic.crud import adaugare,read,modificare,stergere
from Domain.avioane import get_str,get_id,get_nume,get_pret,get_checkin,get_clasa,creeaza_rezervare
def show_menu():
    print('1.CRUD')
    print('2.Trecerea tuturor rezervarilor facute pe un nume citit la o clasa superioara')
    print('X.Exit')
def handle_adaugare(rezervari):
    id=int(input('Dati id-ul rezervarii'))
    nume =input('Dati numele rezervarii')
    clasa =input('Dati clasa la care se face rezervarea')
    pret = float(input('Dati pretul rezervarii'))
    checkin =input('Precizati cu Da/Nu starea checkin-ului la aceasta rezervare')
    return adaugare(rezervari, id, nume, clasa, pret, checkin)
def handle_show_all(rezervari):
    for rezervare in rezervari:
        print(get_str(rezervare))
def handle_show_details(rezervari):
    id_rezervare=int(input('Dati id-ul rezervarii pentru care doriti detalii'))
    rezervare=read(rezervari,id_rezervare)
    print(f'nume:{get_nume(rezervare)}')
    print(f'clasa:{get_clasa(rezervare)}')
    print(f'pret:{get_pret(rezervare)}')
    print(f'checkin:{get_checkin(rezervare)}')
def handle_modificare(rezervari):
    id = int(input('Dati id-ul rezervarii care se actualizeaza'))
    nume = input('Dati noul nume')
    clasa = input('Dati noua clasa la care se face rezervarea')
    pret = float(input('Dati noul pret'))
    checkin = input('Precizati cu Da/Nu starea checkin-ului la aceasta noua rezervare')
    return modificare(rezervari, creeaza_rezervare(id,nume,clasa,pret,checkin))
def handle_stergere(rezervari):
    id = int(input('Dati id-ul rezervarii care se va sterge'))
    return stergere(rezervari,id)

def handle_crud(rezervari):
    while True:
        print('1.Adaugare')
        print('2.Modificare')
        print('3.Stergere')
        print('a.Afisare')
        print('d.Detalii rezervare')
        print('b.Revenire')
        optiune=input('Optiunea aleasa:')
        if optiune=='1':
            rezervari=handle_adaugare(rezervari)
        elif optiune=='2':
            rezervari=handle_modificare(rezervari)
        elif optiune=='3':
            rezervari=handle_stergere(rezervari)
        elif optiune=='a':
            handle_show_all(rezervari)
        elif optiune=='d':
            handle_show_details(rezervari)
        elif optiune=='b':
            break
        else:
            print('Optiune invalida')
    return rezervari
def run_UI(rezervari):
    while True:
        show_menu()
        optiune=input('Optiunea aleasa:')
        if optiune=='1':
            rezervari=handle_crud(rezervari)
        elif optiune=='x':
            break
        else:
            print('Optiune invalida')
    return rezervari
