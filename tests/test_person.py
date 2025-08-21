from sqlmodel import Session, select

from jubilant_disco.tables import Person


def test_pay(session: Session):
    selPerson1 = select(Person).where(Person.id == 1)
    person1 = session.exec(selPerson1).first()
    assert person1 is not None
    selPerson2 = select(Person).where(Person.id == 2)
    person2 = session.exec(selPerson2).first()
    assert person2 is not None
    person1.pay(person2, 10)

    session.add_all([person1, person2])
    session.commit()

    assert person1.money == 0
    assert person2.money == 20
