import filetype

def validar_archivo(archivo):
    ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "gif"}
    ALLOWED_MIMETYPES = {"image/jpeg", "image/png", "image/gif"}
    if archivo is None:
        return False
    if archivo.filename == "":
        return False
    ftype_guess = filetype.guess(archivo)
    if ftype_guess.extension not in ALLOWED_EXTENSIONS:
        return False
    if ftype_guess.mime not in ALLOWED_MIMETYPES:
        return False
    return True