"""Main FastAPI application for Gen AI Gateway."""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict, List, Any, Optional
from gen_ai_gateway.src.models import (
    PresentationResponse,
    CreatePresentationRequest,
    GenerateContentRequest,
    HealthResponse
)
from gen_ai_gateway.src.services import AIGatewayService

app = FastAPI(
    title="Gen AI Gateway",
    description="A FastAPI-based Gen AI Gateway service with PPT wrapper functionality",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Initialize the AI Gateway service
ai_service = AIGatewayService()


@app.get("/", response_model=HealthResponse)
async def health_check() -> HealthResponse:
    """Health check endpoint."""
    return HealthResponse(
        status="healthy",
        message="Gen AI Gateway is running",
        version="1.0.0"
    )


@app.get("/presentations", response_model=List[PresentationResponse])
async def get_presentations() -> List[PresentationResponse]:
    """Get all presentations."""
    try:
        presentations = ai_service.get_all_presentations()
        return [PresentationResponse(**presentation) for presentation in presentations]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/presentations/{presentation_id}", response_model=PresentationResponse)
async def get_presentation(presentation_id: str) -> PresentationResponse:
    """Get a specific presentation by ID."""
    try:
        presentation = ai_service.get_presentation_by_id(presentation_id)
        return PresentationResponse(**presentation)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/presentations", response_model=PresentationResponse)
async def create_presentation(request: CreatePresentationRequest) -> PresentationResponse:
    """Create a new presentation."""
    try:
        presentation = ai_service.create_presentation(
            title=request.title,
            author=request.author,
            template_id=request.template_id
        )
        return PresentationResponse(**presentation)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/generate", response_model=Dict[str, Any])
async def generate_content(request: GenerateContentRequest) -> Dict[str, Any]:
    """Generate AI content for presentations."""
    try:
        content = ai_service.generate_slide_content(
            topic=request.topic,
            slide_type=request.slide_type
        )
        return content
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/templates", response_model=List[Dict[str, Any]])
async def get_templates() -> List[Dict[str, Any]]:
    """Get all available presentation templates."""
    try:
        templates = ai_service.get_templates()
        return templates
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/stats", response_model=Dict[str, Any])
async def get_stats() -> Dict[str, Any]:
    """Get presentation statistics."""
    try:
        stats = ai_service.get_presentation_stats()
        return stats
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


def main():
    """Main entry point for the application."""
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)


if __name__ == "__main__":
    main()
