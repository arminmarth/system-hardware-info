# System Hardware Info

A simple Python program that displays system hardware information using a PyQt GUI.

## Features

- Shows CPU usage, memory usage, and disk usage
- Uses the psutil library to retrieve hardware information

## Dependencies

- Python 3
- PyQt5
- psutil

## Build and Run

To build and run the program, follow these steps:

1. Install the dependencies using the following command:

      pip install PyQt5 psutil

2. Run the program using the following command:

      python3 system-hardware-info.py

This will launch the PyQt window that displays system hardware information. You can interact with the window to view different hardware details, and you can close the window by clicking the "x" button in the top-right corner.

### Using Docker

1. Build the Docker image using the following command:

      docker build -t system-hardware-info .

2. Run the Docker image using the following command:

      docker run --rm -it system-hardware-info

This will launch the PyQt window that displays system hardware information. You can interact with the window to view different hardware details, and you can close the window by clicking the "x" button in the top-right corner.
