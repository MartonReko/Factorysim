from sqlmodel import Session, select

from jubilant_disco.tables import Good


def test_goodsCreated(session: Session):
    statement = select(Good).where(Good.name == "wheat")
    for row in session.exec(statement).all():
        assert row.name == "wheat"
