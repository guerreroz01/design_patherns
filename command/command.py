from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Optional


class Command(ABC):
    """
    The Command interface declares a method for executing a command.
    """

    @abstractmethod
    def execute(self) -> None:
        ...


class SimpleCommad(Command):
    """
    Some commands can implement simple operations on their own.
    """

    def __init__(self, payload: str) -> None:
        self._payload = payload

    def execute(self) -> None:
        print(f"SimpleCommand: See, I cand do simple things like printing"
              f"({self._payload})")


class ComplexCommand(Command):
    """
    However, some commands can delegate more complex operations to other
    objects, called "receivers."
    """

    def __init__(self, receiver: Receiver, a: str, b: str) -> None:
        """
        Complex commands can accept one or several receiver objects along with
        any context data via the constructor.
        """

        self._receiver = receiver
        self._a = a
        self._b = b

    def execute(self) -> None:
        """
        Commands can delegate to any methods of a receiver.
        """

        print("ComplexCommand: Complex stuff should be done by a receiver object", end="")
        self._receiver.do_something(self._a)
        self._receiver.do_something_else(self._b)


class Receiver:
    """
    The Receiver classes contain some important business logic. They know how
    to perform all kinds of operations, associated with carrying out a request.
    In fact, any class may serve as a Receiver.
    """

    def do_something(self, a: str) -> None:
        print(f"\nReceiver: Working on ({a}.)", end="")

    def do_something_else(self, b: str) -> None:
        print(f"\nReceiver: Also working on ({b}.)", end="")


class Invoker:
    """
    The Invoker is associated with one or several commands. It sends a request
    to the command.
    """

    def __init__(self) -> None:
        self._on_start: Optional[Command] = None
        self._on_finish: Optional[Command] = None

    @property
    def on_start(self) -> Optional[Command]:
        return self._on_start

    @property
    def on_finish(self) -> Optional[Command]:
        return self._on_finish

    @on_start.setter
    def on_start(self, command: Command) -> None:
        self._on_start = command

    @on_finish.setter
    def on_finish(self, command: Command) -> None:
        self._on_finish = command

    def do_something_important(self) -> None:
        """
        The Invoker does not depend on concrete commands or receiver classes.
        The Invoker passes a request to a receiver indirectly, by executing
        a command.
        """

        print("Invoker: Does anybody want something done before I begin?")
        if isinstance(self._on_start, Command):
            self._on_start.execute()

        print("Invoker: ...doing something really important...")

        print("Invoker: Does anybody want something done after I finish?")
        if isinstance(self._on_finish, Command):
            self._on_finish.execute()


def main():
    """
    The client code can parameterize an invoker with any commands.
    """

    invoker = Invoker()
    invoker._on_start = SimpleCommad("Say Hi")
    receiver = Receiver()
    invoker._on_finish = ComplexCommand(
        receiver, "Send Email", "Save report"
    )
    invoker.do_something_important()
    


if __name__ == '__main__':
    main()
