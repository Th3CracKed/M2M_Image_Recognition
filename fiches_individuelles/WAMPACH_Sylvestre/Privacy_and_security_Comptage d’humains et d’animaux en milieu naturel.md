# Comptage d’humains et d’animaux en milieu naturel

Cours: M2M Mini projet *Sipeed MAix BiT k210*

WAMPACH Sylvestre



## Privacy & Security

Dans ce projet nous réalisons du comptage d'humains et d'animaux à l'aide d'une caméra et d'une carte électronique. Les données peuvent être transmises à l'aide d'un réseau long porté à faible consommation électrique de type LoRaWAN. Les humains et différents animaux sont identifiés à l'aide d'un algorithme de reconnaissance d'image.

Afin d'identifier quelles espèces passe devant la caméra il est nécessaire d'avoir un algorithme de reconnaissance des images. **Cette reconnaissance d'images peut soulever des problèmes de sécurité et vie privée.**

Or ici l'analyse d'image **n'est traitée uniquement sur l'appareil en local**. En effet cette reconnaissance d'image n'a uniquement pour objectif de distinguer les animaux et les personnes qui passe devant le capteur. Les données sont ensuite horodaté et insérer dans une base de données qui sauvegarde uniquement **sous forme textuelle** les événements avec l'entité identifiée (Enregistrer les images en mémoire prendrait trop de place et ne pourrait pas être transmis facilement sur un réseau de type LoRaWAN). Ci-dessous, un exemple simplifié des données envoyées:

```json
{
 "applicationID": "123",
 "batteryLevel": 90.5,
 "devEUI": "a47b11fa",
 "time": "2020-01-14 04:16:22",
 "events": [
     {
     "entity": "wolf",
     "accuracy": 0.86,
     "time": "2020-01-13 12:22:04"
    },
    {
     "entity": "rabbit",
     "accuracy": 0.92,
     "time": "2020-01-13 11:47:22"
    }
 ]
}

```

Les données sont anonymes car il n'y a pas d'informations supplémentaires fournies avec le flux vidéo venant de la caméra qui nous permet de faire un lien entre une personne est la donnée.

Si les données circulent à l’aide d’un réseau de type LoRa il faut faire attention au chiffrement des données et ne pas faire circuler les informations en clair (cependant ici, il ne s’agit pas d’information sensible). Le réseau LoRaWAN par exemple supporte **le chiffrage de bout en bout.**

La possibilité pour une personne de supprimer les données personnelles collectées (comme nous pouvons le retrouver aujourd'hui sur certain sites web) par ce type d’équipement ne semble pas adaptée à ce cas d'usage. **En effet aucune information permet de relier une donnée à une personne physique.**

Pour ce qui concerne la visualisation des données avec un logiciel comme Grafana, les données sont protégés par une **authentification identifiant et mot de passe.**

En cas de vol de l’équipement physique, il faut s’assurer qu’il n’y a pas de faille de sécurité pour accéder aux données. Cela permet d'éviter qu'une tierce personne n’exploite les données récoltées. En effet cet équipement dispose d'une mémoire intégré qui sauvegarde en local les événements rencontrés dans la journée afin d'économiser le nombre de transmission radio en une plus grande requête. Après chaque transmission les données sont supprimées en local, ce qui permet de vider la mémoire et de ne pas nécessiter un grand espace de stockage.

Il pourrait avoir la possibilité qu'une personne simule la présence de plusieurs animaux à l'aide de photos qu'il ferait passer devant le capteur afin de biaiser les résultats captés par le capteur et modifier les études statistiques. En fonction de l'importance des données, même s'il s'agit d'un scénario peu probable, il est possible d'ajouter des capteurs pour fiabiliser les données (Ex: capteur thermique, capteur de proximité). 

Il faut assurer lors de la réception des données qu'elles proviennent de source fiable et authentifié, ajouter un identifiant à chaque appareil et une correspondance avec une base de données permet de minimiser les fausses transmissions. Par exemple sur le réseau LoRaWAN tous les appareils doivent être équipés de **clés uniques** lorsqu'ils quittent le fabricant.

La sécurité peut entraîner **un coût en matière de performance et rapidité** des transmissions dues au chiffrage, déchiffrage et à l'authentification des données.  

Sur ce type de petit d'équipement il est difficile d'envisager un système de mise à jour à distance (OTA) du logiciel embarqué en cas de découverte d'une faille de sécurité.

Pour conclure, la sécurité est un défi majeur des objets connectés qu'il ne faut pas négliger en fonction du domaine d'application (lois/ RGPD). Si les données sont exploitées à titre commercial ou communautaire il n'y a pas les mêmes contrainte en matière de niveau de sécurité.