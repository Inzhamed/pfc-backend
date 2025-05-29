from fastapi import APIRouter, HTTPException, Request
from app.models import Report
from app.crud import create_report, get_report_by_id, list_reports_for_defect, update_report, delete_report, list_reports

router = APIRouter()

@router.post("/", response_model=str)
def api_create_report(report: Report, request: Request):
    return create_report(report)

@router.get("/", response_model=list[Report])
def api_list_reports():
    return list_reports()

@router.get("/defect/{defect_id}", response_model=list[Report])
def api_list_reports_for_defect(defect_id: str):
    return list_reports_for_defect(defect_id)

@router.get("/{report_id}", response_model=Report)
def api_get_report(report_id: str):
    report = get_report_by_id(report_id)
    if not report:
        raise HTTPException(status_code=404, detail="Report not found")
    return report

@router.put("/{report_id}")
def api_update_report(report_id: str, update_data: dict):
    return update_report(report_id, update_data)

@router.delete("/{report_id}")
def api_delete_report(report_id: str):
    return delete_report(report_id)