from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Import your snapshot router.
# Make sure you have created backend/app/routes/snapshot.py with a router variable.
from app.routes.snapshot import router as snapshot_router
from app.routes.tax import router as tax_router

app = FastAPI(title="Financial Snapshot API")

# Configure CORS middleware so that your frontend (e.g., running on localhost:5173) can access the API.
origins = [
    "http://localhost:5173",  # Replace with your frontend URL during development.
    "http://localhost",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,         # Allows specified origins.
    allow_credentials=True,
    allow_methods=["*"],           # Allows all HTTP methods.
    allow_headers=["*"],
)

# Include your snapshot routes under the /api prefix.
app.include_router(snapshot_router, prefix="/api")
app.include_router(tax_router, prefix="/api")

# Entry point for running the app.
if __name__ == "__main__":
    # Use uvicorn to run the app on port 8000.
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
