VENV := venv
MODULE := outliers
PYTHON := $(VENV)/bin/python
PIP := $(VENV)/bin/pip
PYTEST := $(VENV)/bin/pytest

# create a virtual environment
# using "@" symbol to avoid the command being echoed
venv:
	@python -m venv $(VENV)

activate-venv:
	@. $(VENV)/bin/activate && export PATH=$(VENV)/bin:$$PATH

# install the outliers package to your local file
install:
	@$(PIP) install .

# run the outliers module
run:
	@$(PYTHON) -m $(MODULE)

# test the functions if it works properly
test:
	@$(PYTEST)

# declare the targets clean and test as phony targets.
.PHONY: venv install run test clean uninstall

# cleaning up temporary files and directories
clean:
	rm -rf .pytest_cache .coverage .pytest_cache coverage.xml __pycache__

# uninstall the package
uninstall:
	@$(PIP) uninstall outliers

# delete the virtual environment
venv-delete:
	rm -rf $(VENV)