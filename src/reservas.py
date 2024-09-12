import random


def main():

    Titulo = input("Ingrese su titulo(Sr. o Sra.): ")
    Nombre = input("Ingrese su nombre: ")
    Apellido = input("Ingrese su apellido: ")
    nombre_completo = f"{Titulo} {Nombre} {Apellido}"
    print(f"{nombre_completo}, ¡Bienvenido a FastFast Airlines!")

    Distancia_ciudades = {
        "Medellin": {"Bogota": 240, "Cartagena": 461},
        "Bogota": {"Cartagena": 657, "Medellin": 240},
        "Cartagena": {"Medellin": 461, "Bogota": 657}
    }

    Origen = input("Seleccione su origen (Medellin, Bogota, Cartagena): ")
    Destino = input("Seleccione su destino (Medellin, Bogota, Cartagena): ")
    Dia_de_la_semana = input(
        "Ingrese el dia de la semana en que desea viajar: ")
    Dia_del_mes = int(input("Ingrese el dia del mes (1-30): "))

    def calcular_precio(Distancia, Dia_de_la_semana):
        if Distancia < 400:
            if Dia_de_la_semana.lower() in ["lunes", "martes", "miercoles", "jueves"]:
                return 79900
            else:
                return 119900
        else:
            if Dia_de_la_semana.lower() in ["lunes", "martes", "miercoles", "jueves"]:
                return 156900
            else:
                return 213000

    def silla_asignada(Preferencia_silla):
        if Preferencia_silla == "pasillo":
            return "C"
        elif Preferencia_silla == "ventana":
            return "A"
        else:
            return "B"

    Distancia = Distancia_ciudades[Origen][Destino]
    Precio = calcular_precio(Distancia, Dia_de_la_semana)

    Preferencia_silla = input(
        "¿prefiere un asiento en el pasillo, junto a la ventana, o si no tiene preferencia? ").lower()
    Silla = silla_asignada(Preferencia_silla)
    Numero_silla = random.randint(1, 29)
    silla_asignada = f"{Numero_silla}{Silla}"

    print(f"\nReserva confirmada:")
    print(f"Nombre: {nombre_completo}")
    print(f"Origen: {Origen}")
    print(f"Destino: {Destino}")
    print(f"Fecha de vuelo: {Dia_de_la_semana}{Dia_del_mes}")
    print(f"Precio del boleto: ${Precio}")
    print(f"Asiento asignado: {silla_asignada}")


if __name__ == "__main__":
    main()
