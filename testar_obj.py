import trimesh

obj_path = r"C:\projetos\campus-ifce\campus_ifce_fortaleza.obj"
cena = trimesh.load(obj_path, force="scene")

print("Tipo:", type(cena).__name__)
print("Objetos na cena:", len(cena.geometry))
print("Bounding box:", cena.bounds)
print("Total de vÃ©rtices:", sum(len(g.vertices) for g in cena.geometry.values()))
print("Total de faces:", sum(len(g.faces) for g in cena.geometry.values()))