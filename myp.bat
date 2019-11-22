@echo off
call "C:\Program Files\QGIS 3.4\bin\o4w_env.bat"
call "C:\Program Files\QGIS 3.4\bin\qt5_env.bat"
call "C:\Program Files\QGIS 3.4\bin\py3_env.bat"

@echo on
"C:\Program Files\QGIS 3.4\apps\Python37\Scripts\pyrcc5" -o resources.py resources.qrc