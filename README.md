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
│── requirements.txt # Dependencias del proyecto
│── templates/
│ └── index.html # Interfaz web
│── static/ # (opcional) Archivos CSS/JS si quieres personalizar

## 🚀 Instalación y ejecución

2. Crear entorno virtual (opcional pero recomendado)
python -m venv venv
source venv/bin/activate    # En Linux/Mac
venv\Scripts\activate       # En Windows

3. Instalar dependencias
pip install -r requirements.txt

5. Ejecutar la aplicación
python app.py


La aplicación se iniciará en:
👉 http://127.0.0.1:5000/

🛠 Tecnologías utilizadas

Python
Flask
CLIPSPY  (motor de reglas basado en CLIPS)

📜 Licencia

Este proyecto se distribuye bajo la licencia MIT.
Eres libre de usarlo, modificarlo y compartirlo.

---

👉 Solo reemplaza `aljeison` con tu usuario de GitHub.  








