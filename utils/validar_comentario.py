def validar_comentario(nombre, comentario):
    return nombre is not None and comentario is not None and \
        len(nombre) <= 80 and len(nombre) >= 3 and \
        len(comentario) >= 5