---
layout: page
title: GaN Nanoribbons Thermal Transport
description: Molecular dynamics study of doping and defects impact on thermal properties
img: assets/img/4.jpg
importance: 4
category: work
related_publications: true
---

## Impact of Doping and Defects on Thermal Transport of Monolayer GaN Nanoribbons

This computational research project investigates thermal transport properties in monolayer gallium nitride (GaN) nanoribbons using advanced molecular dynamics simulation techniques.

### Research Overview

The study focuses on understanding how doping and structural defects influence thermal transport mechanisms in GaN nanoribbons, providing crucial insights for the design of next-generation nanoelectronic devices.

### Computational Methodology

🔬 **Molecular Dynamics Simulations**: Advanced computational modeling to study thermal behavior at the atomic level

📊 **Statistical Analysis**: Comprehensive data analysis to quantify thermal transport properties

⚙️ **Parameter Optimization**: Systematic investigation of doping concentrations and defect types

### Key Research Questions

**Doping Effects**: How do different dopant types and concentrations affect thermal conductivity?

**Defect Influence**: What is the impact of various structural defects on heat transport?

**Design Optimization**: How can these findings inform nanoelectronic device design?

### Technical Approach

The research utilizes state-of-the-art molecular dynamics simulation software to model:

1. **Pristine GaN Nanoribbons**: Baseline thermal properties
2. **Doped Systems**: Various dopant types and concentrations
3. **Defective Structures**: Different defect configurations
4. **Thermal Analysis**: Heat flux and temperature gradient calculations

### Research Team

**Principal Investigator**: Md Zesun Ahmed Mia

**Collaborators**:
- Nazmus Saadat As-Saquib
- Mehedi Hasan Himel  
- Mehedi Hossen Limon
- Samia Subrina (Supervisor)

### Results and Impact

**Novel Insights**: First comprehensive study of combined doping and defect effects on GaN nanoribbon thermal transport

**Device Applications**: Direct implications for thermal management in nanoelectronic devices

**Theoretical Contributions**: Enhanced understanding of nanoscale thermal physics

### Conference Presentation

Successfully presented at the **13th International Conference on Electrical and Computer Engineering (ICECE) 2024**, receiving positive feedback from the research community.

**Publication Details**: Pages 685-690, IEEE Conference Proceedings

### Future Directions

This research opens pathways for:
- Advanced thermal management strategies
- Optimized nanoelectronic device designs  
- Enhanced materials engineering approaches
- Further computational studies of 2D materials

The work contributes to the broader understanding of thermal transport in two-dimensional semiconductor materials and their applications in modern electronics.

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
    {% include figure.liquid path="assets/img/6.jpg" title="example image" class="img-fluid rounded z-depth-1" %}
  </div>
  <div class="col-sm-4 mt-3 mt-md-0">
    {% include figure.liquid path="assets/img/11.jpg" title="example image" class="img-fluid rounded z-depth-1" %}
  </div>
</div>
```

{% endraw %}
