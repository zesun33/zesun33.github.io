---
layout: page
title: Neuromorphic Devices with Hydrogen Gradients
description: Self-sensitizable devices for enhanced synaptic plasticity
img: assets/img/2.jpg
importance: 2
category: work
related_publications: true
---

## Self-Sensitizable Neuromorphic Devices Based on Adaptive Hydrogen Gradient

This collaborative research project focuses on developing innovative neuromorphic devices that utilize adaptive hydrogen gradients to achieve enhanced synaptic plasticity and learning capabilities.

### Project Overview

The research demonstrates a breakthrough in neuromorphic computing by creating self-sensitizable devices that can adapt and learn through hydrogen gradient manipulation. This work represents a significant advancement in brain-inspired computing technologies.

### Key Features

🧠 **Synaptic Plasticity**: Enhanced learning capabilities mimicking biological neural networks

⚡ **Self-Sensitization**: Adaptive behavior without external programming

🔬 **Hydrogen Gradients**: Novel use of hydrogen dynamics for device operation

### Research Contributions

**Technical Innovation**: Development of adaptive hydrogen gradient technology for neuromorphic applications

**Material Science**: Advanced understanding of hydrogen behavior in neuromorphic devices

**Computing Applications**: New pathways for brain-inspired computing systems

### Collaborative Research

This project involved extensive collaboration with an international research team, bringing together expertise in:

- Materials Science and Engineering
- Neuromorphic Computing
- Hydrogen Dynamics
- Device Physics

### Research Team

**Principal Investigators**:

- Tao Zhang (Lead)
- Mingjie Hu
- **Md Zesun Ahmed Mia** (Contributing Researcher)
- Hao Zhang, Wei Mao, and others

**Institutions**: Multiple international research institutions

### Publication Impact

Published in **Matter** (Elsevier, 2024), Vol. 7, No. 5, pages 1799-1816, this work has garnered significant attention in the neuromorphic computing community.

### Future Directions

The research opens new avenues for:

- Advanced neuromorphic computing architectures
- Bio-inspired learning systems
- Energy-efficient computing solutions

Every project has a beautiful feature showcase page.
It's easy to include images in a flexible 3-column grid format.
Make your photos 1/3, 2/3, or full width.

To give your project a background in the portfolio page, just add the img tag to the front matter like so:

    ---
    layout: page
    title: project
    description: a project with a background image
    img: /assets/img/12.jpg
    ---

<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/1.jpg" title="example image" class="img-fluid rounded z-depth-1" %}
    </div>
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/3.jpg" title="example image" class="img-fluid rounded z-depth-1" %}
    </div>
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/5.jpg" title="example image" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    Caption photos easily. On the left, a road goes through a tunnel. Middle, leaves artistically fall in a hipster photoshoot. Right, in another hipster photoshoot, a lumberjack grasps a handful of pine needles.
</div>
<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/5.jpg" title="example image" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    This image can also have a caption. It's like magic.
</div>

You can also put regular text between your rows of images.
Say you wanted to write a little bit about your project before you posted the rest of the images.
You describe how you toiled, sweated, _bled_ for your project, and then... you reveal its glory in the next row of images.

<div class="row justify-content-sm-center">
    <div class="col-sm-8 mt-3 mt-md-0">
        {% include figure.liquid path="assets/img/6.jpg" title="example image" class="img-fluid rounded z-depth-1" %}
    </div>
    <div class="col-sm-4 mt-3 mt-md-0">
        {% include figure.liquid path="assets/img/11.jpg" title="example image" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    You can also have artistically styled 2/3 + 1/3 images, like these.
</div>

The code is simple.
Just wrap your images with `<div class="col-sm">` and place them inside `<div class="row">` (read more about the <a href="https://getbootstrap.com/docs/4.4/layout/grid/">Bootstrap Grid</a> system).
To make images responsive, add `img-fluid` class to each; for rounded corners and shadows use `rounded` and `z-depth-1` classes.
Here's the code for the last row of images above:

{% raw %}

```html
<div class="row justify-content-sm-center">
  <div class="col-sm-8 mt-3 mt-md-0">
    {% include figure.liquid path="assets/img/6.jpg" title="example image"
    class="img-fluid rounded z-depth-1" %}
  </div>
  <div class="col-sm-4 mt-3 mt-md-0">
    {% include figure.liquid path="assets/img/11.jpg" title="example image"
    class="img-fluid rounded z-depth-1" %}
  </div>
</div>
```

{% endraw %}
