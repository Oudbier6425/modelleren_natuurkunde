###### Versie 1.2 15 november 2021
# === Instructies Modelleren ===


## Openen en bewerken van bestanden

Voor het modelleren heb je geen speciale software / programma / app nodig. Het bestand 
waarmee je wilt werken, moet lokaal staan, dus ergens op de computer. Een nieuw bestand 
beginnen doe je door een bestaand bestand onder een andere naam op te slaan.

1. Download het bestand (van e-mail, van [vaksites](https://sites.google.com/a/vszutphen.nl/natuurkunde-havo-vwo/vakles-12e-klas/modelleren?authuser=0), deze github repo, etc.), sla het ergens lokaal op (in eigen map, op bureaublad, op USB-stick, etc.).
2. Onder een andere naam opslaan: Geef de bestandsnaam de extentie (laatste drie 
tekens) “.htm”! Sla dan op als “andere bestanden”, zodat er niet vanzelf een andere 
extentie bij komt.

Daarna kun je het bestand op twee manieren openen; één om te bewerken, één om het 
resultaat te bekijken.

3. Bestand rechts-klikken; Openen met > Kladblok. In dit venster kun je het model (in het bestand) bekijken en bewerken. (Linux: GEdit is erg fijn!)
4. Bestand rechts-klikken; Openen met > Goolge Chrome (of andere webbrowser). In dit venster kun je het resultaat van het model bekijken.

Het bewerken van je model gaat in het tekstvenster (zie punt 3), je kunt dan het resultaat 
bekijken in de webbrowser (zie punt 4). Je kunt beide vensters naast elkaar zetten, of steeds 
wisselen van venster.

5. Verander model (in tekstvester). Opslaan: ***Ctrl-S***.
6. Wissel venster (van tekstvenster naar webbrowser). Wisselen: ***Alt-Tab***.
7. Herlaadt webpagina (want model is veranderd). Herladen: ***F5***.
8. Wissel weer terug naar tekstvenster. ***Alt-Tab*** Enzovoorts.

Wil je het veranderde model bewaren, sla het dan op in een eigen plekje of mail het naar 
jezelf of zo. Van de schoolcomputers worden bureaublad en lokale mappen gewist na 
gebruik! Voorkom verlies van werk…

## Fouten opsporen

Als je model in de webbrowser geen (correct) beeld geeft nadat je iets gewijzigd hebt, heb je 
waarschijnlijk een foutje gemaakt. De meest voorkomende fouten op een rijtje:

* Je hebt ergens een ***komma*** gebruikt in plaats van een ***punt*** voor een decimaal getal.
* Je bent ergens een ***puntkomma*** vergeten achter te zetten (moet altijd in javascript)
* De maximale of minimale waarden op de x-as en y-as kloppen niet meer.
* Je bent een ***startwaarden*** vergeten op te geven voor een nieuwe variabele.
* Je hebt een ***spelfout*** gemaakt in de naam van een variabele.
* Je bent ergens een ***haakje*** vergeten of hebt een haakje teveel staan.
* Je hebt er geen rekening mee gehouden dat hoeken bij sin, cos, tan in radialen moeten.
* De naam waaronder je het opgeslagen hebt eindigt niet op ".htm".


## Over programmeren in javascript

Dit model is een klein programmaatje in een taal die "javascript" heet. Javascript is een taal 
die veel gebruikt wordt in webpagina's. Vrijwel elke website die je bezoekt bevat wel een 
klein stukje javascript. Elke browser kan een programmaatje in javascript lezen en uitvoeren. 
Je hoeft hiervoor niks te installeren. Met (vrijwel) elke browser kun je Javascript uitvoeren. Je 
hoeft niet te kunnen programmeren om met dit model te kunnen werken maar een paar 
dingetjes zijn wel handig om te weten:


#### EINDE REGEL
Elke programmeerregel moet in Javascript eindigen op een puntkomma (;)

#### WISKUNDIGE FUNCTIES
Optellen, aftrekken vermenigvuldigen en delen gaan in javascript op dezelfde manier als 
normaal maar...

* Getallen moeten met een decimale punt in plaats van een komma. Geen 3,4 maar 3.4 dus.
* Machtsverheffen: In Javascript schrijft je "Math.pow(x,y)" voor x tot de macht y. 
* Wortel: In javascript schrijft je "Math.sqrt(x)" voor de wortel van x.
* Sin,cos,tan: In Javascript schrijft je "Math.sin(x)" voor de sinus van x.
* Het getal pi is in Javascript "Math.PI".
* Wetenschappelijke notatie: "3,2 maal 10 tot de 6de" schrijf je in Javascript als 3.2e6

#### COMMENTAAR
In het programma hierboven kom je af en toe '//' tegen. In javascript betekent dit een 
comment'. Alles wat in de regel hierachter staat, wordt door de browser genegeerd en heeft 
dus voor het programma geen enkele betekenis. Je kunt commentaar gebruiken om het model 
voor jezelf duidelijker te maken.

#### TEKEN VOOR :=
Bij modelregels in opgaven wordt meestal ":=" gebruikt in plaats van "=" om aan te geven dat 
een variabel een bepaalde waarde moet krijgen. In Javascript is dit niet zo. Je gebruikt hier het 
gewone "="-teken.

#### MEER WETEN OVER JAVASCRIPT
Voor het werken met dit model hoef je niet echt te kunnen programmeren in javascript. 
Maar misschien vind je het wel leuk om het toch te kunnen. Het is namelijk een hele 
makkelijke manier om te leren programmeren omdat je er geen speciale software voor nodig 
hebt:
Elke browser kan een programmaatje in javascript uitvoeren. Op internet kun je allerlei 
(gratis) online cursussen javascript vinden als je meer wil weten...
