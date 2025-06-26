from pydantic import BaseModel, Field

class Pipe:
    class Valves(BaseModel):
        FOO: str = Field(default="bar")

    def __init__(self):
        self.valves = self.Valves()

    def pipe(self, body: dict):
        print("Valves FOO", self.valves.FOO)
        print("body", body)
        return f"Hello, World! {self.valves.FOO}"
