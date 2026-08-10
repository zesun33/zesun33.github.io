---
layout: page
title: Micron ML Accelerator Pathfinding
description: Pre-silicon analysis of NVM-based Compute-in-Memory architectures for LLM inference acceleration at Micron Technology
importance: 2
category: Research
related_publications: false
published: true
---

## Micron ML Accelerator Pathfinding

**Industry Project** &nbsp;—&nbsp; Micron Technology, Pathfinding and Strategy Group, Richardson, TX (05/2026–07/2026)

This industry pathfinding project analyzes how **Non-Volatile Memory (NVM)-based Compute-in-Memory (CIM) architectures** can accelerate large language model (LLM) inference, with an emphasis on energy, latency, and throughput trade-offs relative to conventional digital accelerators.

### Project Overview

As LLM serving scales to hyperscale, the memory bandwidth and energy cost of conventional digital accelerators (GPU/TPU) become dominant bottlenecks. NVM-based CIM offers a path to in-memory compute that can substantially reduce data movement for inference workloads. This project models NVM device characteristics and quantifies how that reduction translates into TPOT, TTFT, energy, and latency benefits for state-of-the-art LLMs.

### Key Analyses

- **CIM-NVM Architecture Analysis**: Modeling NVM device characteristics (technology-agnostic across PCM, RRAM, MRAM, FeFET) to evaluate speedup and energy savings for memory-centric ML inference workloads.
- **LLM Serving Characterization**: Profiling state-of-the-art LLMs (LLama-3, Gemma-3, Gemma-4) under Prefill-Decode (PD) and Attention-FFN (AFD) disaggregation schemes; quantifying TPOT and TTFT trade-offs.
- **Quantization Error Analysis**: Quantifying how INT8/INT4/FP8/mixed-precision quantization error propagates through CIM compute paths; identifying safe operating ranges.
- **CIM Analog Error Mitigation**: Studying noise-aware and retraining-aware techniques to recover model accuracy under analog compute noise and limited ADC precision.

### Research Team

- **Lead**: Md Zesun Ahmed Mia (PhD Candidate, Penn State)
- **Host Group**: Pathfinding and Strategy, Micron Technology, Richardson, TX
- **Intern Manager / Mentor**: Dave Roberts (Micron)
