import os
from colorama import Fore, init
import tools
from locales import TEXTS

init(autoreset=True)

def seleccionar_idioma():
    os.system("cls" if os.name == "nt" else "clear")
    print(Fore.WHITE + "Select Language / Seleccione Idioma:")
    print("1. English")
    print("2. Español")
    
    opcion = input("\n>> ")
    return "en" if opcion == "1" else "es"

def ejecutar_seleccion(opcion, t):

    menu_acciones = {
        "1": tools.verificar_conectividad,
        "2": tools.mostrar_config_red,
        "3": tools.limpiar_cache_dns,
        "4": tools.reiniciar_red,
        "5": tools.verificar_proxy,
        "6": tools.analizar_uso_red,
        "7": tools.ejecutar_scandisk,
        "8": tools.listar_actualizaciones,
        "9": tools.reparar_imagen_dism,
        "10": tools.verificar_integridad_sfc,
        "11": tools.liberar_espacio_disco,
        "12": tools.generar_informe_sistema,
        "13": tools.listar_procesos_activos,
        "14": tools.listar_servicios_activos,
        "15": tools.verificar_servicio_update,
        "16": tools.deshabilitar_servicio,
        "17": tools.comprobar_estado_fsutil,
        "18": tools.mostrar_uso_disco,
        "19": tools.mostrar_rendimiento,
        "20": tools.mostrar_eventos_error
    }

    accion = menu_acciones.get(opcion)

    if accion:
        accion(t)
        return True
    elif opcion == "0":
        print(Fore.YELLOW + t["msg_exit"])
        return False
    else:
        print(Fore.RED + t["msg_error"])
        input(t["msg_continue"])
        return True

def mostrar_menu():
    # 1. Selección de idioma
    lang_code = seleccionar_idioma()
    t = TEXTS[lang_code]

    # 2. Bucle principal del menú
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        
        print(Fore.GREEN + f"\n{t['header']}")

        # Sección: Red
        print(Fore.CYAN + f"\n[{t['cat_network']}]")
        for i in range(1, 7):
            print(f"[{i}] {t[f'opt_{i}']}")

        # Sección: Sistema
        print(Fore.RED + f"\n[{t['cat_system']}]")
        for i in range(7, 13):
            print(f"[{i}] {t[f'opt_{i}']}")

        # Sección: Servicios
        print(Fore.YELLOW + f"\n[{t['cat_services']}]")
        for i in range(13, 17):
            print(f"[{i}] {t[f'opt_{i}']}")

        # Sección: Avanzado
        print(Fore.BLUE + f"\n[{t['cat_advanced']}]")
        for i in range(17, 21):
            print(f"[{i}] {t[f'opt_{i}']}")

        print(Fore.WHITE + f"\n[0] {t['opt_exit']}")

        opcion = input(f"\n{t['prompt_choice']}")

        # 3. Ejecución de la lógica
        if not ejecutar_seleccion(opcion, t):
            break

if __name__ == "__main__":
    mostrar_menu()