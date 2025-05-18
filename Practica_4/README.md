
# Laboratorio de Comunicaciones
## Universidad Industrial de Santander

# Práctica 4

### Integrantes
- **Maria Fernanda Guerrero Santos** - 2202343
- **Michelle Garzón Campos** - 2202785

Escuela de Ingenierías Eléctrica, Electrónica y de Telecomunicaciones  
Universidad Industrial de Santander


---

## Declaración de Originalidad y Responsabilidad
Los autores de este informe certifican que el contenido aquí presentado es original y ha sido elaborado de manera independiente. Se han utilizado fuentes externas únicamente como referencia y han sido debidamente citadas.

Asimismo, los autores asumen plena responsabilidad por la información contenida en este documento. 

Uso de IA: Se utilizó ChatGPT para reformular secciones del texto y verificar gramática, pero el contenido técnico fue desarrollado íntegramente por los autores.

---
## Contenido

### Resumen
En la práctica realizada se midieron las modulaciones angulares de múltiples señales de FM y PM. Para la primera parte se estudiaron las principales características de las emisoras radiales, presentes en el espectro radioeléctrico en el intervalo de las frecuencias entre 88 y 108 MHz, y realizando las mediciones requeridas en el analizador de espectros. Para la segunda parte, se usa una señal modulada en frecuencia y se determina su ancho de banda en función del índice de modulación (en los casos de banda estrecha y banda ancha), y se calculan los coeficientes de Bessel teóricos para la modulación PM y se comparan con los valores prácticos. Se concluye que las señales pueden ser moduladas a través de diferentes métodos, cada uno con características especiales.

### Introducción
El proceso de modulación de una señal es fundamental para que pueda ser transmitida a través de un medio físico, por lo tanto, se vuelve fundamental comprender los fenómenos que lo afectan y qué se comportamiento debe esperarse del mismo. 
El uso de señales FM para la transmisión de las emisoras de radio sigue, incluso en el mundo actual, siendo una importante herramienta de comunicación entre las comunidades. Para garantizar la calidad del servicio y la seguridad de la información se presentan regulaciones en el espectro radioeléctrico nacional, que definen el espacio, la potencia y la identificación de cada emisor.
Por otro lado, la modulación de fase, aunque similar a la modulación FM, tiene menos aplicaciones prácticas debido a que requiere equipos de recepción más complejos, aunque se también se usa para radiodifusión y comunicaciones digitales. Esto implica que es necesario conocer la forma de manejar estas modulaciones y entender sus principales características.


### Procedimiento

Para el primer caso analizado, el de las señales FM, a través del comportamiento en frecuencia se puede ver la información enviada en la banda base de la señal. Esto se logra usando el código del modulador FM de GNU radio, y analizando el comportamiento en el dominio de la frecuencia de ciertas estaciones de radio ya establecidas. 
 Luego, al modificar el intervalo de frecuencias observado, se busca obtener otro tipo de señales y observar también esta información. Esto se hace modificando el intervalo de frecuencias que se tenía de forma inicial, para que muestre un rango más amplio, y tomando nota de las señales que se pudieron observar, además de las frecuencias en las que se encontraban, usando las regulaciones para saber el tipo de señal captada.
Finalmente se compara lo obtenido con la respuesta que se observa en el analizador de espectros y los resultados de la Radio Definida por Software y el Analizador de espectro. Se usa como parámetro las funciones que tienen un menor ancho de banda, mientras cumplieran con los requisitos de potencia requeridos.

Para la segunda parte, se analizan señales con dos casos de modulación angular: modulación de banda estrecha y modulación de banda ancha. Para esto se observa el comportamiento en el osciloscopio a medida que se varía el valor de kp*Am, y se calcula la potencia de la señal, y el ancho de banda a través del analizador de espectros. 
Luego, se hallan y se comparan los valores de los coeficientes de Bessel teóricos con los encontrados en la práctica, para la modulación en PM. Con estos coeficientes se calcula la potencia de cada componente en frecuencia.
Para la segunda parte, se analizan señales con dos casos de modulación angular: modulación de banda estrecha y modulación de banda ancha. Para esto se observa el comportamiento en el osciloscopio a medida que se varía el valor de kp*Am, y se calcula la potencia de la señal, y el ancho de banda a través del analizador de espectros. 
Luego, se hallan y se comparan los valores de los coeficientes de Bessel teóricos con los encontrados en la práctica, para la modulación en PM. Con estos coeficientes se calcula la potencia de cada componente en frecuencia.

### Conclusiones

-	Las emisoras de radio cumplen con los requisitos impuestos por la ANE, y que muchas transmiten información adicional para garantizar una mejor calidad en el servicio.
-	Aunque todas las emisoras tienen una respuesta en el dominio de la frecuencia, algunas no poseen la suficiente potencia como para cumplir con los parámetros esperados.
-	La respuesta de la modulación de banda ancha es más fácil de apreciar a simple vista, aunque las amplitudes en voltaje se mantengan iguales.



Volver al [INICIO](#laboratorio-de-comunicaciones)
