Liczba wartości abnormalnych w poryciu śniegu: 9

Liczba wartości abnormalnych w długości sezonu: 9

Liczba wartości abnormalnych w ilości armatek: 10

Liczba wartości abnormalnych w poryciu śniegu, długości sezonu i ilości armatek: 23

Tylko 2 rekordy, które sa nietypowe w 1d, są typowe w 3d.

400 rekordów jest całkowicie typowe.


|Resort                   |Latitude   |Longitude  |Country    |Continent|Season          |
|-------------------------|-----------|-----------|-----------|------|----------------|
|Kaunertal Glacier        |46.8774734 |10.7136205 |Austria    |Europe|September - June|
|Stubai Glacier           |46.995462  |11.14049   |Austria    |Europe|September - June|
|Saas-Fee                 |46.107342  |7.9247055  |Switzerland|Europe|July - April    |
|Cervinia                 |45.96300885|7.715412186|Switzerland|Europe|Year-round      |
|Hintertux Glacier        |47.061277  |11.665036  |Austria    |Europe|Year-round      |
|Moelltal Glacier         |46.980483  |13.050646  |Austria    |Europe|June - May      |
|Indoor ski area Snow Arena|54.03173   |23.960042  |Lithuania  |Europe|Year-round      |
|Zermatt - Matterhorn     |45.96300885|7.715412186|Switzerland|Europe|Year-round      |
(wszędzie też summer skiing)


Najbardziej nietypowe kraje:

Litwa i Finlandia: 100% przypadków nietypowości w 2D i 3D, co wskazuje na unikalne warunki w tych lokalizacjach.

Serbia: Brak nietypowości w 1D i 2D, ale pełna nietypowość w 3D.

Norwegia: Nietypowość w 2D (80%) i 3D (80%) przy braku w 1D, co sugeruje, że lokalne kombinacje wymiarów prowadzą do nietypowych wyników.

Andora: Nietypowość w 3D (80%) przy braku nietypowości w 1D i 2D.

Wysokie wyniki nietypowości w Europie i Oceanii mogą wynikać z większego zróżnicowania kurortów, np. różnic w długości sezonu lub zaawansowania technologicznego.

W Ameryce Południowej niskie wartości nietypowości w 3D mogą sugerować mniej zróżnicowane warunki w badanych kurortach.

Występuje niska zależność między nietypowościami w 1D i 3D co sugeruje, że na podstawie jednego parametru ciężko przewidzieć anomalie w 3D

## Klasteryzacja

|   Cluster | ('Average Snow', 'mean') | ('Average Snow', 'median') |   ('Average Snow', 'min') |   ('Average Snow', 'max') |   ('Average Snow', 'std') |   ('Average Snow', 'count') |   ('Season Length', 'mean') |   ('Season Length', 'median') |   ('Season Length', 'min') |   ('Season Length', 'max') |   ('Season Length', 'std') |   ('Season Length', 'count') |   ('Snow cannons', 'mean') |   ('Snow cannons', 'median') |   ('Snow cannons', 'min') |   ('Snow cannons', 'max') |   ('Snow cannons', 'std') |   ('Snow cannons', 'count') |
|----------:|-------------------------:|---------------------------:|--------------------------:|--------------------------:|--------------------------:|----------------------------:|----------------------------:|------------------------------:|---------------------------:|---------------------------:|---------------------------:|-----------------------------:|---------------------------:|-----------------------------:|--------------------------:|--------------------------:|--------------------------:|----------------------------:|
|         0 |                    65.81 |                      66.04 |                     25.87 |                     89.67 |                     13.79 |                          54 |                      217.52 |                           182 |                        181 |                        365 |                      54.91 |                           54 |                     132.17 |                          9   |                         0 |                      1060 |                    242.62 |                          54 |
|         1 |                    61.06 |                      60.60 |                     43.08 |                     92.31 |                      8.81 |                         325 |                      124.06 |                           121 |                         30 |                        151 |                      23.54 |                          325 |                     100.82 |                         10   |                         0 |                       747 |                    170.04 |                         325 |
|         2 |                    23.90 |                      26.06 |                      0.79 |                     42.68 |                     13.93 |                          62 |                      121.47 |                           121 |                         30 |                        181 |                      30.15 |                           62 |                     134.03 |                         60.5 |                         0 |                       793 |                    182.26 |                          62 |
|         3 |                    59.21 |                      61.32 |                     34.16 |                     74.28 |                      8.37 |                          30 |                      148.03 |                           151 |                        121 |                        182 |                      25.39 |                           30 |                    1358.87 |                       1074   |                       750 |                      2383 |                    577.96 |                          30 |


Klaster 3 to największe ośrodki z najdłuższymi trasami i bardzo dużą liczbą armatek śnieżnych, co sugeruje wysoką komercjalizację i nowoczesność.

Klaster 0 oferuje długi sezon z umiarkowaną długością tras, co czyni go dobrym wyborem dla średniej wielkości ośrodków.

Klaster 1 to najliczniejszy zbiór ośrodków z przeciętnymi trasami i średnią liczbą armatek, raczej dla ośrodków o umiarkowanych warunkach śniegowych.

Klaster 2 to najmniejsze ośrodki z krótkimi trasami i najmniejszą ilością śniegu – są silnie uzależnione od sztucznego naśnieżania.

# Analiza klastrów w podziale na różne konfiguracje

## Podział 1

| Cluster | Liczność | Average Snow (mean ± std) | Season Length (mean ± std) | Snow Cannons (mean ± std) | Opis |
|---------|---------|--------------------------|----------------------------|--------------------------|------|
| 0       | 52      | 20.30 ± 12.45              | 129.73 ± 30.12               | 125.67 ± 191.23            | Najmniejsza średnia opadów śniegu |
| 1       | 259     | 58.24 ± 8.42               | 115.20 ± 22.30               | 100.65 ± 156.84            | Średnie wartości |
| 2       | 36      | 59.08 ± 7.82               | 160.44 ± 58.14               | 1277.08 ± 560.84           | Najwięcej armat śnieżnych |
| 3       | 124     | 67.65 ± 10.57              | 174.81 ± 42.37               | 83.87 ± 148.33             | Najwyższa średnia opadów śniegu |

## Podział 2

| Cluster | Liczność | Average Snow (mean ± std) | Season Length (mean ± std) | Snow Cannons (mean ± std) | Opis |
|---------|---------|--------------------------|----------------------------|--------------------------|------|
| 0       | 53      | 20.62 ± 12.55              | 131.28 ± 31.90               | 124.62 ± 189.54            | Najmniejsza średnia opadów śniegu |
| 1       | 240     | 57.88 ± 8.05               | 113.25 ± 21.63               | 101.56 ± 153.38            | Średnie wartości |
| 2       | 34      | 59.92 ± 8.57               | 144.85 ± 25.39               | 1285.97 ± 578.47           | Duża liczba armat śnieżnych |
| 3       | 130     | 67.16 ± 10.78              | 160.35 ± 20.60               | 77.41 ± 148.43             | Wysokie opady śniegu |
| 4       | 14      | 64.45 ± 7.86               | 294.93 ± 53.02               | 300.93 ± 393.27            | Najdłuższy sezon |

## Podział 3

| Cluster | Liczność | Average Snow (mean ± std) | Season Length (mean ± std) | Snow Cannons (mean ± std) | Opis |
|---------|---------|--------------------------|----------------------------|--------------------------|------|
| 0       | 53      | 20.62 ± 12.55              | 131.28 ± 31.90               | 124.62 ± 189.54            | Najmniejsza średnia opadów śniegu |
| 1       | 232     | 58.11 ± 8.21               | 112.85 ± 21.81               | 80.33 ± 118.74             | Niska liczba armat śnieżnych |
| 2       | 43      | 58.96 ± 8.51               | 135.67 ± 19.00               | 883.02 ± 330.97            | Duża liczba armat śnieżnych |
| 3       | 123     | 67.28 ± 10.96              | 161.37 ± 20.47               | 58.99 ± 114.69             | Wysokie opady śniegu |
| 4       | 14      | 64.45 ± 7.86               | 294.93 ± 53.02               | 300.93 ± 393.27            | Najdłuższy sezon |
| 5       | 6       | 61.10 ± 1.16               | 181.00 ± 0.00                | 2383.00 ± 0.00             | Stałe wartości dla sezonu i armat śnieżnych |

