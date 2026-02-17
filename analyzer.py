import json
import sys

def analyze(filepath):
    events = []
    with open(filepath, "r") as f:
        for line in f:
            events.append(json.loads(line))

    if not events:
        print("No events found.")
        return

    start = events[0]["ts"]
    end = events[-1]["ts"]
    total_runtime = end - start

    blocked_time = 0
    active_waits = {}

    for e in events:
        if e["type"] == "wait":
            active_waits[e["pid"]] = e["ts"]

        if e["type"] == "abort" and e["pid"] in active_waits:
            wait_start = active_waits.pop(e["pid"])
            blocked_time += (e["ts"] - wait_start)

    blocked_percent = (blocked_time / total_runtime) * 100 if total_runtime else 0

    print("=" * 60)
    print("ELYRIA SCOPE — BLOCKING ANALYSIS")
    print("=" * 60)
    print(f"Total runtime (ns): {total_runtime}")
    print(f"Total blocked time (ns): {blocked_time}")
    print(f"Blocked %: {blocked_percent:.2f} %")
    print("=" * 60)

if __name__ == "__main__":
    analyze(sys.argv[1])
