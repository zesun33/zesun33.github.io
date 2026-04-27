---
layout: post
title: TrilinearCIM Preprint Released on arXiv!
date: 2026-04-20 09:00:00-0400
inline: false
related_posts: false
published: true
---

📄 Excited to share our latest preprint **"Trilinear Compute-in-Memory Architecture for Energy-Efficient Transformer Acceleration"** is now available on arXiv!

We propose **TrilinearCIM**, a Double-Gate FeFET (DG-FeFET) Compute-in-Memory architecture that performs the full Transformer attention dataflow entirely in-memory—without any runtime NVM reprogramming of the dynamic Q, K, V operands. A novel three-operand multiply-accumulate primitive ($Y = A \cdot B \cdot C$) maps static projection weights to the non-volatile top gate while applying dynamic token activations through the volatile back gate.

On BERT-base (GLUE) and ViT-base (ImageNet, CIFAR-10/100), TrilinearCIM delivers up to **46.6% energy reduction** and **20.4% latency improvement** over conventional FeFET CIM, while reducing global buffer capacity by ~3×.

**Authors**: Md Zesun Ahmed Mia, Jiahui Duan, Kai Ni, Abhronil Sengupta

🔗 [arXiv:2604.07628](https://arxiv.org/abs/2604.07628)
