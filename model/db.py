from sqlalchemy import create_engine, desc as descend, extract, func
from sqlalchemy.orm import sessionmaker, declarative_base, relationship

DB_NAME = "tarea2"
DB_USERNAME = "cc5002"
DB_PASSWORD = "programacionweb"
DB_HOST = "localhost"
DB_PORT = 3306

DATABASE_URL = f"mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_engine(DATABASE_URL, echo=False, future=True)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

def get_comunas(region_id):
    from .comuna import Comuna
    session = SessionLocal()
    comunas = session.query(Comuna).filter_by(region_id=region_id).all()
    session.close()
    return comunas

def get_regiones():
    from .region import Region
    session = SessionLocal()
    regiones = session.query(Region).all()
    session.close()
    return regiones

def get_region_by_name(name):
    from .region import Region
    session = SessionLocal()
    region = session.query(Region).filter_by(nombre=name).first()
    return region

def get_region_by_id(id):
    from .region import Region
    session = SessionLocal()
    region = session.query(Region).filter_by(id=id).first()
    return region

def nombre_comuna_por_id(comuna_id):
    from .comuna import Comuna
    session = SessionLocal()
    comuna = session.query(Comuna).filter_by(id=comuna_id).first()
    return comuna

def crear_aviso(comuna_id,
                sector, 
                nombre, 
                email, 
                celular, 
                tipo, 
                cantidad, 
                edad, 
                medida, 
                fecha_entrega, 
                desc):
    from .aviso_adopcion import AvisoAdopcion, TipoAnimal, UnidadMedida
    from datetime import datetime
    session = SessionLocal()
    aviso = AvisoAdopcion(
        fecha_ingreso=datetime.now(),
        comuna_id=comuna_id,
        sector=sector,
        nombre=nombre,
        email=email,
        celular=celular,
        tipo=TipoAnimal[tipo],
        cantidad=cantidad,
        edad=edad,
        unidad_medida=UnidadMedida[medida[0]],
        fecha_entrega=datetime.fromisoformat(fecha_entrega),
        descripcion=desc
    )
    session.add(aviso)
    session.commit()
    id = aviso.id
    session.close()
    return id

def crear_foto(aviso_id, nombre, ruta):
    from .foto import Foto
    session = SessionLocal()
    foto = Foto(
        ruta_archivo=ruta,
        nombre_archivo=nombre,
        aviso_id=aviso_id
    )
    session.add(foto)
    session.commit()
    session.close()

def crear_contacto(nombre, identificador, aviso_id):
    from .contactar_por import ContactarPor, TipoContacto
    session = SessionLocal()
    contacto = ContactarPor(
        nombre=TipoContacto[nombre],
        identificador=identificador,
        aviso_id=aviso_id
    )
    session.add(contacto)
    session.commit()
    session.close()

def ultimos_lista():
    from .aviso_adopcion import AvisoAdopcion
    session = SessionLocal()
    ultimos = session.query(AvisoAdopcion).order_by(descend(AvisoAdopcion.id)).limit(5).all()
    session.close()
    return ultimos

def listado_offset(offs=0):
    from .aviso_adopcion import AvisoAdopcion
    session = SessionLocal()
    ultimos = session.query(AvisoAdopcion).limit(5).offset(offs).all()
    session.close()
    return ultimos

def obtener_foto(aviso_id):
    from .foto import Foto
    session = SessionLocal()
    foto = session.query(Foto).filter_by(aviso_id=aviso_id).first()
    session.close()
    return foto.nombre_archivo

def obtener_fotos(aviso_id):
    from .foto import Foto
    session = SessionLocal()
    fotos = session.query(Foto).filter_by(aviso_id=aviso_id).all()
    session.close()
    return fotos

def numero_fotos(aviso_id):
    from .foto import Foto
    session = SessionLocal()
    count = session.query(Foto).filter_by(aviso_id=aviso_id).count()
    session.close()
    return count

def numero_avisos():
    from .aviso_adopcion import AvisoAdopcion
    session = SessionLocal()
    count = session.query(AvisoAdopcion).count()
    session.close()
    return count

def obtener_aviso(aviso_id):
    from .aviso_adopcion import AvisoAdopcion
    session = SessionLocal()
    aviso = session.query(AvisoAdopcion).filter_by(id=aviso_id).first()
    session.close()
    return aviso

def obtener_contactos(aviso_id):
    from .contactar_por import ContactarPor
    session = SessionLocal()
    contactos = session.query(ContactarPor).filter_by(id=aviso_id).all()
    session.close()
    return contactos

def numero_avisos_tipo(tipo):
    from .aviso_adopcion import AvisoAdopcion
    session = SessionLocal()
    num = session.query(AvisoAdopcion).filter_by(tipo=tipo).count()
    session.close()
    return num

def numero_avisos_mes_tipo(mes, tipo):
    from .aviso_adopcion import AvisoAdopcion
    from datetime import datetime
    año_actual = datetime.now().year
    session = SessionLocal()
    num = session.query(AvisoAdopcion).filter_by(tipo=tipo).filter(
        extract('month', AvisoAdopcion.fecha_ingreso) == mes,
        extract('year', AvisoAdopcion.fecha_ingreso) == año_actual
    ).count()
    session.close()
    return num

def numero_avisos_mes():
    from .aviso_adopcion import AvisoAdopcion
    from datetime import datetime
    session = SessionLocal()
    mes_actual = datetime.now().month
    año_actual = datetime.now().year
    avisos_del_mes = session.query(extract('day', AvisoAdopcion.fecha_ingreso), extract('month', AvisoAdopcion.fecha_ingreso), extract('year', AvisoAdopcion.fecha_ingreso), func.count(AvisoAdopcion.id)).filter(
        extract('month', AvisoAdopcion.fecha_ingreso) == mes_actual,
        extract('year', AvisoAdopcion.fecha_ingreso) == año_actual
    ).group_by(extract('day', AvisoAdopcion.fecha_ingreso), extract('month', AvisoAdopcion.fecha_ingreso), extract('year', AvisoAdopcion.fecha_ingreso)).all()
    session.close()
    return avisos_del_mes

def agregar_comentario(nombre, comentario, aviso_id):
    from .comentario import Comentario
    from datetime import datetime
    now = datetime.now()
    session = SessionLocal()
    comentario = Comentario(nombre=nombre, texto=comentario, aviso_id=aviso_id, fecha=now)
    session.add(comentario)
    session.commit()
    session.close()

def obtener_comentarios(aviso_id):
    from .comentario import Comentario
    session = SessionLocal()
    comentarios = session.query(Comentario).filter_by(aviso_id=aviso_id).all()
    session.close()
    return comentarios