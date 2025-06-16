---
layout: page
title: Electronic Braille Device
description: Ultra low-cost, high-speed assistive technology for visually impaired
img: assets/img/3.jpg
importance: 3
category: work
related_publications: true
---

## Ultra Low Cost, Low Power, High Speed Electronic Braille Device

This research project focuses on developing innovative assistive technology to improve accessibility for visually impaired individuals through the design and implementation of an ultra-low-cost, high-speed electronic Braille device.

### Project Mission

Making Braille technology accessible and affordable for everyone, regardless of economic background, through innovative engineering and cost-effective design solutions.

### Key Features

💰 **Ultra Low Cost**: Designed with affordability as a primary constraint to ensure widespread accessibility

⚡ **High Speed**: Rapid text-to-Braille conversion for real-time reading experiences

🔋 **Low Power**: Energy-efficient design for extended battery life

♿ **User-Centered**: Developed with direct input from the visually impaired community

### Technical Innovations

**Hardware Design**: 
- Cost-optimized component selection
- Efficient power management systems
- Durable, portable form factor

**Software Implementation**:
- Fast text processing algorithms
- Multiple language support
- Intuitive user interface

**Accessibility Features**:
- Audio feedback for navigation
- Customizable reading speeds
- Multiple input methods

### Research Methodology

The project employed a comprehensive approach including:

1. **User Research**: Direct engagement with visually impaired community
2. **Cost Analysis**: Extensive market research for component optimization
3. **Prototype Development**: Iterative design and testing process
4. **Performance Evaluation**: Speed and accuracy benchmarking

### Impact and Applications

**Educational Settings**: Supporting students with visual impairments in academic environments

**Professional Use**: Enabling workplace accessibility and productivity

**Personal Communication**: Facilitating independent access to digital content

### Collaboration

**Research Partner**: Kazi Toukir Ahmed

**Presentation**: International Conference on Advances in Computing, Communication, Electrical, and Smart Systems (iCACCESS) 2024

### Future Development

The project continues to evolve with plans for:
- Enhanced connectivity features
- Multi-language expansion
- Integration with smart devices
- Community feedback incorporation

This research demonstrates the potential for engineering solutions to create meaningful social impact while maintaining technical excellence and innovation.

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
