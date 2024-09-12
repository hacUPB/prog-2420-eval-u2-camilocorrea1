
def main():
    
    Altitud_inicial = float(input("Ingrese la altitud inicial del satélite (en kilómetros): "))
    Arrastre = float(input("Introduzca el coeficiente de arrastre inicial: "))
    Alt_minima = float(input("Ingrese la altitud mínima segura (en kilómetros): "))
    
    Alt_actual = Altitud_inicial
    Orbitas_completadas = 0
    
    while Alt_actual > Alt_minima and Arrastre > 0.00001:
        
        altitud_perdida = Arrastre * Alt_actual
        Alt_actual -= altitud_perdida
        Arrastre += 0.001
        Orbitas_completadas +=1
        
        
    if Alt_actual <= Alt_minima:
        print(f"El satélite ha reingresado en la atmósfera terrestre después de {Orbitas_completadas} órbitas.")
        
         
        
        
        
    

if __name__ == "__main__":
    main()

    
   
  