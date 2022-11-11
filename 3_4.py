# excersixe 3.4 
import pyvisa
import matplotlib.pyplot as plt

# rm = pyvisa.ResourceManager("@py")
# ports = rm.list_resources()
# print(ports)
# device = rm.open_resource(
# "ASRL4::INSTR", read_termination="\r\n", write_termination="\n"
# )
# print(device.query("*IDN?"))

# gives defenition list_devices and the class arduinoVISADevice
from arduino_device import ArduinoVISADevice, list_devices

# # vraagt poort aan
# def list_devices():
#     rm = pyvisa.ResourceManager("@py")
#     ports = rm.list_resources()
#     print(ports)
#     return ports

# class ArduinoVISADevice:

#     # define device
#     def __init__(self, port):
#         rm = pyvisa.ResourceManager("@py")
#         self.device = rm.open_resource(port, read_termination = "\r\n", write_termination="\n")
#         return
    
#     def get_identification(self):
#         return self.device.query("*IDN?")

#     def set_output_value(self,value):
#         return self.device.query(f"OUT:CH0 {value}")

#     def get_output_value(self):
#         return self.device.query(f"OUT:CH0?")

#     def get_input_value(self, channel): 
#         return self.device.query(f"MEAS:CH{channel}?")

#     def get_input_voltage(self, channel): 
#         return (float(self.device.query(f"MEAS:CH{channel}?"))) *(3.3 / (1023))


# make a fuction to get a listsv of ports : _buiten_ de class
print(list_devices())

# de poort moet je mogelijk zelf aanpassen
port = "ASRL5::INSTR"

# zorg dat de device al geopend wordt in de __init__()
device = ArduinoVISADevice(port=port)

# print identification string
print(device.get_identification())

# set OUTPUT voltage on channel 0, using ADC values (0 - 1023)
print(device.set_output_value(value=512))

# get the previously set OUTPUT voltage in ADC values (0 - 1023)
ch0_value = device.get_output_value()
print(ch0_value)

# measure the voltage on INPUT channel 2 in ADC values (0 - 1023)
ch2_value = device.get_input_value(channel = 2)
print(ch2_value)

# measure the voltage on INPUT channel 2 in volts (0 - 3.3 V)
ch2_voltage = device.get_input_voltage(channel=2)
print(ch2_voltage)

# # oude code 
# # The list for the voltages in the stroomkring with unit Volt
# voltages_U0 = []
# voltages_U1 = []
# voltages_U2 = []
# voltages_Uled = [] 
# current_led = []

# # output of chanel 0
# for i in range(0, 1023): 

#     # ADC_0 = (device.query(f"OUT:CH0 {i}"))
#     ADC_0 = device.set_output_value(i)
#     U_0 = (int(ADC_0) * 3.3)/1023 
#     voltages_U0.append(U_0)

#     # measure voltages U_1
#     # ADC_1 = (device.query(f"MEAS:CH1?"))
#     ADC_1 = device.get_input_value(1)
#     U_1 = (int(ADC_1) * 3.3)/1023 
#     voltages_U1.append(U_1)

#     # measure voltages U_2
#     #ADC_2 = (device.query(f"MEAS:CH2?"))
#     ADC_2 = device.get_input_value(2)
#     U_2 = (int(ADC_2) * 3.3)/1023 
#     voltages_U2.append(U_2)

# # calculate voltages over the LED
# for U_1, U_2 in zip(voltages_U1, voltages_U2):
#     U_led = U_1 - U_2 
#     voltages_Uled.append(U_led)

# print(voltages_U0)
# print(voltages_U1)
# print(voltages_U2)
# print(voltages_Uled)

# # calculate current over the LED, the current over the LED is the same as over the resistance because they are in serie
# for Uled in voltages_Uled:
#     I_led = Uled / 220
#     current_led.append(I_led)

# # plot current LED against votage LED 
# plt.plot(current_led, voltages_Uled)
# plt.xlabel("current (A)")
# plt.ylabel("voltage (V)")

# # import csv 
# import csv

# header = ['U', 'I']

# with open('results.csv', 'w', encoding='UTF8', newline='') as csvfile:

#     # define header and the command 'writer' to write
#     writer = csv.writer(csvfile)
#     writer.writerow(header)
    
#     # make the rows
#     for i, j in zip(voltages_Uled, current_led):
#         writer.writerow([i, j])
        

