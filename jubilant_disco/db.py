from sqlalchemy import Engine
from sqlmodel import StaticPool, create_engine

from jubilant_disco.observer import TimePassed


class Db:
    def __init__(self, _file_name: str = "") -> None:
        time_passed: TimePassed = TimePassed()
        file_name: str = _file_name
        url: str = f"sqlite:///{file_name}"
        connect_args: dict[str, bool] = {"check_same_thread": False}
        engine: Engine = create_engine(url=url, echo=True, connect_args=connect_args)
        if file_name == "":
            engine = create_engine(
                url="sqlite://",
                echo=True,
                connect_args={"check_same_thread": False},
                poolclass=StaticPool,
            )
