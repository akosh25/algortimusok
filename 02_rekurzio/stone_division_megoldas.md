
# Stone Division - Megoldás

# Stone Division, Revisited probléma - Hackerrank, közepes nehézség
Link: https://www.hackerrank.com/challenges/stone-division-2/problem?isFullScreen=true


## Megközleítés
A feladat megoldásához egy rekurzív mélységi keresés (DFS) algoritmust használunk memoizációval. 

1. **Memoizáció alkalmazása**: A memoizáció segítségével elkerüljük az ismételt számításokat, így csökkentve a program futási idejét.
2. **Rekurzió a DFS segítségével**: A `dfs(n)` függvény minden lehetséges felosztást megvizsgál, és kiszámítja az adott halmaz maximális lépéseinek számát.
3. **Ellenőrzés és felosztás**: Csak akkor osztjuk a halmazt tovább, ha az osztható az adott x értékkel (ahol x ∈ S), és az osztás után a halmaz mérete nem csökken 1 alá.

### Algoritmus
- A memoizáció biztosítja, hogy minden halmazméretre csak egyszer számoljuk ki a maximális lépések számát.
- Az algoritmus rekurzívan keresi meg a lehetséges lépéseket, és mindig azt a felosztást választja, amely a legtöbb lépést eredményezi.
- A `stoneDivision` függvény végigjárja az összes lehetséges felosztást, és visszaadja a maximális lépések számát, amely elérhető az adott n méretű halmazból.