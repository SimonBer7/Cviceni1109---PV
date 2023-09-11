raining_x_sunny = False
windy_x_clear = False
fog_x_clear = False

if not raining_x_sunny and not windy_x_clear:
    print("Je dobre pocasi, neni potreba destnik")
if (fog_x_clear or raining_x_sunny) and windy_x_clear:
    print("Vemte si s sebou destnik")
if windy_x_clear and raining_x_sunny:
    print("Vemte si s sebou cepici")
if windy_x_clear:
    print("Vmete si s sebou reflexni obleceni")
if raining_x_sunny and windy_x_clear and fog_x_clear:
    print("Nebezpecne pocasi !!!")
if not raining_x_sunny and not windy_x_clear and not fog_x_clear:
    print("Idealni pocasi :)")
