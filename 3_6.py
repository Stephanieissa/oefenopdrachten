import pyvisa
from arduino_device import ArduinoVISADevice, list_devices

from diode_experiment import DiodeExperiment

# class DiodeExperiment:

#     def __init__(self, port):
#         self.device = ArduinoVISADevice(port = port)
#         return

#     def scan(self, start, stop): 

#         # oude code 
#         # The list for the voltages in the stroomkring with unit Volt
#         voltages_U0 = []
#         voltages_U1 = []
#         voltages_U2 = []
#         voltages_Uled = [] 

#         for i in range(start, stop): 

#             # ADC_0 = (device.query(f"OUT:CH0 {i}"))
#             ADC_0 = self.device.set_output_value(i)
#             U_0 = (int(ADC_0) * 3.3)/1023 
#             voltages_U0.append(U_0)

#             # measure voltages U_1
#             # ADC_1 = (device.query(f"MEAS:CH1?"))
#             ADC_1 = self.device.get_input_value(1)
#             U_1 = (int(ADC_1) * 3.3)/1023 
#             voltages_U1.append(U_1)

#             # measure voltages U_2
#             #ADC_2 = (device.query(f"MEAS:CH2?"))
#             ADC_2 = self.device.get_input_value(2)
#             U_2 = (int(ADC_2) * 3.3)/1023 
#             voltages_U2.append(U_2)

#         # calculate voltages over the LED
#         for U_1, U_2 in zip(voltages_U1, voltages_U2):
#             U_led = U_1 - U_2 
#             voltages_Uled.append(U_led)

#         return print(voltages_U0), print(voltages_U1), print(voltages_U2), print(voltages_Uled)

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
