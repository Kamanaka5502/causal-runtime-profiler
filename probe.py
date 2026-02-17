import json
import time

class Probe:
    def __init__(self, filepath="events.jsonl"):
        self.file = open(filepath, "w")
        self.eid = 0

    def event(self, actor, event_type, resources, outcome="pending", parent_id=None):
        self.eid += 1
        event = {
            "eid": self.eid,
            "pid": parent_id,
            "actor": actor,
            "type": event_type,
            "resources": resources,
            "outcome": outcome,
            "ts": time.monotonic_ns()
        }
        self.file.write(json.dumps(event) + "\n")
        self.file.flush()
        return self.eid

    def close(self):
        self.file.close()

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.close()


def attempt(probe, actor, resources):
    return probe.event(actor, "attempt", resources, "pending")

def wait(probe, actor, resources, parent_id):
    return probe.event(actor, "wait", resources, "blocking", parent_id)

def abort(probe, actor, resources, parent_id, reason="timeout"):
    return probe.event(actor, "abort", resources, reason, parent_id)

def commit(probe, actor, resources, parent_id):
    return probe.event(actor, "commit", resources, "success", parent_id)
