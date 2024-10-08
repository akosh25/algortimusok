# 4. Gráfok
# Roads and Libraries probléma - Hackerrank, közepes nehézség
Link: https://www.hackerrank.com/challenges/torque-and-development/problem?isFullScreen=true

## Leírás
Az algoritmusok annyira jók lettek a piaci előrejelzések tekintetében, hogy most már tudjuk, mi lesz a Wooden Orange Toothpicks (WOT) részvényeinek árfolyama a következő napokban.

Minden nap vásárolhatunk egy WOT-részvényt, eladhatunk tetszőleges számú WOT-részvényt, vagy egyáltalán nem kötünk tranzakciót. 
Kérdés: Mekkora az a maximális profit, amit egy optimális kereskedési stratégia mellett elérhetünk?

Példa: price = [1, 3]
Végy egy részvényt az első napon, majd add el a második napon 2 egységnyi nyereségért. Visszatérítés: 2.
price = [2, 1]
Nem érhető el nyereség, mivel egyik nap sem éri meg venni vagy eladni. Visszatérítés: 0.

## Funkció leírás: 
Készítsd el a stockmax függvényt a lenti formában:
stockmax egy tömböt (prices) kap bemenetként, ami a részvény napi árainak előrejelzéseit tartalmazza.
A függvény egy egész számot ad vissza, ami a maximálisan elérhető nyereség.

## Bemenet Formátuma:
Az első sor tartalmazza a tesztesetek számát t.
Mindegyik teszteset két részből áll:
Az első sor tartalmazza a napok számát n.
A második sor tartalmazza a WOT napi részvényárainak listáját price[i] minden i napra.

### Korlátok:
1 ≤ t ≤ 10

1 ≤ n ≤ 50,000

1 ≤ price[i] ≤ 100,000


## Kimenet Formátuma: 
Adj vissza t sort, mindegyik a maximálisan elérhető nyereséget tartalmazza a megfelelő tesztesethez.