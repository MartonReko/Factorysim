import pytest
from sqlmodel import Session

from jubilant_disco.db import Db
from jubilant_disco.tables import (
    Good,
    Occupation,
    Person,
    Recipe,
    RecipeItem,
    Workplace,
)


@pytest.fixture(name="session")
def session_fixture():
    with Session(bind=Db().engine) as session:
        yield session


@pytest.fixture(name="create_db")
def create_db_fixture(session: Session) -> None:
    goods: dict[str, Good] = {
        "wheat": Good(name="wheat"),
        "bread": Good(name="bread"),
    }
    session.add_all(list(goods.values()))
    session.commit()

    recipes: dict[str, Recipe] = {"bread": Recipe(name="bread")}
    session.add_all(list(recipes.values()))
    session.commit()

    bread_recipe: list[RecipeItem] = [
        RecipeItem(
            good=goods["wheat"],
            recipe=recipes["bread"],
        ),
        RecipeItem(
            good=goods["bread"],
            recipe=recipes["bread"],
            type=RecipeItem.Type.OUTPUT,
        ),
    ]
    session.add_all(bread_recipe)
    session.commit()

    workplaces: dict[str, Workplace] = {
        "bread factory": Workplace(name="bread factory", recipe=recipes["bread"])
    }
    session.add_all(list(workplaces.values()))
    session.commit()

    people: list[Person] = [Person(money=10) for _i in range(0, 10)]
    session.add_all(people)
    session.commit()

    occupations: list[Occupation] = [
        Occupation(person=p, workplace=workplaces["bread factory"]) for p in people
    ]

    session.add_all(occupations)
    session.commit()
