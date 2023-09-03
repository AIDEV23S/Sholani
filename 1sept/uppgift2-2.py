# Skriv ett program som beräknar volymne och arean av en sfär. som indata ges sfärens radie.

import math

r = float(input('Vad är sfärens radie? '))

sphereVolume = (4/3) * math.pi * r**3

sphereArea = 4 * math.pi * r**2

print(f'Volume: {sphereVolume: .2f}')
print(f'Area: {sphereArea: .2f}')
