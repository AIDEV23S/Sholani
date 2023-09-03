# I USA brukar en bils bensinförbrukning anges i miles/gallon. 
# Skriv ett program som läser in en bensinförbrukning som är angiven på detta sätt och översätter den till det för oss vanligare liter/mil.
# Följande gäller 1 mile = 1.609 km och 1 gallon = 3.785 liter

milesPerGallon = float(input('Ange bensinförbrukning i miles/gallon: '))

milesToKm = 1.609
literPerGallon = 3.785
swedishMile = 10

literPerMile = (milesPerGallon * literPerGallon) / (milesToKm * 10)

print(f'{milesPerGallon} miles/gallon = {literPerMile: .3f} liter/mil')