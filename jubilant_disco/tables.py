from typing import override
from sqlmodel import Relationship

from jubilant_disco.models import (
    ActorBase,
    GoodBase,
    OccupationBase,
    PersonBase,
    ProductBase,
    RecipeBase,
    RecipeItemBase,
    WorkplaceBase,
)
from jubilant_disco.observer import Observer, Subject
from jubilant_disco.dbManager import dbManager


class Actor(ActorBase, table=True):
    products: list["Product"] | None = Relationship(back_populates="actor")

    def pay(self, actor: "Actor", money: int) -> None | bool:
        if self.money < money:
            return False

        actor.money += money
        self.money -= money

        dbManager.writeToDb([actor, self])

    def buy(self, product: "Product") -> None:
        pass


class Good(GoodBase, table=True):
    products: list["Product"] | None = Relationship(back_populates="good")
    recipe_items: list["RecipeItem"] | None = Relationship(back_populates="good")


class Product(ProductBase, table=True):
    good: "Good" = Relationship(back_populates="products")
    actor: "Actor" = Relationship(back_populates="products")

    def split(self, quantity: int) -> None:
        pass

    def use(self) -> None:
        pass


class RecipeItem(RecipeItemBase, table=True):
    good: "Good" = Relationship(back_populates="recipe_items")
    recipe: "Recipe" = Relationship(back_populates="recipe_items")


class Recipe(RecipeBase, table=True):
    recipe_items: list["RecipeItem"] | None = Relationship(back_populates="recipe")
    workplaces: list["Workplace"] | None = Relationship(back_populates="recipe")


class Occupation(OccupationBase, table=True):
    workplace: "Workplace" = Relationship(back_populates="occupations")
    person: "Person" = Relationship(back_populates="occupations")


class Person(PersonBase, Observer, table=True):
    occupations: list["Occupation"] | None = Relationship(back_populates="person")

    @override
    def update(self, subject: Subject) -> None:
        pass


class Workplace(WorkplaceBase, table=True):
    recipe: "Recipe" = Relationship(back_populates="workplaces")
    occupations: list["Occupation"] | None = Relationship(back_populates="workplace")

    def produce(self) -> None:
        pass
