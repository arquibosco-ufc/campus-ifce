# Campus IFCE Fortaleza - Cenario 3D

Programa Python que usa o modelo 3D do campus do IFCE Fortaleza (convertido de IFC para OBJ) como cenario base.

## Como o modelo foi gerado

1. Fonte: areas internas ifce fortaleza layoutqqqq ATUALIZACAO.ifc
2. Conversao para OBJ via converter.py (usa ifcopenshell)
3. Resultado: campus_ifce_fortaleza.obj
   - ~38 MB
   - 355.228 vertices
   - 721.115 faces

## Como rodar

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python testar_obj.py
```
