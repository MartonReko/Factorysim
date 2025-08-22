import weakref
from abc import ABC, abstractmethod
from typing import override


class Subject(ABC):
    def __init__(self) -> None:
        self.observers: weakref.WeakSet[Observer] = weakref.WeakSet()

    def attach(self, observer: "Observer") -> None:
        self.observers.add(observer)

    def detach(self, observer: "Observer") -> None:
        self.observers.remove(observer)

    @abstractmethod
    def notify(self) -> None: ...


class TimePassed(Subject):
    speed: int = 1

    @override
    def notify(self) -> None:
        for obs in self.observers:
            obs.update(self)


class Observer(ABC):
    @abstractmethod
    def update(self, subject: Subject) -> None: ...
