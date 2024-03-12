# Makefile
SHELL=/bin/sh

.SHELLFLAGS = -e -c
.ONESHELL:

# Virtual environment
VENV_NAME = env

.PHONY: activate
activate:
	source $(VENV_NAME)/bin/activate

deactivate:
	@echo "Deactivating virtual environment..."
	@$(shell . deactivate 2>/dev/null || true)