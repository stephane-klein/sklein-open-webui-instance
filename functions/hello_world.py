from pydantic import BaseModel, Field

class Pipe:
    class Valves(BaseModel):
        pass

    def __init__(self):
        self.valves = self.Valves()

    def pipe(self, body: dict):
        print("body", body)
        return "Hello, World!"
