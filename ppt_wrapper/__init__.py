"""PPT Wrapper module for Gen AI Gateway."""

from typing import Dict, List, Any, Optional
from datetime import datetime


class PPTWrapper:
    """Wrapper class for PPT-related operations with mock data."""
    
    def __init__(self):
        """Initialize the PPT wrapper with mock data."""
        self._mock_presentations = [
            {
                "id": "ppt_001",
                "title": "AI in Healthcare",
                "author": "Dr. Jane Smith",
                "created_at": "2024-01-15T10:30:00Z",
                "slides_count": 25,
                "status": "completed",
                "content": {
                    "summary": "Comprehensive overview of AI applications in healthcare",
                    "key_topics": ["Machine Learning", "Medical Imaging", "Drug Discovery"],
                    "audience": "Healthcare professionals"
                }
            },
            {
                "id": "ppt_002",
                "title": "Future of Transportation",
                "author": "John Doe",
                "created_at": "2024-02-20T14:15:00Z",
                "slides_count": 18,
                "status": "in_progress",
                "content": {
                    "summary": "Exploring autonomous vehicles and smart city infrastructure",
                    "key_topics": ["Autonomous Vehicles", "Smart Infrastructure", "Sustainability"],
                    "audience": "Urban planners and engineers"
                }
            },
            {
                "id": "ppt_003",
                "title": "Climate Change Solutions",
                "author": "Dr. Emily Green",
                "created_at": "2024-03-10T09:45:00Z",
                "slides_count": 32,
                "status": "completed",
                "content": {
                    "summary": "Innovative approaches to combat climate change",
                    "key_topics": ["Renewable Energy", "Carbon Capture", "Policy Changes"],
                    "audience": "Environmental scientists and policymakers"
                }
            }
        ]
        
        self._mock_templates = [
            {
                "id": "template_001",
                "name": "Corporate Presentation",
                "description": "Professional corporate presentation template",
                "category": "business",
                "slides_included": ["title", "agenda", "content", "charts", "conclusion"]
            },
            {
                "id": "template_002",
                "name": "Academic Research",
                "description": "Template for academic research presentations",
                "category": "academic",
                "slides_included": ["title", "abstract", "methodology", "results", "references"]
            },
            {
                "id": "template_003",
                "name": "Startup Pitch",
                "description": "Template for startup pitch presentations",
                "category": "startup",
                "slides_included": ["problem", "solution", "market", "business_model", "team"]
            }
        ]
    
    def get_presentations(self) -> List[Dict[str, Any]]:
        """Get all presentations."""
        return self._mock_presentations.copy()
    
    def get_presentation_by_id(self, presentation_id: str) -> Dict[str, Any]:
        """Get a specific presentation by ID."""
        for presentation in self._mock_presentations:
            if presentation["id"] == presentation_id:
                return presentation.copy()
        raise ValueError(f"Presentation with ID {presentation_id} not found")
    
    def create_presentation(self, title: str, author: str, template_id: Optional[str] = None) -> Dict[str, Any]:
        """Create a new presentation."""
        presentation_id = f"ppt_{len(self._mock_presentations) + 1:03d}"
        new_presentation = {
            "id": presentation_id,
            "title": title,
            "author": author,
            "created_at": datetime.now().isoformat() + "Z",
            "slides_count": 0,
            "status": "draft",
            "template_id": template_id,
            "content": {
                "summary": f"New presentation: {title}",
                "key_topics": [],
                "audience": "General audience"
            }
        }
        self._mock_presentations.append(new_presentation)
        return new_presentation.copy()
    
    def get_templates(self) -> List[Dict[str, Any]]:
        """Get all available templates."""
        return self._mock_templates.copy()
    
    def get_template_by_id(self, template_id: str) -> Dict[str, Any]:
        """Get a specific template by ID."""
        for template in self._mock_templates:
            if template["id"] == template_id:
                return template.copy()
        raise ValueError(f"Template with ID {template_id} not found")
    
    def generate_slide_content(self, topic: str, slide_type: str = "content") -> Dict[str, Any]:
        """Generate mock slide content for a given topic."""
        mock_content = {
            "slide_type": slide_type,
            "topic": topic,
            "title": f"{topic.title()} Overview",
            "content": {
                "bullet_points": [
                    f"Key insight about {topic}",
                    f"Important aspect of {topic}",
                    f"Future implications of {topic}"
                ],
                "notes": f"Speaker notes for {topic} slide",
                "suggested_images": [
                    f"chart_related_to_{topic.lower().replace(' ', '_')}",
                    f"diagram_showing_{topic.lower().replace(' ', '_')}"
                ]
            },
            "generated_at": datetime.now().isoformat() + "Z"
        }
        return mock_content
    
    def get_presentation_stats(self) -> Dict[str, Any]:
        """Get statistics about presentations."""
        total_presentations = len(self._mock_presentations)
        completed_presentations = len([p for p in self._mock_presentations if p["status"] == "completed"])
        total_slides = sum(p["slides_count"] for p in self._mock_presentations)
        
        return {
            "total_presentations": total_presentations,
            "completed_presentations": completed_presentations,
            "in_progress_presentations": total_presentations - completed_presentations,
            "total_slides": total_slides,
            "average_slides_per_presentation": total_slides / total_presentations if total_presentations > 0 else 0,
            "available_templates": len(self._mock_templates)
        }
