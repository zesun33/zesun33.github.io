---
layout: page
title: Variation-Tolerant Ferroelectric Neural Computing
description: Device-circuit-algorithm co-design for variation-tolerant FeFET-based neuromorphic systems
importance: 2
category: Research
related_publications: saha2025toward
---

## Overview

This research addresses the **reliability challenges of ferroelectric field-effect transistors (FeFETs)** in neuromorphic computing, particularly the device-level non-idealities that emerge at scaled dimensions. These variations can significantly degrade the accuracy of **in-memory crossbar-based AI accelerators**.

## FeFET Device Characterization

We characterize hafnia-based FeFETs with the gate stack comprising:

- **Doped HfO₂** (8nm thick) as ferroelectric layer
- **SiO₂** (1nm thick) as native oxide interlayer
- Device sizes: **0.24µm × 0.24µm**, **0.5µm × 0.24µm**, and **1µm × 1µm**

### Conductance Modulation

Devices are programmed using a pulse scheme with:

- **Reset pulse**: -4V to ensure negative polarization
- **Programming pulse**: 2V to 4V with 20mV steps
- **Read voltage**: 1.2V at gate terminal

Larger devices show gradual conductance changes due to more domains, while scaled devices exhibit **stochastic, discrete, and non-linear** conductance changes.

## Key Non-Idealities

### Cycle-to-Cycle (C2C) Variations

Significant variations in programming profiles across 50 repeated measurements of individual devices, caused by stochastic nucleation processes dominating polarization switching dynamics.

### Device-to-Device (D2D) Variations

Deviations measured across 3 different devices of each dimension, with lower operating voltages significantly increasing conductance variations in scaled devices.

### Variation Severity

The ratio σ/µ (standard deviation to mean) increases significantly at lower programming voltages, especially in smaller devices with fewer ferroelectric domains.

## Variation-Aware Design Approach

We propose algorithmic techniques to combat variations leveraging recent advances in deep learning, including:

1. **Bayesian Neural Network (BNN) Formulation**: Treating synaptic weights as probability distributions
2. **Hardware-Algorithm Co-Design**: Mapping BNN framework onto FeFET crossbar arrays
3. **Self-Repair Mechanisms**: Drawing inspiration from glial cell self-repair in biological brains

## Impact

This work contributes to enabling **reliable, energy-efficient neuromorphic computing** by bridging device physics, circuit design, and algorithm development for variation-tolerant FeFET-based AI accelerators.

## Publication

This work was presented at the **IEEE 68th International Midwest Symposium on Circuits and Systems (MWSCAS) 2025** as a Special Session Paper.

[Read the paper](https://ieeexplore.ieee.org/document/11244385/)
