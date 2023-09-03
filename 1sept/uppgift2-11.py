# Skriv ett program som beräknar hur många mil en bil har gått under det senaste året och bilens genomsnittliga bensinförbrukning per mil.
# När programmet körs ska det fråga efter dagens mätarställning, mätarställningen för ett år sedan och hur många liter bensin som har förbrukats under året.

import math

meterSettingsToday = float(input('Mätarställning idag? '))
meterSettingsOneYearAgo = float(input('Mätarställning ett år sen? '))
milesDriven = meterSettingsToday - meterSettingsOneYearAgo

print(f'Antal körda mil: {milesDriven: .0f}')

litersConsumed = float(input('Antal liter bensin förbrukat? '))
consumptionPerMile = litersConsumed / milesDriven

print(f'Förbrukning per mil: {consumptionPerMile: .2f}')
