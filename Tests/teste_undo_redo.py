from Logic.crud import adaugare
from Logic.undo_redo import do_redo, do_undo
def test_undo_redo():
    rezervari=[]
    undo_lst=[]
    redo_lst=[]
    rezervari = adaugare(rezervari, 1, 'r1', 'economy', 200, 'Da', undo_lst, redo_lst)
    rezervari = adaugare(rezervari, 2, 'r2', 'economy', 350, 'Nu', undo_lst, redo_lst)
    rezervari = adaugare(rezervari, 3, 'r3', 'economy_plus', 500, 'Da', undo_lst, redo_lst)
    rezervari=do_undo(undo_lst,redo_lst,rezervari)
    assert len(rezervari)==2
    rezervari=do_undo(undo_lst,redo_lst,rezervari)
    assert len(rezervari)==1
    rezervari = do_undo(undo_lst, redo_lst, rezervari)
    assert len(rezervari) == 0
    assert do_undo(undo_lst, redo_lst, rezervari) is None
    assert len(rezervari) == 0
    rezervari = adaugare(rezervari, 1, 'r1', 'economy', 200, 'Da', undo_lst, redo_lst)
    rezervari = adaugare(rezervari, 2, 'r2', 'economy', 350, 'Nu', undo_lst, redo_lst)
    rezervari = adaugare(rezervari, 3, 'r3', 'economy_plus', 500, 'Da', undo_lst, redo_lst)
    assert do_redo(undo_lst, redo_lst, rezervari) is None
    assert len(rezervari)==3
    rezervari = do_undo(undo_lst, redo_lst, rezervari)
    rezervari = do_undo(undo_lst, redo_lst, rezervari)
    assert len(rezervari) == 1
    rezervari = do_redo(undo_lst, redo_lst, rezervari)
    assert len(rezervari) == 2
    rezervari = do_redo(undo_lst, redo_lst, rezervari)
    assert len(rezervari) == 3
    rezervari = do_undo(undo_lst, redo_lst, rezervari)
    rezervari = do_undo(undo_lst, redo_lst, rezervari)
    assert len(rezervari) == 1
    rezervari = adaugare(rezervari, 4, 'r4', 'business', 1000, 'Nu', undo_lst, redo_lst)
    assert do_redo(undo_lst, redo_lst, rezervari) is None
    assert len(rezervari)==2
    rezervari = do_undo(undo_lst, redo_lst, rezervari)
    assert len(rezervari)==1
    rezervari = do_undo(undo_lst, redo_lst, rezervari)
    assert len(rezervari)==0
    rezervari = do_redo(undo_lst, redo_lst, rezervari)
    rezervari = do_redo(undo_lst, redo_lst, rezervari)
    assert len(rezervari)==2
    assert do_redo(undo_lst, redo_lst, rezervari) is None
    assert len(rezervari) == 2



