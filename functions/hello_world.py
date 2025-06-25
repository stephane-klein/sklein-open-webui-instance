from pydantic import BaseModel, Field

from open_webui.shared.utils import add

class Pipe:
    class Valves(BaseModel):
        pass

    def __init__(self):
        self.valves = self.Valves()

    def pipe(self, body: dict):
        print("body", body)

        return f"Hello, World! {add(1, 2)}"
