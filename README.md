# RoboCupJunior 2024 (Crusaders Team)

![GitHub Actions Workflow Status](https://img.shields.io/github/actions/workflow/status/danielmoraless/rcj2024/rpi-workflow.yml)

---

## Requerimientos
* Python (>=3.11.4)

## Arquitectura de software
Encuentra la documentación sobre la arquitectura de software implementada, [aquí](./docs/arch.md).

## Tabla de conexiones

### TCS3200 N.° 1 (L)

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

### TCS3200 N.° 2 (R)

| TCS3200 | RPi (BOARD) |
|:-------:|:-----------:|
| OUT | 36 (GPIO 16) |
| S2 | 38 (GPIO 20) |
| S3 | 40 (GPIO 21) |

### Controlador L298N
| L298N | RPi 4 (BOARD) |
|:-----:|:-------------:|
| ENA | 33 (GPIO 13, PWM1) |
| IN1 | 8 (GPIO 14) |
| IN2 | 10 (GPIO 15) |
| ENB | 32 (GPIO 12, PWM0) |
| IN3 | 12 (GPIO 18) |
| IN4 | 16 (GPIO 23) |

### IR SENSORS
- L: 37 (GPIO 26)
- R: 35 (GPIO 19)