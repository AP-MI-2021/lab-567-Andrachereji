from Tests.test_crud import get_data
from Logic.ieftinire_rezervari import get_ieftinire_rezervari
from Logic.crud import read
from Domain.rezervare import get_pret
def test_ieftinire():
    rezervari = get_data()
    modificare_rezervari=get_ieftinire_rezervari(rezervari,10,[],[])
    rezervare_veche=read(rezervari,1)
    rezervare_noua=read(modificare_rezervari,1)
    assert get_pret(rezervare_veche)>get_pret(rezervare_noua)
    try:
        _=get_ieftinire_rezervari(rezervari,10000,[],[])
        assert False
    except ValueError:
        assert True

