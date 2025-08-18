from abc import ABC, abstractmethod
from typing import override


class Subject(ABC):
    observers: list["Observer"] = []

    def __init__(self) -> None:
        self.observers = []

    def attach(self, observer: "Observer") -> None:
        self.observers.append(observer)

    def detach(self, observer: "Observer") -> None:
        self.observers.remove(observer)

    @abstractmethod
    def notify(self) -> None:
        pass


class Observer(ABC):
    def update(self, subject: Subject) -> None:
        pass

    def update(self, subject: "TimePassed") -> None:
        pass


class TimePassed(Subject):
    speed: int = 1

    @override
    def notify(self) -> None:
        for obs in self.observers:
            obs.update(self)
