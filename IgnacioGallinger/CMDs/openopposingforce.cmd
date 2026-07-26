@echo off
echo --- Comprobando el estado de Bots y copiando liblist.gam ---

REM --- VARIABLES DE RUTA (Asegúrate de que estas rutas son correctas) ---
SET BOTS_BASE_DIR="C:\Program Files\ValveGoldSrcGames\IgnacioGallinger\Bots\OpposingForceDeathmtachBots"
SET BOTS_ON_LIB="C:\Program Files\ValveGoldSrcGames\IgnacioGallinger\Bots\OpposingForceDeathmtachBots\liblists\liblist.gam"
SET NO_BOTS_LIB="C:\Program Files\ValveGoldSrcGames\IgnacioGallinger\opposingforcemultiplayerpicturesfixed\s\liblist.gam"
SET DEST_DIR="C:\Program Files\ValveGoldSrcGames\gearbox"

REM --- LÓGICA CONDICIONAL PARA COPIAR liblist.gam ---

IF EXIST %BOTS_BASE_DIR%\botson.txt (
    echo [ESTADO: BOTS ACTIVADOS] Copiando liblist.gam CON bots.
    REM Copia el liblist.gam CON bots
    xcopy /Y %BOTS_ON_LIB% %DEST_DIR%
) ELSE (
    REM El archivo botson.txt NO existe (o existe botsoff.txt/ninguno), se asume SIN bots.
    echo [ESTADO: BOTS DESACTIVADOS] Copiando liblist.gam SIN bots.
    REM Copia el liblist.gam SIN bots
    xcopy /Y %NO_BOTS_LIB% %DEST_DIR%
)

IF ERRORLEVEL 1 (
    echo ERROR: El archivo liblist.gam NO se pudo copiar.
    pause
    exit
)

echo Archivo liblist.gam actualizado correctamente.
echo Abriendo Half-Life Opposing Force...

REM Ejecutar el acceso directo
start "" "C:\Program Files\ValveGoldSrcGames\IgnacioGallinger\Games\of.lnk"

REM Esperar 3 segundos antes de cerrar
timeout /t 3 > nul

exit