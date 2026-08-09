---
layout: page
title: TrilinearCIM - All-in-Memory Transformer Acceleration
description: DG-FeFET Compute-in-Memory architecture eliminating runtime NVM reprogramming for Transformer attention
importance: 1
category: Research
related_publications: true
published: true
---

## TrilinearCIM: Trilinear Compute-in-Memory Architecture for Energy-Efficient Transformer Acceleration

**arXiv preprint (2026)** &nbsp;—&nbsp; [arXiv:2604.07628](https://arxiv.org/abs/2604.07628)

This research project introduces **TrilinearCIM**, a Double-Gate FeFET (DG-FeFET)-based Compute-in-Memory (CIM) architecture that eliminates the core bottleneck of Transformer acceleration on CIM hardware: repeated runtime non-volatile memory (NVM) reprogramming of dynamic attention operands (Q, K, V).

### Research Motivation

Conventional FeFET CIM accelerators struggle with Transformer attention because the dynamic operands (queries, keys, values) generated at runtime must be repeatedly reprogrammed into the ferroelectric state. This reprogramming is energy-hungry, slow, and degrades device endurance, making in-memory acceleration of attention impractical. TrilinearCIM rethinks the dataflow so that the entire attention computation can stay inside NVM cores without any runtime reprogramming.

### Core Innovations

**DG-FeFET Three-Operand Primitive**: TrilinearCIM introduces a novel three-operand multiply-accumulate primitive ($Y = A \cdot B \cdot C$) enabled by Double-Gate FeFET back-gate modulation. Static projection weights are mapped to the non-volatile top gate, while dynamic token activations are applied through the volatile back gate.

**No Runtime NVM Reprogramming**: To our knowledge, this is the first architecture that performs the complete Transformer attention computation exclusively in NVM cores without runtime reprogramming of the ferroelectric state.

**Buffer Reduction**: By eliminating intermediate Q/K matrix storage, the design reduces global buffer capacity requirements by approximately **3×**.

**End-to-End In-Memory Attention**: The full attention dataflow—including the Q·K and (·)·V stages—is executed in-memory through DG-FeFET back-gate dynamics, rather than ping-ponging between NVM cores and digital logic.

### Results

Evaluations on **BERT-base (GLUE)** and **ViT-base (ImageNet, CIFAR-10/100)** show that TrilinearCIM:

- Outperforms conventional FeFET CIM on **7 of 9 GLUE tasks**.
- Achieves up to **46.6% energy reduction**.
- Delivers up to **20.4% latency improvement**.
- Incurs only **37.3% area overhead** relative to a baseline FeFET CIM accelerator.

### Research Team

**First Author**: Md Zesun Ahmed Mia

**Collaborators**:

- Jiahui Duan
- Kai Ni
- Abhronil Sengupta

**Institution**: Pennsylvania State University

### Publication

**Venue**: arXiv preprint (2026)

**Links**:

- [arXiv](https://arxiv.org/abs/2604.07628)
- [PDF](../assets/pdf/Trilinear_Compute_in_Memory_Architecture_for_Energy_Efficient_Transformer_Acceleration.pdf)

### Future Directions

TrilinearCIM opens several avenues for follow-up work:

- Extending the DG-FeFET trilinear primitive to other dynamic-operand workloads (e.g., state-space models, linear attention variants).
- Co-design of training-time quantization and DG-FeFET non-idealities for end-to-end accuracy on large language models.
- Integration with neuromorphic and astromorphic computing pipelines for fully in-memory long-context Transformers.
