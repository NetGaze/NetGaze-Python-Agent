import json

from netgaze_agent.stomp_client import StompClient

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


def on_sub(msg):
    print("MESSAGE: " + msg)


url = 'localhost:8080/netgaze-agent-event-listener'

if __name__ == "__main__":
    client = StompClient(url, sockjs=False, wss=False)
    client.connect()
    # client.subscribe("/topic", on_sub)
    # time.sleep(2)
    client.send("/app/event-listener", json.dumps(data))
