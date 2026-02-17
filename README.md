# Causal Runtime Profiler

A minimal deterministic runtime probe that reconstructs structured blocking windows and forward-progress loss from raw event streams.

This is not a latency tool.
It measures causal stall.

## What It Demonstrates

In multi-agent systems, most observability tools show:
- latency
- error rates
- throughput

They do NOT reconstruct:
- blocking windows
- wait duration
- forward-progress gaps

This demo shows how to measure that.

## Quick Start

git clone https://github.com/Kamanaka5502/causal-runtime-profiler.git
cd causal-runtime-profiler
python example_instrumentation.py

No dependencies required.

## Example Output

============================================================
ELYRIA SCOPE — BLOCKING ANALYSIS
============================================================
Total runtime (ns): 5001809759
Total blocked time (ns): 5001375462
Blocked %: 99.99 %
============================================================

This means nearly all runtime was spent inside structured blocking windows.

No useful forward progress occurred during those intervals.

## Why It Matters

If 20 agents hit the same 1-second blocking window,
you do not get latency.
You get structured compute waste.

This profiler reconstructs that loss directly from event streams.
