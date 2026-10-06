---
layout: page
title: ML Systems
description: A measured CUDA GEMM comparison, CPU/GPU exercises, and clearly labeled future inference and attention studies.
importance: 10
category: Open-source tools
github: https://github.com/zesun33/personal-projects
published: true
_styles: |
  article table { width: 100%; table-layout: fixed; }
  article th, article td { overflow-wrap: anywhere; }
---

## Choose by what you want to learn

| Project                                                                    | What exists                             | First useful task                                                         |
| -------------------------------------------------------------------------- | --------------------------------------- | ------------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| [CUDA GEMM]({{ '/projects/cuda-gemm-optimization/'                         | relative_url }})                        | Implemented comparison and recorded measurements                          | Run the checked naive/tiled/cuBLAS comparison or inspect recorded data |
| [Kernel Forge]({{ '/projects/kernel-forge/'                                | relative_url }})                        | CUDA generation/profiling CLI                                             | Generate a vector-add template and inspect checked timings             |
| [CUDA memory exercise](https://github.com/zesun33/cuda-memory-benchmark)   | Notes and incomplete bandwidth exercise | Complete and check the copy/timing TODOs                                  |
| [OpenMP lab](https://github.com/zesun33/parallel-computing-lab)            | CPU parallelism exercises               | Complete a parallel loop and compare correct results across thread counts |
| [TensorRT study](https://github.com/zesun33/resnet-tensorrt-bench)         | Roadmap only                            | Define export, preprocessing, accuracy, and baseline measurement          |
| [Triton attention](https://github.com/zesun33/triton-flash-attention-lite) | Roadmap only                            | Define reference attention and correctness before implementing a kernel   |

## Learn through a concrete attempt

The [tutorial project]({{ '/projects/hw-ml-tutorials/' | relative_url }}) walks through shapes, commands, correctness checks, and result interpretation. Hardware and shape affect performance; target speedups are not measured results. The [complete directory]({{ '/repositories/' | relative_url }}#ml-systems) gives each project's current scope.
