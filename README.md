# ProjectManager

## Tool to manage folders in 3D film.

### Version : 0.00


```
+ root
    + references
    + shared_maps
        - dirt.png
    + asset
        + props
            + boat
                + maps
                    - boat_diffuse.png
                    - boat_spec.png
                + concept
                + modeling
                + rig
            + barrel
                + concept
                + modeling
                + rig
        + characters
            + jean
                + concept
                + modeling
                + rig
            + pierre
                + concept
                    + wip
                        - pierre_sheet_001.psd
                        - pierre_sheet_002.psd
                        - pierre_sheet_003.psd
                    + output
                        - pierre_sheet.png
                + modeling
                    + wip
                        - pierre_modeling_001.max
                        - pierre_modeling_002.max
                        - pierre_modeling_003.max
                    + output
                        - pierre_modeling.max
                + rig
                    - pierre_rig.max
        + environments
            + cabin
                + maps
                    - cabin_diffuse.png
                    - cabin_spec.png
                + concept
                    - cabin_sheet.png
                    - cabin_atmosphere.png
                + modeling
                    - cabin_modeling.max

    + scene
        + p001
            + storyboard
            + animatic2d
            + animation
            + fx
            + render
            + compositing
        + p002
            + storyboard
            + animatic2d
            + animation
            + fx
            + render
            + compositing
```


asset : boat, barrel, jean, ...
(asset_type : prop, character, ...)

shot : p001, p002, ...

task : modeling, compositing, ...

wip : cabin_diffuse_001.png, cabin_diffuse_002.png, ...

output : cabin_diffuse.png


-- User Story

"En tant que graphiste, je souhaite pouvoir ouvrir la derniere version de mon travail"

-> lister les assets / shots
-> lister les taches de l'asset / shot
-> trouver la derniere version de la tache
