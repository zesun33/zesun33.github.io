---
layout: page
title: Hardware and ML tutorials
description: Eight consecutive lessons with commands, runnable examples, deliberate failures, expected results, and troubleshooting.
importance: 0
category: Open-source tools
portfolio_id: hw-ml-tutorials
published: true
---

## Learn by producing a result

This separate tutorial project connects the tools through small engineering attempts. Each lesson explains the problem, prerequisites, commands, expected output, and limits. Begin with a self-checking hardware example; move to GPU experiments or reference-model behavior when those match your goals.

{% include portfolio_project.liquid %}

## Choose a lesson

| Lesson                                                                                                      | Practical outcome                                                | Hardware requirements                          |
| ----------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------- |
| [1. First simulation](https://github.com/zesun33/hw-ml-tutorials/blob/main/lessons/01-first-simulation.md)  | Generate and verify a counter; deliberately break and restore it | Podman and the Verilog image                   |
| [2. Sensor-event counter](https://github.com/zesun33/hw-ml-tutorials/blob/main/lessons/02-event-counter.md) | Check idle, event, reset, and wrap behavior                      | Podman or Docker                               |
| [3. MCP workflow](https://github.com/zesun33/hw-ml-tutorials/blob/main/lessons/03-mcp-workflow.md)          | Collect review, simulation, and synthesis JSON reports           | Verilog and ASIC images; no LLM account        |
| [4. GitHub hardware CI](https://github.com/zesun33/hw-ml-tutorials/blob/main/lessons/04-hardware-ci.md)     | Catch functional regressions on source changes                   | GitHub Actions                                 |
| [5. GEMM comparison](https://github.com/zesun33/hw-ml-tutorials/blob/main/lessons/05-gemm.md)               | Check and compare four FP32 implementations                      | CUDA; recorded-data plotting needs only Python |
| [6. Kernel generation](https://github.com/zesun33/hw-ml-tutorials/blob/main/lessons/06-kernel-forge.md)     | Generate templates and interpret measured/model reports          | CUDA for execution                             |
| [7. Spiking-tile reference](https://github.com/zesun33/hw-ml-tutorials/blob/main/lessons/07-lif-model.md)   | Trace threshold, pipeline, and refractory behavior               | Python only for the model example              |
| [8. Next experiments](https://github.com/zesun33/hw-ml-tutorials/blob/main/lessons/08-next-experiments.md)  | Turn an exercise or architecture into a checked first milestone  | Depends on the chosen task                     |

## Evidence and contribution

The repository contains runnable positive and negative hardware fixtures and a real MCP SDK client. GPU lessons require an actual GPU for fresh timings. Model traces and recorded-data plots offer accessible routes with narrower claims. Read the validation record before reusing a result, then use the lesson template to contribute another example.
