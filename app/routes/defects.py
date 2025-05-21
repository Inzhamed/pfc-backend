from fastapi import APIRouter, HTTPException
from app.models import Defect
from app.crud import create_defect, get_defect_by_id, list_defects, update_defect, delete_defect

router = APIRouter()

@router.post("/", response_model=str)
def api_create_defect(defect: Defect):
    return create_defect(defect)

@router.get("/", response_model=list[Defect])
def api_list_defects():
    return list_defects()

@router.get("/{defect_id}", response_model=Defect)
def api_get_defect(defect_id: str):
    defect = get_defect_by_id(defect_id)
    if not defect:
        raise HTTPException(status_code=404, detail="Defect not found")
    return defect

@router.put("/{defect_id}")
def api_update_defect(defect_id: str, update_data: dict):
    return update_defect(defect_id, update_data)

@router.delete("/{defect_id}")
def api_delete_defect(defect_id: str):
    return delete_defect(defect_id)