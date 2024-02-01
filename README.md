# RoboCupJunior 2024 (Crusaders Team)

## Requerimientos
* Los requerimientos de [ImageAI](https://imageai.readthedocs.io/en/latest/).
* Python (>=3.11.4)

## Tabla de conexiones

### TCS3200 N.° 1

| TCS3200 | RPi 4 (BOARD) |
|:-------:|:-------------:|
|   VCC   |    2 (5V)     |
|   GND   |    6 (GND)    |
|    OE   |    6 (GND)    |
|    S0   |    6 (GND)    |
|    S1   |     2 (5V)    |
|    S2   |  11 (GPIO 17) |
|    S3   |  13 (GPIO 27) |
|   OUT   |  15 (GPIO 22) |

### Controlador L298N
| L298N | RPi 4 (BOARD) |
|:-----:|:-------------:|
| IN1 | 8 (GPIO 14) |
| IN2 | 10 (GPIO 15) |
| IN3 | 12 (GPIO 18) |
| IN4 | 16 (GPIO 23) |