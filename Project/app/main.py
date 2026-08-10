from fastapi import FastAPI

from Project.app.controllers import nfa_controller

app = FastAPI(title="NFA to DFA Web Server")

app.include_router(nfa_controller.router)