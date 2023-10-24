# Simple Python Port Scanner

This is a simple command-line port scanner implemented in Python. It allows you to scan a range of ports on a target host to check for open ports.

## Features

- Concurrent scanning of multiple ports using threads.
- Option to scan a specific range of ports or all available ports.
- Graceful handling of user interruptions (Ctrl+C).
- Sorting and displaying open ports.

## Usage

To use the port scanner, you can run the script with the following command:

```bash
python scanner.py -H <host> [options]
```
## Running with Docker
Build the Docker image:

```bash
docker build -t portscanner .
```

Run the Docker container with a mounted volume for the wordlist:

```bash
docker run -it --rm portscanner -H <host> [options]
```

## Options

- `-H`, `--host`: Specify the target IP address or hostname (required).
- `-s`, `--start`: Specify the start port (default is 1).
- `-e`, `--end`: Specify the end port (default is 1024).
- `-a`, `--all`: Scan all available ports (from 1 to 65535).

## Examples

Scan a specific range of ports:

```bash
python scanner.py -H 127.0.0.1 -s 80 -e 100
```
Scan all available ports:

```bash
python scanner.py -H 127.0.0.1 -a
```
Scan a specific range of ports using docker:
```bash
docker run -it --rm portscanner -H 127.0.0.1 -s 80 -e 100
```

## Implementation

The script uses the concurrent.futures module for multithreaded port scanning, and it handles KeyboardInterrupt (Ctrl+C) to ensure a graceful exit.