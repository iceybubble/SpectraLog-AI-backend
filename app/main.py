from fastapi import FastAPI

from app.api.v1.ingest import router as ingest_router  # type: ignore

app = FastAPI(
    title="SpectraLog AI - Android Ingestion API",
    version="0.1.0",
)


@app.get("/health")
def health():
    return {"status": "ok"}


# Include the /api/v1/ingest endpoint
app.include_router(ingest_router, prefix="/api/v1")
