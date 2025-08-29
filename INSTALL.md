# Gen AI Gateway - Installation and Quick Start Guide

## Project Overview

The Gen AI Gateway is a FastAPI-based service that provides AI-powered presentation generation capabilities with a PPT wrapper for handling presentation data.

## Project Structure

```
gen-ai-gateway/
├── gen_ai_gateway/          # Main application package
│   ├── apps/               # FastAPI applications
│   │   ├── __init__.py
│   │   └── main.py         # Main FastAPI app with GET/POST endpoints
│   ├── src/                # Source code modules
│   │   ├── __init__.py
│   │   ├── models.py       # Pydantic models
│   │   └── services.py     # Business logic services
│   ├── tests/              # Test files
│   │   ├── __init__.py
│   │   ├── conftest.py     # Test configuration
│   │   ├── test_main.py    # API endpoint tests
│   │   └── test_ppt_wrapper.py  # PPT wrapper tests
│   └── __init__.py
├── ppt_wrapper/            # PPT wrapper with mock data
│   └── __init__.py         # PPT wrapper class with mock data
├── pyproject.toml          # Modern Python project configuration
├── setup.cfg               # Setup configuration
├── tox.ini                 # Tox configuration for testing
├── requirements.txt        # Basic dependencies
├── Dockerfile              # Container configuration
├── docker-compose.yml      # Docker compose setup
├── Makefile               # Common development tasks
├── run.py                 # Simple script to run the app
├── .gitignore             # Git ignore file
└── README.md              # Project documentation
```

## Quick Start

### 1. Install Dependencies

```bash
# Install the package and dependencies
pip install -e .

# Or install from requirements.txt
pip install -r requirements.txt
```

### 2. Run the Application

**Option 1: Using the run script**
```bash
python run.py
```

**Option 2: Using uvicorn directly**
```bash
uvicorn gen_ai_gateway.apps.main:app --reload --host 0.0.0.0 --port 8000
```

**Option 3: Using tox**
```bash
tox -e dev
```

**Option 4: Using Make**
```bash
make run
```

### 3. Access the API

- **Application:** http://localhost:8000
- **API Documentation:** http://localhost:8000/docs
- **ReDoc Documentation:** http://localhost:8000/redoc

## API Endpoints

### GET Endpoints

1. **Health Check**
   - `GET /` - Returns application health status

2. **Get All Presentations**
   - `GET /presentations` - Returns list of all presentations

3. **Get Presentation by ID**
   - `GET /presentations/{presentation_id}` - Returns specific presentation

4. **Get Templates**
   - `GET /templates` - Returns available presentation templates

5. **Get Statistics**
   - `GET /stats` - Returns presentation statistics

### POST Endpoints

1. **Create Presentation**
   - `POST /presentations` - Creates a new presentation
   - Body: `{"title": "string", "author": "string", "template_id": "string"}`

2. **Generate Content**
   - `POST /generate` - Generates AI content for slides
   - Body: `{"topic": "string", "slide_type": "content"}`

## Development

### Install Development Dependencies
```bash
pip install -e .[dev]
```

### Run Tests
```bash
# Using pytest
pytest gen_ai_gateway/tests/ -v

# Using tox
tox

# Using make
make test
```

### Code Formatting
```bash
# Format code
make format

# Check formatting
make lint
```

### Type Checking
```bash
make mypy
```

## Docker Support

### Build and Run with Docker
```bash
# Build image
docker build -t gen-ai-gateway .

# Run container
docker run -p 8000:8000 gen-ai-gateway
```

### Using Docker Compose
```bash
docker-compose up --build
```

## Mock Data

The PPT wrapper includes mock data for:
- 3 sample presentations with various topics
- 3 presentation templates
- Generated slide content functionality
- Presentation statistics

## Example API Usage

### Create a New Presentation
```bash
curl -X POST "http://localhost:8000/presentations" \
     -H "Content-Type: application/json" \
     -d '{"title": "My New Presentation", "author": "John Doe", "template_id": "template_001"}'
```

### Generate Content
```bash
curl -X POST "http://localhost:8000/generate" \
     -H "Content-Type: application/json" \
     -d '{"topic": "Artificial Intelligence", "slide_type": "content"}'
```

### Get All Presentations
```bash
curl "http://localhost:8000/presentations"
```

## Configuration Files

- **pyproject.toml**: Modern Python packaging and tool configuration
- **setup.cfg**: Traditional setup configuration
- **tox.ini**: Testing automation across multiple Python versions
- **Makefile**: Common development commands

## Next Steps

1. Install the dependencies: `pip install -e .`
2. Run the application: `python run.py`
3. Visit http://localhost:8000/docs to explore the API
4. Start building your AI-powered presentation features!
