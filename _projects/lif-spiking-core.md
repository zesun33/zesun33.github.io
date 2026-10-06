---
layout: page
title: "LIF spiking core: from neuron to mesh"
description: "Study event-driven neuron tiles and routing with reference models, simulation tests, and coverage notes."
importance: 3
category: Open-source tools
portfolio_id: lif-spiking-core
published: true
---

## The problem

A neuromorphic hardware design combines fixed-point neuron dynamics, synaptic configuration, pipeline timing, and spike routing. Checking only a neuron equation leaves interface and scheduling behavior untested.

## What I built

I built neuron and tile RTL, a five-port AER router, and an integrated 2×2 mesh, with Python reference models and simulation testbenches. The repository preserves open-tool implementation artifacts and their evidence limits.

{% include portfolio_project.liquid %}

## A first useful result

The tutorial programs one synapse and traces input pipelining, threshold crossing, subtractive reset, and refractory suppression in Python. It then points to the RTL comparison testbench. The model trace is an accessible first step without a simulator.

## Evidence and limits

[Verification notes](https://github.com/zesun33/lif-spiking-core/blob/main/VERIFICATION.md) distinguish recorded passes from partial functional coverage. A model trace establishes software behavior; hardware changes need fresh RTL tests. Open-tool artifacts do not establish fabricated silicon, complete timing signoff, or calibrated physical-device behavior.
