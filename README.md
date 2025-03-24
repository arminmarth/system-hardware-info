# System Hardware Info

A Python application that displays real-time system hardware information using a PyQt GUI.

## Features

- **CPU Information**: Shows CPU cores, frequency, and usage percentage
- **Memory Information**: Displays total, used, and available memory with usage percentage
- **Disk Information**: Lists all disk partitions with storage details
- **Auto-refresh**: Updates information every 2 seconds
- **Manual refresh**: Button to manually refresh all information
- **Modern UI**: Clean interface with organized sections

## Screenshots

![System Hardware Info Screenshot](screenshots/app_screenshot.png)

## Dependencies

- Python 3.11+
- PyQt5 5.15.9+
- psutil 5.9.5+

## Installation

### Standard Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/arminmarth/system-hardware-info.git
   cd system-hardware-info
   ```

2. Create and activate a virtual environment (recommended):
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:
   ```bash
   python main.py
   ```

### Using Docker

1. Build the Docker image:
   ```bash
   docker build -t system-hardware-info .
   ```

2. Run the Docker container:
   ```bash
   docker run --rm -it -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix system-hardware-info
   ```
   Note: Running GUI applications in Docker requires X11 forwarding to be properly set up on your host system.

## Usage

The application displays system information in three main sections:

1. **CPU Information**:
   - Number of physical and logical cores
   - Current CPU frequency
   - Current CPU usage percentage

2. **Memory Information**:
   - Total system memory
   - Used memory
   - Available memory
   - Memory usage percentage

3. **Disk Information**:
   - List of all mounted partitions
   - Total, used, and free space for each partition
   - Usage percentage for each partition

Information is automatically refreshed every 2 seconds, or you can click the "Refresh Information" button to update manually.

## Project Structure

- `main.py` - Application entry point
- `src/` - Source code directory
  - `ui/` - User interface components
  - `collectors/` - System information collectors
  - `utils/` - Utility functions and configuration
- `tests/` - Unit tests
- `requirements.txt` - Python dependencies
- `Dockerfile` - Docker configuration for containerized deployment

## Troubleshooting

### Common Issues

1. **PyQt5 Installation Errors**:
   - On Linux, you may need to install additional packages: `sudo apt-get install python3-pyqt5`
   - On Windows, try using a pre-built wheel: `pip install PyQt5==5.15.9`

2. **Permission Errors for Disk Information**:
   - Some disk partitions may not be accessible due to permission restrictions
   - Run the application with elevated privileges if needed

3. **Display Issues in Docker**:
   - Ensure X11 forwarding is properly configured
   - Try setting the DISPLAY environment variable correctly

## Development

### Running Tests

```bash
pytest
```

For test coverage report:

```bash
pytest --cov=src
```

### Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is open source and available under the [MIT License](LICENSE).
