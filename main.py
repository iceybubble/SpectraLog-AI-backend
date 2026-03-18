from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Direct imports
from app.api.v1 import logs, alerts, correlation, xai, dashboard, cases, ingest

app = FastAPI(
    title="SpectraLog AI API",
    description="AI-Powered Forensic SIEM Platform",
    version="1.0.0",
)

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://localhost:3000",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers directly
app.include_router(logs.router, prefix="/api/v1")
app.include_router(alerts.router, prefix="/api/v1")
app.include_router(correlation.router, prefix="/api/v1")
app.include_router(xai.router, prefix="/api/v1")
app.include_router(dashboard.router, prefix="/api/v1")
app.include_router(cases.router, prefix="/api/v1")
app.include_router(ingest.router, prefix="/api/v1")


@app.get("/")
async def root():
    return {
        "message": "SpectraLog AI - Forensic SIEM Platform",
        "version": "1.0.0",
        "status": "running",
        "docs": "/docs"
    }


@app.get("/health")
async def health_check():
    return {"status": "healthy"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)