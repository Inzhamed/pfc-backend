from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes import users, defects, reports, notifications

app = FastAPI()

# Allow CORS for your frontend (adjust the origin in production)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace "*" with your frontend URL in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register routers
app.include_router(users.router, prefix="/api/users", tags=["users"])
app.include_router(defects.router, prefix="/api/defects", tags=["defects"])
app.include_router(reports.router, prefix="/api/reports", tags=["reports"])
app.include_router(notifications.router, prefix="/api/notifications", tags=["notifications"])