# The name of the target (executable) file
TARGET = system-hardware-info

# The name of the main Python file
MAIN_FILE = system-hardware-info.py

# The Python interpreter to use
PYTHON = python3

# The PyQt5 module to use
PYQT = PyQt5

# The psutil module to use
PSUTIL = psutil

# The name of the file that contains the compiled Python code
COMPILED_FILE = $(TARGET).pyc

# The name of the file that contains the frozen executable
EXECUTABLE_FILE = $(TARGET)

# The commands to build the target
build: $(COMPILED_FILE)

# Compile the Python code
$(COMPILED_FILE): $(MAIN_FILE)
	$(PYTHON) -m $(PYQT) pyuic5 -o $(COMPILED_FILE) $(MAIN_FILE)

# Freeze the compiled code into an executable
$(EXECUTABLE_FILE): $(COMPILED_FILE)
	$(PYTHON) -m $(PYQT) pyinstaller -F $(COMPILED_FILE)

# Clean up the build files
clean:
	rm -f $(COMPILED_FILE) $(EXECUTABLE_FILE)
