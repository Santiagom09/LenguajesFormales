from pydantic import BaseModel, Field


class Transition(BaseModel):
    from_state: int = Field(alias="from")
    symbol: str
    to: list[int]
    model_config = {"populate_by_name": True}


class NFARequest(BaseModel):
    states: list[int]
    alphabet: list[str]
    initial: int
    accepting: list[int]
    transitions: list[Transition]


class DFATransition(BaseModel):
    from_state: str = Field(alias="from")
    symbol: str
    to: str
    model_config = {"populate_by_name": True}


class DFAResponse(BaseModel):
    dfaStates: list[str]
    transitions: list[DFATransition]
    acceptingStates: list[str]
    initial: str


class SimulateRequest(BaseModel):
    dfa: DFAResponse
    input: str


class SimulateResponse(BaseModel):
    path: list[str]
    accepted: bool

    