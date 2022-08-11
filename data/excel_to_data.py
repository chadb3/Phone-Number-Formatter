#pip install pylightxl
import pylightxl as xl
retStr = "{"
dictionaryBase = "{}:\"{}\""
db = xl.readxl('NpasInSvcByNumRpt.xlsx')
sheet=db.ws_names[0]
count=0
skip=True
#print(db.ws(sheet).row(row=2))
for row in db.ws(sheet).rows:
    # this is to skip the first row that only describes the info (NPA:"Location")
    if(not skip):
        if(count>0):
            retStr+=','
        print(row)
        retStr+=dictionaryBase.format(row[0],row[1])
        count+=1
    skip = False
print("\n"*10)
retStr+="}"
print(retStr)