<p align="center">
  <img src=".github/media/banner.png">
</p>
<p align="center">
  <img src="https://img.shields.io/badge/Author-erickcasita-blue?style=for-the-badge">
</p>
`Update Promotions SAT` is a tool to assign promotions generated by the ERP SIVE.

## Install

Download the project from Github to a local folder

`https://github.com/erickcasita/backup_files_sive`

## Config

Create directory named "json" and create tree files names:

- clientes-mayoristas.json

example

```
[
    {
        "CVECLI": "851",
        "CLIENTE": "ERIKA SEDAS SOSA",
        "RUTA": "36"
    },
    {
        "CVECLI": "8517",
        "CLIENTE": "GLORIA SEBA POLITO",
        "RUTA": "75"
    },
    {
        "CVECLI": "716",
        "CLIENTE": "TOMASA TOTO MALAGA",
        "RUTA": "75"
    }
]

```

- promos-mayoristas.json

example

```
[
    {
        "CVEPMC": "876",
        "NOMPMC": "PRO PAC MED TRADIC"
    },
    {
        "CVEPMC": "883",
        "NOMPMC": "PRO STELLA 6PK TRADIC"
    },
    {
        "CVEPMC": "884",
        "NOMPMC": "PRO MICH U VID NR TRADIC"
    }
]

```

- promos-tradicional.json

example
```
[
    {
        "CVEPMC": "952",
        "NOMPMC": "PRO CC TRADICIONAL"
    },
    {
        "CVEPMC": "953",
        "NOMPMC": "PRO VC TRADICIONAL"
    },
    {
        "CVEPMC": "954",
        "NOMPMC": "PRO CF TRADICIONAL"
    }
]

```
## Execute

Run script 

`python UpdatePromotions.py`