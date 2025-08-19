from sqlmodel import SQLModel, Session


class dbManager:
    @staticmethod
    def writeToDb(data: list[SQLModel]) -> None:
        from jubilant_disco.db import engine

        if data:
            with Session(engine) as session:
                session.add_all(data)
                session.commit()
