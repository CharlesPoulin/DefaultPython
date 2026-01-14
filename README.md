# DefaultPython

[![CI](https://github.com/USERNAME/REPO/actions/workflows/ci.yml/badge.svg)](https://github.com/USERNAME/REPO/actions/workflows/ci.yml)
[![Python Version](https://img.shields.io/badge/python-3.13-blue.svg)](https://python.org)
[![Code Style: ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![Checked with mypy](http://www.mypy-lang.org/static/mypy_badge.svg)](http://mypy-lang.org/)

A Python project managed with [uv](https://docs.astral.sh/uv/).

## Quick Start with `uv`

`uv` is an extremely fast Python package manager and project manager.

### 1. Installation
If you don't have `uv` installed yet:
```bash
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### 2. Project Setup
Synchronize the virtual environment and install dependencies:
```bash
uv sync
```
*Note: This project also includes a `Makefile`, so you can just run `make install`.*

### 3. Adding Dependencies
Add a new package to your project:
```bash
uv add requests
```
To add a development dependency:
```bash
uv add --dev pytest
```

### 4. Running the Project
Run the main script:
```bash
uv run defaultpython
```
Or use the `Makefile`:
```bash
make run
```

### 5. Running Commands in the Venv
You can run any command within the context of your project's virtual environment:
```bash
uv run python --version
uv run ruff check .
```

### 6. Managing Python Versions
`uv` can automatically download and manage Python versions for you:
```bash
uv python install 3.12
```

### 7. Pre-commit Hooks
This project uses `pre-commit` to ensure code quality.
Install the hooks:
```bash
uv run pre-commit install
```
Run hooks manually:
```bash
uv run pre-commit run --all-files
```

### 8. Docker Support
Build the container:
```bash
docker build -t defaultpython .
```
Run the container:
```bash
docker run defaultpython
```

## Editor Support
- **VS Code**: Recommended settings and extensions are included in `.vscode/`.
- **EditorConfig**: Standard coding styles are defined in `.editorconfig`.

## Task Runner

This project uses [Task](https://taskfile.dev/) for cross-platform task running (works on Windows, Mac, and Linux).

### Install Task
```bash
# Windows (with winget)
winget install Task.Task

# Mac
brew install go-task

# Linux
sh -c "$(curl --location https://taskfile.dev/install.sh)" -- -d -b ~/.local/bin
```

### Available Tasks
```bash
task              # Show all available tasks
task install      # Sync dependencies
task run          # Run the CLI application
task run-api      # Run the FastAPI app with hot reload
task test         # Run tests with coverage
task lint         # Run ruff linting
task lint-fix     # Auto-fix linting issues
task format       # Format code with ruff
task type-check   # Run mypy type checks
task security     # Run bandit security checks
task check        # Run ALL checks (lint, format, type-check, security, test)
task release      # Bump version and generate changelog
task clean        # Remove caches and build artifacts
task docker-build # Build Docker image
task docker-run   # Run Docker container
```

> **Note**: A `Makefile` is also included for environments where Task isn't available.

## Automatic Releases
When you merge to `main`, the `Release` workflow matches your commit messages (e.g., `feat: new thing`, `fix: bug`) and automatically:
1. Bumps the version.
2. Updates `CHANGELOG.md`.
3. Creates a GitHub Release.
