import re
import sys

if sys.argv[1]:
    file = sys.argv[1]
else:
    file = "input.obj" #? EDIT HERE
    
if sys.argv[2]:
    out = sys.argv[2]
else:
    out = "output.obj" #? EDIT HERE

contents = open(file, "r").read()
model = open(out, "w")

is_uv = bool(re.search(r"#include \"\.\.\\Materials\\UVMap\.h\"", contents))
print(f"# GENERATED FILE WILL BE LOSSY. INCLUDES UV: {is_uv}")
model.write(f"# GENERATED FILE WILL BE LOSSY. INCLUDES UV: {is_uv}\n\n")

basis_vertexes = re.search(r"Vector3D basisVertices\[\d*\] = {([^}]*)", contents).group(1)
for i in re.findall(r"(?<=Vector3D\()[0-9\.\-f,]*(?=f\)),?", basis_vertexes):
    v = f"{i}".replace("f,", " ")
    print(f"v {v}")
    model.write(f"v {v}\n")

basis_indexes = re.search(r"IndexGroup basisIndexes\[\d*\] = {([^}]*)", contents).group(1)
num_basis_indexes = re.findall(r"(?<=IndexGroup\()[^\)]*", basis_indexes)
if is_uv:
    uv_indexgroup = re.search(r"IndexGroup uvIndexGroup\[\d*\] = {([^}]*)", contents).group(1)
    num_uv_indexgroup = re.findall(r"(?<=IndexGroup\()[^\)]*", uv_indexgroup)
        
for i in range(len(num_basis_indexes)):
    d = "f "
    for j in range(3):
        d += f"{int(str(num_basis_indexes[i]).split(',')[j]) + 1}"
        if is_uv:
            d += f"/{int(str(num_uv_indexgroup[i]).split(',')[j]) + 1}" 
        d += " "
    d = d[:-1]
    print(d)
    model.write(f"{d}\n")
    
if is_uv:
    uv_vertices = re.search(r"Vector2D uvVertices\[\d*\] = {([^}]*)", contents).group(1)
    for i in re.findall(r"(?<=Vector2D\()[0-9\.f,]*(?=f\))", contents):
        vt = f"{i}".replace("f,", " ")
        print(f"vt {vt}")
        model.write(f"vt {vt}\n")
