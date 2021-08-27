1. Scope and NameSpace
    Built-in names(abc)
    Global names in module
    Local names on a function invocation

    The scope is a regian in a program where a namespace is directly accesible
    in classes at least three nested scopes:
        - innermost scope
        - enclosing functions
        - module's global namespace
        - the outermost built-in names

2. OOP
    - programming paradigm
    - concept of classes and objects
    - class is a blueprint that defined the nature of a future object
    - a class is used to create individual instance of object
    - object is data abstraction that captures an internal representation and an interface
    - objects has:
        - State : color, size, weight
        - Behavior: turn on, turn off

3.Class
    Classes support tho kinds of operations:
        - attribute references - access atribute using "."
        - instantiation - uses finction notations

    attributes
        attribute references:
            - methods - define the behavior (__init__ is dunder method)
            - data attributes - state of the objects    
                - instance variables
                - class variables

                - __doc__
                - __dict__

4. Inheritance
    - is the capability of one class to inherit the methods and properties from another class
    4 types
        - Single
        - Multiple -(mother, father - child(mather,father))
        - Myltilevel -(grandpa, father(grandpa), child(father))
        - Hierarchical - (parent , child1(parent), child2(parent))

    - What is super()
        - Built-in method which returns a temporary object of the superclass

    - mixins 
        - Allow inheritance and use of only desired features from the parent class not all of them

5. Polymorphism
    - Polymorphism is based on the Greek words Poly (many) and morphism (forms)
    - In software engineering, polymorphism means the usage of an objects though the interface of their base class - използването на обекти през интерфейса на техните базови класове.
    -means same function name being uses for different types

6. abstraction

    the main benefit of an abstract class is to provide guidline for its _subclasses
        we have abstractmethods we do not implement but the subclasses must has thair implementation.


7. Design Patterns
    - general and reusable solutions(ideas) to common problems in software design

    - Creational
    - Structural    
    - Behavior

    1. Creational Pattern
        - deal with object creation mechanisms
        Two main ideas: 
            - Encapsulating knowledge about which classes the system uses
            - Hiding how instances of these classes are created

        list of crational patterns
            - Singleton
            - Simple Factory
            - Factory Method
            - Abstract factory
            - Builder
            - Prototype
            - Fluent Interface
            - Object Pool
            - Lazy initialization

    2. Structural Pattern
        Describe ways to assemle objects to implement a new functionality

        list:
            - Facade
            - Composite
            - Flyweight
            - Proxy
            - Decorator
            - Adapter
            - Bridge

    3. Behavioral patterns

        Concerned with interaction between objects
            - either with the assignment of responsibilities
            - increases flexibility

        list:
            -chain of responsibility
            -iterator
            -command
            -template method
            -strategy
            -observer
            -mediator
            -memento
            -state
            -interpreter
            -visitor
