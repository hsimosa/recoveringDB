README

Como recuperar data perdida de una base de datos a partir de realizar ocr sobre documentos pdf.

Esta aplicacion es para efectuar recuperacion de la data en una base de datos (DB) mysql que fue eliminada totalmente, pero no asi unos archivos pdf que forman parte de los registros y que contienen la informacion necesaria para restablecer la BD a su nivel.

La aplicacion se basa en el uso de reconocimiento optico de caracteres (OCR) para identificar unos campos especificos de formato pdf y asi poder reconstruir la BD. Mediante el proceso digital OCR de los archivos pdf uno a uno. 

Como los formatos pdf fueron digitalizados manualmente mediante un escaner, no todas las imagenes tienen una buena resolucion, por lo que este proceso no se puede considerar libre del criterio de un operador, bien sea para recuperar la informacion o para identificar el documento que debe ser nuevamente procesado por escaner.

Para ejecutar la aplicacion de manera completa una vez que se baje a un directorio local, se debe agregar el siguiente par de carpetas:/PROCESAR y la carpeta /IMAGENES. Esta ultima guarda temporalmente las imagenes creadas por el proceso de OCR. La primera carpeta guardara la copia de los documentos que va a ser procesados mediante OCR para extraerle los datos necesarios para los registros de la BD.

Usualmente los documentos pdf provienen de una carpeta /archivos con permisos de ejecucion y propietario diferentes a los se usarian para ejecutar esta aplicacion. Esto obliga a tomar en cuenta el PATH a usar en la aplicacion para evitar errores en la ejecucion.
