# Patrones en Python
Patrones de diseño en Python

Patrón | Referencia
Factory Method | Tanto en factoryMethod.py como en laberintoBuilder.py hay factory methods
Decorator | Se puede ver la estructura del Decorator en los elementos ElementoMapa, Contenedor y Decorator (tiene componente)
Strategy | Este patrón se utiliza en diferentes lugares (las orientaciones, en las bombas)
Composite | Los participantes del Composite son ElementoMapa, Contenedor (tiene hijos) y Hoja
Template Method | Este patrón se utiliza en el método "actua" en Modo (Bicho tiene Modo)
Iterator | ElementoMapa se puede recorrer gracias al método "enumerar", es un iterador interno
Abstract Factory | Se implementa en la clase AbstractFactory junto con el método crearLaberinto de JuegoLaberinto (tiene un parámetro que es un objeto de tipo AbstractFactory
Singleton | Se puede aplicar a las orientaciones
Builder | Este patrón se implementa en las clases de laberintoBuilder.py
Bridge | Los elementos Contenedor "tienen" Forma, ahí se aplica el Bridge
Mediator | Los elementos de tipo Contenedor tienen una colección de ocupantes (son elementos de tipo Ente), el contenedor hace de mediador
Observer | Se aplicará a la vista (laberintoGUI.py)
