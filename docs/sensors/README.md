# Documentación: `lib.core.sensors`

## `lib.core.sensors.ColorSensor`
### `ColorSensor.TCS3200`
`TCS3200` es una clase que tiene las funciones necesarias para interactuar de manera sencilla con el sensor de color [TCS3200](https://www.mouser.com/catalog/specsheets/tcs3200-e11.pdf).

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