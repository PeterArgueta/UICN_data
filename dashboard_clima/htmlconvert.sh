#!/bin/bash

# Ruta de la carpeta que contiene los archivos HTML
carpeta_html="/home/rainy/Documents/git/dashboard_clima/outputhtml"

# Ruta de la carpeta de salida para los archivos PDF
carpeta_pdf="/home/rainy/Documents/git/dashboard_clima/outputhtml/img"

# Verificar si la carpeta de archivos PDF existe, si no, crearla
if [ ! -d "$carpeta_pdf" ]; then
  mkdir -p "$carpeta_pdf"
fi

# Recorrer los archivos HTML en la carpeta
for archivo_html in "$carpeta_html"/*.html; do
  # Obtener el nombre base del archivo HTML sin la extensión
  nombre_base=$(basename "$archivo_html" .html)

  # Ruta de salida para el archivo PDF
  ruta_pdf="$carpeta_pdf/$nombre_base.png"

  # Convertir el archivo HTML a PDF utilizando wkhtmltopdf con orientación horizontal
 # wkhtmltopdf --orientation Landscape "$archivo_html" "$ruta_pdf"
  wkhtmltoimage --format png "$archivo_html" "$ruta_pdf"
  # Verificar si la conversión fue exitosa
  if [ $? -eq 0 ]; then
    echo "Se ha convertido el archivo $archivo_html a $ruta_pdf"
  else
    echo "Error al convertir el archivo $archivo_html a PDF"
  fi
done

echo "Proceso de conversión completado"

