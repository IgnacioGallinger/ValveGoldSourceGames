@echo off
title Bienvenido al Menu de opciones

:: Variables para los modelos de Half-Life
set MODELOS_PRINCIPAL="C:\Program Files (x86)\ValveGoldSrcGames\valve\models"
set MODELOS_HD="C:\Program Files (x86)\ValveGoldSrcGames\valve\modelshd"
set MODELOS_CLASICOS="C:\Program Files (x86)\ValveGoldSrcGames\valve\modelsclassics"

:: Variables para los modelos de Opposing Force
set OP_MODELOS_PRINCIPAL="C:\Program Files (x86)\ValveGoldSrcGames\gearbox\models"
set OP_MODELOS_HD="C:\Program Files (x86)\ValveGoldSrcGames\gearbox\modelshd"
set OP_MODELOS_CLASICOS="C:\Program Files (x86)\ValveGoldSrcGames\gearbox\modelsclassics"

:: Variables para los modelos de Blue Shift
set BS_MODELOS_PRINCIPAL="C:\Program Files (x86)\ValveGoldSrcGames\bshift\models"
set BS_MODELOS_HD="C:\Program Files (x86)\ValveGoldSrcGames\bshift\modelshd"
set BS_MODELOS_CLASICOS="C:\Program Files (x86)\ValveGoldSrcGames\bshift\modelsclassics"

:: Variables para los bots de distintos juegos
set RICOCHET_BOTS="C:\Program Files (x86)\ValveGoldSrcGames\Half-Life\IgnacioGallinger\ricochetbots"
set TFC_BOTS="C:\Program Files (x86)\ValveGoldSrcGames\IgnacioGallinger\Bots\TeamFortressClassicBots"
set TFC_NO_BOTS="C:\Program Files (x86)\ValveGoldSrcGames\IgnacioGallinger\Bots\TeamFortressClassicNOBots"
set DMC_BOTS="C:\Program Files (x86)\ValveGoldSrcGames\IgnacioGallinger\Bots\DeathmatchClassicBots"
set RICOCHET_BOTS="C:\Program Files (x86)\ValveGoldSrcGames\IgnacioGallinger\Bots\RicochetBots"
set DEST_DMC="C:\Program Files (x86)\ValveGoldSrcGames\dmc"
set DOD_BOTS="C:\Program Files (x86)\ValveGoldSrcGames\Half-Life\IgnacioGallinger\dodbots"

set DEST_RICOCHET="C:\Program Files (x86)\ValveGoldSrcGames\ricochet"
set DEST_TFC="C:\Program Files (x86)\ValveGoldSrcGames"
set DEST_DMC="C:\Program Files (x86)\ValveGoldSrcGames\dmc"
set DEST_DOD="C:\Program Files (x86)\ValveGoldSrcGames\dod"

:: Variables para los documentos
set CREDITS_DOC="C:\Program Files (x86)\ValveGoldSrcGames\IgnacioGallinger\documents\Creditos.docx"
set LEEME_DOC="C:\Program Files (x86)\ValveGoldSrcGames\IgnacioGallinger\documents\Leeme.docx"

:start
cls
echo -Ignacio Gallinger 2024
echo ========================================================
echo              Bienvenido al Menu de opciones
echo ========================================================
echo [0] Salir
echo.
echo [1] Opciones
echo [2] Bots
echo [3] Creditos
echo [4] Leeme
echo [5] Comandos
echo.
set /p choice=Selecciona una opcion (0/1/2/3/4/5): 

if "%choice%"=="0" goto salir
if "%choice%"=="1" goto opciones
if "%choice%"=="2" goto bots
if "%choice%"=="3" goto creditos
if "%choice%"=="4" goto leeme
if "%choice%"=="5" goto comandos
goto start

:creditos
echo Abriendo documento de Creditos...
start "" %CREDITS_DOC%
pause
goto start

:leeme
echo Abriendo documento Leeme...
start "" %LEEME_DOC%
pause
goto start

:comandos
cls
echo ======================================================
echo                         Comandos
echo ======================================================
echo.
echo [0] Volver al menu principal
echo.
echo [1] Comandos de Bots
echo [2] Comandos
echo.
set /p cmd_opcion=Selecciona una opcion: 

if "%cmd_opcion%"=="0" goto start
if "%cmd_opcion%"=="1" goto cmd_bots
if "%cmd_opcion%"=="2" goto cmd_comandos
goto comandos

:cmd_bots
cls
echo ======================================================
echo                   Comandos de Bots
echo ======================================================
echo.
echo  ------Bots de Counter Strike y Condition Zero------
echo.
echo - add_bot           // Agrega un bot a la partida.
echo - add_bot_ct        // Agrega un bot a la partida en el equipo Antiterrorista.
echo - add_bot_t         // Agrega un bot a la partida en el equipo Terrorista.
echo - remove_bot        // Elimina un bot de la partida.
echo - list_bots         // Muestra la lista de bots activos.
echo.
pause
goto comandos

:cmd_comandos
cls
echo ======================================================
echo                       Comandos
echo ======================================================
echo.
echo - sv_cheats 0-1     // Activa y Desactivar los trucos de la partida 
echo - restart           // Reinicia la partida
echo - noclip            // Permite atravesar paredes.
echo - god               // Activa el modo invencible.
echo - sv_gravity X      // Ajusta la gravedad (X es el valor).
echo - impulse 101       // Proporciona todas las armas.
echo - map               // Abre el mapa mencionado (EJ:map c0a0)
echo.
pause
goto comandos

:opciones
cls
echo ======================================================
echo                        Opciones
echo ======================================================
echo.
echo.
echo [0] Volver al menu principal
echo.
echo [1] Configuracion de Modelos 3D
echo.
echo [2] Opciones de Aniversarios
echo.
echo [3] Mas Opciones
echo.
echo.
set /p choicee=Selecciona una opcion: 

if "%choicee%"=="0" goto start
if "%choicee%"=="1" goto models
if "%choicee%"=="2" goto aniversario
if "%choicee%"=="3" goto masopciones

goto opciones

:aniversario
cls
echo.
echo ======================================================
echo               Opciones de Aniversarios
echo ======================================================
echo [0] Volver al menu de Opciones
echo.
echo --------------Half-Life 25th Aniversario--------------
echo.
echo [1] Activar Mapas de 25th Aniversario
echo [2] Desactivar Mapas de 25th Aniversario
echo.
echo (Nota: Los de Valve hicieron unas modificaciones en el motor GoldSrc para el 25th
echo y en esta version de Half-Life los mapas pueden tener bugs, bugs visuales, mal
echo rendimiento, mal funcionamiento, etc.)
echo.
echo [3] Activar Modelos de Jugador del 25th Aniversario
echo [4] Desactivar Modelos de Jugador del 25th Aniversario
echo.
echo.
set /p choice="Elige una opcion: " 

if "%choice%"=="0" goto opciones
if "%choice%"=="1" goto amp25
if "%choice%"=="2" goto dmp25
if "%choice%"=="3" goto am25
if "%choice%"=="4" goto dm25
goto aniversario

:masopciones
cls
echo ======================================================
echo                      Más Opciones
echo ======================================================
echo.
echo [0] Volver al Menu de Opciones
echo.
echo [1] Arreglar Lista de Servidores
echo.
echo [2] Restaurar el menu de opciones a los valores predeterminados
echo.
set /p option=Selecciona una opcion: 

if "%option%"=="0" goto opciones
if "%option%"=="1" goto arreglarls
if "%option%"=="2" goto movalorespre
echo Opcion no valida.
pause
goto masopciones

:arreglarls
echo Modificando archivo MasterServers.vdf...
set archivo="C:\Program Files (x86)\ValveGoldSrcGames\platform\config\MasterServers.vdf"

REM Comprobamos si el archivo existe
if not exist %archivo% (
    echo Archivo no encontrado en %archivo%.
    pause
    goto menu
)

REM Crear un archivo temporal para escribir los datos
set tempArchivo="%TEMP%\MasterServers_temp.vdf"
(
    for /f "tokens=*" %%A in ('findstr /n "^" %archivo%') do (
        set "line=%%A"
        setlocal enabledelayedexpansion
        for /f "delims=:" %%B in ("!line!") do (
            if %%B==5 (	
                echo.
                echo 		"0"
                echo 		{
                echo 			"addr"		"ms.gametracker.com:27010"
                echo 		}
                echo 		"1"
                echo 		{
                echo 			"addr"		"ms.gs4u.net:27010"
                echo 		}
                echo 		"2"
            ) else (
                echo !line:*:=!
            )
        )
        endlocal
    )
) > %tempArchivo%

REM Reemplazamos el archivo original con el modificado
move /y %tempArchivo% %archivo% >nul
echo Archivo actualizado correctamente.
pause
goto masopciones

:amp25
echo Activando mapas de Half-Life 25th Aniversario...
xcopy /e /i /y "C:\Program Files (x86)\ValveGoldSrcGames\IgnacioGallinger\aniversarios\maps\*" "C:\Program Files (x86)\ValveGoldSrcGames\valve\maps"
pause 
goto aniversario

:dmp25
echo Desactivando mapas de Half-Life 25th Aniversario...
del "C:\Program Files (x86)\ValveGoldSrcGames\valve\maps\contamination.bsp" /q
del "C:\Program Files (x86)\ValveGoldSrcGames\valve\maps\disposal.bsp" /q
del "C:\Program Files (x86)\ValveGoldSrcGames\valve\maps\pool_party.bsp" /q
del "C:\Program Files (x86)\ValveGoldSrcGames\valve\maps\rocket_frenzy.bsp" /q
del "C:\Program Files (x86)\ValveGoldSrcGames\valve\maps\xen_dm.bsp" /q
del "C:\Program Files (x86)\ValveGoldSrcGames\valve\maps\graphs\disposal.nod" /q
del "C:\Program Files (x86)\ValveGoldSrcGames\valve\maps\graphs\disposal.nrp" /q
pause
goto aniversario

:am25
echo Activando Modelos de Jugador de Half-Life 25th Aniversario
xcopy /e /i /y "C:\Program Files (x86)\ValveGoldSrcGames\IgnacioGallinger\aniversarios\playermodels" "C:\Program Files (x86)\ValveGoldSrcGames\valve\models\player"
pause
goto aniversario

:dm25
echo Desactivando Modelos de Jugador de Half-Life 25th Aniversario
rmdir "C:\Program Files (x86)\ValveGoldSrcGames\valve\models\player\bbbbarney" /s /q
rmdir "C:\Program Files (x86)\ValveGoldSrcGames\valve\models\player\ivan" /s /q
rmdir "C:\Program Files (x86)\ValveGoldSrcGames\valve\models\player\skeleton" /s /q
rmdir "C:\Program Files (x86)\ValveGoldSrcGames\valve\models\player\tmcm" /s /q
pause
goto aniversario

goto aniversario

:models
cls
echo ======================================================
echo                        Modelos
echo ======================================================
echo.
echo [0] Volver al menu de Opciones
echo.
echo ---------------------- Half-Life ----------------------
echo [1] Activar Modelos Clasicos
echo [2] Activar Modelos HD
echo.
echo ------------------- Opposing Force -------------------
echo [3] Activar Modelos Clasicos
echo [4] Activar Modelos HD
echo.
echo ---------------------- Blue Shift --------------------
echo [5] Activar Modelos Clasicos
echo [6] Activar Modelos HD
echo.
set /p opcion=Selecciona una opcion: 

if "%opcion%"=="0" goto opciones
if "%opcion%"=="1" goto clasico
if "%opcion%"=="2" goto hd
if "%opcion%"=="3" goto op_clasico
if "%opcion%"=="4" goto op_hd
if "%opcion%"=="5" goto bs_clasico
if "%opcion%"=="6" goto bs_hd
goto opciones

:clasico
echo Activando Modelos Clasicos para Half-Life...
xcopy /e /i /y %MODELOS_CLASICOS%\* %MODELOS_PRINCIPAL%\
pause
goto opciones

:hd
echo Activando Modelos HD para Half-Life...
xcopy /e /i /y %MODELOS_HD%\* %MODELOS_PRINCIPAL%\
pause
goto opciones

:op_clasico
echo Activando Modelos Clasicos para Opposing Force...
xcopy /e /i /y %OP_MODELOS_CLASICOS%\* %OP_MODELOS_PRINCIPAL%\
pause
goto opciones

:op_hd
echo Activando Modelos HD para Opposing Force...
xcopy /e /i /y %OP_MODELOS_HD%\* %OP_MODELOS_PRINCIPAL%\
pause
goto opciones

:bs_clasico
echo Activando Modelos Clasicos para Blue Shift...
xcopy /e /i /y %BS_MODELOS_CLASICOS%\* %BS_MODELOS_PRINCIPAL%\
pause
goto opciones

:bs_hd
echo Activando Modelos HD para Blue Shift...
xcopy /e /i /y %BS_MODELOS_HD%\* %BS_MODELOS_PRINCIPAL%\
pause
goto models
:bots
cls
echo ======================================================
echo                         Bots
echo ======================================================
echo.
echo [0] Volver al menu principal
echo.
echo --------------Team Fortress Classic--------------
echo.
echo [1] Activar Bots de "Team Fortress Classic"
echo [2] Desactivar Bots de "Team Fortress Classic"
echo.
echo --------------Deathmatch Classic--------------
echo.
echo [3] Activar Bots de "Deathmatch Classic"
echo [4] Desactivar Bots de "Deathmatch Classic"
echo.
echo ------------------Ricochet------------------
echo.
echo [5] Activar Bots de "Ricochet"
echo [6] Desactivar Bots de "Ricochet"
echo.
echo ------------------Day of Defeat------------------
echo.
echo [7] Activar Bots de "Day of Defeat"
echo [8] Desactivar Bots de "Day of Defeat"
echo.
set /p bots_opcion=Selecciona una opcion: 

if "%bots_opcion%"=="0" goto start
if "%bots_opcion%"=="1" goto bots_tfc_activar
if "%bots_opcion%"=="2" goto bots_tfc_desactivar
if "%bots_opcion%"=="3" goto bots_dmc_activar
if "%bots_opcion%"=="4" goto bots_dmc_desactivar
if "%bots_opcion%"=="5" goto bots_ricochet_activar
if "%bots_opcion%"=="6" goto bots_ricochet_desactivar
if "%bots_opcion%"=="7" goto bots_dod_activar
if "%bots_opcion%"=="8" goto bots_dod_desactivar
goto bots

:bots_tfc_activar
echo Activando Bots de Team Fortress Classic...
xcopy /e /i /y %TFC_BOTS%\* %DEST_TFC%\
pause
goto bots

:bots_tfc_desactivar
echo Desactivando Bots de Team Fortress Classic...
del "C:\Program Files (x86)\ValveGoldSrcGames\tfc\liblist.bak" /q
del "C:\Program Files (x86)\ValveGoldSrcGames\tfc\liblist.gam" /q
del "C:\Program Files (x86)\ValveGoldSrcGames\tfc\addons" /s /q
del "C:\Program Files (x86)\ValveGoldSrcGames\FoxBot" /s /q
xcopy /e /i /y "C:\Program Files (x86)\ValveGoldSrcGames\IgnacioGallinger\Bots\TeamFortressClassicNOBots\*" "C:\Program Files (x86)\ValveGoldSrcGames\tfc\"
pause
goto bots

:bots_dmc_activar
echo Activando Bots de Deathmatch Classic...
xcopy "C:\Program Files (x86)\ValveGoldSrcGames\IgnacioGallinger\Bots\DetahmatchClassicBots\*" "C:\Program Files (x86)\ValveGoldSrcGames\dmc\" /E /H /C /I /Y
pause
goto bots

:bots_dmc_desactivar
echo Desactivando Bots de Deathmatch Classic...
del "C:\Program Files (x86)\ValveGoldSrcGames\dmc\liblist.gam" /q
del "C:\Program Files (x86)\ValveGoldSrcGames\dmc\addons" /s /q
xcopy /e /i /y "C:\Program Files (x86)\ValveGoldSrcGames\IgnacioGallinger\Bots\DetahmatchClassicNOBots\*" "C:\Program Files (x86)\ValveGoldSrcGames\dmc\"
pause
goto bots

:bots_dod_activar
echo Activando Bots de Day of Defeat...

REM Copiar todos los archivos y carpetas desde la carpeta origen al destino, reemplazando si es necesario
xcopy "C:\Program Files (x86)\ValveGoldSrcGames\IgnacioGallinger\Bots\DayOfDefeatBots\*" "C:\Program Files (x86)\ValveGoldSrcGames\dod\" /E /H /C /I /Y

if %errorlevel%==0 (
    echo Bots activados exitosamente en Day of Defeat.
) else (
    echo Error al activar los bots. Por favor, verifica las rutas y permisos.
)

pause
goto bots

:bots_dod_desactivar
echo Desactivando Bots de Day of Defeat...

REM Borrar archivos relacionados con los bots
del "C:\Program Files (x86)\ValveGoldSrcGames\dod\dlls\shrikebot.dll" /q
del "C:\Program Files (x86)\ValveGoldSrcGames\dod\shrikebot" /s /q
REM Restaurar archivo liblist.gam desde la carpeta NOBots
xcopy "C:\Program Files (x86)\ValveGoldSrcGames\IgnacioGallinger\Bots\DayOfDefeatNOBots\liblist.gam" "C:\Program Files (x86)\ValveGoldSrcGames\dod\" /Y

if %errorlevel%==0 (
    echo Bots desactivados exitosamente en Day of Defeat.
) else (
    echo Error al desactivar los bots. Por favor, verifica las rutas y permisos.
)

pause
goto bots

:bots_ricochet_activar
echo Activando Bots de Ricochet...

REM Copiar todos los archivos y carpetas desde la carpeta origen al destino, reemplazando si es necesario
xcopy "C:\Program Files (x86)\ValveGoldSrcGames\IgnacioGallinger\Bots\RicochetBots\*" "C:\Program Files (x86)\ValveGoldSrcGames\ricochet\" /E /H /C /I /Y

if %errorlevel%==0 (
    echo Bots activados exitosamente en Ricochet.
) else (
    echo Error al activar los bots. Por favor, verifica las rutas y permisos.
)

pause
goto bots

:bots_ricochet_desactivar
echo Desactivando Bots de Ricochet...

REM Borrar archivos relacionados con los bots
del "C:\Program Files (x86)\ValveGoldSrcGames\ricochet\liblist.gam" /q
del "C:\Program Files (x86)\ValveGoldSrcGames\ricochet\addons" /s /q
REM Restaurar archivo liblist.gam desde la carpeta NOBots
xcopy "C:\Program Files (x86)\ValveGoldSrcGames\IgnacioGallinger\Bots\RicochetNOBots\liblist.gam" "C:\Program Files (x86)\ValveGoldSrcGames\ricochet\" /Y

if %errorlevel%==0 (
    echo Bots desactivados exitosamente en Ricochet.
) else (
    echo Error al desactivar los bots. Por favor, verifica las rutas y permisos.
)

pause
goto bots

:salir
echo Cerrando el programa. ¡Hasta luego!
exit