# Kollokvium feladat
# PALIN - A következő palindróm - SPOJ, közepes nehézség
Link: https://www.spoj.com/problems/PALIN/

## Megoldás

- ellenőrízzük, hogy a K szám palindróm-e
- ha nem, létrehozunk egy potenciális palindrómot úgy, hogy a szám bal felét tükrözzük (left_half)
- ha a generált palindróm kisebb vagy egyenlő K-nál, növeljük a bal oldalt, majd újra tükrözünk

## Hatékonyság
Ez egy hatékony megközelítés, mivel csak a számok "felét" használja, így minimalizálva van a szükséges műveletek száma.