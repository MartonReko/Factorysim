from enum import Enum
from typing import override

from sqlmodel import SQLModel, Field, Session

from jubilant_disco.observer import Observer, TimePassed


class ActorBase(SQLModel):
    id: int | None = Field(default=None, primary_key=True)
    money: int = Field(default=0)

    def pay(self, actor: "ActorBase", money: int) -> None | bool:
        if self.money < money:
            return False

        actor.money += money
        self.money -= money

    def buy(self, product: "ProductBase") -> None:
        pass


class GoodBase(SQLModel):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field()


class RecipeItemBase(SQLModel):
    id: int | None = Field(default=None, primary_key=True)
    good_id: int = Field(default=None, foreign_key="good.id")
    recipe_id: int = Field(default=None, foreign_key="recipe.id")
    quantity: int = Field(default=1)

    class Type(Enum):
        INPUT = "INPUT"
        OUTPUT = "OUTPUT"

    type: Type = Type.INPUT


class RecipeBase(SQLModel):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field()


class OccupationBase(SQLModel):
    id: int | None = Field(default=None, primary_key=True)
    workplace_id: int | None = Field(default=None, foreign_key="workplace.id")
    person_id: int | None = Field(default=None, foreign_key="person.id")
    wage: int = Field(default=0)


class PersonBase(ActorBase, Observer):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(default="")
    birthYear: int = 0
    happiness: int = Field(default=0)
    hunger: int = Field(default=100)

    @override
    def update(self, subject: TimePassed) -> None:
        self.hunger -= subject.speed
        self.happiness -= subject.speed


class WorkplaceBase(ActorBase, Observer):
    id: int | None = Field(default=None, primary_key=True)
    recipe_id: int | None = Field(default=None, foreign_key="recipe.id")
    name: str = Field()
    maxWorkers: int = Field(default=0)

    def produce(self) -> None:
        pass

    @override
    def update(self, subject: TimePassed) -> None:
        self.produce()


class ProductBase(SQLModel):
    id: int | None = Field(default=None, primary_key=True)
    good_id: int | None = Field(default=None, foreign_key="good.id")
    actor_id: int | None = Field(default=None, foreign_key="actor.id")
    quantity: int = Field()
    price: float | None = Field(default=0)

    def split(self, quantity: int) -> None:
        pass

    def use(self) -> None:
        pass
