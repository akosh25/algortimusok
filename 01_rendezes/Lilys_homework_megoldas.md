
# Lily Házi Feladata - Megoldás

# Lily's Homework probléma - Hackerrank, közepes nehézség
Link: https://www.hackerrank.com/challenges/lilys-homework/problem?isFullScreen=true

## Megoldási Megközelítés

A megoldás egy mohó algoritmust alkalmaz a minimum cserék számának meghatározásához. 

1. **Fő Függvény Meghatározása**

    A `lilysHomework(arr)` nevű fő függvény egy `arr` tömböt vesz át, és egy beágyazott `count_swaps(sorted_arr)` függvényt definiál, amely kiszámítja a rendezett tömb eléréséhez szükséges cserék számát.

2. **Cserék Számolása**

    A `count_swaps` függvény a minimum szükséges cseréket számolja ki.
    
    - **Változók Inicializálása:** Inicializál egy `swaps` változót, amely a cserék számát követi, valamint egy `visited` listát, amely nyomon követi, hogy mely elemeket dolgoztuk már fel.
    - **Eredeti Indexek Térképe:** Egy `index_map` nevű szótárban eltároljuk az elemek eredeti indexeit, hogy gyorsan hozzáférjünk azokhoz.
    - **Ciklusok Detektálása:** A tömb elemein végighaladva ciklusokat keres, majd minden ciklushoz kiszámítja a szükséges cserék számát, mint `cycle_size - 1`.
    
3. **Tömb Rendezése**

    - A tömböt növekvő (`sorted_arr_asc`) és csökkenő (`sorted_arr_desc`) sorrendbe rendezzük.
    - Mindkét rendezett tömbhöz kiszámítjuk a szükséges cserék számát a `count_swaps` függvénnyel.
    
4. **Minimum Csereszám Visszaadása**

    - A függvény a két csereszám minimumát adja vissza (`swaps_asc` és `swaps_desc`).


