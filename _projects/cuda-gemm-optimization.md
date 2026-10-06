---
layout: page
title: "CUDA GEMM: measure before optimizing"
description: "Compare naive, shared-memory tiled, and cuBLAS FP32 multiplication with explicit correctness checks."
importance: 2
category: Open-source tools
portfolio_id: cuda-gemm-optimization
published: true
---

## The problem

GPU matrix multiplication combines arithmetic, memory reuse, launch overhead, and numerical choices. A faster-looking result is useful only when it computes the intended answer under comparable conditions.

## What I built

I implemented naive, tiled-16, tiled-32, and cuBLAS FP32 comparisons on identical seeded inputs. A double-precision CPU reference checks the library result; every implementation is checked before recording timings.

{% include portfolio_project.liquid %}

## A first useful result

Try a non-tile-aligned `17 × 31 × 23` case, then square `128` and `256` cases. The tutorial offers both a fresh CUDA run and a route that regenerates recorded RTX A5000 plots without a GPU.

## Evidence and limits

[The recorded comparison](https://github.com/zesun33/cuda-gemm-optimization/blob/main/BENCHMARKS.md) specifies tolerances, warmup, samples, tool versions, and provenance. Timings exclude allocation and host transfers; cuBLAS uses FP32 pedantic math with TF32 disabled. Results depend on shape and hardware and are not an end-to-end speedup promise.

## A recorded comparison

<img class="img-fluid" src="{{ '/assets/img/portfolio/gemm-comparison.png' | relative_url }}" alt="FP32 GEMM throughput for four implementations at 128 and 256 square shapes">

Measured on an RTX A5000 on 2026-10-06, with TF32 disabled. Values use median CUDA-event kernel latency, excluding allocation and transfers. All implementations passed the recorded correctness checks. [Raw data and measurement metadata](https://github.com/zesun33/hw-ml-tutorials/tree/main/results/2026-10-06-rtx-a5000) accompany this chart; these small shapes illustrate why tiling does not guarantee a speedup.
