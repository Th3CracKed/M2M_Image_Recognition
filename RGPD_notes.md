# RGPD

## Authentifier les utilisateurs

Définissez un identifiant (login) unique à chaque utilisateur. 
> Oui; dans notre projet nous utilisons Grafana qui le permet.

Adoptez une politique de mot de passe utilisateur conforme à nos recommandations.
> Grafana ne recommande pas une syntaxe particulière pour les mots de passe. Cependant les comptes peuvent être faits à l’avance pour chaque utilisateur avec des mots de passe forts.

Obliger l’utilisateur à changer son mot de passe après réinitialisation :
> Grafana permet de réinitialiser le mot de passe par défaut.

## Gérer les habilitations

Supprimez les permissions d’accès obsolètes :
> Grafana permet de gérer les accès pour chaque utilisateur par une interface d’administration des utilisateurs.

## Tracer les accès et gérer les incidents

Prévoyez un système de journalisation :
> Chaque modification sur les dashboards sont sauvegardée. Et offre la possibilité d’ajouter des commentaires en lien avec raison de la modification.

Prévoyez les procédures pour les notifications de violation de données à caractère personnel:
> Nous ne traitons pas de données personnelles. (Si nous restons dans le domaine de surveillance des passages animaux/personnes). 

## Sécuriser les postes de travail

Prévoyez une procédure de verrouillage automatique de session :
> Grafana permet automatiquement de déconnecter un utilisateur. Session_life_time.

## Sécuriser l'informatique mobile

Prévoyez des moyens de chiffrement des équipements mobiles :
> Le protocole LoRaWAN permet le chiffrage de bout en bout.

## Protéger le réseau informatique interne

Limitez les flux réseau au strict nécessaire:
> Data minimisation. Dans notre projet nous sommes partie du principe que notre appareil iot sauvegarde localement les événements de la journée dans une mémoire en local pour par la suite les envoyer en une seule grande requête et éviter d'obstruer le réseau avec de multiples petites requêtes par jour. 

## Sécuriser les serveurs

Limitez l’accès aux outils et interfaces d’administration aux seules personnes habilitées :
> Avec une authentification des utilisateurs par identifiant mot de passe.

Installez sans délai les mises à jour critiques :
> Uniquement sur les logiciels de consultation des données (PC). Pas sur les équipements à distance. En effet nous avons déduit qu’il était difficile d’envisager des mises à jour OTA avec un réseau comme LoRaWan.

## Sécuriser les sites web

Vérifiez qu'aucun mot de passe ou identifiant ne passe dans les URLs :
> Voir protocole d’authentification de LoRa et Grafana.

## Sécuriser les échanges avec d'autres organismes

Chiffrez les données avant leur envoi :
> Le protocole LoRa permet le chiffrage de bout en bout des transmissons.

Assurez-vous qu'il s'agit du bon destinataire :
> LoRa permet d’envoyer les données à un serveur spécifique identifié grâce à une authentification MTLS. 


## Encadrer les développements informatiques

Proposez des paramètres respectueux de la vie privée aux utilisateurs finaux :
> Les données de notre projet sont anonymes, car il n’y a pas de possibilité de faire une corrélation entre les données captées et celle d'une personne physique.

Testez sur des données fictives ou anonymisées :
> Oui avec notre script python générateur de données, nous pouvons ajouter des appareils aléatoirement avec des événements fictifs de détection d’image.

