# iot_tool.py
# Collaborative engineering automation and embedded systems computation toolkit
import math

def print_banner():
    print("==========================================================")
    print("=== IoT & Embedded Systems Engineering Toolkit v1.0   ===")
    print("==========================================================")


# ====================================================================
# DEVELOPER ZONE: STUDENTS MUST WRITE CODE EXCLUSIVELY INSIDE THEIR FUNCTION
# ====================================================================

def calculate_variant_1():
    print("\n[Variant 1: Servomotor Control Systems]")
    # DEVELOPER 1: Read theta and omega. Calculate t = theta / omega.
    # Perform bitwise AND between integer theta and 0xFF. Servomotor name, list of angles.
    pass


def calculate_variant_2():
    print("\n[Variant 2: Analog-to-Digital Conversion]")
    print("Пункт 1.1")

    ads = int(input("Введість 10-бітне значення ADC: "))
    vref = 5
    v = (ads/1023)* vref 
    pr = ads << 2
    print("Напруга: ", v)
    print("Значення АЦП з побітовим зсувом у двійковому форматі: ", bin(pr))

    print("Пункт 1.2")

    mark = input("Введіть маркування аналогового датчика: ")
    start = mark.startswith("SENSOR")
    print("Маркування починається з SENSOR:",start)
    print("Довжина рядка маркування:", len(mark))
    print("Перші 6 символів маркування:", mark[:6])

    print("Пункт 1.3")

    vol = [1, 2, 3, 4, 5]
    new =float(input("Введіть нове значення: "))
    vol[0] = new
    vol.pop()
    print("Новий список напруг: ", vol)
    bs = (10, 20)
    print("Парамерти системи (незмінні роздільна здатність та частота): ", bs)

    print("Пункт 1.4")

    pin = int(input("Введіть пін: "))
    voltage = float(input("Введіть напругу: "))

    spisok = {
        "pin": pin,
        "voltage": voltage,
        "status_flags": ["OK", "OVERHEAT","OK"]
    }
    print(spisok)

    un = set(spisok["status_flags"])
    print("Множина унікальних прапорів: ", un)

    ch = ("CRITICAL" not in un) and (spisok["voltage"] < 4.5)
    print("Наявність CRITICAL та напруги менше за 4.5", ch)
    pass


def calculate_variant_3():
    print("\n[Variant 3: Battery Pack Monitoring]")
    # DEVELOPER 3: Read capacity E and power P. Calculate t = E / P.
    # Perform bitwise OR between integer E and P. Reverse LiFePO4 string, cell voltages.
    pass


def calculate_variant_4():
    # № 1
    # Input of the force and area
    print("Введіть прикладену силу(Н): ")
    F = int(input())
    print("Введіть площу(мм^2): ")
    A = int(input())
    # Calculation of mechanical stress and binary shift for the force
    stress = F / A
    shift = bin(F >> 1)
    # Output of results
    print("Механічна напруга: ", stress, "МПа")
    print("Побітовий зсув: ", shift)
    print("\n[Variant 4: Stress and Strain Calculation]")
    # DEVELOPER 4: Read force F and area A. Mechanical stress sigma = F / A.
    # Apply bitwise right shift F >> 1. Material grade string and component strains.
    pass


def calculate_variant_5():
    print("\n[Variant 5: Unmanned Aerial Vehicle Telemetry]")
    # DEVELOPER 5: Read altitude H and vertical speed Vz. Calculate t = H / Vz.
    # Perform bitwise XOR between H and Vz. Validate $GPGGA telemetry string, active sensors.
    pass


def calculate_variant_6():
    print("\n[Variant 6: Digital Communication Protocols]")
    # DEVELOPER 6: Read I2C bus frequency in kHz (F). Period T = 1000000 / (F * 1000).
    # Perform bitwise AND between frequency and 0x0F. USART_BAUDRATE string, rx buffer.
    #1.1
    F = float(input('введіть частоту шини І2С в кГц:  '))
    F_2 = F * 1000 #переводимо в Гц
    T = 10 ** 6 / F_2 # Обчислюємо період за формулою з умови
    result = int(F_2) & 0x0F # Виконуємо побітове AND
    print(f'Результат операції AND:{result}')
    print(f'Період:{T}') #Виводимо результати користувачеві


    #1.2
    name = input('Введіть назву інтерфейсу, наприклад "USART_BAUDRATE_115200":')
    length = len(name) #Рахуємо кількість знаків в назві
    end_1 = name.endswith('115200') #
    a = name[:5] # Беремо з першого по 5 елемент
    print(f"\nЧи закінчується на '115200': {end_1}")
    print(f'Кількість символів у назві інтерфейсу: {length}')
    print(f'Перші 5 символів назви:{a}') #Друкуємо результати


    #1.3
    my_list = [0xAA, 0x01, 0x02, 0xFF]
    my_list[1] = 0x03 #Замінюємо другий (0х01) елемент
    my_list.append(0x00) #Додаємо стоповий байт
    UART = 'baudrate', 'databits', 'parity', 'stopbits', #Створюємо кортеж
    print(f'\nЗмінений список:{my_list}')
    print(f'Кортеж:{UART}') # Друкуємо результати


    #1.4
    D = { 'device_address': 'xxx' ,'protocol': 'UART', 'supported_rates': [111200, 115200, 9600, 115200]}
    a = set(D['supported_rates']) #Створюємо множину значень ключа "supported_rates"
    check_1 = (115200 in a) and (D["protocol"] == "UART") #Перевіряємо умову із завдання
    print(f"\nМножина унікальних швидкостей: {a}") #
    print(f'Результат перевірки умови: "чи присутня швидкість 115200 у множині та чи "UART" є протоколом" : {check_1}') #Друкуємо результат
    print(f'Результат у двійковому форматі: {bin(int(T))}')
    


def calculate_variant_7():
    print("\n[Variant 7: Robot Kinematics Drive Calculation]")
    # DEVELOPER 7: Read gear ratio i and motor RPM Nin.
    # Output shaft Nout = Nin / i. Apply bitwise left shift Nin << 3. Manipulator link string.
    pass


def calculate_variant_8():
    print("\n[Variant 8: Hydraulics Parameter Control]")
    # DEVELOPER 8: Read pressure P and flow rate Q. Hydraulic power W = (P * Q) / 600.
    # Perform bitwise OR between integer P and Q. DTC diagnostic code, oil temperature list.
    pass


def calculate_variant_9():
    print("\n[Variant 9: Climate Control and Ventilation Systems]")
    # DEVELOPER 9: Read heater power (P) and runtime (t). Thermal energy Q = P * t.
    # Perform bitwise XOR between power and time. PLC_HVAC controller identifier string.
    pass


def calculate_variant_10():
    print("\n[Variant 10: Orientation and Navigation Systems (IMU)]")
    # DEVELOPER 10: Read Ax, Ay, Az. Total acceleration A = sqrt(Ax^2 + Ay^2 + Az^2).
    # Apply bitwise right shift Az >> 2. Raw data ACC:X=... string, Euler angles.
    pass


def calculate_variant_11():
    print("\n[Variant 11: BLDC Motor Control Systems]")
    # DEVELOPER 11: Read PWM duty cycle (DUTY) and supply voltage Vdc. Vphase = (DUTY/100)*Vdc.
    # Perform bitwise AND between integer DUTY and 0b11110000. Hall sensors state string.
    pass


def calculate_variant_12():
    print("\n[Variant 12: Optical Encoder Data Acquisition]")
    # DEVELOPER 12: Read PPR and total pulses N. Revolutions (N // PPR), remainder (N % PPR).
    # Apply bitwise left shift N << 1. ENC-OPT encoder serial number, measurement list.
    pass


def calculate_variant_13():
    print("\n[Variant 13: Industrial Modbus RTU Network]")
    # DEVELOPER 13: Read 16-bit Modbus register value R.
    # Split into High and Low bytes, print both in binary format.
    pass


# ====================================================================
# MAIN EXECUTION MODULE (TEAM LEAD UNCOMMENTS DURING INTEGRATION)
# ====================================================================
if __name__ == "__main__":
    print_banner()
    
    # calculate_variant_1()
    # calculate_variant_2()
    # calculate_variant_3()
    # calculate_variant_4()
    # calculate_variant_5()
    # calculate_variant_6()
    # calculate_variant_7()
    # calculate_variant_8()
    # calculate_variant_9()
    # calculate_variant_10()
    # calculate_variant_11()
    # calculate_variant_12()
    # calculate_variant_13()
