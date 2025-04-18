.ONESHELL:

VENV = .venv
ROOT_DIR := $(shell poetry env info --path)

# Determine OS and set paths accordingly
ifeq ($(OS),Windows_NT)
    PYTHON = $(VENV)/Scripts/python
    PIP = $(VENV)/Scripts/pip
    BIN = $(VENV)/Scripts
    ACTIVATE = $(VENV)/Scripts/activate
else
    PYTHON = $(VENV)/bin/python
    PIP = $(VENV)/bin/pip
    BIN = $(VENV)/bin
    ACTIVATE = $(VENV)/bin/activate
endif


# Default target
init: clean venv setup show-info activate

# Clean up files
clean:
	rm -rf $(VENV) cdk.out build dist **/*.egg-info .pytest_cache node_modules .coverage .ruff_cache

# Create .venv from the pyproject.toml file
venv:
	echo "Definining the poetry configs..."
	poetry config virtualenvs.in-project true

	echo "Installing the dependencies..."
	poetry install --quiet

# Download the necessary libs
setup:
	@echo "Virtual env path is: $(ROOT_DIR)"
	. $(ROOT_DIR)/bin/activate 

# Pre-commit setup
setup_precommit:
	@echo "Setting up the pre-commit config"
	pre-commit clean
	pre-commit install
	pre-commit autoupdate

# Show Python version and paths
show-info:
	@echo "OS: $(OS)"
	@echo "Python path: $(PYTHON)"
	@echo "Pip path: $(PIP)"
	@echo "Bin directory: $(BIN)"
	@echo "Activate script: $(ACTIVATE)"
	@$(PYTHON) --version

# Target to remind how to activate the virtual environment
activate:
	@echo "To activate the virtual environment, run:"
	@echo ""
	@echo "On Windows (CMD):"
	@echo "    $(ACTIVATE)"
	@echo ""
	@echo "On Windows (PowerShell):"
	@echo "    & $(ACTIVATE)"
	@echo ""
	@echo "On Unix-like systems (Linux, macOS):"
	@echo "    eval $(poetry env activate)"

# Mark targets as phony
.PHONY: init clean venv setup_dependencies setup_precommit show-info activate