---
layout: page
title: "Kernel Forge: generate, check, and profile"
description: "Create CUDA templates, select a visible GPU, and separate measured timings from modeled Roofline limits."
importance: 4
category: Open-source tools
portfolio_id: kernel-forge
published: true
---

## The problem

A kernel experiment needs a reproducible starting implementation, correct GPU selection, a numerical check, and an interpretable timing result. A theoretical ceiling alone cannot tell you how fast a kernel ran.

## What I built

I built a Python CLI for device discovery, CUDA template generation, checked benchmarking, and Roofline analysis. Device selection follows CUDA-visible ordinals so local masks and multi-GPU hosts can be handled explicitly.

{% include portfolio_project.liquid %}

## A first useful result

Generate vector addition and inspect its measured latency and modeled arithmetic intensity. Then compare naive and tiled matrix templates at the same shape. The tutorial saves doctor output and JSON results before drawing a conclusion.

## Evidence and limits

Portable tests cover device selection and CLI behavior; GPU checks require actual CUDA execution. Roofline ceilings use reference/fallback specifications and modeled traffic, not measured DRAM counters. Current templates are CUDA; this page does not imply an implemented Triton path.
