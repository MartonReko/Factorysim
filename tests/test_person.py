from sqlmodel import Session, select

from jubilant_disco.tables import Person


def test_payTest(session: Session):
    selPerson1 = select(Person).where(Person.id == 1)
    selPerson2 = select(Person).where(Person.id == 2)
    person1 = session.exec(selPerson1).first()
    person2 = session.exec(selPerson2).first()

    session.commit()
