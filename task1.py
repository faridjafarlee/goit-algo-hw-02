from queue import Queue
from dataclasses import dataclass
from datetime import datetime
import itertools
import random
import time


@dataclass(frozen=True)
class Request:
    id: int
    created_at: str
    payload: str


request_queue = Queue()
_id_gen = itertools.count(1)


def generate_request() -> Request:
    req = Request(
        id=next(_id_gen),
        created_at=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        payload=random.choice(["Repair", "Consultation", "Warranty", "Diagnostics"])
    )
    request_queue.put(req)
    print(f"New request added: {req}")
    return req


def process_request() -> None:
    if not request_queue.empty():
        req: Request = request_queue.get()
        print(f"Processing request: {req}")
        # імітація “обробки”
        time.sleep(0.3)
        print(f"Done: request #{req.id}")
    else:
        print("Queue is empty. Nothing to process.")


def main() -> None:
    print("Queue Simulator")
    print("Press Ctrl+C to quit")

    try:
        while True:
            generate_request()
            time.sleep(0.3)  
            process_request()
            time.sleep(1)  
    except KeyboardInterrupt:
        print("\nBye.")


if __name__ == "__main__":
    main()
