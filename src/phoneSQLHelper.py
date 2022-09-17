import sqlite3

def SELECT_PHONE_NUMBER(areaCodeIn):
    con=sqlite3.connect("testDB.sqlite3")

def SELECT_AREA_CODES_FROM_STATE(stateIN):
    fileNamePath="data/PNDB.sqlite3"
    sqlite3Connection=sqlite3.connect(fileNamePath)
    cur=sqlite3Connection.cursor()
    res=cur.execute("SELECT ")

def SELECT_STATE_FROM_ABBR(stateABBR):
    fileNamePath="data/PNDB.sqlite3"


def TEST_SELECT_STATE():
    con=sqlite3.connect("testDB.sqlite3")
    state=con.execute("SELECT STATE FROM US_STATES WHERE ID=111") #=None
    print(state)
    print(state.fetchone())
    print("SELECT STATE FROM US_STATES WHERE ID=1")
    try:
        print("STATE: {}".format(str(state.fetchone()[0])))
    except Exception as k:
        print(k)
    if(state.fetchone()==None):
        print("NO DATA")
    else:
        print(state)
    con.close()

class PhoneNumberDB:
    def __init__(this):
        None
    def SELECT_STATE(this, ITEM_IN):
        None
    def SELECT_PHONE_NUMBER(this,ID_IN):
        None
    def SELECT_AREA_CODE(this,ITEM_IN):
        None