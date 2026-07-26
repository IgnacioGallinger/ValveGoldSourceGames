@echo off
echo --- Comprobando el estado de Bots y copiando archivos liblist.gam ---

REM --- VARIABLES DE RUTA PARA OPPOSING FORCE ---
SET OP_BOTS_BASE_DIR="C:\Program Files\ValveGoldSrcGames\IgnacioGallinger\Bots\OpposingForceDeathmtachBots"
SET OP_BOTS_ON_LIB="C:\Program Files\ValveGoldSrcGames\IgnacioGallinger\Bots\OpposingForceDeathmtachBots\liblists\liblist.gam"
SET OP_NO_BOTS_LIB="C:\Program Files\ValveGoldSrcGames\IgnacioGallinger\opposingforcemultiplayermenufixed\m\liblist.gam"
SET OP_DEST_DIR="C:\Program Files\ValveGoldSrcGames\gearbox"

REM --- LÓGICA CONDICIONAL PARA OPPOSING FORCE (gearbox\liblist.gam) ---

IF EXIST %OP_BOTS_BASE_DIR%\botson.txt (
    echo [OPPOSING FORCE: BOTS ACTIVADOS] Copiando liblist.gam CON bots.
    REM Copia el liblist.gam CON bots
    xcopy /Y %OP_BOTS_ON_LIB% %OP_DEST_DIR%
) ELSE (
    REM El archivo botson.txt NO existe, se asume SIN bots.
    echo [OPPOSING FORCE: BOTS DESACTIVADOS] Copiando liblist.gam SIN bots.
    REM Copia el liblist.gam SIN bots
    xcopy /Y %OP_NO_BOTS_LIB% %OP_DEST_DIR%
)

REM --- COPIAS RESTANTES (SIN CAMBIOS) ---

REM Copiar liblist.gam para Counter-Strike (cstrike)
xcopy /Y "C:\Program Files\ValveGoldSrcGames\IgnacioGallinger\counterstrikebotsproblemfixed\CS1.6\liblist.gam" "C:\Program Files\ValveGoldSrcGames\cstrike"
echo liblist.gam de Counter-Strike copiado.

REM Copiar liblist.gam para Half-Life (valve)
xcopy /Y "C:\Program Files\ValveGoldSrcGames\IgnacioGallinger\halflifemultiplayermenufixed\m\liblist.gam" "C:\Program Files\ValveGoldSrcGames\valve"
echo liblist.gam de Half-Life copiado.

echo Archivos liblist.gam actualizados correctamente.
echo Abriendo Servidor Dedicado...

REM Ejecutar el acceso directo
start "" "C:\Program Files\ValveGoldSrcGames\IgnacioGallinger\Games\ds.lnk"

REM Esperar 1 segundo antes de cerrar
timeout /t 1 > nul

exit