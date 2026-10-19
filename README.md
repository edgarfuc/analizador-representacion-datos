# analizador-representacion-datos

Proyecto de Arquitectura de Computadoras: analizador de representación de datos con Python y Django.



\# Analizador de representación de datos



\*\*Proyecto de Arquitectura de Computadoras\*\*



Aplicación web desarrollada con Python 3.12 y Django para convertir números entre los sistemas binario, octal, decimal y hexadecimal, y analizar la representación de caracteres mediante Unicode y UTF-8.



\## Funcionalidades



\- Conversión entre bases numéricas 2, 8, 10 y 16.

\- Validación de dígitos según la base seleccionada.

\- Validación de valores entre 0 y 65535.

\- Representación binaria con relleno de bits.

\- Cálculo de bits significativos y bytes requeridos.

\- Análisis de texto de hasta 20 caracteres.

\- Visualización del código decimal, punto de código Unicode, hexadecimal y bytes UTF-8.

\- Mensajes de error para entradas inválidas.

\- Pruebas automatizadas.



\## Requisitos



\- Python 3.12 para ejecutar el proyecto localmente.

\- Docker Desktop y Docker Compose para ejecutarlo en un contenedor.



\## Ejecución con Docker



Construir la imagen:



```bash

docker compose build

```



Iniciar la aplicación:



```bash

docker compose up -d

```



Abrir en el navegador:



http://127.0.0.1:8000/



Consultar el estado del contenedor:



```bash

docker compose ps

```



Consultar el consumo de recursos:



```bash

docker stats --no-stream

```



Los límites configurados son 256 MB de memoria RAM y 1 CPU.



Para detener la aplicación:



```bash

docker compose down

```



\## Pruebas automatizadas



Ejecutar las pruebas de la aplicación:



```bash

docker compose exec analizador python manage.py test analizador

```



\## Relación con la arquitectura de Von Neumann



La aplicación utiliza el procesador para ejecutar instrucciones y realizar conversiones, la memoria RAM para almacenar temporalmente datos e instrucciones durante la ejecución, el almacenamiento para conservar los archivos del proyecto y los resultados que se guarden, y los dispositivos de entrada y salida para recibir los datos del usuario y mostrar los resultados en pantalla.



El programa se ejecuta mediante instrucciones procesadas por la CPU y utiliza memoria para trabajar con los valores ingresados. Esto se relaciona con el modelo de Von Neumann, en el que las instrucciones y los datos se procesan mediante los componentes principales del computador.



\## Uso del contenedor Docker



Docker permite ejecutar la aplicación en un entorno aislado y controlar los recursos asignados. El contenedor comparte el kernel del sistema operativo anfitrión, pero mantiene aislados sus procesos y otros recursos. Esto evita la necesidad de ejecutar un sistema operativo completo dentro del contenedor.



\## Evidencias



La carpeta `Evidencias` contiene capturas de la aplicación, las conversiones numéricas, el análisis UTF-8, las pruebas automatizadas, la compilación de Docker, el consumo de recursos y los mensajes de validación.



