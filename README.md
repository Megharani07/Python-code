# Python-code

# System Information Fetcher

This Python script fetches various details about the system and prints them to the console. The script is designed to run in the Command Prompt on Windows 10/11 operating systems.

## Features

- **Installed Software**: Fetches a list of installed software on the system.
- **Internet Speed**: Measures the download and upload speeds in Mbps using the `speedtest` library.
- **Screen Resolution**: Retrieves the screen resolution using the `win32api` library.
- **CPU Information**: Gathers information about the CPU, including model, number of cores, and number of threads.
- **GPU Information**: Retrieves GPU information using the `wmi` library.
- **RAM Size**: Calculates the RAM size in gigabytes using the `psutil` library.
- **Screen Size**: Takes input for the user's screen size.
- **MAC Address**: Retrieves the Wi-Fi MAC address of the system.
- **Public IP Address**: Retrieves the public IP address of the system.
- **Windows Version**: Displays the Windows version using the `platform` library.

## Usage

1. Run the script in the Command Prompt:

    ```bash
    python system_info.py
    ```

2. Follow the prompts and input any required information.

## Prerequisites

Ensure you have the required Python libraries installed:

```bash
pip install speedtest-cli psutil pywin32


Note :
1.Some information may not be available on all systems.
2.Adjustments may be needed based on specific system configurations.
3.Ensure proper permissions to access certain system information.
