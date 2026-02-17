import time
import subprocess
from probe import Probe, attempt, wait, abort

def run_demo():
    with Probe("events.jsonl") as probe:
        for _ in range(5):
            eid = attempt(probe, "agent_blocking", ["R_database"])
            wait(probe, "agent_blocking", ["R_database"], eid)
            time.sleep(1)  # Simulated blocking window
            abort(probe, "agent_blocking", ["R_database"], eid, "timeout")

if __name__ == "__main__":
    run_demo()
    subprocess.run(["python", "analyzer.py", "events.jsonl"])
