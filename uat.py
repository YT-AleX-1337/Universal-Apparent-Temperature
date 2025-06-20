from math import exp

print('Universal Apparent Temperature')
print('Formula by AleX-1337\n')
print('Combines the Wind Chill formula with the heat factor of the Australian Apparent temperature\n\n')

T = min(max(int(float(input('Enter air temperature (°C): '))), -150), 80)           #Cap air temperature between -150°C and 80°C
H = min(max(int(float(input('Enter relative humidity (0% - 100%): '))), 0), 100)    #Cap relative humidity between 0% and 100%
W = min(max(int(float(input('Enter wind speed (km/h): '))), 0), 250)                #Cap wind speed between 0 km/h and 250 km/h

H_A = 0.061 * H * exp(17.27 * T / (237.7 + T))                                      #Calculate water vapor pressure (absolute humidity)
W_C = 13.12 - 0.3785 * T - 11.37 * (W + 1) ** 0.16 + 0.3965 * T * (W + 1) ** 0.16   #Calculate wind effect

T_A = int(T + W_C + 0.33 * H_A)

print(f'Feels like {T_A}°C')
