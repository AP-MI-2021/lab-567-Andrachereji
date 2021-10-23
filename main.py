from Tests.test_crud import test_adaugare, test_read, test_modificare,test_stergere
from UserInterface.console import run_UI
from Logic.crud import adaugare
def main():
    rezervari=[]
    rezervari=adaugare(rezervari, 1, 'r1', 'economy', 200, 'Da')
    rezervari=run_UI(rezervari)
if __name__ == '__main__':
    test_adaugare()
    test_read()
    test_modificare()
    test_stergere()
    main()