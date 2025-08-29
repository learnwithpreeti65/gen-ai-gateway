"""Tests for the PPT wrapper module."""

import pytest
from ppt_wrapper import PPTWrapper


def test_ppt_wrapper_initialization():
    """Test PPT wrapper initialization."""
    wrapper = PPTWrapper()
    assert wrapper is not None
    presentations = wrapper.get_presentations()
    assert len(presentations) == 3


def test_get_presentations():
    """Test getting all presentations."""
    wrapper = PPTWrapper()
    presentations = wrapper.get_presentations()
    assert len(presentations) == 3
    assert presentations[0]["id"] == "ppt_001"
    assert presentations[0]["title"] == "AI in Healthcare"


def test_get_presentation_by_id():
    """Test getting a presentation by ID."""
    wrapper = PPTWrapper()
    presentation = wrapper.get_presentation_by_id("ppt_001")
    assert presentation["id"] == "ppt_001"
    assert presentation["title"] == "AI in Healthcare"
    assert presentation["author"] == "Dr. Jane Smith"


def test_get_nonexistent_presentation():
    """Test getting a presentation that doesn't exist."""
    wrapper = PPTWrapper()
    with pytest.raises(ValueError, match="Presentation with ID nonexistent not found"):
        wrapper.get_presentation_by_id("nonexistent")


def test_create_presentation():
    """Test creating a new presentation."""
    wrapper = PPTWrapper()
    initial_count = len(wrapper.get_presentations())
    
    new_presentation = wrapper.create_presentation(
        title="New Test Presentation",
        author="Test Author",
        template_id="template_001"
    )
    
    assert new_presentation["title"] == "New Test Presentation"
    assert new_presentation["author"] == "Test Author"
    assert new_presentation["status"] == "draft"
    assert new_presentation["template_id"] == "template_001"
    
    # Check that the presentation was added
    updated_presentations = wrapper.get_presentations()
    assert len(updated_presentations) == initial_count + 1


def test_get_templates():
    """Test getting all templates."""
    wrapper = PPTWrapper()
    templates = wrapper.get_templates()
    assert len(templates) == 3
    assert templates[0]["id"] == "template_001"
    assert templates[0]["name"] == "Corporate Presentation"


def test_get_template_by_id():
    """Test getting a template by ID."""
    wrapper = PPTWrapper()
    template = wrapper.get_template_by_id("template_001")
    assert template["id"] == "template_001"
    assert template["name"] == "Corporate Presentation"
    assert template["category"] == "business"


def test_get_nonexistent_template():
    """Test getting a template that doesn't exist."""
    wrapper = PPTWrapper()
    with pytest.raises(ValueError, match="Template with ID nonexistent not found"):
        wrapper.get_template_by_id("nonexistent")


def test_generate_slide_content():
    """Test generating slide content."""
    wrapper = PPTWrapper()
    content = wrapper.generate_slide_content("Artificial Intelligence", "content")
    
    assert content["topic"] == "Artificial Intelligence"
    assert content["slide_type"] == "content"
    assert content["title"] == "Artificial Intelligence Overview"
    assert "bullet_points" in content["content"]
    assert "notes" in content["content"]
    assert "suggested_images" in content["content"]


def test_get_presentation_stats():
    """Test getting presentation statistics."""
    wrapper = PPTWrapper()
    stats = wrapper.get_presentation_stats()
    
    assert "total_presentations" in stats
    assert "completed_presentations" in stats
    assert "in_progress_presentations" in stats
    assert "total_slides" in stats
    assert "average_slides_per_presentation" in stats
    assert "available_templates" in stats
    
    assert stats["total_presentations"] == 3
    assert stats["available_templates"] == 3
