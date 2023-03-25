
Matrice LED contrôlée par MQTT avec ESP32
Ce projet consiste en une matrice LED basée sur WS2812B de 16x16 pixels qui affiche des logos, des animations et les icônes des applications actuellement utilisées sur un ordinateur. Le contrôle de la matrice LED est effectué via MQTT (Message Queuing Telemetry Transport), un protocole de messagerie de type publish-subscribe pour l'Internet des objets. Le projet utilise un ESP32 comme contrôleur et peut être configuré pour se connecter à un réseau Wi-Fi.

Fonctionnalités clés
Affichage de logos, d'animations et d'icônes d'applications actuellement utilisées sur un ordinateur.
Contrôle de la matrice LED via MQTT.
Utilisation d'un ESP32 comme contrôleur.
Possibilité de se connecter à un réseau Wi-Fi.
Installation
Pour utiliser ce projet, vous devez installer les bibliothèques suivantes sous Arduino IDE :

Adafruit_NeoPixel.h
WiFi.h
PubSubClient.h
Le projet a été conçu pour être utilisé avec un broker MQTT et doit être exécuté sous Windows. Vous devez également avoir Python et paho-mqtt installé sur votre système.

Utilisation
Une fois le projet installé, vous pouvez utiliser la matrice LED en suivant les instructions suivantes :

Connectez l'ESP32 à votre ordinateur via un câble USB.
Uploadez le code sur l'ESP32 via Arduino IDE.
Assurez-vous que le broker MQTT est en cours d'exécution.
Exécutez le script Python pour afficher les icônes et les animations sur la matrice LED.
Structure du projet
Le projet se compose de deux parties : la partie matrice LED avec la programmation de l'ESP32 et le montage de la matrice LED avec le fichier G-code pour imprimer le boîtier, et la partie logicielle sous Windows avec le script Python.

Contribution
Les contributions sont les bienvenues ! Vous pouvez contribuer en créant une branche pour ajouter une nouvelle fonctionnalité ou en corrigeant des bugs. Pour plus d'informations, consultez le fichier CONTRIBUTING.md.

Licence
Ce projet est publié sous la licence MIT. Cela signifie que vous êtes libre de l'utiliser, de le modifier et de le distribuer comme bon vous semble, à condition de conserver la mention de l'auteur original. Veuillez consulter le fichier LICENSE pour plus d'informations.

N'hésitez pas à me faire savoir si vous avez des commentaires ou des questions sur ce fichier README.