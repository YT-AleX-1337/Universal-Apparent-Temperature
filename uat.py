from math import exp

print('Universal Apparent Temperature')
print('Formula by AleX-1337\n')

T = min(max(int(float(input('Enter air temperature (°C): '))), -150), 75) #Cap air temperature between -150°C and 70°C
H = min(max(int(float(input('Enter relative humidity (0% - 100%): '))), 0), 100) #Cap relative humidity between 0% and 100%
W = min(max(int(float(input('Enter wind speed (km/h): '))), 0), 250) #Cap wind speed between 0 km/h and 250 km/h

H_A = 0.061 * H * exp(17.27 * T / (237.7 + T)) #Calculate water vapor pressure (absolute humidity)
h = 1 - 2 / (1 + exp(0.2 * T - 2)) #Calculate humidity factor: it should increase apparent temperature when it's hot but slightly decrease it when it's cold
T_WC = 13.12 - 0.379 * T - (11.37 - 0.397 * T) * (W + 1) ** 0.16 #Calculate wind effect (it lowers the apparent temperature when it's cold and slightly increase it when it's hot)
w = 1.2 / (1 + exp(0.1 * T + (W + 1) ** 0.16 - 4)) - 1 / (1 + exp(0.017 * T + 3)) - 0.2 #Calculate wind factor: the higher the temperature, the least effect wind has

T_A = round(T + 0.174 * h * H_A + w * T_WC) #Calculate Universal Apparent Temperature
print(f'Feels like {T_A}°C')
