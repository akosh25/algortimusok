# 1. Rekurziós algoritmus
# Stone Division, Revisited probléma - Hackerrank, közepes nehézség
Link: https://www.hackerrank.com/challenges/stone-division-2/problem?isFullScreen=true

## Leírás
Van egy n darab kőből álló halmazod, amelyet több részhalmazra szeretnél felosztani. Ezen kívül adott egy S halmaz, amely m darab különböző egész számot tartalmaz. Egy lépés végrehajtása a következő módon történik:

## Lépések
Válaszd ki az egyik halmazt (amely jelenleg y darab követ tartalmaz).
Keresd meg az S halmazból valamelyik x számot (x ≠ y) úgy, hogy y osztható legyen x-szel (azaz x egy osztója legyen y-nak). Ha létezik ilyen x, akkor a y köves halmazt feloszthatod y/x darab kisebb egyenlő méretű halmazra.
Az a cél, hogy a lehető legtöbb lépést hajtsd végre.

Adott q darab lekérdezés, ahol minden egyes lekérdezés tartalmaz egy n értéket (a kezdeti kőhalmaz mérete) és egy S halmazt. Minden lekérdezésre meg kell határozni a végrehajtható maximális lépések számát.

## Bemenet formátuma
Az első sor egyetlen egész számot tartalmaz, q-t, ami a lekérdezések számát jelenti. A következő 2 * q sor írja le a lekérdezéseket a következő formában:

### 1. sor
Az első sor tartalmaz két szóközzel elválasztott egész számot: n (a kezdeti kőhalmaz mérete) és m (az S halmaz mérete).

### 2. sor
A második sor tartalmazza az m darab különböző egész számot, amelyek az S halmaz elemei.

## Megkötések
Biztosított, hogy az összes szám különböző az inputban.

1 ≤ 𝑞 ≤ 10

1 ≤ 𝑛 ≤ 10ˇ12

1 ≤ 𝑚 ≤ 1000

1≤ m ≤ 1000

1 ≤ 𝑠𝑖 ≤ 10ˇ12

## Alfeladat:
1 ≤ m ≤ 10 -- a maximum pont 30%-a

## Kimenet formátuma:
Minden lekérdezéshez egy új sorban ki kell írni a maximálisan végrehajtható lépések számát.