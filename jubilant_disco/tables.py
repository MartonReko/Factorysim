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
from jubilant_disco.observer import Observer


class Actor(ActorBase, table=True):
    products: list["Product"] | None = Relationship(back_populates="actor")


class Good(GoodBase, table=True):
    products: list["Product"] | None = Relationship(back_populates="good")
    recipe_items: list["RecipeItem"] | None = Relationship(back_populates="good")


class Product(ProductBase, table=True):
    good: "Good" = Relationship(back_populates="products")
    actor: "Actor" = Relationship(back_populates="products")


class RecipeItem(RecipeItemBase, table=True):
    good: "Good" = Relationship(back_populates="recipe_items")
    recipe: "Recipe" = Relationship(back_populates="recipe_items")


class Recipe(RecipeBase, table=True):
    recipe_items: list["RecipeItem"] | None = Relationship(back_populates="recipe")
    workplaces: list["Workplace"] | None = Relationship(back_populates="recipe")


class Occupation(OccupationBase, table=True):
    workplace: "Workplace" = Relationship(back_populates="occupations")
    person: "Person" = Relationship(back_populates="occupations")


class Person(PersonBase, table=True):
    occupations: list["Occupation"] | None = Relationship(back_populates="person")


class Workplace(WorkplaceBase, Observer, table=True):
    recipe: "Recipe" = Relationship(back_populates="workplaces")
    occupations: list["Occupation"] | None = Relationship(back_populates="workplace")
