
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

## 4A

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

## 4B

### Introducción:
En esta práctica, se estudió la modulación de fase (PM) bajo diferentes valores de kpAm, con el objetivo de observar cómo la variabilidad de este parámetro afecta la señal modulada en el dominio del tiempo y la frecuencia. Se trabajaron dos casos: modulación de fase de banda estrecha y modulación de fase de banda ancha. En el primer punto, se realizaron mediciones con valores de kpAm de menor a mayor, incluyendo valores de kpAm = 0.095, kpAm = 0.8 y kpAm = 600, para observar cómo cambia la modulación a medida que kpAm aumenta. En el segundo punto, se utilizó un rango de valores de kpAm = 3, kpAm = 5 y kpAm = 15, y se realizaron mediciones de potencia en los armónicos, convertidos de dBm a mW, para luego calcular los coeficientes de Bessel teóricos y prácticos.

### Resumen:
La práctica se dividió en dos partes. En el primer punto, se midieron las señales moduladas para tres valores diferentes de kpAm: 0.095, 0.8 y 600, lo que permitió observar el cambio en la modulación de fase de banda estrecha a medida que aumentaba kpAm. En el segundo punto, se trabajó con valores de kpAm = 3, kpAm = 5 y kpAm = 15, lo que generó una modulación de fase de banda ancha. En ambos casos, se calcularon los coeficientes de Bessel teóricos y prácticos, y se compararon los resultados experimentales con los valores teóricos.

### Procedimiento del Primer Punto: Modulación Angular de Banda Estrecha
1. Configuración Inicial:
   - Se configuró el sistema de modulación de fase comenzando con kpAm = 0.095 (valor bajo), luego con kpAm = 0.8 (valor intermedio) y finalmente con kpAm = 600 (valor alto). Este enfoque permitió observar cómo la señal modulada cambia a medida que el valor de kpAm aumenta.

2. Observación en el Osciloscopio:
   - La señal coseno fue conectada al modulador y se observó la señal modulada en el dominio del tiempo mediante un osciloscopio. Se monitorearon las características de la señal, tales como la amplitud, frecuencia y forma de onda.

3. Cálculo de Potencia:
   - Para cada valor de kpAm, se calculó la potencia de la envolvente compleja de la señal modulada utilizando la fórmula:
   Potencia = (Vmax)^2 / 2.

| $kpA_m$ | Potencia (W) |
| ------- | ------------ |
| 0.8     | 0.005408 W   |
| 0.095   | 0.005408 W   |
| 200     | 0.00239508 W |
| 600     | 0.00239508 W |


4. Análisis en el Analizador de Espectros:
   - La señal modulada fue observada en el dominio de frecuencia mediante un analizador de espectros, donde se evaluó la dispersión espectral y se estimó la potencia de la señal modulada.

5. Repetición para los distintos valores de kpAm:
   - Se repitió el proceso para kpAm = 0.8 y kpAm = 600, observando las diferencias en el comportamiento de la señal modulada a medida que el valor de kpAm aumentaba.

### Procedimiento del Segundo Punto: Modulación Angular de Banda Ancha
1. Configuración Inicial:
   - Se configuró el sistema de modulación de fase con tres valores de kpAm = 3, kpAm = 5 y kpAm = 15, lo que representa una modulación de fase de banda ancha.

2. Observación en el Osciloscopio:
   - La señal coseno fue conectada al sistema y se observó la señal modulada en el dominio del tiempo. Se observó una señal más compleja y dispersa debido a la modulación de fase de banda ancha.

3. Medición de Potencia en los Componentes Armónicos:
   - Se utilizó una tabla para registrar la potencia de cada armónico, medida en dBm.
  
4. Cálculo de los Coeficientes de Bessel:
   - A partir de los valores de potencia obtenidos en mW para cada armónico, se calcularon los coeficientes de Bessel teóricos y prácticos. Los coeficientes de Bessel fueron comparados entre los resultados experimentales y los valores teóricos. Se mostró la comparación de los coeficientes de Bessel para diferentes valores de β (como β = 3, β = 5 y β = 15).

Conclusiones:
1. Comportamiento de la Señal:
   - En el primer punto, con kpAm = 0.095, kpAm = 0.8 y kpAm = 600, se observó una transición desde una modulación de fase de banda estrecha hasta una señal más compleja con mayor dispersión espectral a medida que kpAm aumentaba. En el segundo punto, con kpAm = 3, kpAm = 5 y kpAm = 15, la señal modulada mostró una mayor dispersión espectral, lo que corresponde a una modulación de fase de banda ancha.

2. Coeficientes de Bessel:
   - Los coeficientes de Bessel obtenidos experimentalmente se compararon con los coeficientes teóricos, mostrando una buena concordancia, aunque con algunas pequeñas variaciones. Estas diferencias se atribuyen a las condiciones experimentales.

| Coeficiente de Bessel | β = 3 Teórico | β = 3 Práctico | β = 5 Teórico | β = 5 Práctico | β = 15 Teórico | β = 15 Práctico |
|-----------------------|---------------|----------------|---------------|----------------|----------------|-----------------|
| J0(B)                 | 2.59E-01      | 0.260052       | 1.75E-01      | 0.1775968      | 1.45E-02       | 0.0142245       |
| J1(B)                 | 3.39E-01      | 0.339059       | 3.28E-01      | 0.3275791      | 2.06E-01       | 0.2051039       |
| j2(B)                 | 4.85E-01      | 0.4860913      | 4.67E-02      | 0.0465651      | 4.19E-02       | 0.0415717       |
| j3(B)                 | 3.10E-01      | 0.3090629      | 3.65E-01      | 0.3648312      | 2.06E-01       | 0.1940181       |
| j4(B)                 | 1.32E-01      | 0.1320342      | 3.90E-01      | 0.3912324      | 1.19E-01       | 0.1191789       |
| j5(B)                 | 4.35E-02      | 0.0430284      | 2.63E-01      | 0.2611405      | 1.31E-01       | 0.130456        |
| j6(B)                 | 1.16E-02      | 0.0113939      | 1.31E-01      | 0.1310487      | 2.04E-01       | 0.2061496       |
| j7(B)                 | 2.81E-03      | 0.0025473      | 5.40E-02      | 0.0533764      | 3.48E-02       | 0.0344636       |
| j8(B)                 | 8.23E-04      | 0.0004934      | 1.89E-02      | 0.0184052      | 1.73E-01       | 0.1739835       |
| J9(B)                 | -             | -              | -             | -              | 2.19E-01       | 0.220046        |
| J10(B)                | -             | -              | -             | -              | 8.97E-02       | 0.0900717       |
| J11(B)                | -             | -              | -             | -              | 9.98E-02       | 0.0999504       |
| J12(B)                | -             | -              | -             | -              | 2.35E-01       | 0.2366656       |
| J13(B)                | -             | -              | -             | -              | 2.78E-01       | 0.2787146       |
| J14(B)                | -             | -              | -             | -              | 2.45E-01       | 0.2464397       |
| J15(B)                | -             | -              | -             | -              | 1.81E-01       | 0.1813063       |
| J16(B)                | -             | -              | -             | -              | 1.16E-01       | 0.1161727       |
| J16(B)                | -             | -              | -             | -              | 6.66E-02       | 0.0665289       |
| **Potencia Total**    | **0.0135114** | **[mW]** | **0.0132887** | **[mW]** | **0.0133568** | **[mW]** |



En resumen, la práctica proporcionó una comprensión detallada de cómo el valor de kpAm afecta la modulación de fase y cómo se puede medir y calcular la potencia y los coeficientes de Bessel para señales moduladas. Los resultados experimentales fueron consistentes con las expectativas teóricas.





Volver al [INICIO](#laboratorio-de-comunicaciones)
