🚲 Sistema Experto de Diagnóstico para Bicicletas

Este proyecto es un **sistema experto** desarrollado en **Python**, que ayuda a diagnosticar problemas comunes en bicicletas mediante un motor de reglas basado en **CLIPSPY** y una interfaz web con **Flask**.

## ✨ Características
- Interfaz web simple y fácil de usar.
- Ingreso de anomalias seleccionados por el usuario.
- Motor de inferencia basado en **CLIPS**.
- Recomendaciones automáticas para reparación o ajuste.
- Regla combinada: si hay **llanta baja + rueda que vibra**, recomienda *“Revisar neumático y ajustar la rueda”*.

## 📂 Estructura del proyecto

sistema-experto-bicicletas/
│── app.py # Código principal en Flask + CLIPSPY
│── templates/
│ └── Experto.html # Interfaz web
│── static/ # (opcional) Archivos CSS/JS si quieres personalizar

## 🚀 Instalación y ejecución

1. Crear entorno virtual (opcional pero recomendado)
python -m venv venv
source venv/bin/activate    # En Linux/Mac
venv\Scripts\activate       # En Windows

2. Instalar dependencias
Abre una terminal para importar las libretias Flask y clipspy
pip install Flask
pip install clipspy

3. Ejecutar la aplicación
Abre una terminal y navega a la carpeta raíz del proyecto, donde está el archivo app.py. Luego ejecuta:
python app.py

La aplicación se iniciará en:
👉 http://127.0.0.1:5000/

## 🛠 Tecnologías utilizadas
Python
Flask
CLIPSPY  (motor de reglas basado en CLIPS)

## 💡 Funcionamiento
Selecciona .
Haz clic en Calcular para obtener la velocidad recomendada del ventilador basada en las reglas de lógica difusa.
Visualiza los grados de pertenencia y las funciones difusas en gráficas interactivas.

## 🛠️ Requisitos previos
Python 3 instalado (se recomienda crear un virtualenv).

## 📜 Licencia

Este proyecto se distribuye bajo la licencia MIT.
Eres libre de usarlo, modificarlo y compartirlo.








