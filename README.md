# Projekta_darbs
## Projekta darba apraksts
Šis projekts salīdzina datoru kompoonenšu cenas trijos Latvijas interneta veikalos [1a.lv](https://1a.lv), [220.lv](https://220.lv) un [dateks.lv](https://dateks.lv) un pēc tam nosūta ēpastu, kurā interneta veikalā ir idzevīgāk. Projekta autors katru dienu skatijās datora komponenšu cenas latvijas interneta veikalos, jo vēlās uzbūvēt sev datoru, bet tas aizņem ļoti daudz laika, līdz ar to tika nolemts izveidot programmu, kas viņa vietā apskatītos un noteiktu komponenšu cenas, salīdzinātu tās un pēc tam nosūtītu ēpastu, kur ir izdevīgāk.
## Kāds dators būtu vēlams projekta autoram.
Datoram ir jābūt ātram, jaudīgam un ar nākotnes uzlabojumu iespējam. Datoram ir jābūt vismaz 16gb DDR5 lielai operatīvajai atmiņai, lai varētu izmantot diezgan daudz programmas vienlaicīgi, procesoram un videokartei jābūt jaudīgiem, lai varētu spēlēt jaunās videospēles, mātesplatei ir jābūt atbilstīgai procesoram un tai ir jābūt ar iebūvētu wifi, jo dators stāvēs istabā, kur nav pieejams interneta vads, ssd diskam ir jābūt 1tb ar pietiekami ātriem lasīšanas un rakstīšanas ātrumiem, procesora dzesei ir jābūt ūdensdzesei, barošanas blokam ir jaatbilst vismaz C reitingam, korpusam ir jābūt ar iebūvētiem dzesēšanas ventilātorim un nedaudz rgb gaismām.
### Vēlamā datora cena 
Datoram ir jāmaksā apmēram plus, mīnus 1000 eiro.
### Ieteicamās datora komponenetes
Datoram ir jābūt ar norādītajām komponentēm (vai labākām, sliktākas nevar būt):
+ CPU: Procesors AMD Ryzen 5 7600X, 4.7GHz, AM5, 32MB
+ Motherboard: ASRock A620M Pro RS WiFi
+ GPU: Gigabyte Radeon RX 6600 EAGLE GV-R66EAGLE-8GD, 8 GB, GDDR6
+ SSD: Kingston NV2, M.2, 1 TB
+ RAM: 2 x Kingston Fury Beast, DDR5, 8 GB, 6000 MHz
+ PSU: Corsair CV650, 650W, 80PLUS Bronze
+ CPU cooler: Cooler Master MasterLiquid 240L Core ARGB
+ Case: Korpuss Zalman N4 Rev.1, melna
## Projekta darba uzdevums
Projekta galvenais uzdevums ir izveidot programmu, kas salīdzina datoru komponenšu cenas interneta veikalos [1a.lv](https://1a.lv), [220.lv](https://220.lv) un [dateks.lv](https://dateks.lv) pēc dotajām datoru komponentēm. Pēc tam šī programma nosūta ēpasta ziņojumu projekta autoram ar to kurā interneta veikalā ir izdevīgāk uzbūvēt datoru, kā arī kuros interneta veikalos noteiktas datoru komponentes ir izdevīgākas un cik kopā izmaksā uzbūvēt datoru no izdevīgākajiem piedāvājumiem (dažādos interneta veikalos). Projekta mērķis ir atbrīvot laiku projekta autora dzīvē meklējot datora komponenšu cenas, kā arī mērķis ir atvieglot visus apreiķinus un sameklēt izdevīgākos piedāvājumus.
## Projekta darbā izmantotās bibliotēkas
1. Selenium: šī bibliotēka tiek izmantota lai automatizētu pārlūkprogrammu, šajā projekta darbā tā tiek izmantota, lai nolasītu doto datoru komponenšu cenas un nosaukumus no interneta veikaliem.
2. Time: šī bibliotēka tiek izmantota projekta darbā, lai nodrošinātu laika aiztures, piemēram lapas ielādēšanos.
3. Smtplib un email(pakete): šī bibliotēka un pakete tiek izmantota, lai nosūtītu ēpastā ziņojumu ar to kurā interneta veikalā ir izdevīgāk uzbūvēt datoru, kā arī kuros interneta veikalos noteiktas datoru komponentes ir izdevīgākas un cik kopā izmaksā uzbūvēt datoru no izdevīgākajiem piedāvājumiem (dažādos interneta veikalos).
## Projekta darbā izmantotās metodes un koda daļas
1. Selenium bibliotēkas piesaistīšana.
2. get_component_price_1a:
   - Veic meklēšanu pēc konkrētām komponentēm 1a.lv.
   - Iegūst komponentes cenas un nosaukumus.
   - Saglabā informāciju masīvos.
2. get_component_price_220:
   - Veic meklēšanu pēc konkrētām komponentēm 220.lv.
   - Iegūst komponentes cenas un nosaukumus.
   - Saglabā informāciju masīvos.
4. get_component_price_dateks:
   - Veic meklēšanu pēc konkrētām komponentēm dateks.lv.
   - Iegūst komponentes cenas un nosaukumus.
   - Saglabā informāciju masīvos.
5. Informācijas salīdzināšana:
   - Veic salīdzināšanu kurā interneta veikalā ir izdevīgāk uzbūvēt datoru.
   - Rezūltātu saglabāšana.
   - Veic salīdzināšanu kuros interneta veikalos noteiktas datoru komponentes ir izdevīgākas un cik kopā izmaksā uzbūvēt datoru no izdevīgākajiem piedāvājumiem (dažādos interneta veikalos).
   - Rezūltātu saglabāšana masīvos.
6. Ēpasta nosūtīšana:
   - Smtplib un email piesaistīšana, kā arī user_login.py piesaiste.
   - Ēpasta ziņojuma izveide.
   - Ēpasta nosūtišana.
## Programmas izpilde
Programmas izpildi var apskatīties [šeit](https://failiem.lv/u/ks4zwq6zb5).
Lai izpildītos programma, jums ir jaievada savs ēpasts, koda daļās msg['From'] = "" un msg['To'] = "", kā arī jums ir jāpievieno savs ēpats un parole failā user_login.py
