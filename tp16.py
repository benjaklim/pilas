class Pila:
    def __init__(self):
        self.elementos = []
    
    def apilar(self, elemento):
        self.elementos.append(elemento)
    
    def desapilar(self):
        if not self.esta_vacia():
            return self.elementos.pop()
        return None
    
    def esta_vacia(self):
        return len(self.elementos) == 0
    
    def cima(self):
        if not self.esta_vacia():
            return self.elementos[-1]
        return None
    
    def tamano(self):
        return len(self.elementos)
    
    def __str__(self):
        return str(self.elementos)

pila_ep5 = Pila()
pila_ep7 = Pila()

personajes_ep5 = ["Luke Skywalker", "Leia Organa", "Han Solo", "Chewbacca", "Darth Vader", "Yoda", "R2-D2", "C-3PO"]
for personaje in personajes_ep5:
    pila_ep5.apilar(personaje)

personajes_ep7 = ["Rey", "Finn", "Poe Dameron", "Han Solo", "Leia Organa", "Chewbacca", "Kylo Ren", "Luke Skywalker", "R2-D2", "C-3PO"]
for personaje in personajes_ep7:
    pila_ep7.apilar(personaje)

conjunto_ep5 = set(pila_ep5.elementos)

pila_interseccion = Pila()

while not pila_ep7.esta_vacia():
    personaje = pila_ep7.desapilar()
    if personaje in conjunto_ep5:
        pila_interseccion.apilar(personaje)

print("Personajes que aparecen en ambos episodios:", pila_interseccion)
