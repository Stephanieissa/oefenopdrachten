import pyvisa
import time 
import matplotlib.pyplot as plt

minmum_value = 0
print(f"Hoi {minmum_value}!")

max = 1023
print(f"Hoi {max}!")

rm = pyvisa.ResourceManager("@py")
ports = rm.list_resources()
print(ports)
device = rm.open_resource(
"ASRL5::INSTR", read_termination="\r\n", write_termination="\n"
)
print(device.query("*IDN?"))

#for i in range (800, 999):
#   print(device.query(f"OUT:CH0 {i}"))

#    time.sleep(1)

#   print(device.query(f"OUT:CH0 0"))

#    time.sleep(1)

# The list for the voltages in the stroomkring with unit Volt
voltages_U0 = []
voltages_U1 = []
voltages_U2 = []
voltages_Uled = [] 
current_led = []

# output of chanel 0
for i in range(0, 1023): 

    ADC_0 = (device.query(f"OUT:CH0 {i}"))
    U_0 = (int(ADC_0) * 3.3)/1023 
    voltages_U0.append(U_0)

    # measure voltages U_1
    ADC_1 = (device.query(f"MEAS:CH1?"))
    U_1 = (int(ADC_1) * 3.3)/1023 
    voltages_U1.append(U_1)

    # measure voltages U_2
    ADC_2 = (device.query(f"MEAS:CH2?"))
    U_2 = (int(ADC_2) * 3.3)/1023 
    voltages_U2.append(U_2)

# calculate voltages over the LED
for U_1, U_2 in zip(voltages_U1, voltages_U2):
    U_led = U_1 - U_2 
    voltages_Uled.append(U_led)\

print(voltages_U0)
print(voltages_U1)
print(voltages_U2)
print(voltages_Uled)

# calculate current over the LED, the current over the LED is the same as over the resistance because they are in serie
for U2 in voltages_U2:
    I_led = U2 / 220
    current_led.append(I_led)

# plot current LED against votage LED 
plt.scatter(voltages_Uled, current_led)
plt.ylabel("current (A)")
plt.xlabel("voltage (V)")
plt.show()

# import csv 
import csv

header = ['U', 'I']

with open('results.csv', 'w', encoding='UTF8', newline='') as csvfile:

    # define header and the command 'writer' to write
    writer = csv.writer(csvfile)
    writer.writerow(header)
    
    # make the rows
    for i, j in zip(voltages_Uled, current_led):
        writer.writerow([i, j])
        

