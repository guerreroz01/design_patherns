from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Optional


class Strategy(ABC):
    @abstractmethod
    def execute(self, a: int, b: int) -> int:
        ...


class Context:
    def __init__(self) -> None:
        self._strategy: Optional[Strategy] = None

    @property
    def strategy(self) -> Optional[Strategy]:
        print("La estrategia actual es {self._strategy.__name__()}")
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: Strategy) -> None:
        self._strategy = strategy

    def calculate(self, a: int, b: int) -> int:
        return self._strategy.execute(a, b)  # type: ignore


class SumaStrategy(Strategy):
    def execute(self, a: int, b: int) -> int:
        print("La estrategia usada fue la suma.")
        return a + b


class RestaStrategy(Strategy):
    def execute(self, a: int, b: int) -> int:
        print("La estrategia usada fue la resta.")
        return a - b


class MultiplicacionStrategy(Strategy):
    def execute(self, a: int, b: int) -> int:
        print("La estrategia utilizada fue la multiplicacion.")
        return a * b


def main():
    calculator = Context()
    calculator.strategy = SumaStrategy()

    print(calculator.calculate(15, 20))
    print("\n")

    calculator.strategy = RestaStrategy()

    print(calculator.calculate(10, 5))


if __name__ == "__main__":
    main()
