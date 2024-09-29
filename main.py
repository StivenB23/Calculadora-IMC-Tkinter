import tkinter as tk
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph
import webbrowser

root = tk.Tk()
photo = tk.PhotoImage(file="ico_heart.png")
root.wm_iconphoto(False, photo)
root.title("Software IMC Albert Ospina")

# Definir colores y fuentes
bg_color = "#f0f0f0"
title_color = "#3a5fcd"
title_font = ("Helvetica", 24, "bold")
bold_font = ("Helvetica", 12, "bold")

# Variables
peso = tk.DoubleVar()
altura = tk.DoubleVar()

def generate_pdf(imc, weight, height, status, info, recommendations):
    filename = "resultado_imc.pdf"
    doc = SimpleDocTemplate(filename, pagesize=letter)
    styles = getSampleStyleSheet()
    custom_style = ParagraphStyle(
        'CustomStyle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=12,
        textColor=colors.black,
        spaceAfter=12,
    )

    content = []
    content.append(Paragraph("Resultado del IMC", styles['Title']))
    content.append(Paragraph(f"Peso: {weight} kg", custom_style))
    content.append(Paragraph(f"Altura: {height} m", custom_style))
    content.append(Paragraph(f"Su IMC es: {imc}", custom_style))
    content.append(Paragraph(f"Estado de salud: {status}", custom_style))
    
    content.append(Paragraph("Información:", styles['Heading2']))
    content.append(Paragraph(info, custom_style))

    content.append(Paragraph("Recomendaciones:", styles['Heading2']))
    for line in recommendations:
        content.append(Paragraph(line.strip(), custom_style))

    doc.build(content)
    webbrowser.open(filename)

def get_recommendations(status):
    info = ""
    recommendations = []

    if status == "Bajo peso":
        info = (
            "Causas del bajo peso: Puede ser resultado de múltiples factores, incluyendo "
            "desnutrición, trastornos alimentarios, enfermedades crónicas, o condiciones "
            "psicológicas como la depresión.\n"
            "Riesgos asociados: Un sistema inmunológico debilitado, problemas de fertilidad, "
            "osteoporosis y fatiga crónica."
        )
        recommendations = [
            "Consulta médica: Es esencial consultar a un médico o nutricionista.",
            "Aumentar la ingesta calórica: Optar por alimentos densamente calóricos y nutritivos.",
            "Comidas frecuentes y saludables: Realizar cinco a seis comidas pequeñas al día.",
            "Suplementos nutricionales: Considerar el uso de suplementos bajo supervisión.",
            "Ejercicio de fuerza: Incorporar ejercicios de resistencia para aumentar la masa muscular.",
            "Manejo del estrés: Técnicas como la meditación pueden ayudar."
        ]

    elif status == "Peso normal":
        info = (
            "Características de un peso saludable: Menor probabilidad de desarrollar enfermedades crónicas. "
            "Este rango está asociado con una buena relación entre masa muscular y grasa corporal.\n"
            "Beneficios para la salud: Vida más larga y saludable, menor riesgo de enfermedades."
        )
        recommendations = [
            "Mantener una dieta variada y equilibrada.",
            "Realizar al menos 150 minutos de actividad física moderada a la semana.",
            "Beber suficiente agua y limitar bebidas azucaradas.",
            "Priorizar la salud mental mediante el manejo del estrés.",
            "Realizar chequeos médicos regulares."
        ]

    elif status == "Sobrepeso":
        info = (
            "Causas del sobrepeso: Ingesta calórica excesiva y actividad física insuficiente. "
            "También influencias genéticas, hormonales y ambientales.\n"
            "Riesgos asociados: Aumento del riesgo de diabetes tipo 2, enfermedades del corazón y apnea del sueño."
        )
        recommendations = [
            "Establecer un objetivo de pérdida de peso realista.",
            "Llevar un diario de alimentos para identificar patrones.",
            "Aumentar la actividad física en la vida diaria.",
            "Unirse a grupos de apoyo para la pérdida de peso.",
            "Aprender sobre porciones adecuadas y lectura de etiquetas."
        ]

    elif status == "Obesidad I":
        info = (
            "Características de la obesidad I: Implica un riesgo significativo de desarrollar problemas de salud. "
            "Mayor acumulación de grasa en la zona abdominal.\n"
            "Riesgos de salud: Mayor riesgo de enfermedades cardiovasculares y diabetes tipo 2."
        )
        recommendations = [
            "Consultar a un médico para desarrollar un plan de acción.",
            "Trabajar con un nutricionista para crear un plan de alimentación.",
            "Iniciar con ejercicios de bajo impacto y aumentar gradualmente.",
            "Considerar terapia conductual para hábitos alimenticios.",
            "Monitorear el progreso con exámenes médicos regulares."
        ]

    elif status == "Obesidad II":
        info = (
            "Características de la obesidad II: Aumenta el riesgo de comorbilidades serias, "
            "como enfermedades cardíacas y diabetes.\n"
            "Riesgos de salud: Calidad de vida reducida y estigmatización social."
        )
        recommendations = [
            "Consultar a un médico para discutir opciones de tratamiento.",
            "Implementar cambios de estilo de vida más rigurosos.",
            "Contar con la guía de un equipo de atención médica.",
            "Participar en programas de ejercicios grupales.",
            "Considerar terapia para abordar problemas emocionales."
        ]

    elif status == "Obesidad III":
        info = (
            "Características de la obesidad III: Representa uno de los mayores riesgos para la salud y puede "
            "ser potencialmente mortal. Calidad de vida severamente comprometida.\n"
            "Riesgos de salud: Alto riesgo de infartos, derrames cerebrales y problemas respiratorios."
        )
        recommendations = [
            "Buscar atención médica de urgencia para evaluar el estado de salud.",
            "Implementar un programa de pérdida de peso intensivo y supervisado.",
            "Trabajar con un equipo multidisciplinario.",
            "Participar en terapia para abordar aspectos psicológicos.",
            "Realizar seguimiento constante de la salud con chequeos regulares."
        ]

    return info, recommendations

def calculate_imc():
    if altura.get() > 0:  # Verificar que la altura no sea cero
        imc_value = peso.get() / (altura.get() ** 2)
        imc = round(imc_value, 2)
        result_label.config(text=f"Su IMC es: {imc}")  # Mostrar el IMC en la etiqueta
        
        if imc < 18.5:
            status = "Bajo peso"
            result_label.config(fg="blue")
        elif 18.5 <= imc < 25:
            status = "Peso normal"
            result_label.config(fg="green")
        elif 25 <= imc < 30:
            status = "Sobrepeso"
            result_label.config(fg="orange")
        elif 30 <= imc < 35:
            status = "Obesidad I"
            result_label.config(fg="red")
        elif 35 <= imc < 40:
            status = "Obesidad II"
            result_label.config(fg="red")
        else:
            status = "Obesidad III"
            result_label.config(fg="red")

        info, recommendations = get_recommendations(status)
        generate_pdf(imc, peso.get(), altura.get(), status, info, recommendations)
    else:
        result_label.config(text="La altura debe ser mayor que 0.", fg="black")

def reset_fields():
    peso.set(0.0)  # Resetear peso a 0
    altura.set(0.0)  # Resetear altura a 0
    result_label.config(text="", fg="black")  # Limpiar el mensaje de resultado

title_frame = tk.Frame(root)
title_frame.grid(column=0, row=0, sticky="ew", padx=10, pady=10)

# Crear la etiqueta del título
title_label = tk.Label(title_frame, text="Bienvenido a la Aplicación", font=title_font, foreground=title_color, background=bg_color)
title_label.grid(column=0, row=0)

# Crear un marco para el formulario
form_frame = tk.Frame(root, relief="sunken")
form_frame.grid(column=0, row=1, sticky="ew", padx=10, pady=10)

# Crear y ubicar las etiquetas y campos de entrada en el marco del formulario
tk.Label(form_frame, text="Ingrese su peso (kg):", font=bold_font, background=bg_color).grid(column=0, row=0, sticky='E')
tk.Entry(form_frame, textvariable=peso).grid(column=1, row=0, padx=5)

tk.Label(form_frame, text="Ingrese su altura (m):", font=bold_font, background=bg_color).grid(column=0, row=1, sticky='E')
tk.Entry(form_frame, textvariable=altura).grid(column=1, row=1, padx=5)

# Botón para calcular IMC
calculate_button = tk.Button(form_frame, text="Calcular IMC", command=calculate_imc)
calculate_button.grid(column=0, row=2, columnspan=2, pady=10)

# Botón para reiniciar campos
reset_button = tk.Button(form_frame, text="Reiniciar", command=reset_fields)
reset_button.grid(column=0, row=3, columnspan=2, pady=5)

# Etiqueta para mostrar el resultado
result_label = tk.Label(root, text="", font=("Helvetica", 16), bg=bg_color)
result_label.grid(column=0, row=2, pady=10)

# Configurar el color de fondo de la ventana
root.configure(bg=bg_color)

root.mainloop()
