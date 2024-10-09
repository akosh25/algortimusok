
# 3. Dinamikus programozás - Megoldás
# Stock Maximize probléma - Hackerrank, közepes nehézség
Link: https://www.hackerrank.com/challenges/stockmax/problem?isFullScreen=true


1. **Alapötlet**
AHa előre ismerjük a részvények jövőbeli árfolyamait, akkor minden napon meg tudjuk határozni, hogy mi lenne a legjobb eladási pont. Visszafelé haladva az árlistán, mindig naprakészen tarthatjuk a maximális árat, amelyen eladhatnánk a részvényt, így optimalizálva a vásárlási döntéseket.

2. **Miért Visszafelé?**
A visszafelé haladás előnye, hogy bármelyik nap előtt már tudjuk, hogy mi lesz a maximális ár a következő napokban. 

- Ha egy adott napon az ár alacsonyabb, mint a maximális ár, akkor érdemes aznap vásárolni, mert a későbbiekben magasabb áron tudjuk eladni.
- A nyereséget úgy számoljuk ki, hogy a legmagasabb eladási ár és az adott napi ár közötti különbséget hozzáadjuk az összesített nyereséghez.

## Algoritmus

- Visszafelé iterálás: Az árlistát visszafelé járjuk be. Minden lépésben az aktuális árat összehasonlítjuk a jelenlegi max_price értékkel:
- Ha az aktuális ár magasabb, mint a max_price, frissítjük a max_price értékét.
- Ha az aktuális ár alacsonyabb, kiszámítjuk a lehetséges nyereséget: max_price - price, és ezt hozzáadjuk a profit változóhoz.
- Eredmény visszaadása: A teljes nyereséget tartalmazó profit változót adja vissza a függvény.


## Dinamikus programozás
- Az algoritmus mindig a részproblémákra optimalizál, és az ismétlődő számításokat elkerüli. 