---
layout: page
title: Neuromorphic Cybersecurity with Lifelong Learning
description: A bio-inspired SNN architecture for Network Intrusion Detection Systems (NIDS) capable of lifelong learning.
img: assets/img/publication_preview/cybersecurity.png
importance: 1
category: work
related_publications: mia2025neuromorphic
---

## Overview

This project presents a **Spiking Neural Network (SNN)** architecture for **lifelong Network Intrusion Detection Systems (NIDS)**, inspired by the brain's hierarchical processing and energy efficiency.

### Key Innovations

1.  **Hierarchical Architecture**:
    *   **Static SNN**: Efficiently identifies potential intrusions.
    *   **Dynamic SNN**: Adaptive classifier that learns specific attack types.

2.  **Bio-Plausible Learning**:
    *   Utilizes **Grow When Required (GWR)**-inspired structural plasticity.
    *   Implements a novel **Adaptive Spike-Timing-Dependent Plasticity (Ad-STDP)** learning rule.

3.  **Lifelong Learning Capabilities**:
    *   Enables the network to learn new threats incrementally.
    *   Preserves existing knowledge (mitigating catastrophic forgetting).
    *   Achieved **85.3% overall accuracy** on the UNSW-NB15 benchmark in a continual learning setting.

4.  **Hardware Efficiency**:
    *   Demonstrates high operational sparsity.
    *   Optimized for low-power deployment on neuromorphic hardware (validated using Intel Lava framework).

## Publication

This work was presented at the **International Conference on Neuromorphic Systems (ICONS) 2025**.
[Read the paper](https://arxiv.org/abs/2508.04610)
