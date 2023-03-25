import paho.mqtt.client as mqtt
import win32gui, win32process, psutil, time, socket, win32console

def hide_console():
    try:
        window = win32console.GetConsoleWindow()
        win32gui.ShowWindow(window, 0)
    except:
        pass

def sanitize_message(message):
    sanitized_message = ''.join(c for c in message if c.isalnum()).lower()
    return sanitized_message

# Adresse IP du broker MQTT
mqtt_broker = "ADRESSE_IP_DU_BROKER"

# Port utilisé par le broker MQTT
mqtt_port = PORT_DU_BROKER

# Nom d'utilisateur pour se connecter au broker MQTT (facultatif)
mqtt_username = "NOM_D_UTILISATEUR_MQTT"

# Mot de passe pour se connecter au broker MQTT (facultatif)
mqtt_password = "MOT_DE_PASSE_MQTT"
mqtt_topic = socket.gethostname()

hide_console()

current_process = None
previous_explorer_state = None
while True:
    try:
        client = mqtt.Client()
        client.username_pw_set(mqtt_username, mqtt_password)
        client.connect(mqtt_broker, mqtt_port)
        print("Connecté au broker MQTT")

        hwnd = win32gui.GetForegroundWindow()
        tid, pid = win32process.GetWindowThreadProcessId(hwnd)

        if pid > 0:
            process = psutil.Process(pid)
            process_path = process.exe()
            process_name = process_path.split("\\")[-1].split(".")[0]

            state_changed = False
            if current_process != process_name:
                current_process = process_name
                state_changed = True
                print(f"Changement de processus: {current_process}")

            if current_process == "ApplicationFrameHost":
                window_title = win32gui.GetWindowText(hwnd)
                short_title = window_title[:10]
                message = sanitize_message(short_title)
            elif current_process == "explorer":
                window_title = win32gui.GetWindowText(hwnd)
                explorer_state = "bureau" if not window_title else "explorateur"
                if explorer_state != previous_explorer_state:
                    state_changed = True
                previous_explorer_state = explorer_state
                message = sanitize_message(explorer_state)
            else:
                message = sanitize_message(current_process)

            if state_changed:
                result = client.publish(mqtt_topic, payload=message.encode("utf-8"), qos=0, retain=False)

                if result.rc == mqtt.MQTT_ERR_SUCCESS:
                    print("Message publié sur MQTT avec succès")
                else:
                    print(f"Erreur de publication sur MQTT, code retour={result.rc}")

        client.disconnect()

    except (psutil.AccessDenied, psutil.NoSuchProcess):
        print("Erreur lors de la récupération des informations de la fenêtre active")
        time.sleep(5)
        continue

    except Exception as e:
        print(f"Erreur inattendue: {e}")
        time.sleep(5)
        continue

    # Attendre 1 seconde avant de vérifier à nouveau
    time.sleep(1)
