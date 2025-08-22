from sqlalchemy import Engine
from sqlmodel import SQLModel, StaticPool, create_engine

from jubilant_disco.observer import TimePassed


class Db:
    def __init__(self, _file_name: str = "") -> None:
        self.time_passed: TimePassed = TimePassed()
        self.file_name: str = _file_name
        self.url: str = f"sqlite:///{self.file_name}"
        self.connect_args: dict[str, bool] = {"check_same_thread": False}
        self.engine: Engine = (
            create_engine(url=self.url, echo=True, connect_args=self.connect_args)
            if self.file_name != ""
            else create_engine(
                url=self.url,
                echo=True,
                connect_args=self.connect_args,
                poolclass=StaticPool,
            )
        )
        SQLModel.metadata.create_all(self.engine)
