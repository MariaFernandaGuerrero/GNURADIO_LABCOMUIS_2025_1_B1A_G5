# Laboratorio de Comunicaciones
## Universidad Industrial de Santander

# Práctica 5

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

## Introducción
En esta práctica, se explora el funcionamiento de dos tipos de cuantización: cuantización uniforme y cuantización Ley A, con el objetivo de entender cómo estos métodos afectan la calidad de la señal digitalizada y el ruido asociado. La cuantización uniforme distribuye de manera equitativa los niveles de cuantización a lo largo de toda la señal, mientras que la Ley A aplica una compresión logarítmica para mejorar la resolución en las señales de baja amplitud, donde el oído humano es más sensible.

## Resumen
A través de la simulación en GNU Radio, se observó cómo la cuantización influye en la señal procesada, especialmente en cuanto a la calidad de la señal y la relación señal-ruido. En la práctica, se compararon los efectos de la cuantización uniforme con la Ley A, incluyendo la influencia de la constante A, el ancho de banda del filtro pasabajas, y la adición de ruido gaussiano. Además, se abordó cómo estos parámetros pueden ser ajustados para optimizar la resolución y minimizar el ruido de cuantización.

## Procedimiento
### Cuantización Uniforme:

Se implementó un cuantizador uniforme en GNU Radio utilizando bloques como Signal Source, Throttle, Noise Source, y Low Pass Filter.

Se analizó el histograma de la señal y su respuesta frente a la adición de ruido gaussiano y la variación en el ancho de banda del filtro pasabajas.

¿Cómo afecta la resolución del cuantizador o la calidad de la señal después de la cuantización?

- La resolución afecta directamente la calidad de la señal. Aumentar la resolución de la cuantización mejora la calidad de la señal, ya que se reduce el error de cuantización, especialmente en las áreas críticas de la señal.

¿Qué impacto tiene el ruido de cuantización en la señal procesada y cómo se puede minimizar?

- El ruido de cuantización causa distorsión en la señal y reduce su calidad. Se puede minimizar aumentando el número de bits en el proceso de cuantización, lo que mejora la resolución de los niveles y reduce el ruido.

¿Cómo influye el ancho de banda del filtro pasabajas en la calidad de la señal después de la cuantización?

- El ancho de banda del filtro pasabajas afecta la cantidad de información transmitida. Un filtro con un ancho de banda más pequeño limita la información y reduce la calidad de la señal cuantizada, mientras que un filtro con mayor ancho de banda preserva mejor la forma de la señal.

¿Qué impacto tiene la adición de ruido gaussiano en la señal procesada con cuantización Ley A?

- El ruido gaussiano distorsiona la señal, pero al priorizar las amplitudes más bajas, la Ley A ayuda a reducir la percepción del ruido en esas regiones. Esto mejora la calidad de la señal, especialmente en los rangos de baja amplitud.

¿Cómo se puede optimizar la cuantización Ley A para mejorar la relación señal-ruido en sistemas de procesamiento digital?

- La optimización de la cuantización Ley A se logra ajustando adecuadamente la constante A. Al aumentar A, se distribuyen más niveles en las áreas de baja amplitud, lo que mejora la relación señal-ruido al reducir el ruido en esas frecuencias críticas.

### Cuantización Ley A:

- Se modificó la constante A para observar cómo cambia la distribución de los niveles de cuantización. La señal se distribuyó de manera logarítmica en las bajas amplitudes.

- Se compararon los resultados con los de la cuantización uniforme, observando la mejora en la resolución de señales de baja amplitud y la reducción del ruido.

- También se añadió ruido gaussiano y se variaron los anchos de banda del filtro pasabajas para evaluar cómo estos factores afectan la señal cuantizada con Ley A.

¿Cómo influye el valor de la constante A en la distribución de los niveles de cuantización y la percepción del ruido de cuantización?

- Aumentar el valor de A en la cuantización Ley A permite que se pierda menos información a nivel de frecuencia, obteniendo más detalle en frecuencias bajas. Esto se traduce en una mejor resolución en las señales de baja amplitud, lo que facilita el análisis de las señales y reduce la percepción del ruido de cuantización en esos rangos

¿Cuáles son las ventajas del cuantizador Ley A en comparación con la cuantización uniforme?

- La cuantización Ley A tiene la ventaja de distribuir los niveles de cuantización de manera más eficiente en las áreas de baja amplitud, donde el oído humano es más sensible, mientras que la cuantización uniforme distribuye los niveles de manera uniforme en todo el rango. Esto resulta en una mejor calidad de la señal en frecuencias bajas y una reducción del ruido de cuantización en esas áreas críticas, mientras que la cuantización uniforme no mejora la señal en las zonas importantes

¿Cómo afecta el ancho de banda del canal a la calidad de la señal cuantizada y qué implicaciones tiene para el ruido de cuantización?

- El ancho de banda del canal afecta directamente la calidad de la señal cuantizada. Un mayor ancho de banda permite transmitir más detalles de la señal, mejorando la calidad y reduciendo el ruido de cuantización. Sin embargo, un canal con un ancho de banda más pequeño limita la cantidad de información transmitida, lo que puede generar pérdidas de calidad y mayor ruido de cuantización

¿Qué impacto tiene la adición de ruido gaussiano en la señal procesada con cuantización Ley A?

- El ruido gaussiano puede reducir la calidad de la señal cuantizada, pero la cuantización Ley A, al dar más importancia a las amplitudes bajas, ayuda a reducir la percepción de este ruido en las regiones más sensibles, como las frecuencias bajas, mejorando la calidad percibida en esas áreas

¿Cómo se puede optimizar la cuantización Ley A para mejorar la relación señal-ruido en sistemas de procesamiento digital?

- La optimización de la cuantización Ley A se logra ajustando el valor de la constante A. A medida que se aumenta A, se distribuyen más niveles en las frecuencias de baja amplitud, donde el oído humano es más sensible, lo que mejora la relación señal-ruido al reducir el ruido en esas frecuencias y asegurando una mayor resolución en las áreas más importantes de la señal

## Conclusiones

- La cuantización Ley A demuestra ser superior a la cuantización uniforme cuando se trata de preservar la calidad de señales de baja amplitud. Su capacidad para priorizar esas áreas donde el oído humano es más sensible resulta en una mejor percepción de la señal.

- El ruido de cuantización puede ser mitigado aumentando la resolución del cuantizador, y la Ley A ofrece una forma más eficiente de manejar el ruido en señales importantes para la percepción humana.

- El ancho de banda del filtro pasabajas juega un papel crucial en la calidad final de la señal, y su reducción puede resultar en una pérdida significativa de calidad.

- La adición de ruido gaussiano afecta la señal, pero la Ley A ayuda a reducir la percepción de este ruido, mejorando la calidad en las frecuencias más relevantes.
