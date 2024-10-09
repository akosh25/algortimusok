# 4. Gráfok - Megoldás
# Roads and Libraries probléma - Hackerrank, közepes nehézség
Link: https://www.hackerrank.com/challenges/torque-and-development/problem?isFullScreen=true


1. **Költség-összehasonlítás**: Először megvizsgáljuk, hogy a könyvtár építésének költsége kisebb vagy egyenlő-e az út építésének költségével (`c_lib <= c_road`).
   - Ha igaz, akkor a legolcsóbb megoldás minden városban egy-egy könyvtár építése, mivel ez olcsóbb, mint az utak építése. Az összköltség ilyenkor `n * c_lib`.
2. **Gráf Alapú Megközelítés**: Ha az útépítés olcsóbb, mint a könyvtárépítés, akkor a városok kapcsolatait gráfként kezeljük, és keresünk összefüggő komponenseket.
   - **Szomszédsági lista**: A városok közötti kapcsolatok alapján egy szomszédsági listát hozunk létre, ami a városok közötti közvetlen utakat tárolja.
   - **DFS a komponensek megtalálásához**: Mélységi keresést (DFS) használunk, hogy megtaláljuk az összefüggő városcsoportokat. Minden egyes összefüggő komponens egy olyan városcsoport, amelyben a városok közvetlenül vagy közvetve elérik egymást.
3. **Költségszámítás a Komponensek Alapján**: Minden összefüggő komponenshez:
   - Építünk egy könyvtárat (ennek költsége `c_lib`).
   - Az összes többi várost a komponensben utakkal kötjük össze (ennek költsége `(városok száma - 1) * c_road`).
   - Az összköltség a könyvtárak és utak építési költségeinek összege.

## Hatékonyság és Előnyök
- Az algoritmus hatékonyan találja meg az összefüggő komponenseket, és biztosítja, hogy a lehető legkevesebb költséggel biztosítsuk a városok könyvtárhoz való hozzáférését.
- A gráf alapú megközelítés lehetővé teszi, hogy a probléma bonyolultsága csökkenjen, különösen nagyobb városszám esetén.

Ez az algoritmus biztosítja a legkisebb összköltséget, miközben minden város számára elérhetővé teszi a könyvtári hozzáférést.
