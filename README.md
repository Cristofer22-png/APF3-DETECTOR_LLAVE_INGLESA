# Detector de Llave Inglesa en Tiempo Real (Haar Cascade + OpenCV)

Proyecto desarrollado para el curso **Herramientas de Desarrollo Profesional** (Ingeniería Civil – Universidad Tecnológica del Perú, Sede Piura).

## Descripción
Sistema de Visión Computacional entrenado desde cero para detectar e identificar en tiempo real una **llave inglesa cromada de 250 mm (25 × 7 cm)** mediante clasificadores en cascada de características Haar, orientado al control automatizado de herramientas en almacenes de obra (pañoles).

## Contenido del Repositorio
* `APF3_CRISTOFERLACHIRA.py`: Script principal del detector en tiempo real con lectura de cámara multihilo.
* `cascade.xml`: Modelo Haar Cascade entrenado en Cascade Trainer GUI (`60 × 28 px`, 12 etapas).
* `p/` y `n/`: Datasets propios de imágenes positivas (+100 muestras) y negativas (103 muestras).
* `DETECCION.png` / `no detecta.png` / `Clasiffier.png`: Evidencias del entrenamiento y validación en vivo (verdaderos positivos y limitaciones).

## Requisitos e Instalación
1. Instalar Python 3 y las librerías necesarias: `pip install opencv-python imutils`
2. Verificar la IP de DroidCam en `APF3_CRISTOFERLACHIRA.py` y ejecutar: `python APF3_CRISTOFERLACHIRA.py`

## Video Demostrativo
* **Enlace al video (2–4 min):** PEGA_AQUI_TU_LINK_DE_YOUTUBE_O_DRIVE

## Autor
* **Cristofer Smith Lachira Zapata** – Estudiante de Ingeniería Civil (UTP)
