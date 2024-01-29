# Documentación: `lib.core.sensors`

## `lib.core.sensors.ColorSensor`
### `ColorSensor.TCS3200`
`TCS3200` es una clase que tiene las funciones necesarias para interactuar de manera sencilla con el sensor de color [TCS3200](https://www.mouser.com/catalog/specsheets/tcs3200-e11.pdf).

**Ejemplo:**
```python
import RPi.GPIO as GPIO
from lib.core.sensors.ColorSensor import TCS3200

pines = {
	# ... los pines ...
}

sensor = TCS3200(GPIO, pines, 10, 0.1)
```

#### Parámetros:
| Nombre | Descripción | Tipo |
|:------:|:-----------:|:----:|
| `gpio` | se debe pasar `RPi.GPIO` como argumento. | `-` |
| `pins` | un diccionario con el nombre del pin físico (*key*) y el número de pin (*value*). | `dict` |
| `ncycles` | número de ciclos en cada lectura | `int` |
| `delay` | cantidad de tiempo de receso entre cada lectura | `float` |

**Ejemplo de `pins`**:
```python
pines_de_un_sensor = {
	"S2": 17,
	"S3": 27,
	"OUT": 22,
}
```

#### Métodos
| Nombre | Descripción | Argumentos | Tipo de salida |
|:------:|:-----------:|:----------:|:--------------:|
| `read_once` | Configura los pines (*S2*, *S3*) y realiza una lectura. | `color: tuple` | `float` |
| `get_rgb` | Realiza una lectura por cada configuración. | - | `tuple` |
| `color` | Realiza una lectura con `get_rgb` y devuelve el nombre del color dominante. | `make_new_read: bool (default False)` | `str` |

**Ejemplo de `read_once`:**
```python
lectura = sensor.read_once((0, 1)) # S2: LOW, S3: HIGH; para leer AZUL

print(f"Lectura para AZUL: {lectura}")
```

**Ejemplo de `get_rgb`:**
```python
tres_lecturas = sensor.get_rgb()

print(f"Lecturas para ROJO, VERDE Y AZUL: {tres_lecturas}")
```

**Ejemplo de `color`:**
```python
color_detectado = sensor.color()

print(color_detectado)
```