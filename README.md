# Tarea 4

En esta entrega se incluye todo lo de la tarea 3 en la misma carpeta que la entrega anterior.

La tarea 4 se encuentra incluida dentro del directorio tarea4 junto con todos los archivos necesarios. Esto
es importante a tener en cuenta para poder ejecutar la tarea correctamente.

Ademas, se asumio que la aplicacion web de springboot es completamente independiente de la de flask, por lo
tanto para poder acceder a las dos apis se deben ejecutar ambos programas por separado.

Es por esto que la aplicacion de SpringBoot solo contiene la funcionalidad pedida en el pdf, y nada mas que eso,
pues se asume que lo demas es accesible a traves de otro puerto (el de la app web hecha con flask).

Otra cosa importante es notar que la ruta para el listado es */listado*. Si solo se ejecuta esta aplicación web,
al hacer una peticion a localhost:8080 se redigirá precisamente a esa ruta. El objetivo de esto es evitar problemas
si es que se ejecuta la API de Flask y la de Spring Boot al mismo tiempo. Para ello habría que eliminar esta redirección.
