# Single responsibility
# Open/Closed
# Liskov substitution
# Interface sugregation
# Dependancy invertion

SOLID make your code:
    - Extendable
    - Logical
    - Easier to read


1. Single responsibility

    Each class is responsible for only one thing and should have only one reason to change
    
    More than one responsibility is called coupling (обвързаност)


2. Open/Closed

    Classes, modules and functions should be open for extension, but closed for modifications

    This can be achieved through:

        - Abstraction
        - Mix-ins
        - Monkey-Patching
        - Generic functions (using overloading)


3. Liskov substitution(заменим) 

    - унаследените типове трябва да могат да заменят напълно базовите си типове.
    - defines the relationship between subtypes and supertypes in object-oriented programming

    Derived types(производните типове) must be completely substitutable for their base types

    Whatever the parent can do, the descendants should at least be able to do that too

    Derived classes

        - only extend functionalities of the base class
        - must not remove base class behavior


4. Interface sugregation

    A client should not depend on methods it does not use
        - a good way of ensuring this is by separation through multiple inheritance
        - this is precisely the purpose of the mix-ins to provide multiple clients specific behaviors
    
    Python doesn't have interfaces 


5. Dependancy invertion

    Design principle by which we protect our code by making it independent of things that are fragile, volatile or out of our control

    - Dependency Injection


*monkey patching
    Dynamically add an attribute to a instance of a class