from fastapi import APIRouter, HTTPException

from Project.app.gateways.nfa_gateway import procesar_conversion, procesar_simulacion
from Project.app.models.schemas import (
    DFAResponse,
    NFARequest,
    SimulateRequest,
    SimulateResponse,
)

router = APIRouter()


@router.post("/convert", response_model=DFAResponse)
def convertir(nfa: NFARequest) -> DFAResponse:
    try:
        resultado = procesar_conversion(nfa)
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error))

    return resultado


@router.post("/simulate", response_model=SimulateResponse)
def simular(request: SimulateRequest) -> SimulateResponse:
    try:
        resultado = procesar_simulacion(request)
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error))

    return resultado