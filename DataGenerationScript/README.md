# Introduction

Ce script permet de générer des données fictives pour peupler une base de données MySQL.
Les données présentes dans cette base de données sont ensuite visualisé à l'aide du logiciel Grafana.

# Requirement

### Python Version 3
Python version 3. Testé avec python 3.7.3

```bash
python --version 
python3 --version 
```


# Usage:

```bash
cd DataGenerationScript/.

python3 main.py <nb_device_data> <nb_events_data>

Example:
  python3 main.py 20 200    #Génère 20 équipements aléatoire et 200 événements aléatoire de détection caméra.

```

# Results:

Les résultats sont affichés dans la sortie standard et dans deux fichiers dans le dossier `results`.

```bash
DataGenerationScript/
└── results/
    └── res_device.sql
    └── res_event.sql
```