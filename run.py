#!/usr/bin/env python3
"""
Simple script to run the Gen AI Gateway application.
"""

import sys
import subprocess
from pathlib import Path


def main():
    """Main function to run the application."""
    project_root = Path(__file__).parent
    
    print("🚀 Starting Gen AI Gateway...")
    print(f"📁 Project root: {project_root}")
    print("🌐 Server will be available at: http://localhost:8000")
    print("📚 API docs will be available at: http://localhost:8000/docs")
    print("📖 ReDoc will be available at: http://localhost:8000/redoc")
    print("\n" + "="*50 + "\n")
    
    try:
        # Run the uvicorn server
        subprocess.run([
            sys.executable, "-m", "uvicorn",
            "gen_ai_gateway.apps.main:app",
            "--reload",
            "--host", "0.0.0.0",
            "--port", "8000"
        ], cwd=project_root, check=True)
    except KeyboardInterrupt:
        print("\n\n👋 Shutting down Gen AI Gateway...")
    except subprocess.CalledProcessError as e:
        print(f"\n❌ Error starting the application: {e}")
        print("\n💡 Make sure you have installed the dependencies:")
        print("   pip install -e .")
        print("   or")
        print("   pip install -r requirements.txt")
        sys.exit(1)


if __name__ == "__main__":
    main()
