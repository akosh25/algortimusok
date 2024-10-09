# 1. Rendezési algoritmus
# Lily's Homework probléma - Hackerrank, közepes nehézség
Link: https://www.hackerrank.com/challenges/lilys-homework/problem?isFullScreen=true

## Feladat leírása
George akárhányszor próbálja Lily-t elhívni, mindig elfoglalt a házi feladat megoldásával. Ezért George szeretne segíteni neki, hogy gyorsabban végezzen de ez meghaladja a képességeit. Tudnál segíteni Georgenak, hogy megértse Lile házifeladatát, hogy együtt tudjanak lógni?

Vegyünk egy tömböt, ahol n különböző egész szám van, arr = [a[0], a[1], ...a[n-1]]. George bármikor megtud cserélni benne két tetszőleges számot. A tömb akkor lesz szép ha az összege |arr[i] - arr[i-1]| között 0 < i < n minimális.

## Algoritmus célja
A tömb adott, határozd meg a minimum cserék számát ahhoz, hogy jó sorrend legyen és a tömb szépen nézzen ki. 

## Példa
arr = [7,15,12,3]
Egy minimális tömb így néz ki: 
[3,7,12,15]. Ahhoz, hogy ezt megkapjuk George a következő cseréket végzi
3 7 --> [3, 15, 12, 7]
7 15 --> [3, 7, 12, 15]

Tehát összesen csak 2 cserére volt szüksége.