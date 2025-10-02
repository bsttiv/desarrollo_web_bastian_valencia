import re
from datetime import datetime
import model.db as db

def validarTexto(texto, maxlength, minlength=1):
    if texto is None:
        return False
    trimmed = texto.strip()
    return len(trimmed) >= minlength and len(trimmed) <=maxlength

def validarEmail(email):
    if email is None:
        return False
    return bool(re.search(r"^[\w.]+@[a-zA-Z_]+?\.[a-zA-Z]{2,3}$", email))

def validarTelefono(telefono):
    return telefono is None or bool(re.search(r"^\+\d{3}\.\d{8}$", telefono))

def validarCheckbox(checkbox_status, checkbox_value):
    if checkbox_value is None or checkbox_status is None:
        return False
    trimmed = checkbox_value.strip()
    return checkbox_status == "on" and len(trimmed) >= 4 and len(trimmed) <= 50

def validarRadios(r1,r2):
    if r1 is None or r2 is None:
        return False
    return (r1 == "perro" or r1 == "gato") and (r2 == "m" or r2 == "a")

def validarNumero(numero):
    if numero is None:
        return False
    return numero >= 1 and type(numero) is int

def validarFecha(fecha):
    if fecha is None:
        return False
    try:
        date = datetime.fromisoformat(fecha)
        mindate = datetime.now()
        return bool(re.search(r"^\d{4}\-\d{2}\-\d{2}T\d{2}:\d{2}$", fecha)) \
            and (date - mindate).total_seconds() >= 0
    except Exception as e:
        print(e)
        return False

def validarRegionComuna(region, comuna):
    if region is None or comuna is None:
        return None
    reg = db.get_region_by_name(region)
    if reg is None:
        return False
    comunas = db.get_comunas(reg.id)
    return any(map(lambda com: comuna == com.nombre, comunas))

def validarAviso(
    comuna,
    region,
    nombre,
    email,
    celular,
    tipo,
    cantidad,
    edad,
    unidad_medida,
    fecha_entrega,
    checkboxes,
    sector
) :
    errores = []
    if len(checkboxes) == 0:
        errores.append("Contacto")
    else:
        for (_, ch1, ch2) in checkboxes:
            if not validarCheckbox(ch1, ch2): 
                print(ch1, ch2)
                errores.append("Contacto")
                break
    if not validarEmail(email):
        errores.append("Email")
    if not validarFecha(fecha_entrega):
        errores.append("Fecha")
    if not validarTelefono(celular):
        errores.append("Celular")
    if not validarTexto(nombre, 200, 3):
        errores.append("Nombre")
    if sector is not None and not validarTexto(sector, 100, 1) and sector != "":
        errores.append("Sector")
    if not validarRadios(tipo, unidad_medida[0]):
        errores.append("Tipo o Unidad de medida")
    if not validarNumero(cantidad):
        errores.append("Cantidad")
    if not validarNumero(edad):
        errores.append("Edad")
    if not validarRegionComuna(region, comuna):
        errores.append("Error o comuna")
    return errores