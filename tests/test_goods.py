from sqlmodel import Session, select

from jubilant_disco.tables import Good


def test_goodsCreated(session: Session):
    statement = select(Good).where(Good.name == "wheat")
    results = session.exec(statement)
    count: int = 0
    for g in results:
        count += 1
        assert g.name == "wheat"
    assert count == 1
