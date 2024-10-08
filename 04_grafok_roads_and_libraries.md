# 4. Gráfok
# Roads and Libraries probléma - Hackerrank, közepes nehézség
Link: https://www.hackerrank.com/challenges/torque-and-development/problem?isFullScreen=true

## Feladat
Határozd meg a minimális költséget a könyvtárhozzáférés biztosításához HackerLand összes polgára számára.

## Leírás
HackerLand városai számozva vannak 1-től n-ig. Jelenleg nincsenek könyvtárak, és a városok nincsenek összekapcsolva. Két város között bármely, a cities tömbben felsorolt várospár között két-direkcionális utakat lehet építeni. Egy polgár hozzáfér a könyvtárhoz, ha:
- A városa tartalmaz egy könyvtárat.
- Úton eljuthat egy olyan városba, ahol van könyvtár.

## Példa

A bármely út építési költsége c_road, és a bármely városban épített könyvtár költsége c_lib. Építs m utat c_road költséggel, és n könyvtárat c_lib költséggel. Az elérhető utak közül az egyik az m ciklusban nem szükséges.

Összesen q lekérdezés van, ahol minden lekérdezés egy HackerLand térképét, valamint a c_lib és c_road értékét tartalmazza. Minden lekérdezés esetén határozd meg a minimális költséget a könyvtárak elérhetőségének biztosításához minden polgár számára.

## Függvény Leírása

A roadsAndLibraries a következő paramétereket tartalmazza:

- int n: az városok számát jelző egész szám
- int c_lib: a könyvtár építési költsége
- int c_road: az út építési költsége
- int cities[m][2]: minden egyes elem két egész számot tartalmaz, amelyek azt a két várost jelölik, amelyek összeköthetők egy új úttal

Visszatérés
- int: a minimális költség

## Bemeneti Formátum

Az első sor egyetlen egész számot tartalmaz (q), amely a lekérdezések számát jelzi.

A következő sorok minden lekérdezést az alábbi formátumban írnak le:

- Az első sor négy szóközökkel elválasztott egész számot tartalmaz, amelyek a következő értékeket írják le: n, m, c_lib, c_road (a városok száma, az utak száma, a könyvtár költsége és az út költsége).
- A következő m sor mindegyike két szóközökkel elválasztott egész számot tartalmaz, amelyek u és v (az összekapcsolható városok).

## Korlátozások

- 1 <= q <= 10

Minden út két különböző várost köt össze.