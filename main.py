from Tests.test_crud import test_adaugare, test_read, test_modificare,test_stergere
from Tests.test_trecere_clasa_superioara import test_modificare_clasa
from Tests.test_ieftinire_rezervari import test_ieftinire
from Tests.test_pret_maxim_clase import test_pret_max_clase
from UserInterface.console import run_UI
from Logic.crud import adaugare
def main():
    rezervari = []
    rezervari = adaugare(rezervari, 1, 'r1', 'economy', 200, 'Da')
    rezervari = adaugare(rezervari, 2, 'r2', 'economy', 350, 'Nu')
    rezervari = adaugare(rezervari, 3, 'r3', 'economy_plus', 500, 'Da')
    rezervari = adaugare(rezervari, 4, 'r4', 'business', 1000, 'Nu')
    rezervari = adaugare(rezervari, 5, 'r5', 'economy', 260, 'Da')
    rezervari=run_UI(rezervari)
if __name__ == '__main__':
    test_adaugare()
    test_read()
    test_modificare()
    test_stergere()
    test_modificare_clasa()
    test_ieftinire()
    test_pret_max_clase()
    main()