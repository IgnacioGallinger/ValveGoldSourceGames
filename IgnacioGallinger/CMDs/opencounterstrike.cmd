@echo off
echo --- Comprobando rutas y copiando archivo ---

REM Copiar el archivo liblist.gam
xcopy /Y "C:\Program Files\ValveGoldSrcGames\IgnacioGallinger\counterstrikebotsproblemfixed\CZ\liblist.gam" "C:\Program Files\ValveGoldSrcGames\cstrike"

echo Archivo copiado correctamente.
echo Abriendo Counter-Strike...

REM Ejecutar el acceso directo
start "" "C:\Program Files\ValveGoldSrcGames\IgnacioGallinger\Games\cs.lnk"

REM Esperar 3 segundos antes de cerrar
timeout /t 3 > nul

exit