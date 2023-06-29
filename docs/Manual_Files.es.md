



# Archivos
  
Administra tus archivos y carpetas, abre y lee archivos, controla su existencia y obten sus meta datos.  

*Read this in other languages: [English](Manual_Files.md), [Português](Manual_Files.pr.md), [Español](Manual_Files.es.md)*
  
![banner](imgs/Banner_Files.png)
## Como instalar este módulo
  
Para instalar el módulo en Rocketbot Studio, se puede hacer de dos formas:
1. Manual: __Descargar__ el archivo .zip y descomprimirlo en la carpeta modules. El nombre de la carpeta debe ser el mismo al del módulo y dentro debe tener los siguientes archivos y carpetas: \__init__.py, package.json, docs, example y libs. Si tiene abierta la aplicación, refresca el navegador para poder utilizar el nuevo modulo.
2. Automática: Al ingresar a Rocketbot Studio sobre el margen derecho encontrara la sección de **Addons**, seleccionar **Install Mods**, buscar el modulo deseado y presionar install.  



# Como usar este modulo




## Descripción de los comandos

### Abrir carpeta
  
Abre la carpeta contenedora de un archivo
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Ruta de la carpeta |Abre la carpeta de la ruta especificada|C:/User/Usuario/Folder/|
|Asignar resultado a variable||Variable|

### Abrir Archivo
  
Abre un archivo 
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Ruta del archivo |Abre el archivo de la ruta especificada|C:/User/Usuario/Folder/File.extension|
|Asignar resultado a variable||Variable|

### Seleccionar archivo
  
Pide al usuario seleccionar un archivo
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Nombre de la varible donde guardar el path|Al ejecutarlo se abre el explorador de archivos para que podamos seleccionar el archivo, una vez seleccionado nos devuelve la dirección donde se encuentra|Result|

### Seleccionar carpeta
  
Pide al usuario seleccionar una carpeta
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Nombre de la varible donde guardar el path|Al ejecutarse se abre el explorador de archivos para que seleccionemos la carpeta que deseemos, una vez seleccionado nos devuelve la ruta donde se aloja|Result|

### Renombrar carpeta
  
Pide al usuario seleccionar una carpeta para cambiarle el nombre
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Direção da pasta a renomear |Al ejecutar se renombra la carpeta que hayamos especificado|C:/User/Folder/|
|Nuevo nombre de la carpeta||Nuevo nombre|
|Asignar resultado a variable||Variable|

### Leer archivo
  
Lee un archivo y guarda su contenido en una variable
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Ruta de archivo||C:/Users/User/Desktop/file.txt|
|Separar cada línea|Devuelve el contenido de un archivo y lo almacena en una varibale, si se tilda la opcion separar lineas devuelve el contenido del archivo dentro de una lista y cada linea es un elemento dentro de la lista||
|Asignar resultado a variable|Variable donde se almacenara el valor obtenido|Variable|

### Elimina una carpeta
  
Elimina una carpeta con todos sus archivos
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Ruta de la carpeta |Selecciona la ruta de la carpeta a eliminar|C:/User/Usuario/Folder/|
|Asignar resultado a variable||Variable|

### Elimina un archivo
  
Elimina un archivo indicando su extensión y su nombre o parte del nombre
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Ruta de la carpeta |Ruta del archivo a eliminar|C:/User/Usuario/Folder/|
|Tipo de archivo a eliminar|Nombre y extension del archivo a eliminar|nombre*.pdf|
|Asignar resultado a variable||Variable|

### Crear Carpeta
  
Ingrese la ruta y nombre donde quiere crear la carpeta
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Ruta y nombre de carpeta|Ruta donde se creara la carpeta|C:/Users/User/Desktop/folder_test|
|Asignar resultado a variable||Variable|

### Comprobar existencia
  
Comprueba si existe un archivo o carpeta
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Ruta de la carpeta |Direccion de la carpeta a la que se desea comprobar la existencia|C:/User/Usuario/Folder/|
|Asignar resultado a variable||Variable|

### Listar archivos ordenados
  
Lista archivos y selecciona el orden
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Ruta de la carpeta |Direccion de la carpeta de la cual se quiere listar los archivos|C:/User/Usuario/Folder/|
|Ordenar por |Opciones para ordenar, Nombre, Fecha y Tipo||
|Asignar resultado a variable|Variable donde se almacena la lista de elementos de la carpeta|Variable|

### Buscar Archivo
  
Devuelve una lista con coincidencias
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Ruta de la carpeta |Direccion donde se buscara el archivo|C:/User/Usuario/Folder/|
|Filtrar por extensión|Filtra por extension buscando asi todos los archivos con la extension especificada|.pdf|
|Palabra a buscar|Palabra a buscar en el nombre del archivo|fileTest|
|Asignar resultado a variable|Variable donde se almacenaran los nombres de los archivos|Variable|

### Obtener Metadatos
  
Obtiene los metadatos de archivos como: Nombre, fecha de modificación, fecha de creación  y peso del archivo.
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Ruta de los archivos |Direccion donde se buscaran los archivos deseados|C:/User/Usuario/Folder/|
|Seleccionar Metadato|Opciones para obtener todos o un determinado metadato||
|Seleccionar unidad|Devuelve el peso el archivo en la medida especificada|KB, MB o GB|
|Filtrar por nombre|Palabra que deseamos buscar en el nombre del archivo|fileTest|
|Filtrar por extensión|Extension que desamos buscar en los archivos|.pdf|
|Asignar resultado a variable|Variable donde se almacenaran los archivos encontrados|Variable|
