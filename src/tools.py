import os 
from colorama import Fore, init

# Inicializa colorama
init(autoreset=True)

def ejecutar_scandisk(t):
    print(Fore.GREEN + t["msg_running_scandisk"])
    os.system("chkdsk C: /f")
    input(Fore.GREEN + t["msg_continue"])

def listar_actualizaciones(t):
    print(Fore.GREEN + t["msg_running_updates"])
    os.system("wmic qfe list brief /format:table")
    input(Fore.GREEN + t["msg_continue"])

def verificar_conectividad(t):
    print(Fore.GREEN + t["msg_running_ping"])
    os.system("ping 8.8.8.8")
    input(Fore.GREEN + t["msg_continue"])

def mostrar_config_red(t):
    print(Fore.GREEN + t["msg_running_ipconfig"])
    os.system("ipconfig /all")
    input(Fore.GREEN + t["msg_continue"])

def limpiar_cache_dns(t):
    print(Fore.GREEN + t["msg_running_dns"])
    os.system("ipconfig /flushdns")
    input(Fore.GREEN + t["msg_continue"])

def reparar_imagen_dism(t):
    print(Fore.GREEN + t["msg_running_dism"])
    os.system("dism /online /cleanup-image /restorehealth")
    input(Fore.GREEN + t["msg_continue"])

def verificar_integridad_sfc(t):
    print(Fore.GREEN + t["msg_running_sfc"])
    os.system("sfc /scannow")
    input(Fore.GREEN + t["msg_continue"])

def listar_procesos_activos(t):
    print(Fore.GREEN + t["msg_running_processes"])
    os.system("tasklist")
    input(Fore.GREEN + t["msg_continue"])

def liberar_espacio_disco(t):
    print(Fore.GREEN + t["msg_running_cleanmgr"])
    os.system("cleanmgr")
    input(Fore.GREEN + t["msg_continue"])

def listar_servicios_activos(t):
    print(Fore.GREEN + t["msg_running_services"])
    os.system("net start")
    input(Fore.GREEN + t["msg_continue"])

def reiniciar_red(t):
    print(Fore.GREEN + t["msg_running_net_reset"])
    os.system("netsh int ip reset")
    os.system("netsh winsock reset")
    input(Fore.GREEN + t["msg_continue"])

def comprobar_estado_fsutil(t):
    print(Fore.GREEN + t["msg_running_fsutil"])
    os.system("fsutil dirty query C:")
    input(Fore.GREEN + t["msg_continue"])

def mostrar_uso_disco(t):
    print(Fore.GREEN + t["msg_running_usage"])
    os.system("wmic logicaldisk get size,freespace,caption")
    input(Fore.GREEN + t["msg_continue"])

def mostrar_rendimiento(t):
    print(Fore.GREEN + t["msg_running_perf"])
    print(Fore.YELLOW + f"\n{t['label_cpu']}:")
    os.system("wmic cpu get name,loadpercentage")
    print(Fore.YELLOW + f"\n{t['label_ram']}:")
    os.system("wmic memorychip get capacity,speed,manufacturer")
    input(Fore.GREEN + t["msg_continue"])

def verificar_proxy(t):
    print(Fore.GREEN + t["msg_running_proxy"])
    os.system("netsh winhttp show proxy")
    input(Fore.GREEN + t["msg_continue"])

def verificar_servicio_update(t):
    print(Fore.GREEN + t["msg_running_wuauserv"])
    os.system("sc query wuauserv")
    input(Fore.GREEN + t["msg_continue"])

def analizar_uso_red(t):
    print(Fore.GREEN + t["msg_running_netstat"])
    os.system("netstat -e")
    input(Fore.GREEN + t["msg_continue"])

def mostrar_eventos_error(t):
    print(Fore.GREEN + t["msg_running_events"])
    os.system("eventvwr.msc")
    input(Fore.GREEN + t["msg_continue"])

def deshabilitar_servicio(t):
    print(Fore.GREEN + t["msg_disable_service"])
    servicio = input(t["prompt_service_name"])
    os.system(f"sc config {servicio} start= disabled")
    input(Fore.GREEN + t["msg_service_done"].format(service=servicio))

def generar_informe_sistema(t):
    print(Fore.GREEN + t["msg_running_sysinfo"])
    os.system("systeminfo > informe_sistema.txt")
    print(Fore.GREEN + t["msg_sysinfo_done"])
    input(Fore.GREEN + t["msg_continue"])

def ejecutar_solucionador(t):
    print(Fore.GREEN + t["msg_running_msdt"])
    os.system("msdt.exe /id NetworkDiagnosticsNetworkAdapter")
    input(Fore.GREEN + t["msg_continue"])