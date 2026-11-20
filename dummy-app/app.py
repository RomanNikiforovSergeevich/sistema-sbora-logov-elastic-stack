import json
import random
import socket
import time
from datetime import datetime, timezone

LOGSTASH_HOST = "logstash"
LOGSTASH_PORT = 5000

levels = ["INFO", "WARN", "ERROR", "DEBUG"]
services = ["auth-service", "payment-service", "user-service", "notification-service"]

def generate_event():
    return {
        "@timestamp": datetime.now(timezone.utc).isoformat(),
        "level": random.choice(levels),
        "service": random.choice(services),
        "message": f"Random event #{random.randint(1000, 9999)}",
        "response_time_ms": random.randint(10, 500)
    }

def main():
    while True:
        event = generate_event()
        try:
            with socket.create_connection((LOGSTASH_HOST, LOGSTASH_PORT), timeout=5) as sock:
                sock.sendall((json.dumps(event) + "\n").encode("utf-8"))
            print(f"Sent: {event}", flush=True)
        except Exception as e:
            print(f"Failed to send: {e}", flush=True)
        time.sleep(2)

if __name__ == "__main__":
    main()
