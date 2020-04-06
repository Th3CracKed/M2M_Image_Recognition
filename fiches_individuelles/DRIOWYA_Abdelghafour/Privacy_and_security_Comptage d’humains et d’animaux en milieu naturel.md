# Comptage d’humains et d’animaux en milieu naturel

Cours: M2M Mini projet *Sipeed MAix BiT k210*

DRIOWYA Abdelghafour


Le projet consiste à fournir une solution à distance qui permet de compter les animaux à l'aide d'un appareil connecté Maix Bit. 

Cet appareil utilise une caméra et un réseau long porté du type LoRaWAN, et un système de détection d’objet basé sur un algorithme d’apprentissage automatique.

  
**Point de force du sécurité de système :**
Niveau communication, les matériels utilisés supporte une implémentation sécurisée.  

- Le réseau LoRaWAN supporte le mtls ‘mutual TLS authentification qui permet une connexion simultanée entre deux appareils.  

- Support du ‘Data origine authentification’ qui permet de s’assurer qu’un message n’a pas été modifier en transite qui permet d’assurer l’intégrité des données.  
  
- Les données sont chiffrés avant l'envoi, et d'ailleurs l'appareil utilisé est équipé d'accélérateurs d'algorithmes AES et SHA256.
["The K210 embeds AES and SHA256 algorithm accelerators to provide users with basic security features."](https://s3.cn-north-1.amazonaws.com.cn/dl.kendryte.com/documents/kendryte_datasheet_20181011163248_en.pdf)

- Protection contre Replay attaque grâce à protection de l’intégrité de Mac payload, chaque session utilise une session id unique et aléatoire.  

- Les données collectées envoyées sont anonymes et sauvegardées que temporairement, ce qui réduit le coût d’une attaque sur l’appareil Iot.
  
**Accès au serveur Grafana est protégé:**

- Utilisation de HTTPS.  

- Limitant les ips qui peuvent accéder et bien configurer le pare-feu.  

- Réduire les permissions du visiteur autant que possible.  

- Redirection de requêtes vers un serveur proxy.

**Point faible du sécurité de système :**

Un attaquant pourra facilement avoir un accès physique à l’appareil, cependant c’est possible de réduire la sévérité de ce problème.  

- De n'acceptent pas les données qui viennent de cet appareil que si l’appareil est dans le bon endroit (en ajoutant un composant GPS par exemple), cette vérification n'assure pas que l'attaquant ne change pas la position courante mais permettra de filtrer les données en cas de vols, une vérification physique et recommandée.

- Il faut s’assurer que l'IOT ne contient pas des informations d'identification qui permettent de récupérer les données du serveur, et de ne pas stocker des accès sensibles de lecture (ou écriture) pour le serveur Grafana, les données doivent être envoyées et puis persistées par un programme qui lui a accès au serveur et fait les vérifications nécessaires avant.

- Vu la nature de l’appareil IOT, mettre à jour à distance pour fixer une faille de sécurité n’est pas envisageable.
