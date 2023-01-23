# Alvins formathåndbok på norsk
Oversatt av Loke Sjølie ved UiO for å lettere følge flyten i håndboken og for å bli bedre kjent med input. Inneholder lenker til materialet på svensk for kontroll. Teksten er i markdown-format for å vises på GitHub og lignende. I første omgang refererer Alvins formathåndbok til deres grafiske nettbaserte brukergrensesnitt, og mangler da noe presisering for oversettelse til MODS og andre metadataskjema.

Oversettelsen er oppdatert per januar 2023. Det anbefales å undersøke om originalmaterialet har blitt oppdatert i etterkant; dette vil invalidere tidligere oversettelse.

- Maskinoversettelse: N/A (alt er gjort manuelt)
- Oversettelsesstatus bibliografisk format: ca. 75%
- Oversettelsesstatus autoritetsformat: 0%
- Oversettelsesstatus annet: 0%
- MODS-berikelse: N/A (gå gjennom, lenke hvert felt og underfelt til MODS)
- Grovkontrollert (for større feil): NEI, det kan forekomme større avvik fra originalmaterialet og konnotativ forståelse kan bli tapt mellom SV->NOB. Vær varsom!
- Finkontrollert (for mindre feil): NEI, det kan forekomme noe upresise formuleringer og lignende i henhold til originalmaterialet. Sjekk originalen om du er usikker.

## Bibliografisk format
Det bibliografiske formatet omfatter et antall felt som grupperes i overordnet blokk. Disse gruppene listes her i den rekkefølgen de forekommer i registreringsformularet. For Alvin kan blokken ha avvikende felt jf. tidligere "Ediffahpraksis".
<details><summary>>>Les mer<<</summary>
  ### [Ressurstype](https://wiki.epc.ub.uu.se/display/alvininfo/Resurstyp)
  Definisjon: angir egenkaper og generell type av innhold for ressursen. Ressurstype er et obligatorisk element i Alvin, og må *alltid* velges før en ny post kan opprettes. Ressurstypen gjelder for originalversjonen av et objekt. **For digitaliserte versjoner refererer ressurstypen til den analoge originalen**.

  <details><summary>>>Les mer<<</summary>
    
    I Alvin anvendes det et kontrollert vokabular for å beskrive ressurstyper. Dette er hentet fra MODS:
    - Bok/manuskript (tekst): ressurs som er tekstbasert
    - Kart: kartografisk materiale, herunder to- eller tredimensjonale kart, atlas, globuser, digitale kart, og andre kartografiske objekter
    - Musikaler: trykk eller manuskript (tekst) som inneholder notert musikk
    - Lyd (audio): opptak der lyd registreres på mekanisk eller elektrisk (digital) måte slik at lyden kan spilles av, herunder musikk og tale
    - Bilde: todimensjonale bilder
    - Video: opptak av bevegende bilder, med eller uten audio
    - Gjenstand: tredimensjonelle gjenstander, enten kunstige/menneskapte (skulpturer, mynter, klær) eller naturlige
    - Programvare: elektroniske ressurser som ikke faller under noen annen ressurstype, herunder programvare, nettsider, databaser eller numeriske data
    - Blandet innhold: samlinger av ressurser som inneholder en blanding av øvrige ressurstyper

    I tillegg finnes det i Alvin en særskilt ressurstype:
    - Arkiv: består av "handlinger" som "efter hand uppkommit" hos en institusjon eller person som følge av deres virksomhet

    Attributter
    - Manuskript: en ressurs som er hånd- eller maskinskrevet
    - Samling: en post som beskriver flere ulike objekter, for eksempel en bildesamling
  </details>

  ### [Tittel / alternativ tittel](https://wiki.epc.ub.uu.se/pages/viewpage.action?pageId=27462059)
  Definisjon: ord, frase(r), tegn eller gruppe av tegn som navngir objektet eller det verk som dette inneholder. Mapping: MODS - titleInfo, MARC - 20X-24X.

  <details><summary>>>Les mer<<</summary>
    
    #### Felt - Hovedtittel
    **Hovedtittel** refererer til det foretrukne navnet på et objekt, og er navnet som normalt sett anvendes når ressursen siteres. Hovedtittel kan være hentet fra selve ressursen (tittelside, omslag, etc) eller fra andre referansekilder. Hovedtittel er et obligatorisk element i Alvin, og må *alltid* velges før en ny post kan opprettes. Tittel angis etter RDA 2.3 Tittel, RDA 6.2 Verkets tittel. Valgfri skriftform kan anvendes i Alvin. Om tittelen angis med annen skriftform enn det latinske alfabet anbefales det å lette til romanisert alternativ tittel i posten. Det er også mulig å angi en annen leseretning (visning) for høyre-til-venstre-skrift.

    Konstruerte titler: om ressursen ikke har noen tittel, og tittel ikke kan finnes i andre kilder, konstrueres en kort tittel som beskriver gjenstanden:

    1. Ressursens natur (eksempelvis kart, manuskript, dagbok, etc), **eller**
    2. Ressursens emne (eksempelvis navn på personer, institusjoner, hendelser, etc), **eller**
    3. En kombinasjon av 1 og 2

    Samme skrifttype/språk som angis som [Katalogiseringsspråk](https://wiki.epc.ub.uu.se/pages/viewpage.action?pageId=27462128) for posten skal anvendes i disse tilfellene. Dersom ressursen er av en type som normalt *ikke* bærer identifiserende informasjon, skal tittelen ikke settes i klammer og ingen note skal lages om at tittelen er konstruert. Ved særskilt ønske kan i andre tilfeller en allmenn note legges inn slik: Tittel konstruert (Titel konstruerad, Title constructed)

    For arkiv legges "arkivbildarens" (e.g. personen som har laget arkivet) navn ved, eksempelvis Georg Adlersparres arkiv.

    Titler i manuskript kan konstrueres etter modellen *Institusjon. Manuskript. Signum ((hylle)signatur) om intet annet alternativ foretrekkes.* Eksempel: Uppsala universitetsbibliotek. Handskrift. Gr. 21

    #### Felt - Undertittel
    **Undertittel** refererer til tillegg til eller nærmere definisjon av hovedtittelen. Del- og deltitler kan uttrykkes direkte i undertittelfeltet. Eksempel: Ihreska handskriftssamlingen i Uppsala universitets bibliotek (*hovedtittel*) D. 2, Kommenterande katalog (*undertittel*)

    #### Felt - Alternativ tittel
    Det er mulig å angi deler eller deltitler i feltet [Del](https://wiki.epc.ub.uu.se/display/alvininfo/Del). Foretrukket ved mer komplekse nummereringer.

    #### Attributter
    Type av alternativ tittel angis alltid:
    - Alternativ: andre alternative versjoner enn nedstående
    - Forkortet: forkortet versjon av tittelen
    - Uniform: enhetlig tittel for verk som forekommer med flere ulike titler
    - Oversatt: oversettelse eller transkripsjon av tittelen

  </details>
    
  ### [Plassering](https://wiki.epc.ub.uu.se/display/alvininfo/Placering)
  Definisjon: angir ressursens fysiske plassering (institusjon, samling, hyllesignatur). Mapping: MODS - location/physicalLocation/holdingSimple, MARC - 841-88X.

  <details><summary>>>Les mer<<</summary>

    #### Felt - Avdeling/enhet
    Den institusjonen eller enheten som holder ressursen. **Velges fra en kontrollert liste i Alvin**.

    #### Felt - Samling
    Spesifikk samling som ressursen inngår i. **Velges fra en kontrollert liste i Alvin som legges opp lokalt for hver institusjon**.

    #### Felt - "Sigel" (???)
    Kode/sigel i Libris ihht [Biblioteksdatabasen](http://biblioteksdatabasen.libris.kb.se/). Velges fra en kontrollert liste i Alvins om legges opp lokalt for hver institushon. Anvendes for å angi plassering til motsvarende eksemplar om en post i Alvin lenkes til motsvarende post i Libris.

    #### Felt - Plassering
    Spesifikt lokale eller enhet der ressursen er plassert. Fritekst.

    #### Felt - Hyllesignatur (Signum)
    Hyllesignatur eller annen spesifikk kode som identifiserer eksemplaret av ressursen.

    #### Felt - Tidligere hyllesignatur
    Se felt for hyllesignatur. Dette er for tidligere slike. Om flere tidligere signaturer finnes angis disse med kommategn mellom; Copernicana 1, Gr. 21.

    #### Note (anmerkning)
    Ytterlige opplysninger om eksemplaret som ikke rommes i øvrige felt.
  </details>

  ### [Språk](https://wiki.epc.ub.uu.se/pages/viewpage.action?pageId=27462120)
  Definisjon: språket for innholdet (teksten) i ressursen. Mapping: MODS - language, MARC - 008 35-37, 041.

  <details><summary>>>Les mer<<</summary>
  Velges fra en kontrollert liste i Alvin som bygger på koder for språk, som sett i Library of Congress MARC code list for languages, som i sin tur baseres på ISO 639-2 (Codes for the representation on Names of Languages, Part 2 : Alpha-3 Code). Libris-definerte tillegg gjelder for urdansk, lavtysk, og ursvensk (se Alvin ved behov).

  Flere språk kan angis om ressursen inneholder tekst på flere språk.

  For ikke-språklig materale finnes det en særskilt kode (zxx), denne **anvendes normalt sett ikke i Alvin**. Lag en språknote (i notefeltet med type "språk") om den redegjør for noe som ikke fremgår av språkkodene.
  </details>

  ### [Katalogiseringsspråk](https://wiki.epc.ub.uu.se/pages/viewpage.action?pageId=27462128)
  Definisjon: språket som anvendes for å beskrive ressursen i katalogposten *i Alvin* (herunder konstruerte titler, noter, beskrivelser o.l.). Mapping: MODS - recordInfo/languageOfCataloging, MARC - 040b.

  <details><summary>>>Les mer<<</summary>
    
    Velges fra en kontrollert liste i Alvin som bygger på koder for språk, som sett i Library of Congress MARC code list for languages, som i sin tur baseres på ISO 639-2 (Codes for the representation on Names of Languages, Part 2 : Alpha-3 Code). Libris-definerte tillegg gjelder for urdansk, lavtysk, og ursvensk (se Alvin ved behov).

    Katalogiseringsspråk kan anvendes for å identifisere poster med beskrivelser på ulike språk i "tilpassede" grensesnitt til Alvin.
  </details>

  ### [Person](https://wiki.epc.ub.uu.se/display/alvininfo/Person)
  Definisjon: En person som på noe vis er assosiert med ressursen. Mapping: MODS - name/@type="personal", MARC - 100, 700

  <details><summary>>>Les mer<<</summary>

    #### Felt - Navn
    Definisjon: en person som på noe vis er assosiert med ressursen. Mapping: MODS - name/@type="personal", MARC - 100, 700.

    Velges fra autoritetsposter i Alvin ved å begynne å skrive navnet i feltet. Velg da riktig person. Dersom personen mangler autoritetspost **må den først legges inn** i Alvin.

    #### Felt - Rolle
    Definisjon: relasjonen (rollen personen har/hadde) mellom personen og ressursen. Mapping: MODS - name/role, MARC - 100e, 700e.

    Velges fra en kontrollert liste i Alvin som hovedsakelig er hentet fra Library of Congress MARC Code List for Relators. Én person kan gis flere roller, og hver person må ha minst én rolle. Dersom spesifikk rolle er utilgjengelig, velges rollen "annen" (SV: "annan").
  </details>

  ### [Organisasjon](https://wiki.epc.ub.uu.se/display/alvininfo/Organisation)
  Definisjon: en organisasjon (institusjon) som på ett eller annet vis er assosiert med ressursen. Mapping: MODS - name/@type="corporate", MARC - 110, 710.

  <details><summary>>>Les mer<<</summary>

    #### Felt - Navn
    Definisjon: Navnet på en organisasjon (institusjon). Mapping: MODS - name/@type="corporate", MARC - 110, 710.

    Velges fra autoritetsposter i Alvin ved å begynne å skrive navnet i felt. Velg da riktig organisasjon. Dersom organisasjonen mangler autoritetspost **må den først legges inn** i Alvin.

    #### Felt - Rolle
    Definisjon: rollen organisasjonen innehar i relasjon til ressursen. Mapping: MODS - name/role, MARC - 110e, 710e.

    Velges fra en kontrollert liste i Alvin som hovedsakelig er hentet fra Library of Congress MARC Code List for Relators. Én organisasjon kan gis flere roller, og hver organisasjon må ha minst én rolle. Dersom spesifikk rolle er utilgjengelig, velges rollen "annen" (SV: "annan").
  </details>

  ### [Matematiske data (kart)](https://wiki.epc.ub.uu.se/display/alvininfo/Matematiska+data)
  Definisjon: matematiske data assosiert med kartografisk materiale. Mapping: MODS - subject/cartographics, MARC - 255.

  <details><summary>>>Les mer<<</summary>
    
    #### Felt - Skala
    Definisjon: informasjon om skala, forholdet mellom den reelle størrelsen og en representasjon av denne. Mapping: MODS - subject/cartographics/scale, MARC - 255a.

    Angis som numerisk skala uttrykt som et størrelsesforhold (e.g. 1:2). Dersom skalaen ikke finnes oppgis "ubestembar skala" (SV: "obestämbar skala"). Dersom det er flere enn to skalaer oppgis "varierende skala".

    Dersom eksakt skala mangler, men skalalinjal finnes, så skal skalalinjalen oppgis slik: Skalalinjal (SV: skalstock), eventuelt med dennes benevning i parantes: X måleenheter (dvs. hele linjalen) = Y cm. Regn også ut og oppgi skalaen numerisk. Eksempel 1: [ca 1:800 000] : skalalinjal (Schala miliarium): 4 svenske mil = 5,2 cm. Eksempel 2: ca 1:63 360, ubestembar skala eller 1:500 000.

    #### Felt - Projeksjon
    Definisjon: informasjon om projeksjon, metoden som er brukt for å representere utsiden av en sfære eller en annen form. Mapping: MODS - subject/cartographics/projection, MARC - 255b.

    Oppgi projeksjon dersom dette er å se på objektet. Ta også med fraser som i kilden beskriver meridianer, parallellsirkler og/eller ellipser. Eksempel: avstandsriktig kjeglesnitt eller Gauss-projeksjon.

    #### Felt - Koordinater
    Definisjon: informasjon om geografiske koordinater som omfattes av ressursen. Mapping: MODS - subject/cartographics/coordinates, MARC - 255c.

    Koordinatene oppgis i følgende ordning: vestligste longitud - østligste longitud / nordligste latitud - sørligste latitud. Exempel: Ø 15°02'-Ø 15°12'/ N 57°45'-N 57°41'.
  </details>

  ### Felt for musikalske verk
  <details><summary>>>Les mer<<</summary>

    ### [Toneart (musikalske verk)](https://wiki.epc.ub.uu.se/display/alvininfo/Tonart)
    Definisjon: toneart for musikalske verk. Mapping: MARC - 240r, 384.


    Feltet kan anvendes for å fullbyrde eller presisere de tonehøyderelasjonene som etablerer det musikalske verkets eller uttrykkets spesifikke toneart som tonalt sentrum. Posten kan anvendes for å skille ellers likelydende verk- eller uttrykkstitler.

    Velges fra en kontrollert liste i Alvin. Eksempel: A-dur. Se den svenske siden for mer informasjon (tabell).

    ### Medium (musikalske verk)
    [Svenska](https://wiki.epc.ub.uu.se/pages/viewpage.action?pageId=27462350)
    Definisjon: medium for framføring av musikalske verk. Mapping: MARC - 240m, 382.

    Feltet kan anvendes for å fullbyrde eller presisere det medium (stemme, instrument) som et musikast verk eller uttrykk er skrevet for eller oppført av. Posten kan anvendes for å skille ellers likelydende verk- eller uttrykkstitler.

    Velges fra en kontrollert liste i Alvin. Eksempel: trombone. Se den svenske siden for mer informasjon (tabell).
  </details>

  ### [Opprinnelsesinformasjon](https://wiki.epc.ub.uu.se/display/alvininfo/Tillkomstinformation)
  Definisjon: informasjon om ressursens tilblivelse, herunder plass, utgiver og dato tilkoblet ressursen. Mapping: MODS - originInfo, MARC - 25X-28X.

  <details><summary>>>Les mer<<</summary>
    #### Felt - Utgave/opplag
    Definisjon: informasjon som identifiserer ulike versjoner av ressursen. Mapping: MODS - originInfo/edition, MARC - 250.

    Gjengi utgaveinformasjonen slik den forekommer i ressursen. Eksempel: 2. oppl., 3rd edition, Ny utgave

    #### Felt - År/dato
    Definisjon: år eller dato da ressursen ble skapt eller publisert. Mapping: MODS - originInfo/dateIssued, alternativt originInfo/dateCreated (samme felt i Alvin), MARC - 260c, 008 07-10, 11-14.

    Feltet er inndelt i delfelt for år, måned og dag. Kun tall kan oppgis i disse. Ved behov for "Før Kristus" (negative år), trykk på minussymbolet før feltet (-). Det er også mulig å oppgi et datospenn (fra-til). I tillegg finnes fritekstfiltet Vises som. Her er det mulig å presisere usikre dato eller annen informasjon som må uttrykkes med andre tegn enn tall.

    Eksempel: trolig senere halvdel av 1500-tallet eller 1713? Her ligger "senere halvdel av 1500-tallet" inne som 1551-1599 og "1713?" som 1713. I posten kommer teksten fra Vises som til å vises, samtidig som årstallene blir søkbare som sifre.

    #### Felt - Land
    Definisjon: land der ressursen ble lagd eller publisert. Mapping: MODS - originInfor/place, MARC - 008 15-17.

    Aktuelle land velges fra en kontrollert liste i Alvin med koder for land og autonome områder bestående av to eller tre tegn, se LC MARC Code List for Countries. Historiske land legges *suksessivt* inn i Alvin som et komplement til eksisterende land og velges deretter. Lenken til historiske land fungerer ikke pr 19.01.2023.

    #### Felt - Plass/sted
    Definisjon: plass/sted der ressursen ble lagd eller publisert. Mapping: MODS - originInfo/place, MARC - 260a.

    Kobles til autoritetsposter for steder i Alvin. Dersom det aktuelle stedet ikke finnes i Alvin må den først registreres før kobling kan gjøres. Det er også mulig å oppgi at plass/sted er usikker.

    #### Felt - Forlag
    Definisjon: navnet på den som har publisert, utgitt, trykt eller distribuert ressursen. Mapping: MODS - originInfo/publisher, MARC - 260b (for eldre trykk 260a, etter svensk? praksis).

    Her også avtrykk (eldre trykk).
  </details>

  ### [Øvrige år/dato](https://wiki.epc.ub.uu.se/pages/viewpage.action?pageId=27462174)
  Definisjon: informasjon om andre datoer enn de som er koblede til ressursens herkomst. Mapping: MODS - originInfo/dateOther, MARC - 046.

  <details><summary>>>Les mer<<</summary>
    Feltet er inndelt på samme måte som [Opprinnelsesinformasjon-År/dato](####Felt---År/dato), men feltet Vises som er erstattet av Note (anmerkning). I dette feltet er det mulig å nærmere beskrive usikker dato eller annen informasjon.

    #### Øvrige år/dato-attributter
    Se følgende:

    - Bruksperiode (MODS-import: period_of_use)
    - Bestemmelsesår (MODS-import: determination_year)
    - Dato for digitisering (MODS-import: date_of_digitisation)
    - Dato for utgravning (arkaeologi) (MODS-import: excavation_date)
    - Ervervingsdato (MODS-import: acquisition_date)
    - Inventardato (MODS-import: inventory_date)
    - Årstall på objekt (MODS-import: date_on_object)
    - Konserveringshistorikk (MODS-import: conservation_history)
    - Utlån (MODS-import: on_loan)
  </details>

  ### [Fysisk beskrivelse](https://wiki.epc.ub.uu.se/display/alvininfo/Fysisk+beskrivning)
  Definisjon: beskriver ressursens fysiske attributt(er). Mapping: MODS - physicalDescription, MARC - 007, 3XX.

  <details><summary>>>Les mer<<</summary>

    #### Felt - Format
    Definisjon: beskriver ressursens fysiske format og digital versjon av denne. Mapping: MODS - physicalDescription/form, MARC - 007.

    Verdiene *Ikke digitalt* eller *Digitalt* oppgis alltid etter følgende.

    ###### Objekter som finnes i fysisk form
    Normaltilfellet er at en digitaliserer fysiske objekter (lager en digital faksimile av objektet). I slike tilfeller beskriver metadataposten *fortsatt det fysiske objektet*, og ikke de digitale faksimilene. Dette oppgis ved verdien *Ikke digitalt*. De digitale filene er kopier av eksemplaret som beskrives i posten. For å angi at det fysiske eksemplaret er tilgjengelig i digitalisert form settes *Digitalt*. Deretter, dersom det er kjent og korrekt, settes Digital opprinnelse ("Digital ursprung") enten for originalen eller sekundært. Dersom ingen digital faksimile eksisterer velges kun "Ikke digitalt".

    ###### Objekter som kun er digitale
    Der det ikke finnes et fysisk format av eksemplaret som beskrives i metadataposten oppgis **ikke** *Ikke digitalt* under Fysisk beskrivelse. Det man da beskriver er digitale filer. Dette er inntil videre ikke normen i Alvin. Herunder: foto tatt med digitalkamera, en database, eller en e-post. Her oppgis kun *Digital* med tillegget *Skapt digitalt*.

    ###### Samlinger
    For en samlingspost som en bildesamling eller et arkiv settes format til *Ikke digitalt* dersom den inneholder fysiske objekt(er), og *Digitalt* om den inneholder digitale objekt(er). For et fysisk arkiv der man tilfører digitalisert materiale angis *Ikke digitalt* samt *Digitalt, digitalisert fra originalen*. Ettersom man ikke beskriver hvert objekt i arkivet for seg legges denne anmerkelsen på overordnet nivå.

    Merk: at man velger *Digitalt* som format for en samlingspost betyr derfor ikke at hele samlingen eller arkivet er digitalt, eller at det ikke er fysisk. Hvilke deler som er digitaliserte kan ved behov presiseres under [Noter](https://wiki.epc.ub.uu.se/pages/viewpage.action?pageId=27462438). Et arkiv som bare består av e-poster skal derimot kun være *Digitalt*, selv om de digitale faksimilene ikke er opplastet i Alvin.

    #### Felt - Digital opprinnelse (Digitalt ursprung)
    Definisjon: beskriver hvordan ressursens digitale form ble skapt. Mapping: MODS - physicalDescription/digitalOrigin, MARC - 007.

    Feltet er kun synlig dersom felt for format har verdien Digitalt, og bør alltid velges dersom ressursen finnes i digitalt format. Velges fra en kontrollert liste i Alvin som er hentet fra [MODS](http://www.loc.gov/standards/mods/userguide/physicaldescription.html#digitalorigin).

    #### Felt - Teknikk
    Definisjon: beskriver den teknikken som anvendes for å fremstille ressursen. Mapping: MODS - physicalDescription/note, MARC - 340d.

    Velges fra et kontrollert vokabular i Alvin. Se siden på svensk for utvidet beskrivelse og tabell med fremstillingsmåter.

    **Alternativ**: teknikk kan også oppgis som Emneord med Type form/genre.

    ### Felt - Materiale
    Definisjon: beskriver materialet som anvendes som bygger opp eller fremstiller ressursen. Mapping: MODS - physicalDescription/note, MARC - 340d.

    Velges fra et kontrollert vokabular i Alvin koblet til ulike ressurstyper. Se siden på svensk for utvidet beskrivelse og tabell med materialer. Eksempel: pergament, eik.

    **Alternativ**: for en mer utførlig beskrivelse av et manuskripts underlag kan Øvrig fysisk beskrivelse med Type underlag anvendes.
  </details>

  ### [Øvrig fysisk beskrivelse](https://wiki.epc.ub.uu.se/pages/viewpage.action?pageId=27462515)
  Definisjon: noter relatert til den fysiske beskrivelsen av ressursen som ikke direkte kan legges inn i feltet over. Mapping: MODS - physicalDescription/note.

  <details><summary>>>Les mer<<</summary>

    #### Felt - note
    Definisjon: noter relatert til den fysiske beskrivelsen av ressursen. Mapping: som over.

    Feltet repeteres for hver note. Om ingen spesifikk Type kan angis kan Type være tom.

    Attributt: type (Typ). Identifiserer hvilken type av note som lages. Velges fra en kontrollert liste i Alvin. Se siden på svensk for utdypende forklaring.

  </details>

  ### [Manuskriptsbeskrivelse](https://wiki.epc.ub.uu.se/display/alvininfo/Handskriftsbeskrivning)
  Definisjon: En samlet gruppe med spesifikke felt for å beskrive håndskriftressurser. Mapping: **TEI** - felt hentet fra Manuskriptbeskrivelse

  <details><summary>>>Les mer<<</summary>

    #### Felt - Locus
    Definisjon: Definerer en plassering i en manuskriptressurs eller del av en manuskriptressurs, vanligvis som en sekvens av folioreferanser. Mapping: TEI - locus.

    Brukes først og fremst til å spesifisere delene i de ulike komponentene i manuskriptet. Lokus skal alltid angis for hver komponent i en manuskriptbeskrivelse da den identifiserer den respektive delen. I feltet kan folioen angis som et område fra / til. Disse feltene tilsvarer fra- og til-attributtene i locus-elementet til TEI.

    Eksempel: 1r – 25v

    Normalt legges informasjonen inn i Fritekstfeltet som vises som standard i visningsgrensesnittet for bedre lesbarhet. Det er også mulig å legge inn kun informasjon/posten/utsagn (uppgiften?) i dette feltet. Dette feltet tilsvarer selve locus-elementet i TEI.

    Eksempel: ff. 1r-25v

    Tilsvarende eksempel i TEI-koding:

    <\locus from="1r" to="25v">ff. 1r-25v<\/locus>
    
    #### Felt - Incipit (innledende ord)

    Definisjon: åpningsordene i et manuskript eller en av dets deler. Mapping: TEI - incipit.


    #### Felt - Eksplisitt (avslutningsord)

    Definisjon: utsagn på slutten av teksten til et manuskript eller på slutten av en av delene, som indikerer konklusjonen. Mapping: TEI - explicit.
    
    #### Felt - Rubric (rubrikk, begynnelsen av tekstdelen)

    Definisjon: teksten i en rubrikk eller rubrikk knyttet til en bestemt del av et manuskript, dvs. en rekke ord som signaliserer begynnelsen av en tekstdel, ofte med informasjon om forfatteren og tittelen, som på en eller annen måte er forskjellig fra selve teksten, vanligvis med rødt blekk, eller ved bruk av forskjellige størrelser eller typer skrift som visuelt skiller en. Mapping: TEI - rubric.
    
    #### Felt - Endelig rubrikk (slutten av tekstdel)

    Definisjon: teksten til en rubrikk eller rubrikk knyttet til en bestemt del av et manuskript, dvs. en rekke ord som signaliserer slutten på en tekstdel, ofte med informasjon om forfatteren og tittelen, som på en eller annen måte skiller seg ut fra selve teksten, vanligvis med rødt blekk, eller ved bruk av forskjellige størrelser eller typer skrift som visuelt skiller seg ut. Mapping: TEI - finalRubric.


    #### Felt - Skrift

    Definisjon: skrifttype eller den dominerende skrifttypen som brukes i et manuskript eller en samling av manuskripter. Mapping: TEI - scriptDesc.

    Eksempel: tidlig gotisk skrift med marginalendringer i karolingisk minuskel.


    #### Felt - Kollasjon

    Definisjon: beskrivelse av måten bladene eller bifoliaen (et pergament brettet i to for å danne to blader) til et manuskript er fysisk ordnet. Mapping: TEI - collation.

    Eksempel: 12 quires: I: 2 (ff. 1-2); II: 8 (ff. 3-10); III: 8 (ff. 11-18); IV: 8 (ff. 19-26); V: 8 (ff. 27-34); VI: 8 (ff. 35-42); VIII: 8 (ff. 43-50); VIII: 8 (ff. 51-58); IX: 7 (ff. 59-65, f. 61 is added); X: 8 (ff. 66-73); XI: 8 (ff. 74-81); XII: 8 (ff. 82-89).


    #### Felt - Foliering

    Definisjon: Nummerering av blader i et manuskript. Mapping: TEI - foliation.

    Eksempel: Foliert fortløpende 1-92 (ff. 1-2 og 89 er pergamentflueblad, ff. 90-92 er papirblad lagt til senere) med blyant i øvre høyre hjørne av den moderne katalogisten.


    #### Felt - Kolonner / rader

    Definisjon: angir antall kolonner og rader på arket. Mapping: TEI - layout/@columns, @writtenLines.

    Tilsvarer kolonnene og writtenLines-attributtene i TEI-elementoppsettet. Her legges kun inn tall. En mer detaljert eller mer kompleks beskrivelse av layouten til manuskriptet er gitt i Annen fysisk beskrivelse med Layout-typen.
  </details>

  ### [Mynt](https://wiki.epc.ub.uu.se/display/alvininfo/Mynt)
  Definisjon: felt spesifikt for å beskrive mynt(er). Hentet fra den tidligere Myntdatabasen.

  <details><summary>>>Les mer<<</summary>

  #### Felt - Valør
  Angis med siffer + valuta. Eksempel: 1 daler sølvmynt.

  #### Felt - Randtype
  Kontrollert vokabular i Alvin. Se siden på svensk for tabell og utvidet informasjon.

  #### Felt - "Stampställning" (Stempelstilling?)
  Kontrollert vokabular i Alvin. Se siden på svensk for tabell og utvidet informasjon.

  #### Felt - Forfatning
  Kontrollert vokabular i Alvin. Se siden på svensk for tabell og utvidet informasjon.

  </details>

  ### [Abstrakt/beskrivelse](https://wiki.epc.ub.uu.se/pages/viewpage.action?pageId=27462267)
  Definisjon: en beskrivelse eller sammenfatning av ressursens innhold. Mapping: MODS - abstract, MARC - 520.

  <details><summary>>>Les mer<<</summary>

    Beskrivelsen skrives på samme språk som katalogiseringsspråket for posten. Ved behov kan flere abstrakter/beskrivelser legges inn i samme post, da også på ulike språk.

    #### Alternativ
    - En strukturert innholdsfortegnelse over inngående deler i en hoved-/samlingspost kan oppgis i feltet [Innhold](https://wiki.epc.ub.uu.se/pages/viewpage.action?pageId=27462272).

  </details>

  ### [Transkripsjon](https://wiki.epc.ub.uu.se/display/alvininfo/Transkription)

  Definisjon: transkripsjon av tekst eller tall i objektet. Mapping: TEI - body.

  ### [Innhold](https://wiki.epc.ub.uu.se/pages/viewpage.action?pageId=27462272)

  Definisjon: en strukturert innholdsfortegnelse over ressursens innhold. Mapping: MODS - tableOfContents, MARC - 505.

  <details><summary>>>Les mer<<</summary>

    Kan anvendes for å inkludere en fortegnelse over inngående titler/deler i en hoved-/samlingspost istedenfor å lage separate delposter for hver del. Minst tittel og eventuelt opphav med mer oppgis for de kapitler, artikler, deler eller separate verk som inngår i den beskrevne ressursen.

    Eksempel: Culture at home -- Culture and the global -- Global youth -- Global music -- Territories of global globalization. 

    #### Alternativ
    - Innholdsanmerkninger av beskrivende karakter inngår i feltet Abstrakt.

    - Lag separate delposter for hver inngående del og koble disse delene til hoved-/samlingsposten i feltet *Relaterte poster* i Alvin med typen *Inngår i*.

  </details>

  ### [Litteratur](https://wiki.epc.ub.uu.se/display/alvininfo/Litteratur)

  Definisjon: et overordnet felt for referanser til litteratur som baseres på, handler om eller er av særskilt verdi for den beskrevne ressursen. Mapping: EAD - bibliography, TEI - bibl.

  <details><summary>>>Les mer<<</summary>

    Hentet fra EAD/TEI. Anvendes først og fremt for arkiv- og manuskriptsressurser. Direkte motpart savnes i MODS/MARC. Feltet kan anvendes for å fortegne referanser til ulike typer relevant litteratur i fritekstformat.

    #### Alternativ
    - For bibliografiske referanser til ressursen kan Anmerkning av typen Sitering brukes istedenfor.
    
    - Det er også mulig å legge inn selve referansene i strukturert form som egne poster i Alvin og anvende Relaterte poster i Alvin med typen Refereres av samt Del-poster for å koble ressursen til referansen.

  </details>

  ### [Noter](https://wiki.epc.ub.uu.se/pages/viewpage.action?pageId=27462438)
  Definisjon: generell tekstinformasjon relatert til ressursen som ikke kan oppgis i andre felt. Mapping: MODS - note, MARC - 5XX.

  <details><summary>>>Les mer<<</summary>

    #### Attributter
    - Type - identifiserer hvilken type note som oppgis. Velges fra en kontrollert liste i Alvin som bygger på MODS, MARC og EAD, pluss noen tillegg for mynt. Se tabell på den svenske siden for mer informasjon.

    #### Notefelt i MARC med egne felt i Alvin
    - MARC 505 till Innehåll
    - MARC 506 till Åtkomstvillkor
    - MARC 563 till Bokband

  </details>

  ### [Relaterte poster i Alvin](https://wiki.epc.ub.uu.se/display/alvininfo/Relaterade+poster+i+Alvin)
  Definisjon: en lenke til en annen post i Alvin. Mapping: MODS - relatedItem, MARC - 70X-75X, 76X-78X, 80X-83X, 841-88X. **For lenker til ressurser utenfor Alvin: se feltet Eksterne lenker (neste)**.

  <details><summary>>>Les mer<<</summary>

    #### Felt - Tittel
    Mapping: MODS - titleInfo, MARC - 20X-24X.

    Søk opp posten som skal lenkes ved å begynne å skrive inn tittelen i feltet. Velg da riktig tittel.

    ##### Attributt - Del
    Mapping: MODS - part

    Kan brukes for å oppgi en spesifikk fysisk del i den relaterte posten. Anvendes framfor alt for bibliografiske referanser til andre poster i Alvin.

    #### Felt - Nummer
    Definisjon: nummerering eller annen betegnelse for den aktuelle delen. Kan også inneholde tekstinformasjon. Mapping: MODS - part/detail/.

    Eksempel: 2, Del 2, eller Del 2: Bibliografi.

    #### Felt - Omfang
    Definisjon: omfanget av den aktuelle delen, for eksempel sidetall. Kan angis som intervall (eks. 2-5). Mapping: MODS - part/extent/.

    ##### Attributt - Type
    Velges fra et kontrollert vokabular i Alvin. Se siden på svensk for tabell.

  </details>

  ### [Eksterne lenker](https://wiki.epc.ub.uu.se/pages/viewpage.action?pageId=27462285)
  Definisjon: en URL til en ekstern ressurs av varig karakter utenfor Alvin. For lenker til andre poster i Alvin skal Relaterte poster i Alvin brukes istedenfor (se over). Mapping: MODS - location/url, MARC - 856.

  <details><summary>>>Les mer<<</summary>

    #### Felt - URL
    Mapping: MODS - location/url, MARC - 856u.

    En fullstendig URL. Eksempel: http://www.uu.se.

    #### Felt - Beskrivelse
    Mapping: MODS - location/url/@displaylabel, MARC - 856y.

    En fritekstbeskrivelse av lenken som er interagerbar. Bør alltid oppgis. Eksempel: Uppsala universitet.

    ##### Attributt - Type
    Type relasjon. Velges fra et kontrollert vokabular i Alvin. Se siden på svensk for tabell.

  </details>

  ### [Dokumenttype / Objektkategori / Handlingstype](https://wiki.epc.ub.uu.se/pages/viewpage.action?pageId=27462397)
  Definisjon: termer som betegner en kategori som kjennetegner en viss stil, form eller innhold. Mapping: MODS - genre, MARC - 007, 008.

  <details><summary>>>Les mer<<</summary>

    En mer spesifikk kategorisering av ressursens innhold er [Ressurstype](#ressurstype). Ukontrollerte termer eller termer som ikke finnes i listene legges i feltet Emneord (se neste) med typen genre/form.

    Velges fra kontrollerte lister i Alvin som baserer seg på den generelle [MARC Genre Term List](http://www.loc.gov/standards/valuelist/marcgt.html) og lister fra diverse eldre svenske databaser.

    Rubrikk og alternativ for feltet er koblet til ressurstype i Alvin.

    #### Bok/manuskript
    Rubrikk: dokumenttype. Eksempel: avhandling, bibliografi, brev eller tidsskrift.

    #### Arkiv
    Rubrikk: handlingstype. Eksempel: notater, dagbøker, fotografier eller manuskript. Listen hentes fra den tidligere databasen Ediffah.

    #### Øvrige ressurstyper
    Rubrikk: objektkategori. Eksempel: fotografi (bilde), mynt (formål), eller tale (lydinnspilling).

    Se siden på svensk for utfyllende tabell.

  </details>

  ### [Emneord](https://wiki.epc.ub.uu.se/pages/viewpage.action?pageId=27462502)
  Definisjon: en term eller frase som beskriver de primære emnene en ressurs handler om. Mapping: MODS - subject, MARC - 6XX.

  <details><summary>>>Les mer<<</summary>

    #### Felt - Nøkkelord
    Oppgi termen og koble til type og motsvarende *schema*. For ukontrollerte emneord oppgis intet *schema*.

    ##### Attributt - Schema
    Oppgir emneordsskjema. Tilgjengelige alternativ er [Humord](https://data.ub.uio.no/skosmos/humord/nb/), [ICSH](http://id.loc.gov/authorities/subjects.html), [LoB](http://www.ligatus.org.uk/lob/), [NAD](https://sok.riksarkivet.se/nad), [SAO](http://www.kb.se/katalogisering/Svenska-amnesord/) og [TGM2](http://www.kb.se/katalogisering/Svenska-amnesord/genrer-form/tesaurus/).

    ##### Attributt - Type
    Identifiserer hvilken type emneord som oppgis.

    Se også [retningslinjer for indeksering med svenske emneord](http://www.kb.se/dokument/Verktygsladan/Svenska%20%C3%A4mnesord/Riktlinjer/Riktlinjer%20SAO.pdf). Se siden på svensk for utfyllende tabell.

  </details>

  ### [Klassifikasjon](https://wiki.epc.ub.uu.se/display/alvininfo/Klassifikation)
  Definisjon: en betegnelse som viser emnet for en ressurs ved å anvende et formelt system for koding og organisering av ressurser etter fagområder. Mapping: MODS - classification, MARC - 01X-09X.

  <details><summary>>>Les mer<<</summary>

    #### Felt - Klassifikasjon
    Skriv inn koden og koble til det tilsvarende skjemaet.

    Eksempel: Oa (kssb)

    ##### Attributt - Schema
    Klassifikasjonsskjema. Mulige alternativ er [DDK](http://www.kb.se/katalogisering/klassifikation/DDK/), [KSSB (SAB)](http://www.kb.se/katalogisering/Klassifikation/SAB/) og [Iconclass](http://www.iconclass.nl/home).

  </details>

  ### [Del](https://wiki.epc.ub.uu.se/display/alvininfo/Del)
  Definisjon: kan anvendes for å oppgi spesifikk fysisk del av ressursen. Delposten blir vist direkte etter tittelinformasjon i visningsgrensesnittet. Mapping: MODS - part.

  <details><summary>>>Les mer<<</summary>

    #### Felt - Nummer
    Nummerering eller annen betegnelse for den aktuelle delen. Kan også inneholde tekstinformasjon. Eksempel: 2, Del 2 eller Del 2: Bibliografi. Mapping: MODS - part/detail/.

    #### Felt - Omfang
    Definisjon: omfanget av den aktuelle delen, for eksempel sidetall. Kan angis som intervall (eks. 2-5). Mapping: MODS - part/extent/.

    ##### Attributt - Type
    Type av del. Velges fra et kontrollert vokabular i Alvin. Se siden på svensk for tabell.

    #### Alternativ
    Delinformasjon kan også oppgis i ustrukturert form rett i [Undertittel-feltet i Tittel](#felt---undertittel).

    Kommentar om parsing av MODS: Man kan ha flera part-element som då bildar en lista i posten, men i varje del hämtas bara första detail och första extent om det finns mer än en.

  </details>

  ### [Tilgjengelighet](https://wiki.epc.ub.uu.se/pages/viewpage.action?pageId=27462339)
  Definisjon: informasjon om spesifikke lokale restriksjoner, regler eller spesielle prosedyrer pålagt av en arkivinstitusjon, giver, rettslig organ eller annen myndighet angående ressursen. Mapping: EAD - userestrict.

  <details><summary>>>Les mer<<</summary>

    Anvendes først og fremst for arkivressurser. Disse begrensningene kan også være relaterte til reproduksjon, publisering eller sitering av den beskrevne ressursen etter at tilgang til ressursen er bevilget. Eksempel: Fram til 2027 er tillatelse til å kopiere materiale fra denne samlingen begrenset på forespørsel fra giveren.

    #### Alternativ
    For generelle begrensninger gjennom opphavsrett anvendes Tilgangsvilkår.

  </details>

  ### [Tilgangsvilkår](https://wiki.epc.ub.uu.se/pages/viewpage.action?pageId=27462335)
  Definisjon: informasjon om restriksjoner som gjelder for tilgang til en ressurs. Mapping: MODS - accessCondition, MARC - 506.

  Anvendes on fri tilgang til ressursen ikke kan gis digitalt og/eller fysisk på grunnlag av opphavsrett eller andre juridiske bestemmelser.

  <details><summary>>>Les mer<<</summary>

    #### Alternativ
    - Spesifikke, lokale tilgangsbegrensninger av en ressurs kan oppgis i Tilgjengelighet (over).

  </details>

  ### [Bokbind](https://wiki.epc.ub.uu.se/display/alvininfo/Bokband)
  Definisjon: beskriver ressursens nåværende og/eller tidligere innbinding samt disses dekor. Mapping: TEI - bindingDesc, MARC - 563.

  <details><summary>>>Les mer<<</summary>

    Anvendes først og fremst for manuskriptressurser, eldre trykk eller andre spesialsamlinger. Se også [Bokbandsregistrering](https://wiki.epc.ub.uu.se/display/alvininfo/Bokbandsregistrering)(SV) for detaljerte beskrivelser.

    #### Felt - Bind
    Mapping: TEI - bindingDesc, MARC - 563.

    Beskriver ressursens nåværende og/eller tidligere innbinding.

    #### Felt - Dekor
    Mapping: TEI - decoNote.

    Beskriver et dekorativt komponent eller en homogen klasse av slike komponenter ihht bindets utseende.

  </details>

  ### [Dekor](https://wiki.epc.ub.uu.se/display/alvininfo/Dekor)
  Definisjon: beskriver et dekorativt komponent eller en homogen klasse av slike komponenter ihht bindets utseende. Anvendes først og fremst for manuskriptressurser, eldre trykk eller andre spesialsamlinger. Mapping: TEI - decoNote.

  ### [Publiseringsinformasjon](https://wiki.epc.ub.uu.se/display/alvininfo/Publiceringsinformation)
  Definisjon: administrativ informasjon om postens eier(e) og tilgjengelighet. Kun synlig for innloggede administratorer. Mapping: MODS - recordInfo, MARC - 040, 008/00-05, 005.

  <details><summary>>>Les mer<<</summary>

    #### Felt - Eier
    Institusjon som eier posten i Alvin. Oppgis fra en kontrollert liste koblet til innlogging.
    
    #### Felt - Tilgjengelig fra
    Dato og tid når posten publiseres. Kan tas bort ved å avpublisere den, alternativt legges til ved å publisere en upublisert post.

    #### Felt - Tilgjengelig til
    Dato og tid for når en publisert post ikke lenger skal være tilgjengelig. Anvendes normalt sett ikke.

  </details>

  ### [Identifikatorer, generelle](https://wiki.epc.ub.uu.se/pages/viewpage.action?pageId=27462304)
  Definisjon: unike standardtall eller koder som anvendes globalt eller i andre systemer enn Alvin for å identifisere ressursen, eksempelvis ISBN, ISSN, Libris-ID eller DOI. Mapping: MODS - identifier, MARC - 010, 020, 022, 024, 028, 037, 856.

  <details><summary>>>Les mer<<</summary>

    #### URN:NBN
    I Alvin skapes det automatisk en unik, varig identifikator i form av et URN:NBN gjennom Kungliga Biblioteket. Når man forsyner en elektronisk ressurs med URN gjør man det enklere og sikrere å identifisere og gjenfinne ressursen. Et URN endres ikke når en ressurs flyttes til en annen adresse. Det gjør derimot en URL. URN skal ikke byttes ut enn så lenge innholdet i en ressurs ikke endres. Man får heller ikke gi et tidligere brukt URN til en annen ressurs. URN:NBN i Alvin har strukturen urn:nbn:se:alvin:portal:record-[database-ID], eksempelvis urn:nbn:se:alvin:portal:record-80363.

    ##### Attributt - Type
    Type angis alltid. Se siden på svensk for kontrollert vokabular.

  </details>

  ### [Identifikatorer, lokale](https://wiki.epc.ub.uu.se/pages/viewpage.action?pageId=27462311)
  Definisjon: nummer eller koder som anvendes lokalt for å identifisere ressursen, eksempelvis adgangsnummer eller inventarnummer. Mapping: MODS - identifier, MARC - 024 + 2.

  <details><summary>>>Les mer<<</summary>

    #### Lokal Alvin-ID

    Alle Alvin-poster får en unik Alvin-ID automatisk i formen alvin-record:[database-ID], eksempelvis alvin-record:80363. 

    ##### Attributt - Type
    Type angis alltid. Lokale lister legges inn for hver institusjon i Alvin.

    #### Alternativ
    - For identifikatorer som identifiserer ressursen globalt skal Identifikatorer, generelle anvendes.
    - Hyllesignatur legges i Plassering/Signum.
    
  </details>

  ### [Verkslisensiering](https://wiki.epc.ub.uu.se/display/alvininfo/Licensiering+av+verket)
  Definisjon: lisensinformasjon for digitale verk som publiseres i Alvin. Mapping: ingen. Bruk tilgangsvilkår for MODS/MARC.
</details>
## Autoritetsformatet

### []()
Definisjon: 

<details><summary>>>Les mer<<</summary>

  #### Felt 

</details>
