# Laboratorio de Comunicaciones
## Universidad Industrial de Santander

# Práctica 1: TÍTULO PRÁCTICA

### Integrantes
- **PRIMER INTEGRANTE** - Código
- **SEGUNDO INTEGRANTE** - Código

Escuela de Ingenierías Eléctrica, Electrónica y de Telecomunicaciones  
Universidad Industrial de Santander

### Fecha
31 de diciembre de 2030

---

## Declaración de Originalidad y Responsabilidad
Los autores de este informe certifican que el contenido aquí presentado es original y ha sido elaborado de manera independiente. Se han utilizado fuentes externas únicamente como referencia y han sido debidamente citadas.

Asimismo, los autores asumen plena responsabilidad por la información contenida en este documento. 

Uso de IA: Se utilizó ChatGPT para reformular secciones del texto y verificar gramática, pero el contenido técnico fue desarrollado íntegramente por los autores.

---
## Contenido

### Resumen
En esta práctica, en la primera parte se hizo una introducción con el programa GNU radio, en la cual se generaron diferentes señales donde se variaron sus características principales, como offset, frecuencia y amplitud. Esta práctica logró un primer acercamiento con el comportamiento de las señales y cómo modificarlas según sea necesario. En su segunda parte, se hizo un reconocimiento de los equipos, como el osciloscopio, el SDR y el analizador de espectros, donde se logró tener un primer acercamiento al comportamiento de estos instrumentos y la forma de medir con los mismos ciertos parámetros como la ganancia. Para la tercera parte, se usan nuevos equipos, se revisa su configuración y especificaciones técnicas para trabajarlos con señales generadas en GNU radio, para lograr un análisis del comportamiento de las ondas en tiempo y frecuencia. Finalmente, se usa el USRP 2920 para transmitir señales y medir algunos datos como ancho de banda y potencia.
**Palabras clave:** de 2 a 5 palabras clave. 

### Introducción
El laboratorio de comunicaciones requiere conocimientos en diferentes programas e instrumentos, si se quiere tener un correcto uso y medición de las condiciones de las señales de entrada y salida. Esta primera práctica tiene como objetivo hacer una primera introducción a los principales instrumentos y software requeridos en el futuro desarrollo de las demás prácticas. Se dividió en tres partes: en la primera, se hizo un reconocimiento del software GNU radio, que permite controlar las señales generadas. En la segunda parte, se hicieron unas primeras mediciones con la ayuda del osciloscopio, el analizador de espectros y el SDR. En la última parte, se hizo una revisión de las especificaciones técnicas de los diferentes instrumentos, y se usó el USRP 2920 para transmitir señales. Todo esto permite un mayor conocimiento sobre el funcionamiento de los diferentes implementos y la práctica de las mediciones en condiciones más cercanas a las reales.


### Procedimiento
En la primera parte, se hizo una práctica con GNU radio, donde se generaron bloques de señales fuente, cuyos parámetros son controlados por variables generadas por el mismo usuario, que pueden ser modificados, además de realizar diferentes interconexiones que alteran su comportamiento, y finalmente comparando los efectos de onda al variar la relación samp_rate/freq. Se obtuvieron los resultados esperados al comparar con la señal objetivo. En la segunda práctica, además del programa usado anteriormente, se usó el generador de señales SDR conectado al osciloscopio, con el objetivo de medir la ganancia que se presentaba entre la señal de entrada y de la salida, donde se obtuvieron algunas variaciones respecto a los resultados deseados, probablemente debido a distorsiones en la señal del cable o en los instrumentos usados. Luego, usando un analizador de espectros con un atenuador, se midió la ganancia variando los parámetros de frecuencia de operación y ganancia del transmisor, y finalmente se graficó la respuesta en frecuencia del cable, donde se observó un comportamiento decreciente a medida que aumenta la frecuencia.

### Conclusiones
Se sintetizan los principales aportes y puntos relevantes de la práctica, evitando repetir lo ya consignado en las otras secciones del informe. 

### Referencias
Ejemplo de referencia:

- [Proakis, 2014] J. Proakis, M. Salehi. Fundamentals of communication systems. 2 ed. England: Pearson Education Limited, 2014. p. 164-165, 346. Chapter 5 In: [Biblioteca UIS](https://uis.primo.exlibrisgroup.com/permalink/57UIDS_INST/63p0of/cdi_askewsholts_vlebooks_9781292015699)

---
# Ejemplos usando Markdown

Volver al [INICIO](#laboratorio-de-comunicaciones)

## Inclusión de Imágenes
### Imagen de referencia dentro del repositorio:
![Networking](my%20file/test.png)

### Imagen de fuente externa
![GNU Radio logo](https://kb.ettus.com/images/thumb/5/50/gnuradio.png/600px-gnuradio.png)

### Uso de html para cambiar escala de la imagen
<img src="https://kb.ettus.com/images/thumb/5/50/gnuradio.png/600px-gnuradio.png" alt="GNU Radio Logo" width="300">

## Creación de hipevínculos 
- [Aprende Markdown](https://markdown.es/)
- [Más acerca de Markdown](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)
- [Abrir documento en el repositorio](my%20file/test_file.txt). Si hay espacios en la ruta de su archivo, reemplácelos por `%20`.
- Ir a una sección de este documento. Por ejemplo: [Ir a Contenido](#contenido) Tenga en cuenta escribir el título de la sección en minúsculas y los espacios reemplazarlos por guiones.
## Uso de Expresiones Matemáticas
Se pueden incluir ecuaciones en el archivo `README.md` utilizando sintaxis similar a [LaTeX](https://manualdelatex.com/tutoriales/ecuaciones):

### Ecuaciones en Línea
```
La energía de una señal exponencial es $E = \int_0^\infty A^2 e^{-2t/\tau} dt$.
```
**Salida renderizada:**
La energía de una señal exponencial es $E = \int_0^\infty A^2 e^{-2t/\tau} dt$.

### Ecuaciones en Bloque
```
$$E = \int_0^\infty A^2 e^{-2t/\tau} dt = \frac{A^2 \tau}{2}$$
```
**Salida renderizada**
$$E = \int_0^\infty A^2 e^{-2t/\tau} dt = \frac{A^2 \tau}{2}$$

## Creación de Tablas

**Tabla 1.** Ejemplo de tabla en Markdown.

| Parámetro | Valor |
|-----------|-------|
| Frecuencia (Hz) | 1000 |
| Amplitud (V) | 5 |
| Ciclo útil (%) | 50 |

## Inclusión de código

```python
def hello_world():
    print("Hello, World!")
```

También es posible resaltar texto tipo código como `print("Hello, World!")`.

---

Volver al [INICIO](#laboratorio-de-comunicaciones)
