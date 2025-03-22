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

(Screenshots would be added here when available)

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

2. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   python system-hardware-info.py
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

## Development

### Project Structure

- `system-hardware-info.py` - Main application code
- `requirements.txt` - Python dependencies
- `Dockerfile` - Docker configuration for containerized deployment

### Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the [MIT License](LICENSE).
