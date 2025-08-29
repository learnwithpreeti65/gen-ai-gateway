"""Services for the Gen AI Gateway."""

from typing import Dict, List, Any, Optional
from ppt_wrapper import PPTWrapper


class AIGatewayService:
    """Service class for AI Gateway operations."""
    
    def __init__(self):
        """Initialize the AI Gateway service."""
        self.ppt_wrapper = PPTWrapper()
    
    def get_all_presentations(self) -> List[Dict[str, Any]]:
        """Get all presentations."""
        return self.ppt_wrapper.get_presentations()
    
    def get_presentation_by_id(self, presentation_id: str) -> Dict[str, Any]:
        """Get a specific presentation by ID."""
        return self.ppt_wrapper.get_presentation_by_id(presentation_id)
    
    def create_presentation(self, title: str, author: str, template_id: Optional[str] = None) -> Dict[str, Any]:
        """Create a new presentation."""
        return self.ppt_wrapper.create_presentation(title, author, template_id)
    
    def generate_slide_content(self, topic: str, slide_type: str = "content") -> Dict[str, Any]:
        """Generate slide content for a given topic."""
        return self.ppt_wrapper.generate_slide_content(topic, slide_type)
    
    def get_templates(self) -> List[Dict[str, Any]]:
        """Get all available templates."""
        return self.ppt_wrapper.get_templates()
    
    def get_template_by_id(self, template_id: str) -> Dict[str, Any]:
        """Get a specific template by ID."""
        return self.ppt_wrapper.get_template_by_id(template_id)
    
    def get_presentation_stats(self) -> Dict[str, Any]:
        """Get presentation statistics."""
        return self.ppt_wrapper.get_presentation_stats()
