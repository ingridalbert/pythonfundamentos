#comentario
print("Hola mundo")
nombre: str = "Ingrid"
print("Me llamo " + nombre)
apellido: str = "Albert"
print(f"Soy {nombre.upper()} {apellido.lower()}")
edad: int = 22
ciudad: str = "Castellón"
tengo_carnet: bool = True
print(f"{ciudad} {edad} {tengo_carnet}")
print(len(nombre))
print(nombre[0])
print(apellido[len(apellido)-1])
print(apellido[-1])
Ingrid: dict[str, str | int | bool] = {
    "nombre": "Ingrid",
    "edad": 22,
    "ciudad": "Castellón",
    "solterx": True
}
print(Ingrid["nombre"])
compra: list[object] = ["pan", "leche", "huevos"]
compra.append("frutas")
compra.insert(1, "verduras")
compra.pop(-1)
print(compra)

culpable: bool 
if culpable:
    print("Es culpable")
else:
    print("No es culpable")