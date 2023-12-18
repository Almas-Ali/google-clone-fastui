PYTHON = python3.11
REQUIREMENTS_FILE = requirements.txt
PROJECT_ROOT = .

.PHONY: help
help:
	@echo "Usage: make <target>"
	@echo "Targets:"
	@echo "  run              Run the project"
	@echo "  clean            Clean the project"
	@echo "  format           Format the project"
	@echo "  format-check     Check the project format"
	@echo "  install          Install the project dependencies"
	@echo "  test             Run the project tests"
	@echo "  help             Show this help message"
	@echo ""
	@echo "Author: Md. Almas Ali"
	@echo ""
	
.PHONY: run
run:
	$(PYTHON) main.py

.PHONY: clean
clean:
	rm -rf __pycache__ *.pyc .ruff_cache

.PHONY: format
format:
	$(PYTHON) -m ruff format $(PROJECT_ROOT)

.PHONY: format-check
format-check:
	$(PYTHON) -m ruff format --check $(PROJECT_ROOT)

.PHONY: install
install:
	sudo apt install -y $(PYTHON) $(PYTHON)-pip $(PYTHON)-venv $(PYTHON)-dev
	$(PYTHON) -m pip install -r $(REQUIREMENTS_FILE)

.PHONY: test
test:
	# Add your test command here
