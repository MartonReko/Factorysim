from sqlalchemy import Engine
from sqlmodel import Session, SQLModel, create_engine, select

from jubilant_disco.observer import TimePassed
from jubilant_disco.tables import (
    Good,
    Occupation,
    Person,
    Recipe,
    RecipeItem,
    Workplace,
)


def createDb() -> Engine:
    # In memory only
    sqlite_url = "sqlite://"

    connect_args = {"check_same_thread": False}
    engine = create_engine(sqlite_url, echo=True, connect_args=connect_args)
    with Session(engine) as session:
        SQLModel.metadata.drop_all(engine)
        SQLModel.metadata.create_all(engine)
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

        timePassed: TimePassed = TimePassed()
        for person in people:
            timePassed.attach(person)
        for workplace in workplaces.values():
            timePassed.attach(workplace)

        _ = people[0].pay(people[1], 1)
        session.add_all([people[0], people[1]])
        session.commit()

    return engine


class Test:
    engine: Engine = createDb()

    def test_goodsCreated(self):
        with Session(self.engine) as session:
            statement = select(Good).where(Good.name == "wheat")
            results = session.exec(statement)
            count: int = 0
            for g in results:
                count += 1
                assert g.name == "wheat"
            assert count == 1

    def test_payTest(self):
        with Session(self.engine) as session:
            selPerson1 = select(Person).where(Person.id == 1)
            selPerson2 = select(Person).where(Person.id == 2)
            person1 = session.exec(selPerson1).first()
            person2 = session.exec(selPerson2).first()

            # TODO: finish this

            session.commit()
