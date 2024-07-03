from dataclasses import dataclass
@dataclass
class State:

    StateAbb: str
    CCode: int
    StateNme: str

    def __hash__(self):
        return hash(self.CCode)
