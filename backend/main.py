from fastapi import FastAPI
from database.mongodb import connect_db
from routes.auth import router as auth_router
from routes.content_calendar import router as calendar_router
from routes.captions import router as caption_router
from routes.branding import router as branding_router
from routes.campaigns import router as campaign_router
from routes.seo import router as seo_router
from routes.trends import router as trend_router
from routes.ads import router as ad_router
from routes.analytics import router as analytics_router
from routes.design import router as design_router
from routes.mockups import router as mockup_router
from fastapi.middleware.cors import CORSMiddleware
from routes.content_brief import router as brief_router

app = FastAPI(
    title="MarketMind AI API",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://127.0.0.1:3000",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router)
app.include_router(calendar_router)
app.include_router(caption_router)
app.include_router(branding_router)
app.include_router(campaign_router)
app.include_router(seo_router)
app.include_router(trend_router)
app.include_router(ad_router)
app.include_router(analytics_router)
app.include_router(design_router)
app.include_router(mockup_router)
app.include_router(brief_router)

@app.on_event("startup")
def startup_db():
    connect_db()


@app.get("/")
def root():
    return {
        "message": "Welcome to MarketMind AI API"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }
