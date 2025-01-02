
# English Version


**# YouTube Video Downloader**
This repository contains a script to download YouTube videos with automatic subtitles using yt-dlp. Videos are downloaded in `.mp4` format and subtitles in `.vtt` format.
You can specify the subtitle language and the text file containing the URLs of the videos to download.

**## Installation**

### Linux
For the linux installation , refer directly to the github page of [yt-dlp](https://github.com/yt-dlp/yt-dlp/wiki/Installation)

I suggest using directly the pip install

~~~
python3 -m pip install -U "yt-dlp[default]"
~~~


### Windows

For windows, review the last release from the [github repo](https://github.com/yt-dlp/yt-dlp/releases) and put the executable in the same folder as the script. 

**## Requirements**
To run this script, you need **Python 3.12.3** or a compatible version.

**## Included Files**
- `descarga.py`: The main script to execute downloads.
- `prueba.txt`: Example file with URLs to download.
- `español.txt`: File with URLs for Spanish videos.
- `frances.txt`: File with URLs for French videos.

**## Script Usage**
1. Make sure `yt-dlp` is installed in the same directory as the `descarga.py` script.
2. Run the script from the terminal specifying the subtitle language and the URL file. Example:
To download videos with French subtitles using the `url_frances.txt` file:

~~~
python descarga.py fr urls_frances.txt
~~~~

# Spanish version

# YouTube Video Downloader

Este repositorio contiene un script para descargar videos de YouTube con subtítulos automáticos utilizando yt-dlp. Los videos se descargan en formato `.mp4` y los subtitulos en formato `.vtt`.
Puedes especificar el idioma de los subtítulos y el archivo de texto que contiene las URLs de los videos a descargar.

## Instalación

Se usó esta pagina como guía de instalación https://www.rapidseedbox.com/es/blog/yt-dlp-complete-guide 

## Requisitos

Para ejecutar este script, necesitas **Python 3.12.3** o una versión compatible.

## Archivos Incluidos

- `descarga.py`: El script principal para ejecutar las descargas.
- `yt-dlp.exe`: El ejecutable necesario para descargar los videos. Debe estar ubicado en el mismo directorio que el script.
- `prueba.txt`: Archivo de ejemplo con URLs para descargar.
- `español.txt`: Archivo de URLs con videos en español.
- `frances.txt`: Archivo de URLs con videos en francés.

## Uso del Script

1. Asegúrate de que `yt-dlp` esté instalado en el mismo directorio que el script `descarga.py`.
2. Ejecuta el script desde la terminal especificando el idioma de los subtítulos y el archivo con URLs. Ejemplo:

Para descargar videos con subtítulos en francés usando el archivo `frances.txt`:
python descarga.py fr frances.txt
