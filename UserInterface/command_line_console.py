from Logic.crud import adaugare,stergere
from Domain.rezervare import get_str
def show_menu():
    print('pentru adaugarea unuei noi rezervari scrieti add si dati datele necesare separate prin virgula')
    print('pentru stergerea unuei rezervari scrieti delete si dati id-ul rezervari pe care doriti sa o stergeti')
    print('pentru afisarea tuturor datelor scrieti showall')
    print('comenzile sunt separate prin ";"')
    print('tastati x pentru iesire')

def handle_comand_line(rezervari):
    while True:
        show_menu()
        optiune=input('Dati sirul de comenzi dorite:')
        if optiune=='x':
            break
        else:
            comenzi=optiune.split(';')
            for elemente in comenzi:
                date = elemente.split(',')
                if date[0] == 'add':
                    try:
                        obiecte =adaugare(rezervari, int(date[1]), date[2], date[3], float(date[4]), date[5])
                    except ValueError as ve:
                        print("Eroare", ve)
                elif date[0] == 'delete':
                    try:
                        obiecte = stergere(rezervari, int(date[1]))
                    except ValueError as ve:
                        print("Eroare", ve)
                elif date[0]=='showall':
                    try:
                        obiecte=get_str(rezervari)
                    except ValueError as ve:
                        print("Eroare", ve)



