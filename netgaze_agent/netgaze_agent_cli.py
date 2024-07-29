#!/usr/bin/env python
import argparse
import json
import logging

from netgaze_agent.stomp_client import StompClient


def main():
    parser = argparse.ArgumentParser(description="Start NetGaze Agent")
    parser.add_argument("operation", type=str, help="Operation to perform. [start]/[version]")

    args = parser.parse_args()

    operation = args.operation

    if operation == 'start':
        _start()
    elif operation == 'version':
        _version()
    else:
        print(f'Invalid operation - {operation}')


def _start():
    logging.info(f"Starting...")
    data = {
        "name": "Test Agent",
        "host": "1.2.3.4",
        "lastSeenAt": 1715114647900,
        "connections": [
            {
                "name": "Google",
                "description": "Connection to Google",
                "type": "HTTP",
                "host": "google.com",
                "port": 80,
                "active": True,
                "lastCheckedAt": 1715114647695
            }
        ]
    }
    url = 'localhost:8080/netgaze-agent-event-listener'
    client = StompClient(url, sockjs=False, wss=False)
    client.connect()
    client.send("/app/event-listener", json.dumps(data))


def _version():
    print("Version...")


if __name__ == "__main__":
    main()
