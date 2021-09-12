# Amar Nagim
# for loops
# Vanaf 30 terugtellen tot de raketlancering. Print elke tel en print de lancering.

import time

print(f'De raketlancering zal over 30 seconden plaatsvinden:')
time.sleep(1)

for lancering in range(29,-1,-1):
    print(lancering)
    time.sleep(1)
    if lancering == 0:
        print('Raket is gelanceert.')

        

 
