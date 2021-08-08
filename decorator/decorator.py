from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Optional


class Component(ABC):
    """
    the base class Component interface defines operations that can be altered 
    by decorators.
    """
    @abstractmethod
    def operation(self) -> str:
        ...


class ConcreteComponent(Component):
    def operation(self) -> str:
        return "ConcreteComponent"


class Decorator(Component):
    """
    the base Decorator class follows the same interface as the other components
    the primary purpouse of this class is to define the wrapping interface for
    all concrete decorators. The default implementation of the wrapping code might
    include a field for storing a wrapped component and the means to initialize it
    """

    _component: Optional[Component] = None

    def __init__(self, component: Component) -> None:
        self._component = component

    @property
    def component(self) -> str:
        """
        The decorator delegates all work to the wrapped component.
        """

        return self._component

    def operation(self) -> str:
        return self._component.operation()


class ConcreteDecoratorA(Decorator):
    """The Concrete Decorator call the wrapped object and alter its result in 
    some way.
    """

    def operator(self) -> str:
        """Decorator may call parent implementation of the operation, instead 
        of calling the weapped object directly. This approuch simplifies 
        extensions of decorator classes
        """

        return f"ConcreteDecoratorA({self.component.operation()})"


class ConcreteDecoratorB(Decorator):
    """Decorator can excecute their behavior either before or after the call
    to a wrapped object
    """

    def operation(self) -> str:
        return f"ConcreteDecoratorB({self.component.operation()})"


def main():
    # this way the client code can support both simple components...
    simple = ConcreteComponent()
    print("Client: I've got a simple component:")
    print(simple.operation())
    print("\n")

    # ...as well as decorated ones.
    #
    # Note how decorators can wrap not only simple components but the other
    # decorators as well.
    decorator1 = ConcreteDecoratorA(simple)
    decorator2 = ConcreteDecoratorB(decorator1)
    print("Client: Now I've got a decorated component:")
    print(decorator2.operation())


if __name__ == "__main__":
    main()
