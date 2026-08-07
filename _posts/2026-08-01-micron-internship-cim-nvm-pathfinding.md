---
layout: post
title: "Wrapping Up My Micron Internship: CIM-NVM Pathfinding for LLM Inference"
date: 2026-08-01 09:00:00-0400
description: Reflections on my experience as a Machine Learning Engineer Intern at Micron Technology, analyzing NVM-based Compute-in-Memory architectures for LLM inference acceleration.
tags: internship micron CIM NVM LLM machine-learning pathfinding
categories: research career
related_posts: true
published: true
---

After three intensive months as a **Machine Learning Engineer Intern at Micron Technology**, I am reflecting on an experience that brought my academic work in memory-centric ML acceleration into industry pathfinding for next-generation AI accelerators.

## Pathfinding at the Memory–Compute Boundary

I joined Micron’s **Pathfinding and Strategy Group** in **Richardson, TX** (05/2026–07/2026), mentored by **Dave Roberts**. The central question was practical and urgent: as LLM serving scales, the **memory bandwidth and energy cost** of conventional digital accelerators become dominant bottlenecks. Can **Non-Volatile Memory (NVM)-based Compute-in-Memory (CIM)** architectures meaningfully accelerate inference by reducing data movement—and under what workload and precision assumptions?

This internship sat at the intersection of device-aware modeling and hyperscale serving analysis—exactly the space my PhD research targets with architectures such as **TrilinearCIM**.

## CIM-NVM Architecture Analysis

A core thread of the internship was **technology-agnostic modeling of NVM device characteristics** for memory-centric ML inference. Rather than tying conclusions to a single memory technology, we evaluated how NVM-based CIM could translate into **energy, latency, and area** trade-offs relative to digital accelerators at the pathfinding stage.

Working across **LLMs** (LLama-3, Gemma-3, Gemma-4) and **CNNs** forced the analysis to stay workload-aware: stationary weights, dynamic activations, and serving phases do not stress memory and compute the same way.

## LLM Serving: Prefill–Decode and Attention–FFN Disaggregation

Hyperscale LLM inference is not a single kernel. I characterized serving performance under **Prefill–Decode (PD)** and **Attention–FFN (AFD)** disaggregation schemes, quantifying **TPOT** and **TTFT** trade-offs that matter for deployment decisions.

This work sharpened how I think about accelerator design: architectural wins must map onto **serving phases and disaggregation strategies**, not only peak TOPS on a microbenchmark.

## Quantization and Analog Error Mitigation

CIM paths introduce precision and noise constraints that digital GPU/TPU stacks hide behind mature software stacks. I investigated how **quantization error** (including INT8/INT4/FP8 and mixed-precision regimes discussed in our public project materials) propagates through CIM compute, and studied **CIM analog error mitigation**—including noise-aware and retraining-aware approaches—to preserve model accuracy under analog compute noise and limited ADC precision.

These themes connect directly to hardware-aware training and co-design principles I use in academic CIM research.

## Connecting Back to Penn State Research

The Micron internship complemented my PhD agenda in concrete ways:

- **Memory-centric acceleration**: Reinforced why Transformer attention and dynamic operands stress conventional CIM assumptions—motivation behind **TrilinearCIM**’s reprogramming-free attention dataflow
- **Serving-aware evaluation**: Encouraged evaluating accelerators with TPOT/TTFT and disaggregation in mind, not only offline accuracy
- **Error-aware design**: Strengthened the link between quantization, analog non-idealities, and end-to-end model quality

## Looking Forward

As I return fully to my PhD research, I carry a clearer view of how industry pathfinding frames CIM-NVM opportunities for LLM inference—and how academic architectures must speak that language. I am grateful to Dave Roberts and the Pathfinding and Strategy team at Micron for the mentorship and collaboration that made this internship so valuable.

For a concise project summary, see my [Micron ML Accelerator Pathfinding](/projects/micron-ml-accelerator-pathfinding/) page.

---

_This internship was supported by Micron Technology’s intern program. Views expressed here are my own and based on publicly shared project descriptions; they do not disclose confidential Micron results or product roadmaps._
