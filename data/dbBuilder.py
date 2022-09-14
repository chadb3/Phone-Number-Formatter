import sqlite3
from time import sleep
# Builds
# States and Area Code DB
# Builds states DB and their connections. (Maybe) 
print("Starting dbBuilder")
# if DB exists ask if they want to rewrite it.
a= {201:"NJ",202:"DC",203:"CT",204:"MANITOBA",205:"AL",206:"WA",207:"ME",208:"ID",209:"CA",210:"TX",212:"NY",213:"CA",214:"TX",215:"PA",216:"OH",217:"IL",218:"MN",219:"IN",220:"OH",223:"PA",224:"IL",225:"LA",226:"ONTARIO",228:"MS",229:"GA",231:"MI",234:"OH",236:"BRITISH COLUMBIA",239:"FL",240:"MD",242:"BAHAMAS",246:"BARBADOS",248:"MI",249:"ONTARIO",250:"BRITISH COLUMBIA",251:"AL",252:"NC",253:"WA",254:"TX",256:"AL",260:"IN",262:"WI",264:"ANGUILLA",267:"PA",268:"ANTIGUA/BARBUDA",269:"MI",270:"KY",272:"PA",276:"VA",279:"CA",281:"TX",284:"BRITISH VIRGIN ISLANDS",289:"ONTARIO",301:"MD",302:"DE",303:"CO",304:"WV",305:"FL",306:"SASKATCHEWAN",307:"WY",308:"NE",309:"IL",310:"CA",312:"IL",313:"MI",314:"MO",315:"NY",316:"KS",317:"IN",318:"LA",319:"IA",320:"MN",321:"FL",323:"CA",325:"TX",326:"OH",330:"OH",331:"IL",332:"NY",334:"AL",336:"NC",337:"LA",339:"MA",340:"USVI",341:"CA",343:"ONTARIO",345:"CAYMAN ISLANDS",346:"TX",347:"NY",351:"MA",352:"FL",360:"WA",361:"TX",364:"KY",365:"ONTARIO",367:"QUEBEC",368:"ALBERTA",380:"OH",385:"UT",386:"FL",401:"RI",402:"NE",403:"ALBERTA",404:"GA",405:"OK",406:"MT",407:"FL",408:"CA",409:"TX",410:"MD",412:"PA",413:"MA",414:"WI",415:"CA",416:"ONTARIO",417:"MO",418:"QUEBEC",419:"OH",423:"TN",424:"CA",425:"WA",430:"TX",431:"MANITOBA",432:"TX",434:"VA",435:"UT",437:"ONTARIO",438:"QUEBEC",440:"OH",441:"BERMUDA",442:"CA",443:"MD",445:"PA",447:"IL",448:"FL",450:"QUEBEC",458:"OR",463:"IN",464:"IL",469:"TX",470:"GA",473:"GRENADA",474:"SASKATCHEWAN",475:"CT",478:"GA",479:"AR",480:"AZ",484:"PA",501:"AR",502:"KY",503:"OR",504:"LA",505:"NM",506:"NEW BRUNSWICK",507:"MN",508:"MA",509:"WA",510:"CA",512:"TX",513:"OH",514:"QUEBEC",515:"IA",516:"NY",517:"MI",518:"NY",519:"ONTARIO",520:"AZ",530:"CA",531:"NE",534:"WI",539:"OK",540:"VA",541:"OR",548:"ONTARIO",551:"NJ",559:"CA",561:"FL",562:"CA",563:"IA",564:"WA",567:"OH",570:"PA",571:"VA",572:"OK",573:"MO",574:"IN",575:"NM",579:"QUEBEC",580:"OK",581:"QUEBEC",582:"PA",585:"NY",586:"MI",587:"ALBERTA",601:"MS",602:"AZ",603:"NH",604:"BRITISH COLUMBIA",605:"SD",606:"KY",607:"NY",608:"WI",609:"NJ",610:"PA",612:"MN",613:"ONTARIO",614:"OH",615:"TN",616:"MI",617:"MA",618:"IL",619:"CA",620:"KS",623:"AZ",626:"CA",628:"CA",629:"TN",630:"IL",631:"NY",636:"MO",639:"SASKATCHEWAN",640:"NJ",641:"IA",646:"NY",647:"ONTARIO",649:"TURKS & CAICOS ISLANDS",650:"CA",651:"MN",656:"FL",657:"CA",658:"JAMAICA",659:"AL",660:"MO",661:"CA",662:"MS",664:"MONTSERRAT",667:"MD",669:"CA",670:"CNMI",671:"GU",672:"BRITISH COLUMBIA",678:"GA",680:"NY",681:"WV",682:"TX",683:"ONTARIO",684:"AS",689:"FL",701:"ND",702:"NV",703:"VA",704:"NC",705:"ONTARIO",706:"GA",707:"CA",708:"IL",709:"NEWFOUNDLAND AND LABRADOR",712:"IA",713:"TX",714:"CA",715:"WI",716:"NY",717:"PA",718:"NY",719:"CO",720:"CO",721:"SINT MAARTEN",724:"PA",725:"NV",726:"TX",727:"FL",731:"TN",732:"NJ",734:"MI",737:"TX",740:"OH",742:"ONTARIO",743:"NC",747:"CA",753:"ONTARIO",754:"FL",757:"VA",758:"ST. LUCIA",760:"CA",762:"GA",763:"MN",765:"IN",767:"DOMINICA",769:"MS",770:"GA",771:"DC",772:"FL",773:"IL",774:"MA",775:"NV",778:"BRITISH COLUMBIA",779:"IL",780:"ALBERTA",781:"MA",782:"NOVA SCOTIA - PRINCE EDWARD ISLAND",784:"ST. VINCENT & GRENADINES",785:"KS",786:"FL",787:"PUERTO RICO",801:"UT",802:"VT",803:"SC",804:"VA",805:"CA",806:"TX",807:"ONTARIO",808:"HI",809:"DOMINICAN REPUBLIC",810:"MI",812:"IN",813:"FL",814:"PA",815:"IL",816:"MO",817:"TX",818:"CA",819:"QUEBEC",820:"CA",825:"ALBERTA",826:"VA",828:"NC",829:"DOMINICAN REPUBLIC",830:"TX",831:"CA",832:"TX",838:"NY",839:"SC",840:"CA",843:"SC",845:"NY",847:"IL",848:"NJ",849:"DOMINICAN REPUBLIC",850:"FL",854:"SC",856:"NJ",857:"MA",858:"CA",859:"KY",860:"CT",862:"NJ",863:"FL",864:"SC",865:"TN",867:"YUKON-NW TERR. - NUNAVUT",868:"TRINIDAD & TOBAGO",869:"ST. KITTS & NEVIS",870:"AR",872:"IL",873:"QUEBEC",876:"JAMAICA",878:"PA",901:"TN",902:"NOVA SCOTIA - PRINCE EDWARD ISLAND",903:"TX",904:"FL",905:"ONTARIO",906:"MI",907:"AK",908:"NJ",909:"CA",910:"NC",912:"GA",913:"KS",914:"NY",915:"TX",916:"CA",917:"NY",918:"OK",919:"NC",920:"WI",925:"CA",928:"AZ",929:"NY",930:"IN",931:"TN",934:"NY",936:"TX",937:"OH",938:"AL",939:"PUERTO RICO",940:"TX",941:"FL",943:"GA",945:"TX",947:"MI",948:"VA",949:"CA",951:"CA",952:"MN",954:"FL",956:"TX",959:"CT",970:"CO",971:"OR",972:"TX",973:"NJ",978:"MA",979:"TX",980:"NC",983:"CO",984:"NC",985:"LA",986:"ID",989:"MI", 888:"Toll Free"}
file = "PNDB.sqlite3"
connection=sqlite3.connect(file)
for i in a:
    cur=connection.execute("INSERT INTO USA_AREA_CODES(AREA_CODE,STATE) VALUES ('{}','{}')".format(i,a[i]))
    print("{}\t{}".format(i,a[i]))
connection.commit()
connection.close()