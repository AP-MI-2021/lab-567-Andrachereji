from Domain.avioane import creeaza_rezervare, get_id

def adaugare(lst_rezervari, id_rezervare, nume, clasa, pret, checkin):
    '''
    Adauga o noua rezervare la lista
    :param lst_rezervari:lista de rezervari
    :param id_rezervare:id-ul rezervarii
    :param nume:numele rezervarii
    :param clasa:clasa rezervasrii(economy/economy plus/buisness)
    :param pret:pretul rezervarii
    :param checkin:verificare checkin(Da/Nu)
    :return:lista de rezervari dupa adaugarea noi rezervari
    '''
    rezervare=creeaza_rezervare(id_rezervare, nume, clasa, pret, checkin)
    return lst_rezervari + [rezervare]
def read(lst_rezervari, id_rezervare=None):
    '''
    Citeste o rezervare din "baza de date"
    :param lst_rezervari:lista de rezervari
    :param id_rezervare:id-ul rezervarii dorite
    :return:rezervarea cu id-ul id_rezervare sau toata lista de rezervari daca id_rezervare=None
    '''
    rezervare_cu_id=None
    for rezervare in lst_rezervari:
        if get_id(rezervare)==id_rezervare:
            rezervare_cu_id=rezervare
    if rezervare_cu_id:
        return rezervare_cu_id
    else:
        return lst_rezervari
def modificare(lst_rezervari, new_rezervare):
    '''
    Modifica o rezervare
    :param lst_rezervari:lista de rezervari
    :param rezervare:rezervarea care se va modifica, id-ul trebiue sa fie unul existent!
    :return:o lista cu rezervarea modificata
    '''
    new_rezervari=[]
    for rezervare in lst_rezervari:
        if get_id(rezervare)!=get_id(new_rezervare):
            new_rezervari.append(rezervare)
        else:
            new_rezervari.append(new_rezervare)
    return new_rezervari

def stergere(lst_rezervari, id_rezervare):
    '''
    Sterge din lista de rezervari o rezervare cu un id dat
    :param lst_rezervari: lista de rezervari
    :param id_rezervare: id-ul rezervarii pe care dorim sa o stergem
    :return: o lista fara rezervarea cu id-ul id_rezervare
    '''
    new_rezervari=[]
    for rezervare in lst_rezervari:
        if get_id(rezervare)!=id_rezervare:
            new_rezervari.append(rezervare)
    return new_rezervari

