from flask import Flask, render_template, request
import clips

app = Flask(__name__)

# Inicializar motor de reglas
env = clips.Environment()

# Definir plantilla de síntomas
env.build("""
(deftemplate anomalia
    (slot nombre))
""")

# Definir plantilla de diagnósticos
env.build("""
(deftemplate diagnostico
    (slot texto))
""")

# Definir reglas del sistema experto
env.build("""
(defrule llanta-baja
   (anomalia (nombre llanta_baja))
   =>
   (assert (diagnostico (texto "La llanta está desinflada. Se debe Realizar: inflar el neumático."))))
""")

env.build("""
(defrule cadena-suelta
   (anomalia (nombre cadena_suelta))
   =>
   (assert (diagnostico (texto"La cadena se sale. Se debe Realizar: ajustar o reemplazar la cadena."))))
""")

env.build("""
(defrule frenos-flojos
   (anomalia (nombre frenos_flojos))
   =>
   (assert (diagnostico (texto"Los frenos no responden. Se debe Realizar: ajustar zapatas o cables."))))
""")

env.build("""
(defrule ruido-pedales
   (anomalia (nombre ruido_pedales))
   =>
   (assert (diagnostico (texto"Se escuchan ruidos en pedales. Se debe Realizar: revisar rodamientos del eje central."))))
""")

env.build("""
(defrule rueda-vibra
   (anomalia (nombre rueda_vibra))
   =>
   (assert (diagnostico (texto"La rueda vibra. Se debe Realizar: centrar la llanta en radios."))))
""")

env.build("""
(defrule marchas-mal
   (anomalia (nombre marchas_mal))
   =>
   (assert (diagnostico (texto"Problema al cambiar de marcha. Se debe Realizar: ajustar desviador o cambios."))))
""")

# reglas combinadas
env.build("""
(defrule llanta-baja-y-rueda-vibra
   (anomalia (nombre llanta_baja))
   (anomalia (nombre rueda_vibra))
   =>
   (assert (diagnostico (texto"Revisar neumático y ajustar la rueda."))))
""")

env.build("""
(defrule Cada-Floja-y-Ruido-Pedales
   (anomalia (nombre cadena_suelta))
   (anomalia (nombre ruido_pedales))
   =>
   (assert (diagnostico (texto"Revisar el sistema de rodamiento del eje y que la cadena gire de manera correcta."))))
""")


def diagnosticar(anomalias):
    # Limpiar hechos previos
    env.reset()

    # Insertar síntomas seleccionados
    for anomalia, valor in anomalias.items():
        if valor:
            env.assert_string(f"(anomalia (nombre {anomalia}))")

    # Ejecutar motor de inferencia
    env.run()

    # Extraer diagnósticos generados
    diagnosticos = [str(f["texto"]) for f in env.facts() if f.template.name == "diagnostico"]

    if not diagnosticos:
        return ["No se encontraron problemas específicos. Revisión general recomendada."]
    return diagnosticos


@app.route("/", methods=["GET", "POST"])
def index():
    diagnosticos = []
    if request.method == "POST":
        anomalias = {
            "llanta_baja": "llanta_baja" in request.form,
            "cadena_suelta": "cadena_suelta" in request.form,
            "frenos_flojos": "frenos_flojos" in request.form,
            "ruido_pedales": "ruido_pedales" in request.form,
            "rueda_vibra": "rueda_vibra" in request.form,
            "marchas_mal": "marchas_mal" in request.form,
        }
        diagnosticos = diagnosticar(anomalias)

    return render_template("Experto.html", diagnosticos=diagnosticos)


if __name__ == "__main__":
    app.run(debug=True)