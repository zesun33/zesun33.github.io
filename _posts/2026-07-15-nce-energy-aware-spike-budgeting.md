---
layout: post
title: "Energy-Aware Spike Budgeting for Continual Learning in SNNs: Our NCE 2026 Paper"
date: 2026-07-15 09:00:00-0400
description: A deep dive into our Neuromorphic Computing and Engineering paper on adaptive spike budgeting for continual learning in spiking neural networks for neuromorphic vision.
tags: research neuromorphic snn continual-learning mentorship nce
categories: research mentorship
related_posts: true
published: true
---

I am proud to share that our paper, **"Energy-aware spike budgeting for continual learning in spiking neural networks for neuromorphic vision"**, has been published in _Neuromorphic Computing and Engineering_ (IOP Publishing).

This work is especially meaningful to me as a **mentor**. The first authors are my former students at the University of Liberal Arts Bangladesh (ULAB)—**Anika Tabassum Meem** and **Muntasir Hossain Nadid**—whom I supervised while serving as Lecturer in the Department of Electrical and Electronic Engineering. I am the corresponding author on the paper, continuing that mentorship from my ULAB years into a full journal publication.

## The Problem: Continual Learning Under Spike Cost

Neuromorphic vision systems based on **spiking neural networks (SNNs)** promise event-driven, sparse computation for both frame-based and event-based cameras. Yet **catastrophic forgetting**—the abrupt loss of previously learned knowledge when new tasks arrive—remains a central barrier to deployment in continually changing environments.

Most continual learning methods were developed for conventional artificial neural networks. They rarely **jointly** optimize task accuracy and **activity-dependent spike cost**, and exploration on **event-based** datasets has been particularly limited. Fixed spike-rate penalties also struggle across modalities: a coefficient that sparsifies dense frame encodings can over-constrain sparse DVS streams, while one tuned for event data may not sufficiently regularize frame inputs as the replay distribution evolves.

## Our Approach: Adaptive Spike Budgeting

We propose an **energy-aware spike budgeting** framework for continual SNN learning that integrates:

1. **Experience replay** to mitigate forgetting across a task stream
2. **Learnable leaky integrate-and-fire (LIF) neuron parameters** so dynamics can adapt during training
3. An **adaptive spike-budget controller** that enforces dataset-specific spike-activity constraints

Rather than a static sparsity weight, the controller closes a feedback loop by comparing observed mini-batch activity with a target budget during replay. The same control law can tighten or relax the activity constraint as the task stream and input modality change.

## Modality-Dependent Duality

A central finding is an **operational duality** in SNN continual learning:

- On **frame-based** datasets (MNIST, CIFAR-10), spike budgeting acts as a **sparsity-inducing regularizer**, improving accuracy while reducing spike rates by up to **47%**.
- On **event-based** datasets (DVS-Gesture, N-MNIST, CIFAR-10-DVS), **controlled budget relaxation** enables accuracy gains up to **17.45** percentage points with minimal computational overhead.

Across **five benchmarks** spanning both modalities, the method improves the accuracy–spike-activity trade-off while keeping spike activity under explicit control—using an activity-driven synaptic-event proxy rather than a direct hardware-energy measurement.

## Why Mentorship Matters

Beyond the technical contributions, this project reflects what academic mentorship can unlock: undergraduate researchers at ULAB driving a full research stack—from problem formulation through experiments to a peer-reviewed journal paper. Supervising this work reinforced my commitment to open, collaborative science and to creating pathways for students into neuromorphic and ML research.

## Read the Paper

- [DOI (NCE)](https://doi.org/10.1088/2634-4386/ae8627)
- [arXiv:2602.12236](https://arxiv.org/abs/2602.12236)
- [PDF](/assets/pdf/Energy-aware_spike_budgeting_for_continual_learning_in_spiking_neural_networks_for_neuromorphic_vision.pdf)

**Authors:** Anika Tabassum Meem, Muntasir Hossain Nadid, Md Zesun Ahmed Mia
