# RaspberryPi4 RFID Registration System

## Overview
This project provides a simple RFID registration system designed for the Raspberry Pi 4. It uses an RFID reader to scan tags and register/identify users. The core functionality is implemented in `read.py`, which handles tag reading and corresponding logic.

## Features
- Reads RFID tags using a connected RFID reader.
- Registers and identifies users based on the tag information.
- Designed for Raspberry Pi 4 for ease of deployment and use.

## Requirements
- Raspberry Pi 4
- RFID Reader hardware
- Python 3.x
- Additional Python libraries (see [Installation](#installation) for details)

## Installation

1. **Clone the Repository**
    ```bash
    git clone https://github.com/yourusername/RaspberryPi4-RFID-RegistrationSys.git
    cd RaspberryPi4-RFID-RegistrationSys
    ```

2. **Install Dependencies**
    It is recommended to use a virtual environment:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # For Unix-like systems
    # or
    venv\Scripts\activate  # For Windows

    pip install -r requirements.txt
    ```

3. **Hardware Setup**
    - Connect the RFID reader according to its manufacturer's instructions.
    - Ensure the Raspberry Pi GPIO pins match the setup in `read.py`.

## Usage

Run the script to start reading RFID tags:
```bash
python read.py
```
Upon running, the system will wait for RFID tag scans. When a tag is detected, the system processes and registers the information.

## Customization
- **Modification of Behavior:** Feel free to modify the `read.py` script to adapt the registration process as needed.
- **Database Integration:** To store registration data persistently, integrate the script with a database of your choice.

## Contributing
Pull requests and improvements are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
