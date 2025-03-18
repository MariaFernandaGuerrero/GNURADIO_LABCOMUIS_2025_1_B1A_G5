# Laboratorio de Comunicaciones
## Universidad Industrial de Santander

# Práctica 2A. Modelo de canal

### Integrantes
- **Maria Fernanda Guerrero Santos** - 2202343
- **Michelle Garzón Campos** - 2202785

Escuela de Ingenierías Eléctrica, Electrónica y de Telecomunicaciones  
Universidad Industrial de Santander

### Fecha


---

## Declaración de Originalidad y Responsabilidad
Los autores de este informe certifican que el contenido aquí presentado es original y ha sido elaborado de manera independiente. Se han utilizado fuentes externas únicamente como referencia y han sido debidamente citadas.

Asimismo, los autores asumen plena responsabilidad por la información contenida en este documento. 

Uso de IA: Se utilizó ChatGPT para reformular secciones del texto y verificar gramática, pero el contenido técnico fue desarrollado íntegramente por los autores.

## Actividad 1: Actividades de simulación de canal en GNU Radio

- ¿Cuál es el efecto de filtrar las frecuencias altas de una señal?
- ¿Qué sucede al filtrar muy cerca de la frecuencia fundamental de la señal?
- ¿Cuál es el efecto de filtrar las frecuencias bajas de una señal?
- ¿Qué ocurre al eliminar armónicos de una señal?
- ¿Qué efecto tiene la desviación de frecuencia en la señal recibida? ¿Qué efecto(s) produce el filtro cuando la señal recibida se ve afectada por desviación de frecuencia?
- ¿Cómo cuantificar la degradación de la señal al aumentar los niveles de ruido?
- ¿Cómo se puede mejorar la relación señal a ruido en una señal?
- ¿Cómo podría cuantificar la calidad de la señal recibida? Considere el caso de señales analógicas y digitales.

---

## Actividad 2: Fenómenos de canal en el osciloscopio

- ¿Cuál es el efecto del ruido sobre la amplitud de las señales medidas en el osciloscopio? ¿Conservan las mismas relaciones que se evidencian en la simulación?
- ¿La relación señal a ruido creada intencionalmente en el computador se amplifica o se reduce en la señal observada en el osciloscopio?
- Demuestre ¿cómo se puede mejorar la relación señal a ruido en una señal?
- ¿Cómo se evidencia el fenómeno de desviación de frecuencia en el osciloscopio? Evidenciar al menos con dos formas de onda.
- Determine la afectación de un medio de transmisión coaxial (usar cables largos) sobre una señal periódica operando a las capacidades máximas de muestreo del USRP.
  
  
- Usando cables coaxiales de diferentes longitudes, ¿cómo afecta la distancia entre el transmisor y el receptor a la amplitud de la señal medida?
  El largo del cable se generan atenuaciones mas grandes y da paso a ruido.

![Networking](/imagenes/coax_corto.jpg) ![Networking](/imagenes/coax_largo.jpg)

- Usando antenas, ¿cómo afecta la distancia entre el transmisor y el receptor a la amplitud de la señal medida? ¿Es posible compensar el fenómeno?
  La distancia entre las antenas afecta directamente la amplitud de la señal, esto se demosytró en el laboratorio de manera un poco obvia ya que practicamente la distancia entre las antenas tuvo que ser nula para poder visualizar la señal.

![Networking](/imagenes/antenas.jpg)

- ¿Qué modelo de canal básico describe mejor las mediciones obtenidas en la práctica?
  El modelo de perdida por espacio libre FRIIS, el cual describe la pérdida de señal en un enlace inalámbrico en espacio libre, relacionando la potencia recibida con la transmitida, las ganancias de las antenas, la distancia y la longitud de onda.
  
---

## Actividad 3: Fenómenos de canal en el analizador de espectro

- ¿Cuál es el efecto del ruido sobre la respuesta en frecuencia de las señales medidas en el analizador de espectro? ¿Conservan las mismas relaciones que se evidencian en la simulación?
- ¿La relación señal a ruido creada intencionalmente desde el computador se amplifica o se reduce en la señal observada en el analizador de espectro?
- Adjunte la evidencia de la medición de la relación señal a ruido de dos formas de onda distintas.
- ¿Cómo se evidencia el fenómeno de desviación de frecuencia en el analizador de espectro? Evidenciar al menos con dos formas de onda.
- Determine la afectación de un medio de transmisión coaxial (usar cables largos) sobre una señal periódica operando a las capacidades máximas de muestreo del USRP.
  
  
- Usando cables coaxiales de diferentes longitudes, ¿cómo afecta la distancia entre el transmisor y el receptor a la amplitud de la señal medida?
  
  
- Usando antenas, ¿cómo afecta la distancia entre el transmisor y el receptor a la amplitud de la señal medida? ¿Es posible compensar el fenómeno?
  
  
- ¿Qué modelo de canal básico describe mejor las mediciones obtenidas en la práctica?
  
  
---

## Actividad 4: Efectos de los fenómenos de canal en la conversión de frecuencia

- ¿Cómo se evidencian los diferentes fenómenos de canal en la señal recibida?
- ¿Cómo se pueden mitigar los efectos del canal en la señal recibida?
