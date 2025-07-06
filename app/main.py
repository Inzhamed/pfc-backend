from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from app.routes import users, defects, reports, notifications, auth

app = FastAPI()
app.mount(
    "/static",
    StaticFiles(directory="../pfc-desktop-pyqt/static"),
    name="static"
)

# Allow CORS for your frontend (adjust the origin in production)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://inzhamed.github.io/pfc/"],  # Replace "*" with your frontend URL in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register routers
app.include_router(users.router, prefix="/api/users", tags=["users"])
app.include_router(defects.router, prefix="/api/defects", tags=["defects"])
app.include_router(reports.router, prefix="/api/reports", tags=["reports"])
app.include_router(notifications.router, prefix="/api/notifications", tags=["notifications"])
app.include_router(auth.router, prefix="/api/login", tags=["auth"])

