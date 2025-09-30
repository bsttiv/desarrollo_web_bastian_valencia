import os
from flask import Flask, render_template, request, redirect, url_for
import model.db as db
import json
import hashlib
import filetype
from werkzeug.utils import secure_filename
from utils import validar_archivos, validar_aviso
from datetime import datetime

app = Flask("Tarea2")
app.secret_key = "Cl4v3s3cr3t4_t4r34_2_bsttiv"
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['MAX_CONTENT_LENGTH'] = 16*1000*1000

@app.route("/", methods=["GET"])
def index():
    data = []
    for aviso in db.ultimos_lista():
        foto = db.obtener_foto(aviso.id)
        comuna = db.nombre_comuna_por_id(aviso.comuna_id)
        medida = "año(s)" if aviso.unidad_medida == "a" else "mes(es)"
        data.append({
            "fecha": datetime.strftime(aviso.fecha_entrega, "%d/%m/%Y %H:%M"),
            "comuna": comuna.nombre,
            "sector": aviso.sector if aviso.sector != "" else "Sin datos",
            "mascota": f"{aviso.cantidad} {aviso.tipo.name}(s), {aviso.edad} {medida}",
            "foto": f"static/uploads/{foto}"
        })
    return render_template("index.jinja", ultimos=data)

@app.route("/aviso/", methods=["GET", "POST"])
def aviso():
    if request.method == "GET":
        return render_template("agregar-aviso.jinja")
    else:
        if request.form.get("select-region") is None or \
            request.form.get("select-comuna") is None or \
            request.form.get("nombre") is None or \
            request.form.get("email") is None or \
            request.form.get("tipo") is None or \
            request.form.get("cantidad") is None or \
            request.form.get("edad") is None or \
            request.form.get("medida") is None or \
            request.form.get("fecha") is None or \
            len(list(request.files.items())) == 0:
            return "Error de peticion"
        comuna = request.form.get("select-comuna")
        region = request.form.get("select-region")
        nombre = request.form.get("nombre")
        email = request.form.get("email")
        tipo = request.form.get("tipo")
        cantidad = request.form.get("cantidad")
        edad = request.form.get("edad")
        medida = request.form.get("medida")
        fecha = request.form.get("fecha")
        celular = request.form.get("tel")
        desc = request.form.get("desc")
        sector = request.form.get("sector")
        errores = []
        try:
            cantidad = int(cantidad)
            edad = int(edad)
        except Exception:
            errores.append("Una cantidad ingresada no es un numero entero")
        checkboxes = []
        if request.form.get("whatsapp") is not None:
            checkboxes.append(("whatsapp", request.form.get("whatsapp"), request.form.get("whatsapp-input")))
        if request.form.get("tiktok") is not None:
            checkboxes.append(("tiktok", request.form.get("tiktok"), request.form.get("tiktok-input")))
        if request.form.get("x") is not None:
            checkboxes.append(("x", request.form.get("x"), request.form.get("x-input")))
        if request.form.get("instagram") is not None:
            checkboxes.append(("instagram", request.form.get("instagram"), request.form.get("instagram-input")))
        if request.form.get("telegram") is not None:
            checkboxes.append(("telegram", request.form.get("telegram"), request.form.get("telegram-input")))
        if request.form.get("otra") is not None:
            checkboxes.append(("otra", request.form.get("otra"), request.form.get("otra-input")))
        errores.extend(
            validar_aviso.validarAviso(
                comuna,
                region,
                nombre,
                email,
                celular,
                tipo,
                cantidad,
                edad,
                medida,
                fecha,
                checkboxes,
                sector
            )
        )
        for archivo in request.files.values():
            if not validar_archivos.validar_archivo(archivo):
                errores.append("Archivo")
                break
        if len(errores) != 0:
            data_err = {
                "error_title": "Error recibiendo el formulario",
                "error_msg": "Alguno de los siguientes campos tiene errores",
                "error_list": errores
            }
            return render_template("agregar-aviso.jinja", **data_err)
        region_id = db.get_region_by_name(region).id
        comuna_id = list(filter(lambda c: c.nombre==comuna, db.get_comunas(region_id=region_id)))[0].id
        aviso_id = db.crear_aviso(
            comuna_id=comuna_id,
            sector=sector,
            nombre=nombre,
            email=email,
            celular=celular,
            tipo=tipo,
            cantidad=cantidad,
            edad=edad,
            medida=medida,
            fecha_entrega=fecha,
            desc=desc
        )
        for archivo in request.files.values():
            _filename = hashlib.sha256(
                secure_filename(archivo.filename)
                .encode("utf-8")
            ).hexdigest()
            _extension = filetype.guess(archivo).extension
            img_filename = f"{_filename}.{_extension}"
            db.crear_foto(aviso_id, img_filename, "static/uploads/")
            archivo.save(os.path.join(app.config["UPLOAD_FOLDER"], img_filename))
        for checkbox in checkboxes:
            db.crear_contacto(checkbox[0], checkbox[2], aviso_id=aviso_id)
        return render_template("agregar-aviso.jinja", correct_msg="Formulario correctamente enviado! ¿Deseas volver?")

@app.route("/listado/<int:id_aviso>", methods=["GET"])
def listado_id_aviso(id_aviso):
    aviso = db.obtener_aviso(id_aviso)
    if aviso is None:
        return redirect(url_for("listado"))
    comuna = db.nombre_comuna_por_id(aviso.comuna_id)
    medida = "año(s)" if aviso.unidad_medida == "a" else "mes(es)"
    fotos = map(lambda ft: f"uploads/{ft.nombre_archivo}", db.obtener_fotos(id_aviso))
    data = {
        "aviso_id": id_aviso,
        "fecha_ingreso": datetime.strftime(aviso.fecha_ingreso, "%d/%m/%Y %H:%M"),
        "fecha_entrega": datetime.strftime(aviso.fecha_entrega, "%d/%m/%Y %H:%M"),
        "comuna": comuna.nombre,
        "sector": aviso.sector if aviso.sector != "" else "Sin datos",
        "cantidad": aviso.cantidad,
        "tipo": aviso.tipo.name,
        "edad": f"{aviso.edad} {medida}",
        "nombre": aviso.nombre,
        "fotos": list(fotos)
    }
    return render_template("aviso.jinja", **data)

@app.route("/listado/", methods=["GET"])
def listado():
    try:
        query = int(request.args.get("page", 0))*5
    except Exception:
        return redirect(url_for("listado"))
    avisos = db.numero_avisos()
    if query > avisos:
        return redirect(url_for("listado"))
    if avisos > 5:
        paginas = [i for i in range(0, avisos//5+1)]
    data = []
    for aviso in db.listado_offset(query):
        comuna = db.nombre_comuna_por_id(aviso.comuna_id)
        medida = "año(s)" if aviso.unidad_medida == "a" else "mes(es)"
        count = db.numero_fotos(aviso.id)
        data.append({
            "id": aviso.id,
            "fecha_ingreso": datetime.strftime(aviso.fecha_ingreso, "%d/%m/%Y %H:%M"),
            "fecha_entrega": datetime.strftime(aviso.fecha_entrega, "%d/%m/%Y %H:%M"),
            "comuna": comuna.nombre,
            "sector": aviso.sector if aviso.sector != "" else "Sin datos",
            "mascota": f"{aviso.cantidad} {aviso.tipo.name}(s), {aviso.edad} {medida}",
            "contacto": aviso.nombre,
            "numero_fotos": count
        })
    return render_template("lista-avisos.jinja", lista=data, paginas=paginas, actual=query//5)

@app.route("/estadisticas/", methods=["GET"])
def estadisticas():
    return render_template("estadisticas.jinja")

def inicializar_comunas():
    regiones_comunas = []
    regiones = db.get_regiones()
    for region in regiones:
        dicc = {
            "numero": region.id, 
            "nombre": region.nombre,
            "comunas": list(map(lambda a: {"id": a.id, "nombre": a.nombre}, db.get_comunas(region.id)))
        }
        regiones_comunas.append(dicc)
    with open("./static/js/region_comuna.js", "w") as js:
        js.write('let region_comuna = {\n"regiones": ')
        json_lista = json.dumps(regiones_comunas, indent=4)
        js.write(json_lista)
        js.write("};\n")
        js.write("export {region_comuna}")

inicializar_comunas()

if __name__ == "__main__":
    app.run(debug=True)
