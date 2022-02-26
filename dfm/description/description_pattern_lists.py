occupation_pattern_list = set([
    "revisor",
    "revisoren",
    "revisorer",
    "revisorerne",
    "administrator",
    "administratoren",
    "administratorer",
    "administratorerne",
    "analytiker",
    "analytikeren",
    "analytikere",
    "analytikerne",
    "arkitekt",
    "arkitekten",
    "arkitekter",
    "arkitekterne",
    "assistent",
    "assistenten",
    "assistenter",
    "assistenterne",
    "bager",
    "bageren",
    "bagere",
    "bagerne",
    "bartender",
    "bartenderen",
    "bartendere",
    "bartenderne",
    "ejendomsmægler",
    "ejendomsmægleren",
    "ejendomsmæglere",
    "ejendomsmæglerne" "tømrer",
    "tømreren",
    "tømrere",
    "tømrerne",
    "kassemedarbejder",
    "kassemedearbejderen",
    "kassemedarbejdere",
    "kassemedarbejderne",
    "kok",
    "kokken",
    "kokke",
    "kokkene",
    "kemiker",
    "kemikeren",
    "kemikere",
    "kemikerne",
    "chef",
    "chefen",
    "chefer",
    "cheferne",
    "rengøringshjælp",
    "rengøringshjælpen",
    "rengøringshjælpere",
    "rengøringshjælperne",
    "ekspedient",
    "ekspedienten",
    "ekspedienter",
    "ekspedienterne",
    "terapeut",
    "terapeuten",
    "terapeuter",
    "terapeuterne",
    "advokat",
    "advokaten",
    "advokater",
    "advokaterne",
    "diætist",
    "diætisten",
    "diætister",
    "diætisterne",
    "læge",
    "lægen",
    "læger",
    "lægerne",
    "chauffør",
    "chaufføren",
    "chauffører",
    "chaufførerne",
    "redaktør",
    "redatøren",
    "redaktører",
    "redaktørerne",
    "elektriker",
    "elektrikeren",
    "elektrikere",
    "elektrikerne",
    "ingeniør",
    "ingeniøren",
    "ingeniører",
    "ingeniørerne",
    "landmand",
    "landmanden",
    "landmænd",
    "landmændene",
    "brandmand",
    "brandmanden",
    "brandmænd",
    "brandmændene",
    "vagt",
    "vagten",
    "vagter",
    "vagterne",
    "frisør",
    "frisøren",
    "frisører",
    "frisørerne",
    "instruktør",
    "instruktøren",
    "instruktører",
    "instruktørerne",
    "efterforsker",
    "efterforskeren",
    "efterforskere",
    "efterforskerne",
    "pedel",
    "pedellen",
    "pedeller",
    "pedellerne",
    "advokat",
    "advokaten",
    "advokater",
    "advokaterne",
    "bibliotekar",
    "bibliotekaren",
    "bibliotekarer",
    "bibliotekarerne",
    "mekaniker",
    "makanikeren",
    "mekanikere",
    "mekanikerne",
    "sygeplejerske",
    "sygeplersken",
    "sygeplejersker",
    "sygeplejeskerne",
    "politibetjent",
    "politibetjenten",
    "politibetjente",
    "politibetjentene",
    "maler",
    "maleren",
    "malerne",
    "malere",
    "ambulanceredder",
    "ambulanceredderen",
    "ambulancereddere",
    "ambulanceredderne",
    "ambulancebehandler",
    "ambulancebehandleren",
    "ambulancebehandlere",
    "ambulancebehandlerne",
    "patolog",
    "patologen",
    "patologer",
    "patologerne",
    "farmaceut",
    "farmaceuten",
    "farmaceuter",
    "farmaceuterne",
    "blikkenslager",
    "blikkenslageren",
    "blikkenslagere",
    "blikkenslagerne",
    "programmør",
    "programmøren",
    "programmører",
    "programmørerne",
    "psykolog",
    "psykologen",
    "psykologer",
    "psykologerne",
    "receptionist",
    "receptionisten",
    "receptionister",
    "receptionisterne",
    "sekretær",
    "sekretæren",
    "sekretærer",
    "sekretærerne",
    "kirurg",
    "kirurgen",
    "kirurger",
    "kirurgerne",
    "skrædder",
    "skrædderen",
    "skræddere",
    "skrædderne",
    "tekniker",
    "teknikeren",
    "teknikere",
    "teknikerne",
    "terapeut",
    "terapeuten",
    "terapeuter",
    "terapeuterne",
    "dyrlæge",
    "dyrlægen",
    "dyrlæger",
    "dyrlægerne",
    "forfatter",
    "forfatteren",
    "forfattere",
    "forfatterne",
])

female_gendered_terms = set([
    "pige",
    "pigen",
    "piger",
    "pigerne",
    "søster",
    "søsteren",
    "søstere",
    "søsterne",
    "mor",
    "moren",
    "mødre",
    "mødrene",
    "kone",
    "konen",
    "koner",
    "konerne",
    "brud",
    "bruden",
    "brude",
    "brudene",
    "dame",
    "damen",
    "damer",
    "damerne",
    "datter",
    "datteren",
    "døtre",
    "døtrene",
])

male_gendered_terms = set([
    "dreng",
    "drengen",
    "drenge",
    "drengene",
    "bror",
    "broren",
    "brødre",
    "brødrene",
    "far",
    "faren",
    "fædre",
    "fædrene",
    "mand",
    "manden",
    "mænd",
    "mændene",
    "brudgom",
    "brudgommen",
    "brudgomme",
    "brudgommene",
    "herre",
    "herren",
    "herrer",
    "herrerne",
    "søn",
    "sønnen",
    "sønner",
    "sønnerne",
])

danish_adult_words = set([
    "amatør",
    "anal",
    "anus",
    "babes",
    "bdsm",
    "begær",
    "bestialitet",
    "blodig",
    "blowjob",
    "bordel",
    "bordeller",
    "bryster",
    "bøsse",
    "bøssefilm",
    "c-skål",
    "damer",
    "dating",
    "dildo",
    "dildoer",
    "dildomaskine",
    "dyrisk",
    "ejakulation",
    "ejakulere",
    "ejakulerede",
    "ejakulerer",
    "elskerinde",
    "endetarm",
    "erotik",
    "erotisk",
    "erotiske",
    "escort",
    "escortpige",
    "escortpiger",
    "escortpigerne",
    "fanden",
    "fisse",
    "fisser",
    "fræk",
    "frække",
    "frækt",
    "fucked",
    "fucker",
    "gangbang",
    "gay",
    "hardcore",
    "hentai",
    "homo",
    "hore",
    "intim",
    "intime",
    "kinky",
    "klitoris",
    "kneppe",
    "kusse",
    "kvinder",
    "latex",
    "latino",
    "lesbisk",
    "liderlig",
    "liderlige",
    "lort",
    "lorte",
    "luder",
    "masochist",
    "massage",
    "massageescort",
    "massageklinik",
    "massagen",
    "massagepige",
    "massagepiger",
    "massagepigerne",
    "milf",
    "nigger",
    "niggere",
    "nøgenbillede",
    "nøgenbilleder",
    "nøgenbillederne",
    "nøgne",
    "onanere",
    "orgasme",
    "orgasmer",
    "patter",
    "pecker",
    "penis",
    "piger",
    "pigesex",
    "pik",
    "pis",
    "pisse",
    "pisser",
    "pisses",
    "porn",
    "porno",
    "porno-casting",
    "pornofilm",
    "pornografi",
    "pornostar",
    "pornostjerne",
    "pornostjernen",
    "pornostjerner",
    "prostitueret",
    "røv",
    "røvhul",
    "røvhuller",
    "sadist",
    "samleje",
    "sex",
    "sexcam",
    "sexdating",
    "sexdatingsites",
    "sexfilm",
    "sexfoto",
    "sexhistorier",
    "sexparadis",
    "sexshop",
    "sexstillinger",
    "sexvideo",
    "sexvideoer",
    "sexvideoerne",
    "sexvideoen",
    "sexy",
    "shemale",
    "shemales",
    "sjofelhed",
    "sjofelheder",
    "sjofelhederne",
    "skamlæber",
    "skider",
    "sluger",
    "sm",
    "spanking",
    "sprække",
    "sprøjteorgasme",
    "sprøjteorgasmer",
    "sprøjteorgasmen",
    "sprøjteorgasmerne",
    "strip",
    "svans",
    "swinger",
    "swingerdating",
    "swingerklub",
    "sæd",
    "sædafgang",
    "tantra",
    "telefonsex",
    "testikel",
    "thai",
    "thaimassage",
    "thaipiger",
    "tranny",
    "tæve",
    "tæver",
    "tøs",
    "tøser",
    "urin",
    "vagina",
    "vaginaen",
    "viagra",
    "viagraen",
    "voldtage",
    "voldtager",
    "voldtægt" "vulva",
    "webcam",
    "webcam-chat",
    "x-bedømt",
    "xxx",
])
