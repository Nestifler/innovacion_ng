from flask import Flask, render_template, request, redirect, url_for, flash
import json
import os
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'ng_innovacion_tecnologica_2026'

# ==================================================
#        DATOS EXACTOS DE TU EMPRESA Y SERVICIOS
# ==================================================
INFO_EMPRESA = {
    "nombre": "INNOVACIÓN TECNOLÓGICA NG",
    "eslogan": "Soluciones Tecnológicas Integrales",
    "descripcion": "Expertos en Seguridad Electrónica, Redes, Cableado Estructurado y Soporte Técnico. Calidad, orden y garantía en cada proyecto.",
    "tecnico": "Nestor Fabian González Moreno",
    "cargo": "Técnico Asesor Especializado",
    "telefono": "322 802 2560",
    "whatsapp": "573228022560",
    "correo": "innovaciontecnologicang@gmail.com",
    "ubicacion": "Bogotá y alrededores",
    "experiencia": "Más de 8 años de experiencia respaldando empresas y hogares",
    
    # SERVICIOS COMPLETOS
    "servicios": [
        {
            "id": 1,
            "categoria": "Seguridad Electrónica",
            "titulo": "SISTEMAS DE CÁMARAS CCTV",
            "resumen": "Vigila tu propiedad estés donde estés",
            "descripcion": """
                ✅ Diseño, instalación y configuración de cámaras analógicas e IP de alta definición.<br>
                ✅ Visualización y grabación 24/7 desde tu celular, tablet o computador.<br>
                ✅ Protección profesional del cableado mediante <strong>Tubería EMT y accesorios certificados</strong> en instalaciones visibles, garantizando estética y seguridad.<br>
                ✅ Asesoría gratuita, capacitación y garantía escrita.
            """,
            "imagen": "cctv.png",
            "icono": "📹"
        },
        {
            "id": 2,
            "categoria": "Seguridad Electrónica",
            "titulo": "SISTEMAS DE ALARMA Y DETECCIÓN",
            "resumen": "Protección activa contra intrusos",
            "descripcion": """
                ✅ Instalación de sistemas de alarma perimetral, sensores de movimiento, apertura y barreras.<br>
                ✅ Avisos inmediatos a tu teléfono ante cualquier intento de ingreso.<br>
                ✅ Integración total con tus cámaras de seguridad.<br>
                ✅ Equipos de marcas líderes y resistentes a condiciones ambientales.
            """,
            "imagen": "Alarmas.png",
            "icono": "🚨"
        },
        {
            "id": 3,
            "categoria": "Redes y Conectividad",
            "titulo": "CABLEADO ESTRUCTURADO | REDES Y TUBERÍA EMT",
            "resumen": "Infraestructura sólida, ordenada y profesional",
            "descripcion": """
                💎 <strong>NUESTRO DIFERENCIAL:</strong> Utilización obligatoria de <strong>Tubería EMT (Tubo Metálico Ligero), codos, uniones y accesorios</strong> para todas las rutas expuestas. Cumplimos norma RETIE.<br><br>
                ✅ Diseño e instalación de redes de datos, internet y telefonía.<br>
                ✅ Tendido de cables, certificación de puntos y conexiones.<br>
                ✅ Montaje, organización y etiquetado técnico de <strong>RACKS, gabinetes y bandejas</strong>. Orden extremo y facilidad de mantenimiento.<br>
                ✅ Soluciones para oficinas, empresas, conjuntos residenciales y colegios.
            """,
            "imagen": "tencido_de_cable.png",
            "icono": "🔌"
        },
        {
            "id": 4,
            "categoria": "Redes y Conectividad",
            "titulo": "INSTALACIÓN Y CONFIGURACIÓN DE INTERNET Y WIFI",
            "resumen": "Señal rápida, estable y sin zonas muertas",
            "descripcion": """
                ✅ Distribución óptima de señal en todo el espacio.<br>
                ✅ Configuración profesional de módems, routers, switches y repetidores.<br>
                ✅ Redes seguras y balanceadas para que todos los dispositivos funcionen a máxima velocidad.<br>
                ✅ Olvídate de las caídas de conexión que detienen tu negocio.
            """,
            "imagen": "rack1.png",
            "icono": "📶"
        },
        {
            "id": 5,
            "categoria": "Soporte y Mantenimiento",
            "titulo": "REPARACIÓN Y MANTENIMIENTO DE COMPUTADORES",
            "resumen": "Tus equipos funcionando como nuevos",
            "descripcion": """
                ✅ Mantenimiento preventivo y correctivo de equipos de cómputo, portátiles y servidores.<br>
                ✅ Eliminación de virus, malware y programas basura.<br>
                ✅ Optimización de rendimiento, formateo e instalación de software original.<br>
                ✅ Reparación de fallas de hardware: placas, pantallas, teclados, baterías y más.<br>
                ✅ Evita pérdidas de tiempo y dinero por equipos lentos o dañados.
            """,
            "imagen": "computadores.png",
            "icono": "💻"
        },
        {
            "id": 6,
            "categoria": "Soporte y Mantenimiento",
            "titulo": "IMPRESORAS, FOTOCOPIADORAS Y ESCÁNERES",
            "resumen": "El dolor de cabeza de oficina, solucionado",
            "descripcion": """
                ✅ Servicio técnico especializado en todas las marcas y modelos.<br>
                ✅ Limpieza técnica profunda, calibración y mantenimiento general.<br>
                ✅ Solución definitiva a atascos de papel, mala calidad de impresión y errores de sistema.<br>
                ✅ Recarga y cambio de tóner y tintas con garantía de funcionamiento.<br>
                ✅ Reparación de mecanismos y piezas electrónicas.
            """,
            "imagen": "impresoras.png",
            "icono": "🖨️"
        }
    ],

    # PORTAFOLIO DE TRABAJOS REALIZADOS
    "portafolio": [
        {
            "categoria": "Instalaciones con Tubería EMT",
            "titulo": "Recorridos profesionales y seguros",
            "descripcion": "Instalación completa utilizando Tubería EMT galvanizada, codos y accesorios. Protección total contra golpes, roedores y ambiente. Acabado limpio, alineado y estético que cumple con todas las normas técnicas.",
            "imagenes": ["emt1.png", "emt2.png"],
            "video": "portafolio/video1.mp4"
        },
        {
            "categoria": "Organización de Racks y Gabinetes",
            "titulo": "Orden es sinónimo de calidad",
            "descripcion": "Montaje de gabinete de comunicaciones con organización extrema de cableado estructurado, uso de accesorios de sujeción, rutas definidas y etiquetado técnico detallado. Facilita mantenimientos futuros y evita fallas.",
            "imagenes": ["rack1.png"],
            "video": None
        },
        {
            "categoria": "Sistemas de Seguridad CCTV",
            "titulo": "Estética y cobertura 24/7",
            "descripcion": "Proyectos de videovigilancia para oficinas y hogares. Instalación de cámaras en puntos estratégicos, cableado protegido y configuración remota. Un trabajo bien hecho debe funcionar perfecto y verse perfecto.",
            "imagenes": ["cctv1.png"],
            "video": None
        }
    ]
}

# ==================================================
#                    RUTAS WEB
# ==================================================
@app.route('/')
def inicio():
    # ✅ AQUÍ SE ENVÍAN LOS DATOS AL HTML (antes faltaba)
    return render_template('index.html', empresa=INFO_EMPRESA, servicios=INFO_EMPRESA["servicios"], portafolio=INFO_EMPRESA["portafolio"])

@app.route('/servicios')
def servicios():
    # ✅ AQUÍ SE ENVÍAN LOS DATOS AL HTML
    return render_template('servicios.html', empresa=INFO_EMPRESA, servicios=INFO_EMPRESA["servicios"])

@app.route('/portafolio')
def portafolio():
    # ✅ AQUÍ SE ENVÍAN LOS DATOS AL HTML
    return render_template('portafolio.html', empresa=INFO_EMPRESA, portafolio=INFO_EMPRESA["portafolio"])

@app.route('/nosotros')
def nosotros():
    return render_template('nosotros.html', empresa=INFO_EMPRESA)

@app.route('/contacto', methods=['GET', 'POST'])
def contacto():
    if request.method == 'POST':
        nombre = request.form['nombre']
        telefono = request.form['telefono']
        servicio = request.form['servicio']
        mensaje = request.form['mensaje']
        
        # Guardar mensaje en archivo
        mensaje_data = {
            "fecha": datetime.now().strftime("%d/%m/%Y %H:%M"),
            "nombre": nombre,
            "telefono": telefono,
            "servicio": servicio,
            "mensaje": mensaje
        }
        
        ruta_archivo = "base_datos/mensajes.json"
        mensajes = []
        if os.path.exists(ruta_archivo):
            with open(ruta_archivo, 'r', encoding='utf-8') as f:
                mensajes = json.load(f)
        
        mensajes.append(mensaje_data)
        with open(ruta_archivo, 'w', encoding='utf-8') as f:
            json.dump(mensajes, f, indent=4, ensure_ascii=False)
        
        flash("✅ ¡Mensaje enviado con ÉXITO! Te responderemos muy pronto.")
        return redirect(url_for('contacto'))
    
    return render_template('contacto.html', empresa=INFO_EMPRESA)

# ✅ CONFIGURACIÓN OBLIGATORIA PARA RENDER
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
