import ifcopenshell
import ifcopenshell.geom

ifc_path = r"C:\Users\arqui\OneDrive\Documentos\campus_ifce_fortaleza.ifc"
obj_path = r"C:\Users\arqui\OneDrive\Documentos\campus_ifce_fortaleza.obj"

print("Abrindo IFC...")
model = ifcopenshell.open(ifc_path)

settings = ifcopenshell.geom.settings()
settings.set(settings.USE_WORLD_COORDS, True)

print("Gerando geometria (pode demorar alguns minutos)...")
iterator = ifcopenshell.geom.iterator(settings, model)
if not iterator.initialize():
    raise RuntimeError("Nao foi possivel gerar a geometria do IFC.")

with open(obj_path, "w", encoding="utf-8") as f:
    offset = 1
    count = 0
    for shape in iterator:
        geom = shape.geometry
        verts = geom.verts
        faces = geom.faces

        for i in range(0, len(verts), 3):
            f.write(f"v {verts[i]} {verts[i+1]} {verts[i+2]}\n")

        for i in range(0, len(faces), 3):
            f.write(
                f"f {faces[i] + offset} "
                f"{faces[i+1] + offset} "
                f"{faces[i+2] + offset}\n"
            )

        offset += len(verts) // 3
        count += 1
        if count % 100 == 0:
            print(f"  {count} elementos processados...")

print("Concluido! OBJ gerado em:", obj_path)
