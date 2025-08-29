# Gen AI Gateway

A FastAPI-based Gen AI Gateway service with PPT wrapper functionality.

## Project Structure

```
gen-ai-gateway/
├── gen_ai_gateway/
│   ├── apps/           # FastAPI application
│   ├── src/            # Source code
│   └── tests/          # Test files
├── ppt_wrapper/        # PPT wrapper functionality
├── pyproject.toml      # Project configuration
├── setup.cfg           # Setup configuration
├── tox.ini            # Tox configuration
└── README.md          # This file
```

## Installation

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -e .
   ```

## Development

Install development dependencies:
```bash
pip install -e .[dev]
```

## Running the Application

### Using uvicorn directly:
```bash
uvicorn gen_ai_gateway.apps.main:app --reload --host 0.0.0.0 --port 8000
```

### Using tox:
```bash
tox -e dev
```

## Testing

Run tests using pytest:
```bash
pytest
```

Or using tox:
```bash
tox
```

## Code Formatting

Format code using black and isort:
```bash
tox -e format
```

Check code formatting:
```bash
tox -e lint
```

## Type Checking

Run mypy for type checking:
```bash
tox -e mypy
```

## API Endpoints

- `GET /`: Health check endpoint
- `POST /generate`: Generate AI content
- `GET /docs`: OpenAPI documentation
- `GET /redoc`: ReDoc documentation
