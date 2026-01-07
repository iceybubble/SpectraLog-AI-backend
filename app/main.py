from fastapi import FastAPI
from app.api.v1.ingest import router as ingest_router
from app.api.v1.cases import router as cases_router

app = FastAPI(title="SpectraLogAI Backend")

app = FastAPI(
    title="SpectraLog AI - Android Ingestion API",
    version="0.1.0",
)


@app.get("/health")
def health():
    return {"status": "ok"}


# Include the /api/v1/ingest endpoint
app.include_router(ingest_router, prefix="/api/v1")
app.include_router(ingest_router)
app.include_router(cases_router, prefix="/api/v1")
