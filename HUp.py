import os
import time

# Ruta al archivo de log del minero (actualizar según sea necesario)
log_file_path = "/hive/miners/custom/qubjetskiAMDGPU/gpu/log/2024-06-22.log"

# Intervalo de tiempo para leer el archivo de log (en segundos)
interval = 0.7

def modificar_valores(hashrate):
    # Aquí puedes modificar los valores de hashrate según tus necesidades
    hashrate_modificado = hashrate * 10.1  # Ejemplo: aumentar hashrate en 10%
    return hashrate_modificado

def verificar_rutas():
    if os.path.exists(log_file_path):
        print(f"El archivo {log_file_path} existe.")
        if os.access(log_file_path, os.R_OK):
            print(f"Tienes permisos de lectura para {log_file_path}.")
        else:
            print(f"No tienes permisos de lectura para {log_file_path}.")
            return False

        if os.access(log_file_path, os.W_OK):
            print(f"Tienes permisos de escritura para {log_file_path}.")
        else:
            print(f"No tienes permisos de escritura para {log_file_path}.")
            return False
    else:
        print(f"El archivo {log_file_path} no existe.")
        return False

    return True

def leer_y_modificar_log():
    while True:
        if verificar_rutas():
            with open(log_file_path, 'r') as file:
                log_data = file.readlines()
                
            # Supongamos que el hashrate se encuentra en una línea específica del log
            for i, line in enumerate(log_data):
                if "hashrate" in line:
                    try:
                        # Extraer el valor del hashrate
                        hashrate = float(line.split()[1])
                        print(f"Hashrate original: {hashrate}")
                        
                        # Modificar el hashrate
                        hashrate_modificado = modificar_valores(hashrate)
                        print(f"Hashrate modificado: {hashrate_modificado}")
                        
                        # Reemplazar el valor en el log
                        log_data[i] = f"hashrate {hashrate_modificado}\n"
                    except ValueError as e:
                        print(f"Error al convertir hashrate a float: {e}")
                        continue
            
            # Escribir los datos modificados de vuelta al archivo de log
            with open(log_file_path, 'w') as file:
                file.writelines(log_data)
                print(f"Datos escritos de vuelta al archivo {log_file_path}.")
        time.sleep(interval)

if __name__ == "__main__":
    leer_y_modificar_log()

