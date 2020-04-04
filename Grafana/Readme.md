# Grafana / Mysql
Étapes pour installer Grafana et visualiser les données présentent dans une base de données d'événements de détection d'animaux et d'humain.

Démo Vidéo de démonstration installation: [https://drive.google.com/open?id=1to3Lmrpa5p6n_ldvlMCuhmxqRK6jarPy](https://drive.google.com/open?id=1to3Lmrpa5p6n_ldvlMCuhmxqRK6jarPy) 

### Environnement d'execution:
Testé sur Ubuntu 19.04, 
Docker version 18.09.9, build 1752eb3, 
mysql  Ver 14.14 Distrib 5.7.28 

## Grafana docker installation sans plugin:

```bash
sudo docker run -d --network="host" --name=grafana -p 3000:3000 grafana/grafana
```

### Option network host:

`--network="host"`

Lors de l'installation d'une base de données MySQL pour exploiter les données sur grafana. Nous n'avons pas réussi à faire communiquer l'image docker grafana et l'image MySQL ensemble.
La solution trouvée consiste à installer MySQL en local sur la machine sans docker. C'est pour cette raison que nous avons ajouté cette option.

#### Installation MySQL

[https://doc.ubuntu-fr.org/mysql](https://doc.ubuntu-fr.org/mysql)

### Ajouter un plugin à grafana:
Ce rendre sur le site et choisir un plugin: 
[https://grafana.com/grafana/plugins/grafana-worldmap-panel](https://grafana.com/grafana/plugins/grafana-worldmap-panel)

Installer le plugin avec l'option `-e "GF_INSTALL_PLUGINS=PLUGIN_NAME_HERE` :

:warning: Nous aurons besoin du plugin `grafana-worldmap-panel` lors de l'import des dashboards exemple.

Par exemple:
```bash
sudo docker run -d --network="host" --name=grafana -e "GF_INSTALL_PLUGINS=grafana-worldmap-panel" grafana/grafana
```



### Installer plusieurs plugins en même temps:

```bash
sudo docker run -d --network="host" --name=grafana -e "GF_INSTALL_PLUGINS=pr0ps-trackmap-panel,alexandra-trackmap-panel,grafana-worldmap-panel" grafana/grafana
```

# Ouvrir grafana dans le navigateur:

localhost:3000

ou

Récupérer l'adresse ip `inet` de `docker0` depuis la liste de la commande.

```bash
$> ip addr show
# Récupérer inet de docker0.

# Dans le navigateur:

172.17.0.1:3000

```

## Visualiser les données

Insérer les données générées par le script dans la base de données Sql. 
Par exemple dans la base de données `m2m`

```bash
$> mysql -u root -p
mysql> CREATE DATABASE m2m
mysql> use m2m

```

``` mysql

# créer les tables:
mysql> CREATE TABLE events (
                    id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
                    accuracy FLOAT(30) NOT NULL,
                    entity VARCHAR(30) NOT NULL,
                    time TIMESTAMP NOT NULL
                    );

mysql> CREATE TABLE devices (
                id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
                devEUI VARCHAR(30) NOT NULL,
                latitude FLOAT(30) NOT NULL,
                longitude FLOAT(30) NOT NULL,
                batteryLevel FLOAT(30) NOT NULL,
                time TIMESTAMP NOT NULL
                );

# Insérer les données du script

INSERT INTO events VALUES (0,0.44,'loup','2020-01-14 04:16:22');
...

INSERT INTO devices VALUES (0,'c9a00f5b',44.73231315,4.86315991,98,'2020-02-16 06:38:37');
...

```


### Connexion Grafana
Ouvrir Grafana et se connecter:
Par défaut identifiant: `admin` MDP: `admin`

### Connecter une base de données:

Onglet `create a data source`

MySQL avec les identifiants.
**Host=** localhost:3306
**Database=** m2m
**User=** root

Enregistrer et tester.

### Importer les tableaux de bords exemple dans grafana.

Dans le dossier `DashboardSamples` du dépôt git. Importer les JSON dans Grafana.






