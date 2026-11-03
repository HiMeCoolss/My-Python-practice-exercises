def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius*(9/5)+32)
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit-32)*(5/9)
    return celsius

def temperature_report(city, morning_celsius, afternoon_celsius):
    difference = afternoon_celsius-morning_celsius
    morning_fahrenheit = celsius_to_fahrenheit(morning_celsius)
    afternoon_fahrenheit = celsius_to_fahrenheit(afternoon_celsius)
    report = "City: " + city
    report += "\nMorning: " + str((morning_celsius)) + " / " + str(round(morning_fahrenheit,1))
    report += "\nAfternoon: " + str(afternoon_celsius) + " / " + str(round(afternoon_fahrenheit,1))
    report += "\nTemperature increase: " + str(round(difference,1))
    return report

a = temperature_report("Hanoi", 21, 28)
print(a)

#OR:

print(temperature_report("Hanoi, 21, 28))
