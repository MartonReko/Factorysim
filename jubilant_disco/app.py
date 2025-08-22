from fastapi import FastAPI

app = FastAPI()


""" @app.on_event("startup")
def on_startup():
    SQLModel.metadata.create_all(engine)


@app.get("/people/", response_model=list[Person])
def read_heroes():
    with Session(engine) as session:
        people = session.exec(select(Person)).all()
        return people
 """
