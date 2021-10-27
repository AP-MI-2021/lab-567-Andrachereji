from Domain.rezervare import creeaza_rezervare,get_id
from Logic.crud import adaugare,modificare,read,stergere

def get_data():
    return [
        creeaza_rezervare(1, 'r1', 'economy', 200, 'Da'),
        creeaza_rezervare(2, 'r2', 'business', 1200, 'Da'),
        creeaza_rezervare(3, 'r3', 'economy', 500, 'Nu'),
        creeaza_rezervare(4, 'r4', 'economy_plus', 800, 'Da'),
        creeaza_rezervare(5, 'r5', 'business', 1400, 'Nu'),
    ]
def test_adaugare():
    rezervari=get_data()
    params=(100, 'rnew', 'economy', 300, 'Da')
    r_new=creeaza_rezervare(*params)
    new_rezervari=adaugare(rezervari, *params)
    assert len(new_rezervari)==len(rezervari)+1
    assert r_new in new_rezervari
def test_read():
    rezervari = get_data()
    some_r=rezervari[2]
    assert read(rezervari,get_id(some_r))==some_r
    assert read(rezervari,None)==rezervari
def test_modificare():
    rezervari = get_data()
    r_update=creeaza_rezervare(1,'r1','economy_plus',600,'Nu')
    updated=modificare(rezervari, r_update)
    assert r_update in updated
    assert r_update not in rezervari
    assert len(updated)==len(rezervari)
def test_stergere():
    rezervari = get_data()
    to_delete=3
    r_deleted=read(rezervari, to_delete)
    deleted=stergere(rezervari, to_delete)
    assert r_deleted not in deleted
    assert r_deleted in rezervari
    assert len(deleted)==len(rezervari)-1

