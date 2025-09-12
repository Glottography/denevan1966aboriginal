# Releasing the dataset

In case of upstream changes in glottography-data:
```shell
cldfbench download cldfbench_denevan1966aboriginal.py
```

## Recreate the CLDF data

```shell
cldfbench makecldf cldfbench_denevan1966aboriginal.py --glottolog-version v5.2
cldfbench cldfreadme cldfbench_denevan1966aboriginal.py
cldfbench zenodo cldfbench_denevan1966aboriginal.py
cldfbench readme cldfbench_denevan1966aboriginal.py
```

## Validation

```shell
cldf validate cldf
```

```shell
cldfbench geojson.validate cldf
```

```shell
cldfbench geojson.glottolog_distance cldf --format pipe
```

| ID | Distance | Contained | NPolys |
|:---------|-----------:|:------------|---------:|
| baur1253 | 0 | True | 1 |
| cani1243 | 0 | True | 1 |
| cayu1262 | 0 | True | 1 |
| iton1250 | 0 | True | 1 |
| movi1243 | 0 | True | 1 |
