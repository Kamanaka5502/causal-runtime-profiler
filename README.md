# Causal Runtime Profiler

A minimal deterministic runtime probe for reconstructing blocking windows and forward-progress gaps in multi-agent systems.

## Quick Start

git clone https://github.com/Kamanaka5502/causal-runtime-profiler.git
cd causal-runtime-profiler
python example_instrumentation.py

No dependencies required.

The demo generates an event stream and immediately runs the analyzer.

Example output:

Total runtime (ns): 5001809759
Total blocked time (ns): 5001375462
Blocked %: 99.99 %

This demonstrates structured blocking detection and forward-progress loss.
