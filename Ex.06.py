# Outdoor events

""" temp = 20
is_raining = True

if temp > 35 or temp < 0 or is_raining:
    print("The outdoor event is canceled")
else:
    print("The outdoor event is still scheduled") """

temp = 41
is_sunny = False

if temp >= 28 and is_sunny:
    print("It is HOT 🥵 and SUNNY ☀️ outside")
elif temp <= 0 and is_sunny:
    print("It is COLD 🥶 and SUNNY️️ ☀️ outside ")
elif 28 > temp > 0 and is_sunny:
    print("It is WARM 😊 and SUNNY️️ ☀️ outside ")
elif temp >= 28 and not is_sunny:
    print("It is HOT 🥵 and CLOUDY ☁️ outside")
elif temp <= 0 and not is_sunny:
    print("It is COLD 🥶 and CLOUDY ☁️ outside ")
elif 28 > temp > 0 and not is_sunny:
    print("It is WARM 😊 and CLOUDY ☁️ outside ")