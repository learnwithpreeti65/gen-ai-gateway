"""Pydantic models for the Gen AI Gateway."""

from pydantic import BaseModel
from typing import Dict, List, Any, Optional
from datetime import datetime


class HealthResponse(BaseModel):
    """Health check response model."""
    status: str
    message: str
    version: str


class PresentationContent(BaseModel):
    """Presentation content model."""
    summary: str
    key_topics: List[str]
    audience: str


class PresentationResponse(BaseModel):
    """Presentation response model."""
    id: str
    title: str
    author: str
    created_at: str
    slides_count: int
    status: str
    content: PresentationContent
    template_id: Optional[str] = None


class CreatePresentationRequest(BaseModel):
    """Request model for creating a new presentation."""
    title: str
    author: str
    template_id: Optional[str] = None


class GenerateContentRequest(BaseModel):
    """Request model for generating AI content."""
    topic: str
    slide_type: str = "content"


class SlideContent(BaseModel):
    """Slide content model."""
    bullet_points: List[str]
    notes: str
    suggested_images: List[str]


class GeneratedSlide(BaseModel):
    """Generated slide model."""
    slide_type: str
    topic: str
    title: str
    content: SlideContent
    generated_at: str


class Template(BaseModel):
    """Template model."""
    id: str
    name: str
    description: str
    category: str
    slides_included: List[str]


class PresentationStats(BaseModel):
    """Presentation statistics model."""
    total_presentations: int
    completed_presentations: int
    in_progress_presentations: int
    total_slides: int
    average_slides_per_presentation: float
    available_templates: int
