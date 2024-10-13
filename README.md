# V2Reconstructor

Extract (most of) model data from [Prototracer](https://github.com/coelacant1/ProtoTracer)'s Object3D files (file.h) to .obj file.

The file will not be the same as the original obj file (unless it is really simple).

## Sample

Sample contains file from [ProtoTracerOBJConverter](https://github.com/coelacant1/ProtoTracerOBJConverter)

## Usage

```bash
python V2Reconstructor.py <input file> <output file>
```

## Quality

### Horrible
Model is unrecognizable

- DVD.obj

### Bad
Contains imperfection/holes throughout the model, can be fixed by filling or remeshing.

- Artisans.hhttps://github.com/coelacant1/ProtoTracerOBJConverter
- Proto.h

### Good
Nearly perfect

- Bee.obj
- Charmander.obj
- Creeper.obj
- Cube.obj
- DragonStatue.obj
- Pikachu.obj **\*model is really large**
- Rocks.obj
- SolidCube.obj
- Spyro.obj

## Fish
:fish: