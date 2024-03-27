import re

# Purely meant as a testbed for further development of the regex patterns

text_1 = 'SCHRIFTELIJKE VRAAG\nnr. 1037\nvan BRUNO TOBBACK\ndatum: 6 september 2023\naan ZUHAL DEMIR\nVLAAMS MINISTER VAN JUSTITIE EN HANDHAVING, OMGEVING, ENERGIE EN TOERISME\nOmgevingsvergunning  -  Adviesverlening bij vergunningsaanvragen\nIn mijn schriftelijke vraag nr. 1133 van 6 september 2022 vroeg ik cijfers op over de \nadviesverlening door de afdeling Ruimte en de afdeling Milieu van het departement \nOmgeving in het kader van de omgevingsvergunningsprocedure, vanaf de \ninwerkingtreding van het Omgevingsvergunningsdecreet. Om inzicht te krijgen in de \nhuidige stand van zaken, had ik graag een uitgebreid en geactualiseerd overzicht gekregen \nmet de cijfers voor 2022 en 2023 (voor zover al beschikbaar).\n1.Hoeveel aanvragen tot het bekomen van een omgevingsvergunning werden er jaarlijks \ningediend sinds de inwerkingtreding van het Omgevingsvergunningsdecreet?\na) Graag een onderverdeling per jaar.\nb) Graag een onderverdeling naargelang de vergunningverlenende overheid in eerste \naanleg (gemeente, provincie, minister).\nc) Graag een onderverdeling naargelang het voorwerp van de aanvraag \n(stedenbouwkundige handelingen, ingedeelde activiteiten,...).\n2. Hoeveel administratieve beroepen tegen vergunningsbeslissingen werden er jaarlijks \ningediend sinds de inwerkingtreding van het Omgevingsvergunningsdecreet?\na) Graag een onderverdeling per jaar.\nb) Graag een onderverdeling naargelang de vergunningverlenende overheid in eerste \naanleg.\nc) Graag een onderverdeling naargelang het voorwerp van de aanvraag \n(stedenbouwkundige handelingen, ingedeelde activiteiten,...).\n3. Graag een overzicht van het aantal adviesvragen die werden gesteld aan het \ndepartement Omgeving sinds de inwerkingtreding van het \nOmgevingsvergunningsdecreet. \na) Graag een onderverdeling per jaar.\nb) Graag een onderverdeling naargelang de vergunningverlenende overheid die de \nadviesvraag stelt en de aanleg (eerste aanleg dan wel administratief beroep).\nc) Wat betreft de dossiers die behandeld worden op provinciaal niveau: graag een \nonderverdeling per provincie.\nd) Graag een onderscheid naargelang de adviesverlenende instantie, nl. afdeling \nRuimte respectievelijk afdeling Milieu.\n4. In hoeveel van de bovenvermelde adviesaanvragen hebben de afdeling Ruimte \nrespectievelijk de afdeling Milieu ook effectief een advies geformuleerd?\na) Graag een onderverdeling per jaar.\nb) Graag een onderverdeling naargelang de vergunningverlenende overheid die de \nadviesvraag stelt en de aanleg (eerste aanleg dan wel administratief beroep).c) Wat de dossiers betreft die behandeld worden op provinciaal niveau: graag een \nonderverdeling per provincie.\nd) Graag een onderscheid naargelang de adviesverlenende instantie, nl. afdeling \nRuimte resp. afdeling Milieu.ZUHAL DEMIR \nVLAAMS MINISTER VAN JUSTITIE EN HANDHAVING, OMGEVING, ENERGIE EN TOERISME\nANTWOORD\nop vraag nr. 1037 van 6 september 2023\nvan BRUNO TOBBACK\n1-2.Bij dossiers die – in eerste aanleg (EA) of laatste aanleg (LA) – door het Vlaams Gewest \ndienen beslist te worden, is er een 100% adviseringsgraad vanuit het Departement \nOmgeving (milieu en stedenbouwkundig luik). We zien ook een stijging van het aantal \nberoepen (bij de Minister) tegen beslissingen van de deputatie. Zowel de Vlaamse \ndossiers als de beroepsdossiers betreffen veelal complexe dossiers die een grondige \nadvisering en personeelsinzet vanuit het departement vereisen. \nOp vlak van advisering heeft het Departement Omgeving prioriteiten gesteld in de \nbehandeling van aanvragen en advisering van lokale overheden. Uitgangspunten zijn \ndaarbij enerzijds het subsidiariteitsprincipe in een interbestuurlijke context waarin alle \nbestuursniveaus – gemeentelijk, provinciaal en gewestelijk – over een \nbeslissingsbevoegdheid beschikken en daarnaast een afweging op basis van de impact \nvan de aangevraagde handelingen. \nDe dossiers die aan het departement worden voorgelegd voor advies worden \ngescreend op een aantal criteria. Dit gebeurt op een uniforme manier over heel \nVlaanderen met behulp van een adviseringskader. Samen met het Departement \nOmgeving wordt er een voorstel voorbereid om tot een aanpassing van dit \nadviseringskader te komen. Hierdoor worden er significant meer dossiers geadviseerd \nop een risicogebaseerde manier, afgestemd op de Vlaamse beleidsprioriteiten en met \nrespect voor de subsidiariteit. Het werkvolume van deze significante toename aan \nbehandelde dossiers noodzaakt een netto capaciteitsverhoging bij het departement, \nzowel op vlak van de vergunningverlening/advisering als versterking op GOVC. Dat \nheeft uiteraard een impact op de personeelsbehoefte. Op basis van een eerste \ninschatting moet de werking zo versterkt worden met een 10-tal personeelsleden. \nDaarom bereidt het Departement Omgeving op mijn vraag een aanpassing voor van \nhet Personeelsplan zodat de nodige extra personeelsleden aangeworven kunnen \nworden.\n3-4.Ik verwijs hiervoor naar de bijlage.  \nEr wordt een onderscheid gemaakt tussen de adviesvragen van de dossiers in eerste \naanleg (EA) en laatste aanleg (LA).\nBIJLAGE\nAdviesverlening vanuit Departement Omgeving bij dossiers in EA en LA'
text_2 = 'SCHRIFTELIJKE VRAAG\nnr. 606\nvan SARAH SMEYERS\ndatum: 20 september 2023\naan MATTHIAS DIEPENDAELE\nVLAAMS MINISTER VAN FINANCIËN EN BEGROTING, WONEN EN ONROEREND ERFGOED\nCO2-negatieve gevelsteen  -  Toepassing\nBegin september raakte bekend dat de Limburgse baksteenproducent Vandersanden erin \ngeslaagd is om een CO 2-negatieve gevelsteen te ontwikkelen. Bij de productie van de \nstenen komt geen koolstofdioxide vrij. Sterker nog: het bedrijf gebruikt de uitstoot van \nCO2 van andere bedrijven om de stenen hard te maken. Bovendien zijn de stenen zelf voor \ntachtig procent samengesteld uit reststromen uit de staalindustrie.\nAan het project werd bijna vijf jaar lang intensief gewerkt. Wie zo’n ‘Pirrouet’-gevelsteen - \nwant zo heet het ‘beestje’ - wil gebruiken, zal echter nog een klein beetje geduld moeten \nuitoefenen. Pas op het einde van het jaar wordt de fabriek opgeleverd, waarna men nog \neen maand nodig zal hebben om ten volle op te starten. Als alles goed gaat, zal men dus \nin het eerste kwartaal van 2024 de Pirrouettes op de markt kunnen gooien om ze dan \nvanaf de zomer effectief te gebruiken in de bouw.\nIn se niets dan goed nieuws: Vlaanderen toont zich weer eens langs zijn meest ecologisch-\nergonomisch innovatieve kant. Zo zien we het graag.\nDuurzaamheid, hergebruik en het zo efficiënt mogelijk gebruiken van, bij voorkeur, \nhernieuwbare energie zijn wellicht zaken die niet meer zullen verdwijnen. Denk in dit \nverband ook alleen al maar aan het toenemende belang in de sector van het circulaire \nbouwen. Als Vlaanderen daarin het voortouw kan nemen, is dat natuurlijk dubbelop. \nBovendien is het een oude economische wijsheid: de bouwsector is de kanariepiet in de \nmijn. Doet die sector het goed, dan boert heel de economie goed.\n1. Mogen we op korte tot middellange termijn nog soortgelijke ecologisch-ergonomische \nontwikkelingen, die in de hele bouwsector toepasbaar zijn, verwachten?\n2. Heeft de minister weet van goede praktijken en/of proeftuinen dienaangaande?\n3. Kan de sociale woningsector, naar analogie met bijvoorbeeld het ASTER-project, \nhierbij het voortouw nemen?MATTHIAS DIEPENDAELE\nMINISTER VAN FINANCIËN EN BEGROTING, WONEN EN ONROEREND ERFGOED\nANTWOORD \nop vraag nr. 606 van 20 september 2023\nvan SARAH SMEYERS\n1. Gezien de bredere tendens tot circulair bouwen, kunnen we verwachten dat dergelijke \nontwikkelingen in de bouwsector navolging zullen kennen. Niet in het minst om \nconcurrentieel te blijven, maar ook vanuit de verdere uitbouw van het normenkader \nrond deze materie, zullen de milieuprestaties van materialen verder aan belang winnen \nen de bouwsector aanzetten tot verdere innovaties op dit vlak.\nNet zoals de productie van een CO2-negatieve gevelsteen nu het levenslicht ziet, \nvermoeden we dat soortgelijke initiatieven zich momenteel echter nog in \nontwikkelingsfase bevinden. Concrete initiatieven die rijp zijn voor marktintroductie zijn \nons niet bekend. Veralgemeende toepassing is in die zin pas op middellange termijn te \nverwachten, want veronderstelt dat er een zeker marktaanbod door meerdere spelers \nkan aangeboden worden.\n2. Binnen de oproep Innovatieve Projecten voor de sociale huisvesting wordt een kader \naangeboden om met nieuwe producten, diensten of procedures aan de slag te gaan. \nWeerhouden projectvoorstellen binnen deze oproep kunnen een afwijking krijgen op het \nnormale referentiekader voor sociale woningbouw bestaande uit de ontwerpleidraad, de \nsimulatietabel en het bouwtechnisch bestek. De oproep geeft een belangrijke impuls \naan projecten door een subsidie te koppelen aan innovaties in 6 pijlers: circulair bouwen, \ninnovatieve bouwmethoden, innovatieve technieken/energieconcepten, groen/blauwe \nstructuren, duurzame mobiliteit en planmatige concepten. Deze oproep fungeert dus als \neen proeftuin die op een brede manier inzet op de verdere verduurzaming van het \npatrimonium. Binnen de oproep van 2022 werden 27 projecten weerhouden, waarvan \n16 inzetten op circulariteit. Het gebruik van nieuwe (circulaire of biobased) materialen \nis een mogelijke invulling van deze specifieke pijler. Een nieuwe oproep voor 2023 is \nlopende.\nDe oproep zet expliciet in op kennisdeling zodat de goede praktijken tijdens de \nontwikkeling en uitvoering van het project gedeeld worden naar de sector. De projecten \nuit de oproep 2022 zijn momenteel nog in uitwerking. Het is bijgevolg te vroeg om een \nevaluatie met een verzameling van goede praktijken op te maken.\n3. Het kader van de open oproep innovatieve projecten, zoals hierboven geschetst, heeft \ntot doel de sociale woningsector zowel procedureel als financieel de ruimte te geven om \neen voorloperrol op te nemen. Om hiervan resultaat te zien, is het belangrijk het kader \nstructureel verder te zetten zodat zowel de woonmaatschappijen als de bouwsector \nhierop kunnen inspelen.'
text_3 = "SCHRIFTELIJKE VRAAG\nnr. 1532\nvan JOS D'HAESE\ndatum: 7 juli 2023\naan LYDIA PEETERS\nVLAAMS MINISTER VAN MOBILITEIT EN OPENBARE WERKEN\nDe Lijn  -  Kosten ticketverkoop\nDe Lijn maakt jaarlijks kosten die gepaard gaan met de ticketverkoop. Onder die kosten \nvallen bijvoorbeeld het onderhouden van de app voor ticketverkoop, de automaten, het \nprinten van abonnementen enzovoort. Ook het checken van die tickets kost De Lijn geld, \nwant ze moet daarvoor investeren in scanners op de bus die de tickets checken en lonen \nbetalen aan controleurs die dat mee moeten handhaven.\n1. Graag zou ik een jaarlijkse evolutie sinds 2014 krijgen van de totale kosten die De Lijn \nmaakt voor het verkopen en controleren van abonnementen en tickets van reizigers. \n2. Graag ook een jaarlijkse evolutie sinds 2014 van het aantal ticketcontroleurs en de \nrespectieve personeelskosten. LYDIA PEETERS\nVLAAMS MINISTER VAN MOBILITEIT EN OPENBARE WERKEN\nANTWOORD\nop vraag nr. 1532 van 7 juli 2023\nvan JOS D’HAESE\n1. 2014: 12 791 969 euro\n2015: 13 777 550 euro\n2016: 12 858 136 euro\n2017: 15 366 673 euro\n2018: 14 986 297 euro\n2019: 14 597 375 euro\n2020: 12 684 251 euro\n2021: 11 941 833 euro\n2022: 13 628 748 euro\n2. Onderstaande cijfers tonen de totale kost van de dienst lijncontrole. Ze bevatten dus \nook het ondersteunend personeel met betrekking tot lijncontrole. Het is belangrijk om \nhierbij op te merken dat het takenpakket van lijncontroleurs uit veel meer bestaat \ndan ticketcontrole. Zij zorgen ook voor o.a. bijstand van chauffeurs bij agressie, \ninterventies op het terrein, ondersteuning bij ongevallen … \n2018: 17 956 299 euro\n2019: 16 191 206 euro\n2020: 16 020 736 euro\n2021: 17 709 048 euro\n2022: 19 002 565 euro\nMerk op dat de cijfers van vóór 2018 niet gegeven kunnen worden, omdat toen met \neen ander systeem gewerkt werd.\nDe evolutie van het aantal controleurs kan u terugvinden in het antwoord op \nschriftelijke vraag nr. 851 van mevrouw Els Robeyns, gesteld op 21 februari 2023."
header_pattern = r'''[\s\n]*SCHRIFTELIJKE VRAAG[\s\n]*(?P<number>.+?)[\s\n]*van[\s\n]*(?P<sender>.+?)[\s\n]*datum:[\s\n]*(?P<date>.+?)[\s\n]*aan[\s\n]*(?P<responder>.+?)[\s\n]*\n[\s\n]*(?P<jurisdiction>.+?)\s*\n\s*(?P<topic>.+?)\s*\n'''
match_header_1 = re.search(header_pattern, text_1)
print(match_header_1.group('number'))
print(match_header_1.group('sender'))
print(match_header_1.group('date'))
print(match_header_1.group('responder'))
print(match_header_1.group('jurisdiction'))
print(match_header_1.group('topic'))
print("-------------------- header for text 1 works --------------------")

match_header_2 = re.search(header_pattern, text_2)
print(match_header_2.group('number'))
print(match_header_2.group('sender'))
print(match_header_2.group('date'))
print(match_header_2.group('responder'))
print(match_header_2.group('jurisdiction'))
print(match_header_2.group('topic'))
print("-------------------- header for text 2 works --------------------")

questions_pattern = r'''[\s\n]*SCHRIFTELIJKE VRAAG[\s\n]*(?P<number>.+?)[\s\n]*van[\s\n]*(?P<sender>.+?)[\s\n]*datum:[\s\n]*(?P<date>.+?)[\s\n]*aan[\s\n]*(?P<responder>.+?)[\s\n]*\n[\s\n]*(?P<jurisdiction>.+?)\s*\n\s*(?P<topic>.+?)\s*\n(?P<questions>[\s\S]*)(?P=responder)[\s\S]*(?P=jurisdiction)[\s\S]*ANTWOORD\s*'''
match_questions = re.search(questions_pattern, text_2)
print(match_questions.group('questions'))
print("-------------------- questions work --------------------")

answers_pattern = r'''[\s\n]*SCHRIFTELIJKE VRAAG[\s\n]*(?P<number>.+?)[\s\n]*van[\s\n]*(?P<sender>.+?)[\s\n]*datum:[\s\n]*(?P<date>.+?)[\s\n]*aan[\s\n]*(?P<responder>.+?)[\s\n]*\n[\s\n]*(?P<jurisdiction>.+?)\s*\n\s*(?P<topic>.+?)\s*\n(?P<questions>[\s\S]*)(?P=responder)\s*\n\s*(?P=jurisdiction)\s*\n\s*ANTWOORD[\s\S]*(?P=sender)(?P<answers>[\s\S]*)'''
match_answers = re.search(answers_pattern, text_2)
print(match_answers.group('answers'))
print("-------------------- answers work --------------------")