---
layout: page
title: RMAAT - Bio-Inspired Transformers
description: Efficient long-context sequence processing using astrocyte-inspired memory and attention
importance: 1
category: work
related_publications: true
published: true
---

## RMAAT: Astrocyte-Inspired Memory Compression and Replay for Efficient Long-Context Transformers

**Accepted at ICLR 2026**

This research project introduces computational principles derived from astrocytes—glial cells critical for biological memory and synaptic modulation—to address the quadratic complexity bottleneck in Transformers.

### Research Motivation

Traditional transformer models face significant computational challenges when processing long sequences due to the quadratic scaling of attention mechanisms. This project addresses these limitations by incorporating biological principles of attention and memory processing.

### Core Innovations

🧠 **Segment-Based Recurrent Processing**: RMAAT processes input sequences in segments. Persistent **memory tokens** propagate contextual information across segments, maintaining a recurrent state.

🔄 **Astrocyte-Inspired Retention Factor (LTP)**: An adaptive compression mechanism governs memory tokens. A novel **retention factor**, derived from simulated astrocyte Long-Term Plasticity (LTP), decides what information to keep or discard.

⚡ **Linear-Complexity Attention (STP)**: Within each segment, attention is computed using an efficient, **linear-complexity mechanism** inspired by astrocyte Short-Term Plasticity (STP), avoiding the O(N^2) cost of standard attention.

📚 **Astrocytic Memory Replay Backpropagation (AMRB)**: A novel training algorithm designed for memory efficiency in recurrent networks.

### Results

Evaluations on the **Long Range Arena (LRA)** benchmark demonstrate RMAAT's:

- Competitive accuracy compared to standard Transformers.
- Substantial improvements in computational efficiency.
- Significant reduction in memory usage.

### Research Team

**Principal Investigator**: Md Zesun Ahmed Mia

**Collaborators**:

- Malyaban Bal
- Abhronil Sengupta

**Institution**: Pennsylvania State University

### Publication

**Conference**: International Conference on Learning Representations (ICLR) 2026

**Links**:

- [OpenReview](https://openreview.net/forum?id=sTkJdbVxsI)
- [arXiv](https://arxiv.org/abs/2601.00426)
- [PDF](../assets/pdf/RMAAT__Astrocyte_Inspired_Memory_Compression_and_Replay_for_Efficient_Long_Context_Transformers__ICLR_2026_.pdf)

### Future Directions

This research opens new avenues for:

- Further bio-inspired AI architectures
- Enhanced efficiency in large language models
- Applications in real-time sequence processing
- Integration with neuromorphic computing systems

The work contributes to the broader goal of developing more efficient and biologically plausible artificial intelligence systems.
