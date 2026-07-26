import tkinter as tk
from tkinter import messagebox
import os
import shutil
import requests
from bs4 import BeautifulSoup
import re
import webbrowser
from PIL import Image, ImageTk

# --- VARIABLES Y CONSTANTES ---
# Directorios base del juego
VALVE = "C:\\Program Files\\ValveGoldSrcGames\\valve"
GEARBOX = "C:\\Program Files\\ValveGoldSrcGames\\gearbox"
BSHIFT = "C:\\Program Files\\ValveGoldSrcGames\\bshift"
IGNACIO_GALLINGER = "C:\\Program Files\\ValveGoldSrcGames\\IgnacioGallinger"
PLATFORM = "C:\\Program Files\\ValveGoldSrcGames\\platform"
CSTRIKE = "C:\\Program Files\\ValveGoldSrcGames\\cstrike"
CZERO = "C:\\Program Files\\ValveGoldSrcGames\\czero"
DEST_TFC = "C:\\Program Files\\ValveGoldSrcGames\\tfc"
DEST_DMC = "C:\\Program Files\\ValveGoldSrcGames\\dmc"
DEST_RICOCHET = "C:\\Program Files\\ValveGoldSrcGames\\ricochet"
DEST_DOD = "C:\\Program Files\\ValveGoldSrcGames\\dod"

# Directorios de contenido
ANIVERSARIOS = os.path.join(IGNACIO_GALLINGER, "aniversarios")
MODELOS_PRINCIPAL = os.path.join(VALVE, "models")
MODELOS_HD = os.path.join(VALVE, "modelshd")
MODELOS_CLASICOS = os.path.join(VALVE, "modelsclassics")

OP_MODELOS_PRINCIPAL = os.path.join(GEARBOX, "models")
OP_MODELOS_HD = os.path.join(GEARBOX, "modelshd")
OP_MODELOS_CLASICOS = os.path.join(GEARBOX, "modelsclassics")

# Definiciones AÑADIDAS para BLUE SHIFT (BSHIFT)
BS_MODELOS_PRINCIPAL = os.path.join(BSHIFT, "models")
BS_MODELOS_HD = os.path.join(BSHIFT, "modelshd")
BS_MODELOS_CLASICOS = os.path.join(BSHIFT, "modelsclassics")

TFC_BOTS = os.path.join(IGNACIO_GALLINGER, "Bots", "TeamFortressClassicBots", "tfc")
DMC_BOTS = os.path.join(IGNACIO_GALLINGER, "Bots", "DeathmatchClassicBots")
RICOCHET_BOTS = os.path.join(IGNACIO_GALLINGER, "Bots", "RicochetBots")
DOD_BOTS = os.path.join(IGNACIO_GALLINGER, "Bots", "DayOfDefeatBots")

# DIRECTORIOS PARA BOTS (HLDM y OFDM)
HLDM_BOTS_BASE = os.path.join(IGNACIO_GALLINGER, "Bots", "HalfLifeDeathmtachBots")
HLDM_BOTS_ADDONS = os.path.join(HLDM_BOTS_BASE, "addons")
HLDM_BOTS_DLLS_SRC = os.path.join(HLDM_BOTS_BASE, "dlls", "sandbot.dll")
HLDM_BOTS_STATUS = os.path.join(HLDM_BOTS_BASE, "status")
HLDM_BOTS_DLLS_DEST = os.path.join(VALVE, "dlls")
HLDM_BOTS_ADDONS_DEST = os.path.join(VALVE, "addons")

OFDM_BOTS_BASE = os.path.join(IGNACIO_GALLINGER, "Bots", "OpposingForceDeathmtachBots")
OFDM_BOTS_ADDONS = os.path.join(OFDM_BOTS_BASE, "addons")
OFDM_BOTS_DLLS_SRC = os.path.join(OFDM_BOTS_BASE, "dlls", "sandbot.dll")
OFDM_BOTS_STATUS = os.path.join(OFDM_BOTS_BASE, "status")
OFDM_BOTS_DLLS_DEST = os.path.join(GEARBOX, "dlls")
OFDM_BOTS_ADDONS_DEST = os.path.join(GEARBOX, "addons")

# Documentos
DOCUMENTACION_DOC = os.path.join(IGNACIO_GALLINGER, "documents", "ValveGoldSrc.docx")
LEEME_DOC = os.path.join(IGNACIO_GALLINGER, "documents", "Leeme.txt")
COMANDOS_DOC = os.path.join(IGNACIO_GALLINGER, "documents", "comandoshtml", "index.html")

# URL y versión instalada
GOOGLE_DRIVE_URL = "https://drive.google.com/file/d/1fP46sdjd9kZTAe_u84VZxNVIa5VbvQL_/view"
INSTALLED_VERSION = "1.0"

# --- FUNCIONES COMUNES ---

def mostrar_mensaje(mensaje):
    messagebox.showinfo("Información", mensaje)

def mostrar_cargando():
    cargando = tk.Toplevel(ventana)
    cargando.title("Cargando...")
    cargando.geometry("300x100")
    label = tk.Label(cargando, text="Por Favor no apague la PC", font=("Arial", 14))
    label.pack(expand=True, fill="both", padx=10, pady=10)
    cargando.update()
    return cargando

def copiar_archivos(origen, destino, mensaje_exito="Archivos copiados con éxito."):
    cargando = mostrar_cargando()
    try:
        # Crea el directorio padre si no existe (importante para DLLs y archivos sueltos)
        os.makedirs(os.path.dirname(destino) if not os.path.isdir(origen) else destino, exist_ok=True)
        
        if os.path.isdir(origen):
            # Copia el contenido de la carpeta (dirs_exist_ok=True para merge)
            shutil.copytree(origen, destino, dirs_exist_ok=True)
        else:
            # Copia un único archivo
            shutil.copy2(origen, destino)
        cargando.destroy()
        mostrar_mensaje(mensaje_exito)
    except Exception as e:
        cargando.destroy()
        mostrar_mensaje(f"Error al copiar archivos: {e}")

def eliminar_archivos(ruta, mensaje_exito="Archivos eliminados con éxito."):
    cargando = mostrar_cargando()
    try:
        if os.path.isdir(ruta):
            shutil.rmtree(ruta)
        else:
            os.remove(ruta)
        cargando.destroy()
        mostrar_mensaje(mensaje_exito)
    except FileNotFoundError:
        # Si no se encuentra el archivo/carpeta, se considera exitoso para el propósito de "desactivar"
        cargando.destroy()
        mostrar_mensaje(mensaje_exito)
    except Exception as e:
        cargando.destroy()
        mostrar_mensaje(f"Error al eliminar archivos: {e}")

def abrir_documento(ruta):
    try:
        os.startfile(ruta)
    except Exception as e:
        mostrar_mensaje(f"Error al abrir el documento: {e}")

def abrir_url_docs():
    webbrowser.open("https://docs.google.com/document/d/16J2kposcrYTsmSms5Je_0ZucM0e-Axsr/edit?usp=drive_link&ouid=105871175129988172205&rtpof=true&sd=true")
def abrir_url_github():
    webbrowser.open("https://github.com/IgnacioGallinger/ValveGoldSourceGames")
def abrir_url_youtube():
    webbrowser.open("https://www.youtube.com/@ignaciogallinger1184")

def cambiar_color_entrada(event):
    event.widget.config(bg="gray")

def cambiar_color_salida(event):
    # Usa event.widget.winfo_toplevel().cget('bg') para obtener el color de fondo de la ventana
    # o simplemente "SystemButtonFace" para el color por defecto del botón.
    event.widget.config(bg="SystemButtonFace")

def cambiar_color_clic(event):
    event.widget.config(bg="yellow")

def cambiar_ventana(nueva_ventana):
    for widget in ventana.winfo_children():
        widget.destroy()
    nueva_ventana()

# --- FUNCIÓN: VERIFICAR LA EXISTENCIA DE LOS ARCHIVOS CRÍTICOS ---
def verificar_archivos_bots():
    """Verifica si todos los archivos y carpetas críticos para cada bot existen
       en la carpeta de origen de IgnacioGallinger."""
       
    # Rutas absolutas para Day of Defeat
    DOD_BOT_DLL = os.path.join(DOD_BOTS, "dlls", "shrikebot.dll")
    DOD_BOT_FOLDER = os.path.join(DOD_BOTS, "shrikebot")
    
    # Rutas absolutas para Deathmatch Classic
    DMC_METAMOD = os.path.join(DMC_BOTS, "addons", "metamod")
    DMC_PARABOT = os.path.join(DMC_BOTS, "addons", "parabot")
    
    # Rutas absolutas para Ricochet
    RICOCHET_BOTS_BASE = os.path.join(IGNACIO_GALLINGER, "Bots", "RicochetBots")
    RICOCHET_RICOBOT = os.path.join(RICOCHET_BOTS_BASE, "ricobot")
    RICOCHET_NAMES = os.path.join(RICOCHET_BOTS_BASE, "bot_names.txt")
    RICOCHET_WHINE = os.path.join(RICOCHET_BOTS_BASE, "bot_whine.txt")

    # Rutas absolutas para Team Fortress Classic
    TFC_BOTS_BASE = os.path.join(IGNACIO_GALLINGER, "Bots", "TeamFortressClassicBots")
    TFC_FOXBOT = os.path.join(TFC_BOTS_BASE, "FoxBot")
    TFC_TFC_MOD = os.path.join(TFC_BOTS_BASE, "tfc")

    # Rutas absolutas para Half-Life (Deathmatch)
    HLDM_ADDONS = os.path.join(HLDM_BOTS_BASE, "addons")
    HLDM_DLLS = os.path.join(HLDM_BOTS_BASE, "dlls")
    HLDM_STATUS = os.path.join(HLDM_BOTS_BASE, "status")
    
    # Rutas absolutas para Opposing Force (Deathmatch)
    OFDM_ADDONS = os.path.join(OFDM_BOTS_BASE, "addons")
    OFDM_DLLS = os.path.join(OFDM_BOTS_BASE, "dlls")
    OFDM_STATUS = os.path.join(OFDM_BOTS_BASE, "status")
    
    # Define la lógica de verificación para cada juego
    estado_bots = {}
    
    # Day of Defeat: Ambos deben existir
    estado_bots['Day of Defeat'] = (
        os.path.exists(DOD_BOT_DLL) and os.path.isdir(DOD_BOT_FOLDER)
    )
    
    # Deathmatch Classic: Ambas carpetas deben existir
    estado_bots['Deathmatch Classic'] = (
        os.path.isdir(DMC_METAMOD) and os.path.isdir(DMC_PARABOT)
    )
    
    # Half-Life (Deathmatch): Las 3 carpetas deben existir
    estado_bots['Half-Life (Deathmatch)'] = (
        os.path.isdir(HLDM_ADDONS) and os.path.isdir(HLDM_DLLS) and os.path.isdir(HLDM_STATUS)
    )
    
    # Opposing Force (Deathmatch): Las 3 carpetas deben existir
    estado_bots['Opposing Force (Deathmatch)'] = (
        os.path.isdir(OFDM_ADDONS) and os.path.isdir(OFDM_DLLS) and os.path.isdir(OFDM_STATUS)
    )
    
    # Ricochet: Carpeta y 2 archivos deben existir
    estado_bots['Ricochet'] = (
        os.path.isdir(RICOCHET_RICOBOT) and 
        os.path.exists(RICOCHET_NAMES) and 
        os.path.exists(RICOCHET_WHINE)
    )
    
    # Team Fortress Classic: Ambas carpetas deben existir
    estado_bots['Team Fortress Classic'] = (
        os.path.isdir(TFC_FOXBOT) and os.path.isdir(TFC_TFC_MOD)
    )
    
    return estado_bots


# --- FUNCIONES DE GESTIÓN DE BOTS (HLDM y OFDM) ---

def gestionar_estado_bots(base_dir, activar=True):
    estado_dir = os.path.join(base_dir, "status")
    
    if activar:
        archivo_a_borrar = os.path.join(base_dir, "botsoff.txt")
        archivo_a_copiar_src = os.path.join(estado_dir, "botson.txt")
        archivo_a_copiar_dest = os.path.join(base_dir, "botson.txt")
    else:
        archivo_a_borrar = os.path.join(base_dir, "botson.txt")
        archivo_a_copiar_src = os.path.join(estado_dir, "botsoff.txt")
        archivo_a_copiar_dest = os.path.join(base_dir, "botsoff.txt")
        
    try:
        # 1. Borrar el archivo contrario si existe (ignorar si no se encuentra)
        if os.path.exists(archivo_a_borrar):
            os.remove(archivo_a_borrar)
        
        # 2. Copiar el archivo de estado
        shutil.copy2(archivo_a_copiar_src, archivo_a_copiar_dest)
    except FileNotFoundError:
        pass
    except Exception as e:
        print(f"Advertencia: Error al gestionar el archivo de estado {base_dir}: {e}")

def activar_bots_hldm():
    cargando = mostrar_cargando()
    try:
        shutil.copytree(HLDM_BOTS_ADDONS, HLDM_BOTS_ADDONS_DEST, dirs_exist_ok=True)
        os.makedirs(HLDM_BOTS_DLLS_DEST, exist_ok=True)
        shutil.copy2(HLDM_BOTS_DLLS_SRC, os.path.join(HLDM_BOTS_DLLS_DEST, "sandbot.dll"))
        gestionar_estado_bots(HLDM_BOTS_BASE, activar=True)
        cargando.destroy()
        mostrar_mensaje("Bots de Half-Life Deathmatch activados con éxito.")
    except Exception as e:
        cargando.destroy()
        mostrar_mensaje(f"Error al activar bots HLDM: {e}")

def desactivar_bots_hldm():
    cargando = mostrar_cargando()
    try:
        ruta_dll = os.path.join(HLDM_BOTS_DLLS_DEST, "sandbot.dll")
        if os.path.exists(ruta_dll):
            os.remove(ruta_dll)
        ruta_metamod = os.path.join(HLDM_BOTS_ADDONS_DEST, "metamod")
        if os.path.exists(ruta_metamod):
            shutil.rmtree(ruta_metamod)
        gestionar_estado_bots(HLDM_BOTS_BASE, activar=False)
        cargando.destroy()
        mostrar_mensaje("Bots de Half-Life Deathmatch desactivados con éxito.")
    except Exception as e:
        cargando.destroy()
        mostrar_mensaje(f"Error al desactivar bots HLDM: {e}")

def activar_bots_ofdm():
    cargando = mostrar_cargando()
    try:
        shutil.copytree(OFDM_BOTS_ADDONS, OFDM_BOTS_ADDONS_DEST, dirs_exist_ok=True)
        os.makedirs(OFDM_BOTS_DLLS_DEST, exist_ok=True)
        shutil.copy2(OFDM_BOTS_DLLS_SRC, os.path.join(OFDM_BOTS_DLLS_DEST, "sandbot.dll"))
        gestionar_estado_bots(OFDM_BOTS_BASE, activar=True)
        cargando.destroy()
        mostrar_mensaje("Bots de Opposing Force Deathmatch activados con éxito.")
    except Exception as e:
        cargando.destroy()
        mostrar_mensaje(f"Error al activar bots OFDM: {e}")

def desactivar_bots_ofdm():
    cargando = mostrar_cargando()
    try:
        ruta_dll = os.path.join(OFDM_BOTS_DLLS_DEST, "sandbot.dll")
        if os.path.exists(ruta_dll):
            os.remove(ruta_dll)
        ruta_metamod = os.path.join(OFDM_BOTS_ADDONS_DEST, "metamod")
        if os.path.exists(ruta_metamod):
            shutil.rmtree(ruta_metamod)
        gestionar_estado_bots(OFDM_BOTS_BASE, activar=False)
        cargando.destroy()
        mostrar_mensaje("Bots de Opposing Force Deathmatch desactivados con éxito.")
    except Exception as e:
        cargando.destroy()
        mostrar_mensaje(f"Error al desactivar bots OFDM: {e}")

# --- OTRAS FUNCIONES (Mantenidas para ser completas) ---

def activar_sprays_25th():
    cargando = mostrar_cargando()
    logos_folder = os.path.join(VALVE, "logos")
    source_folder = os.path.join(IGNACIO_GALLINGER, "aniversarios", "sprays", "sprays25th")
    if not os.path.exists(source_folder):
        cargando.destroy()
        mostrar_mensaje(f"La carpeta de sprays (sprays25th) no existe:\n{source_folder}")
        return
    try:
        if os.path.exists(logos_folder):
            for item in os.listdir(logos_folder):
                item_path = os.path.join(logos_folder, item)
                if os.path.isdir(item_path):
                    shutil.rmtree(item_path)
                else:
                    os.remove(item_path)
        
        for item in os.listdir(source_folder):
            src_item = os.path.join(source_folder, item)
            dest_item = os.path.join(logos_folder, item)
            if os.path.isdir(src_item):
                shutil.copytree(src_item, dest_item, dirs_exist_ok=True)
            else:
                shutil.copy2(src_item, dest_item)
        cargando.destroy()
        mostrar_mensaje("Sprays del 25th Aniversario activados con éxito.")
    except Exception as e:
        cargando.destroy()
        mostrar_mensaje(f"Error al activar sprays del 25th Aniversario: {e}")

def desactivar_sprays_25th():
    cargando = mostrar_cargando()
    logos_folder = os.path.join(VALVE, "logos")
    source_folder = os.path.join(IGNACIO_GALLINGER, "aniversarios", "sprays", "spraysNO25th")
    if not os.path.exists(source_folder):
        cargando.destroy()
        mostrar_mensaje(f"La carpeta de sprays (spraysNO25th) no existe:\n{source_folder}")
        return
    try:
        if os.path.exists(logos_folder):
            for item in os.listdir(logos_folder):
                item_path = os.path.join(logos_folder, item)
                if os.path.isdir(item_path):
                    shutil.rmtree(item_path)
                else:
                    os.remove(item_path)
        for item in os.listdir(source_folder):
            src_item = os.path.join(source_folder, item)
            dest_item = os.path.join(logos_folder, item)
            if os.path.isdir(src_item):
                shutil.copytree(src_item, dest_item, dirs_exist_ok=True)
            else:
                shutil.copy2(src_item, dest_item)
        cargando.destroy()
        mostrar_mensaje("Sprays del 25th Aniversario desactivados con éxito.")
    except Exception as e:
        cargando.destroy()
        mostrar_mensaje(f"Error al desactivar sprays del 25th Aniversario: {e}")

def desactivar_mapas_aniversario():
    cargando = mostrar_cargando()
    archivos = ["contamination.bsp", "disposal.bsp", "pool_party.bsp", "rocket_frenzy.bsp", "xen_dm.bsp"]
    errores = []
    for mapa in archivos:
        ruta = os.path.join(VALVE, "maps", mapa)
        try:
            if os.path.exists(ruta):
                os.remove(ruta)
        except Exception as e:
            errores.append(f"Error al eliminar {mapa}: {e}")
    cargando.destroy()
    if errores:
        mostrar_mensaje("Se encontraron errores al eliminar los mapas:\n" + "\n".join(errores))
    else:
        mostrar_mensaje("Mapas del 25th Aniversario desactivados con éxito.")

def desactivar_modelos_aniversario():
    cargando = mostrar_cargando()
    modelos = ["bbbbarney", "ivan", "skeleton", "tmcm"]
    errores = []
    for modelo in modelos:
        ruta = os.path.join(VALVE, "models", "player", modelo)
        try:
            if os.path.exists(ruta):
                if os.path.isdir(ruta):
                    shutil.rmtree(ruta)
                else:
                    os.remove(ruta)
        except Exception as e:
            errores.append(f"Error al eliminar {modelo}: {e}")
    
    cargando.destroy()
    if errores:
        mostrar_mensaje("Se encontraron errores al eliminar los modelos:\n" + "\n".join(errores))
    else:
        mostrar_mensaje("Modelos del 25th Aniversario desactivados con éxito.")

def desactivar_bots_dod():
    cargando = mostrar_cargando()
    try:
        rutas_eliminar = [
            os.path.join(DEST_DOD, "liblist.gam"),
            os.path.join(DEST_DOD, "dlls", "shrikebot.dll"),
            os.path.join(DEST_DOD, "shrikebot")
        ]
        for ruta in rutas_eliminar:
            if os.path.exists(ruta):
                if os.path.isdir(ruta):
                    shutil.rmtree(ruta)
                else:
                    os.remove(ruta)
        origen = os.path.join(IGNACIO_GALLINGER, "Bots", "DayOfDefeatNOBots", "liblist.gam")
        destino = os.path.join(DEST_DOD, "liblist.gam")
        shutil.copy2(origen, destino)
        cargando.destroy()
        mostrar_mensaje("Bots de Day of Defeat desactivados con éxito.")
    except Exception as e:
        cargando.destroy()
        mostrar_mensaje(f"Error al desactivar bots DOD: {e}")

def desactivar_bots_tfc():
    cargando = mostrar_cargando()
    try:
        rutas_eliminar = [
            os.path.join(DEST_TFC, "addons", "metamod"),
            os.path.join(DEST_TFC, "liblist.gam"),
            os.path.join(DEST_TFC, "liblist.bak")
        ]
        for ruta in rutas_eliminar:
            if os.path.exists(ruta):
                if os.path.isdir(ruta):
                    shutil.rmtree(ruta)
                else:
                    os.remove(ruta)
        origen = os.path.join(IGNACIO_GALLINGER, "Bots", "TeamFortressClassicNOBots", "liblist.gam")
        destino = os.path.join(DEST_TFC, "liblist.gam")
        shutil.copy2(origen, destino)
        cargando.destroy()
        mostrar_mensaje("Bots de Team Fortress Classic desactivados con éxito.")
    except Exception as e:
        cargando.destroy()
        mostrar_mensaje(f"Error al desactivar bots TFC: {e}")

def desactivar_bots_dmc():
    cargando = mostrar_cargando()
    try:
        rutas_eliminar = [
            os.path.join(DEST_DMC, "addons", "metamod"),
            os.path.join(DEST_DMC, "addons", "parabot"),
            os.path.join(DEST_DMC, "liblist.gam")
        ]
        for ruta in rutas_eliminar:
            if os.path.exists(ruta):
                if os.path.isdir(ruta):
                    shutil.rmtree(ruta)
                else:
                    os.remove(ruta)
        origen = os.path.join(IGNACIO_GALLINGER, "Bots", "DeathmatchClassicNOBots", "liblist.gam")
        destino = os.path.join(DEST_DMC, "liblist.gam")
        shutil.copy2(origen, destino)
        cargando.destroy()
        mostrar_mensaje("Bots de Deathmatch Classic desactivados con éxito.")
    except Exception as e:
        cargando.destroy()
        mostrar_mensaje(f"Error al desactivar bots DMC: {e}")

def desactivar_bots_ricochet():
    cargando = mostrar_cargando()
    try:
        rutas_eliminar = [
            os.path.join(DEST_RICOCHET, "ricobot"),
            os.path.join(DEST_RICOCHET, "bot_names.txt"), # Corregido de "bot_names" a "bot_names.txt"
            os.path.join(DEST_RICOCHET, "bot_whine.txt"), # Corregido de "bot_whine" a "bot_whine.txt"
            os.path.join(DEST_RICOCHET, "liblist.gam")
        ]
        for ruta in rutas_eliminar:
            if os.path.exists(ruta):
                if os.path.isdir(ruta):
                    shutil.rmtree(ruta)
                else:
                    os.remove(ruta)
        origen = os.path.join(IGNACIO_GALLINGER, "Bots", "RicochetNOBots", "liblist.gam")
        destino = os.path.join(DEST_RICOCHET, "liblist.gam")
        shutil.copy2(origen, destino)
        cargando.destroy()
        mostrar_mensaje("Bots de Ricochet desactivados con éxito.")
    except Exception as e:
        cargando.destroy()
        mostrar_mensaje(f"Error al desactivar bots Ricochet: {e}")

def procesar_cambio_modelos(tipo):
    """
    Función centralizada para evitar repetición de código.
    tipo: 'steam' o 'nosteam'
    """
    cargando = mostrar_cargando()
    try:
        # Configuración de carpetas y archivos
        player_folders = ["arctic", "gign", "gsg9", "guerilla", "leet", "sas", "terror", "urban", "vip"]
        vgui_files = ["arctic.tga", "gign.tga", "gsg9.tga", "guerilla.tga",
                      "leet.tga", "sas.tga", "terror.tga", "urban.tga", "vip.tga"]

        # Determinar carpeta de origen según el botón presionado
        carpeta_origen = "cstrikesteamplayers" if tipo == "steam" else "cstrikenosteamplayers"
        
        # Rutas completas
        ruta_base_origen = os.path.join(IGNACIO_GALLINGER, carpeta_origen)
        origen_vgui = os.path.join(ruta_base_origen, "vgui")
        origen_player = os.path.join(ruta_base_origen, "player")

        destino_vgui = os.path.join(CSTRIKE, "gfx", "vgui")
        destino_player = os.path.join(CSTRIKE, "models", "player")

        # --- 1. Procesar VGUI (.tga) ---
        if os.path.exists(origen_vgui):
            # Nos aseguramos de que el destino exista
            os.makedirs(destino_vgui, exist_ok=True)
            for archivo in vgui_files:
                ruta_archivo_src = os.path.join(origen_vgui, archivo)
                if os.path.exists(ruta_archivo_src):
                    shutil.copy2(ruta_archivo_src, destino_vgui)

        # --- 2. Procesar Modelos (.mdl) ---
        if os.path.exists(origen_player):
            for folder in player_folders:
                src = os.path.join(origen_player, folder)
                dest = os.path.join(destino_player, folder)
                
                if os.path.exists(src):
                    # Borramos la carpeta destino para evitar conflictos de archivos viejos
                    if os.path.exists(dest):
                        shutil.rmtree(dest)
                    # Copiamos la carpeta completa
                    shutil.copytree(src, dest)

        # Finalización exitosa
        cargando.destroy()
        nombre_exito = "Steam" if tipo == "steam" else "No-Steam"
        mostrar_mensaje(f"Modelos {nombre_exito} de Counter-Strike activados con éxito!")

    except Exception as e:
        if 'cargando' in locals():
            cargando.destroy()
        mostrar_mensaje(f"Error crítico al activar modelos {tipo}: {str(e)}")

# --- Botones finales para tu interfaz ---

def activar_player_models_cs_steam():
    procesar_cambio_modelos("steam")

def activar_player_models_cs_nosteam():
    procesar_cambio_modelos("nosteam")

def obtener_nombre_archivo_drive():
    try:
        response = requests.get(GOOGLE_DRIVE_URL)
        soup = BeautifulSoup(response.text, 'html.parser')
        titulo = soup.title.string.replace(' - Google Drive', '')
        return titulo
    except Exception as e:
        # Aquí se usa una herramienta de logging básica, aunque el mensaje sigue siendo informativo
        print(f"Error al obtener el nombre del archivo: {e}") 
        return "No se pudo obtener el nombre."
def parsear_version_personalizada(version_str):
    """Extrae y parsea los números de una cadena de versión como 'b5.0' o 'v5.1'"""
    match = re.search(r'[\d.]+', version_str)
    if match:
        version_numbers = [int(num) for num in match.group().split('.')]
        return version_numbers
    return None

# --- VENTANAS DE LA INTERFAZ ---

def ventana_principal():
    ventana.title("Menú de Configuración de Juego de Valve de GoldSrc")
    # Aumentar la ventana para que se vea mejor el diseño de dos columnas si la ventana principal es 
    ventana.geometry("950x650") 

    # Cuadro con información de las versiones
    cuadro_versiones = tk.Frame(ventana, bd=2, relief="groove")
    cuadro_versiones.place(x=10, y=10)

    # Lógica de comparación de versiones (omitiendo detalle por ser igual al anterior)
    nombre_archivo = obtener_nombre_archivo_drive()
    ultima_version_str = nombre_archivo.split()[-1]
    
    tk.Label(cuadro_versiones, text=f"Versión Instalada: {INSTALLED_VERSION}", font=("Arial", 12)).pack(padx=10, pady=5)
    tk.Label(cuadro_versiones, text=f"Versión Reciente: {ultima_version_str}", font=("Arial", 12)).pack(padx=10, pady=5)

    installed_version_parsed = parsear_version_personalizada(INSTALLED_VERSION)
    latest_version_parsed = parsear_version_personalizada(ultima_version_str)

    if installed_version_parsed is None or latest_version_parsed is None:
        estado_texto = "Estado de versión no disponible"
        estado_color = "gray"
    elif installed_version_parsed < latest_version_parsed:
        estado_texto = "¡Nueva Actualización Disponible!"
        estado_color = "red"
    elif installed_version_parsed > latest_version_parsed:
        estado_texto = "Welcome Back Ignacio"
        estado_color = "darkblue"
    else:
        estado_texto = "Versión Más Reciente"
        estado_color = "black"
    
    tk.Label(cuadro_versiones, text=estado_texto, font=("Arial", 12, "bold"), fg=estado_color).pack(padx=10, pady=5)

    # Título y subtítulo del menú principal
    tk.Label(ventana, text="Menú de Configuraciones", font=("Arial", 22, "bold")).pack(pady=40)
    tk.Label(ventana, text="Selecciona una opción para continuar", font=("Arial", 16)).pack(pady=5)
    
    # Botones principales
    botones_principales = [
        ("Opciones", lambda: cambiar_ventana(ventana_opciones)),
        ("Bots", lambda: cambiar_ventana(ventana_bots)),
        ("Documentación", lambda: abrir_documento(DOCUMENTACION_DOC)),
        ("Léeme", lambda: abrir_documento(LEEME_DOC)),
        ("Comandos", lambda: abrir_documento(COMANDOS_DOC))
    ]
    for texto, comando in botones_principales:
        boton = tk.Button(ventana, text=texto, font=("Arial", 16), width=20)
        boton.pack(pady=8)
        boton.bind("<Enter>", cambiar_color_entrada)
        boton.bind("<Leave>", cambiar_color_salida)
        boton.bind("<Button-1>", cambiar_color_clic)
        boton.config(command=comando)
        
    # Botón de cerrar
    boton_cerrar = tk.Button(ventana, text="Cerrar Programa", font=("Arial", 16), width=20, bg="red", fg="white", command=ventana.quit)
    boton_cerrar.pack(side="bottom", pady=8)
    boton_cerrar.bind("<Enter>", lambda e: boton_cerrar.config(bg="darkred"))
    boton_cerrar.bind("<Leave>", lambda e: boton_cerrar.config(bg="red"))
    boton_cerrar.bind("<Button-1>", lambda e: boton_cerrar.config(bg="darkred"))
    
    
    # Etiquetas de copyright
    tk.Label(ventana, text="-Valve 1998-2006", font=("Arial", 10)).place(relx=0.0, rely=1.0, anchor="sw", x=10, y=-10)
    tk.Label(ventana, text="-Ignacio Gallinger 2024-2026", font=("Arial", 10)).place(relx=0.0, rely=1.0, anchor="sw", x=10, y=-30)
    tk.Label(ventana, text="(ESTO NO ES OFICIAL Y NO BUSCA FOMENTAR LA PIRATERÍA)", font=("Arial", 8), fg="red").place(relx=1.0, rely=1.0, anchor="se", x=-10, y=-10)

    ruta_script = os.path.dirname(os.path.abspath(__file__))

    ventana.Documentation_LOGO = tk.PhotoImage(file=os.path.join(ruta_script, "Documentation_LOGO.png"))
    ventana.GitHub_LOGO = tk.PhotoImage(file=os.path.join(ruta_script, "GitHub_LOGO.png"))
    ventana.YouTube_LOGO = tk.PhotoImage(file=os.path.join(ruta_script, "YouTube_LOGO.png"))

    boton_emoji = tk.Button(ventana, image=ventana.Documentation_LOGO, command=abrir_url_docs)
    boton_emoji.place(relx=1.0, rely=0.0, anchor="ne", x=-10, y=10, width=45, height=45)
    boton_emoji.bind("<Enter>", cambiar_color_entrada)
    boton_emoji.bind("<Leave>", cambiar_color_salida)

    # --- PEGA ESTO JUSTO DEBAJO ---
    # Primer botón nuevo
    boton_nuevo_1 = tk.Button(ventana, image=ventana.GitHub_LOGO, command=abrir_url_github)
    boton_nuevo_1.place(relx=1.0, rely=0.0, anchor="ne", x=-60, y=10, width=45, height=45)
    boton_nuevo_1.bind("<Enter>", cambiar_color_entrada)
    boton_nuevo_1.bind("<Leave>", cambiar_color_salida)

    # Segundo botón nuevo
    boton_nuevo_2 = tk.Button(ventana, image=ventana.YouTube_LOGO, command=abrir_url_youtube)
    boton_nuevo_2.place(relx=1.0, rely=0.0, anchor="ne", x=-110, y=10, width=45, height=45)
    boton_nuevo_2.bind("<Enter>", cambiar_color_entrada)
    boton_nuevo_2.bind("<Leave>", cambiar_color_salida)

def ventana_opciones():
    # ... (Mantenido igual)
    tk.Label(ventana, text="Opciones", font=("Arial", 22, "bold")).pack(pady=10)
    tk.Label(ventana, text="Configura las opciones del juego", font=("Arial", 16)).pack(pady=5)
    botones_opciones = [
        ("Configuración de Modelos Half-Life", lambda: cambiar_ventana(ventana_modelos)),
        ("Opciones de Aniversario", lambda: cambiar_ventana(ventana_aniversario)),
        ("Más Opciones", lambda: cambiar_ventana(ventana_mas_opciones))
    ]
    for texto, comando in botones_opciones:
        boton = tk.Button(ventana, text=texto, font=("Arial", 16), width=30)
        boton.pack(pady=8)
        boton.bind("<Enter>", cambiar_color_entrada)
        boton.bind("<Leave>", cambiar_color_salida)
        boton.bind("<Button-1>", cambiar_color_clic)
        boton.config(command=comando)
    boton_volver = tk.Button(ventana, text="Volver al Menú Principal", font=("Arial", 14), 
                             width=20, command=lambda: cambiar_ventana(ventana_principal))
    boton_volver.pack(side="bottom", pady=8)
    boton_volver.bind("<Enter>", cambiar_color_entrada)
    boton_volver.bind("<Leave>", cambiar_color_salida)
    boton_volver.bind("<Button-1>", cambiar_color_clic)

def ventana_modelos():
    tk.Label(ventana, text="Configuración de Modelos 3D", font=("Arial", 22, "bold")).pack(pady=10)
    tk.Label(ventana, text="Selecciona una opción para cambiar los modelos", font=("Arial", 16)).pack(pady=5)
    botones_modelos = [
        ("Activar Modelos Clásicos (Half-Life)", lambda: copiar_archivos(MODELOS_CLASICOS, MODELOS_PRINCIPAL, "Modelos Clásicos de Half-Life activados con éxito.")),
        ("Activar Modelos HD (Half-Life)", lambda: copiar_archivos(MODELOS_HD, MODELOS_PRINCIPAL, "Modelos HD de Half-Life activados con éxito.")),
        ("Activar Modelos Clásicos (Opposing Force)", lambda: copiar_archivos(OP_MODELOS_CLASICOS, OP_MODELOS_PRINCIPAL, "Modelos Clásicos de Opposing Force activados con éxito.")),
        ("Activar Modelos HD (Opposing Force)", lambda: copiar_archivos(OP_MODELOS_HD, OP_MODELOS_PRINCIPAL, "Modelos HD de Opposing Force activados con éxito.")),
        ("Activar Modelos Clásicos (Blue Shift)", lambda: copiar_archivos(BS_MODELOS_CLASICOS, BS_MODELOS_PRINCIPAL, "Modelos Clásicos de Blue Shift activados con éxito.")),
        ("Activar Modelos HD (Blue Shift)", lambda: copiar_archivos(BS_MODELOS_HD, BS_MODELOS_PRINCIPAL, "Modelos HD de Blue Shift activados con éxito."))
    ]
    for texto, comando in botones_modelos:
        boton = tk.Button(ventana, text=texto, font=("Arial", 16), width=35)
        boton.pack(pady=8)
        boton.bind("<Enter>", cambiar_color_entrada)
        boton.bind("<Leave>", cambiar_color_salida)
        boton.bind("<Button-1>", cambiar_color_clic)
        boton.config(command=comando)
    boton_volver = tk.Button(ventana, text="Volver al Menú Anterior", font=("Arial", 14), width=20, command=lambda: cambiar_ventana(ventana_opciones))
    boton_volver.pack(side="bottom", pady=8)
    boton_volver.bind("<Enter>", cambiar_color_entrada)
    boton_volver.bind("<Leave>", cambiar_color_salida)
    boton_volver.bind("<Button-1>", cambiar_color_clic)

def ventana_aniversario():
    # ... (Mantenido igual)
    tk.Label(ventana, text="Opciones de Aniversario", font=("Arial", 22, "bold")).pack(pady=10)
    tk.Label(ventana, text="Activa o Desactiva contenido de los aniversarios", font=("Arial", 16)).pack(pady=5)
    tk.Label(ventana, text="Half-Life", font=("Arial", 18, "bold")).pack(pady=5)
    botones_aniversario = [
        ("Activar Mapas 25th Aniversario", lambda: copiar_archivos(os.path.join(ANIVERSARIOS, "maps"), os.path.join(VALVE, "maps"), "Mapas del 25th Aniversario activados con éxito.")),
        ("Desactivar Mapas 25th Aniversario", lambda: desactivar_mapas_aniversario()),
        ("Activar Modelos 25th Aniversario", lambda: copiar_archivos(os.path.join(ANIVERSARIOS, "playermodels"), os.path.join(VALVE, "models", "player"), "Modelos del 25th Aniversario activados con éxito.")),
        ("Desactivar Modelos 25th Aniversario", lambda: desactivar_modelos_aniversario()),
        ("Activar Sprays del 25th Aniversario", lambda: activar_sprays_25th()),
        ("Desactivar Sprays del 25th Aniversario", lambda: desactivar_sprays_25th())
    ]
    for texto, comando in botones_aniversario:
        boton = tk.Button(ventana, text=texto, font=("Arial", 16), width=35)
        boton.pack(pady=8)
        boton.bind("<Enter>", cambiar_color_entrada)
        boton.bind("<Leave>", cambiar_color_salida)
        boton.bind("<Button-1>", cambiar_color_clic)
        boton.config(command=comando)
    boton_volver = tk.Button(ventana, text="Volver al Menú Anterior", font=("Arial", 14), width=20, command=lambda: cambiar_ventana(ventana_opciones))
    boton_volver.pack(side="bottom", pady=8)
    boton_volver.bind("<Enter>", cambiar_color_entrada)
    boton_volver.bind("<Leave>", cambiar_color_salida)
    boton_volver.bind("<Button-1>", cambiar_color_clic)

def ventana_mas_opciones():
    # ... (Mantenido igual)
    tk.Label(ventana, text="Más Opciones", font=("Arial", 22, "bold")).pack(pady=10)
    tk.Label(ventana, text="Opciones adicionales para el juego", font=("Arial", 16)).pack(pady=5)
    
    botones_mas_opciones = [
        ("Arreglar Lista de Servidores", lambda: copiar_archivos(os.path.join(IGNACIO_GALLINGER, 
            "MasterServers.vdf"),
            os.path.join(PLATFORM, "config", "MasterServers.vdf"), "Lista de Servidores arreglada con éxito.")),
        
        ("Counter-Strike No Steam PlayerModels", activar_player_models_cs_nosteam),
        ("Counter-Strike Steam PlayerModels", activar_player_models_cs_steam)
    ]
    
    for texto, comando in botones_mas_opciones:
        boton = tk.Button(ventana, text=texto, font=("Arial", 16), width=35)
        boton.pack(pady=8)
        boton.bind("<Enter>", cambiar_color_entrada)
        boton.bind("<Leave>", cambiar_color_salida)
        boton.bind("<Button-1>", cambiar_color_clic)
        boton.config(command=comando)
    
    boton_volver = tk.Button(ventana, text="Volver al Menú Anterior", font=("Arial", 14), width=20,
                             command=lambda: cambiar_ventana(ventana_opciones))
    boton_volver.pack(side="bottom", pady=8)

# --- VENTANA DE BOTS (ACTUALIZADA con Lógica de Habilitación) ---

def ventana_bots():
    # Eliminada: ventana.geometry("750x800")
    tk.Label(ventana, text="Opciones de Bots", font=("Arial", 22, "bold")).pack(pady=10)
    tk.Label(ventana, text="Configura los bots para los juegos", font=("Arial", 16)).pack(pady=5)
    
    # Marco principal para los botones en cuadrícula
    grid_frame = tk.Frame(ventana)
    grid_frame.pack(padx=20, pady=10) # Reducimos el pady para dar más espacio
    
    # 1. Obtener el estado de los archivos de bots
    estado_archivos = verificar_archivos_bots()

    # Lista de juegos y sus comandos
    juegos_bots = [
        ("Half-Life (Deathmatch)", activar_bots_hldm, desactivar_bots_hldm),
        ("Opposing Force (Deathmatch)", activar_bots_ofdm, desactivar_bots_ofdm),
        ("Team Fortress Classic", lambda: copiar_archivos(TFC_BOTS, DEST_TFC, "Bots de Team Fortress Classic activados con éxito."), desactivar_bots_tfc),
        ("Deathmatch Classic", lambda: copiar_archivos(DMC_BOTS, DEST_DMC, "Bots de Deathmatch Classic activados con éxito."), desactivar_bots_dmc),
        ("Ricochet", lambda: copiar_archivos(RICOCHET_BOTS, DEST_RICOCHET, "Bots de Ricochet activados con éxito."), desactivar_bots_ricochet),
        ("Day of Defeat", lambda: copiar_archivos(DOD_BOTS, DEST_DOD, "Bots de Day of Defeat activados con éxito."), desactivar_bots_dod)
    ]
    
    # Colocar los botones en la cuadrícula
    row = 0
    
    for titulo, comando_activar, comando_desactivar in juegos_bots:
        
        # Determinar el estado para este juego
        esta_activado = estado_archivos.get(titulo, False)
        
        # Colores y estados según la disponibilidad de archivos
        if esta_activado:
            color_fondo = "SystemButtonFace" # Color por defecto para habilitado
            cursor_tipo = "hand2" # Cursor de mano para indicar interactividad
            estado_btn = tk.NORMAL
        else:
            color_fondo = "light gray" # Gris para indicar deshabilitado
            cursor_tipo = "arrow" # Cursor normal, no funcional
            estado_btn = tk.DISABLED
            
        # Título del juego (Fuente más pequeña para ahorrar espacio)
        tk.Label(grid_frame, text=titulo, font=("Arial", 12, "bold")).grid(row=row, column=0, columnspan=2, pady=(10, 3), sticky="ew")
        row += 1
        
        # Botón Activar (Columna 0)
        texto_activar = "Activar Bots"
        boton_activar = tk.Button(grid_frame, text=texto_activar, font=("Arial", 10), width=25, command=comando_activar, 
                                  bg=color_fondo, state=estado_btn, cursor=cursor_tipo)
        boton_activar.grid(row=row, column=0, padx=5, pady=3, sticky="ew")
        
        # Aplicar los bindings solo si el botón está habilitado
        if esta_activado:
            boton_activar.bind("<Enter>", cambiar_color_entrada)
            boton_activar.bind("<Leave>", cambiar_color_salida)
            boton_activar.bind("<Button-1>", cambiar_color_clic)
        
        # Botón Desactivar (Columna 1)
        texto_desactivar = "Desactivar Bots"
        boton_desactivar = tk.Button(grid_frame, text=texto_desactivar, font=("Arial", 10), width=25, command=comando_desactivar, 
                                     bg=color_fondo, state=estado_btn, cursor=cursor_tipo)
        boton_desactivar.grid(row=row, column=1, padx=5, pady=3, sticky="ew")
        
        # Aplicar los bindings solo si el botón está habilitado
        if esta_activado:
            boton_desactivar.bind("<Enter>", cambiar_color_entrada)
            boton_desactivar.bind("<Leave>", cambiar_color_salida)
            boton_desactivar.bind("<Button-1>", cambiar_color_clic)
        
        row += 1
        
    # Botón Volver al final
    boton_volver = tk.Button(ventana, text="Volver al Menú Anterior", font=("Arial", 14), width=25, command=lambda: cambiar_ventana(ventana_principal))
    boton_volver.pack(side="bottom", pady=10) # Reducimos pady
    boton_volver.bind("<Enter>", cambiar_color_entrada)
    boton_volver.bind("<Leave>", cambiar_color_salida)
    boton_volver.bind("<Button-1>", cambiar_color_clic)

# cstrikesteamplayers
# --- INICIALIZACIÓN DE LA VENTANA PRINCIPAL ---
ventana = tk.Tk()
cambiar_ventana(ventana_principal)
ventana.mainloop()