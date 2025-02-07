#LED Resistor Calculator
x=float(input("Enter Supply Voltage (V): "))
y = float(input("Enter LED Voltage (V): "))
z = float(input("Enter LED Current (A): "))
w = (x-y)/z
print("Required Resistor Value = ", w,"\u03A9")