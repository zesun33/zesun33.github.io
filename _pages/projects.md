---
layout: page
title: Projects
permalink: /projects/
description: Research projects and practical engineering tools, with examples, implementation status, and paths to get started.
nav: true
nav_order: 3
display_categories: [Research, Open-source tools]
horizontal: false
_styles: |
  .projects h2.category { color: var(--global-text-color); }
---

<!-- pages/projects.md -->

Explore the research stories below, or try a small engineering result with the [step-by-step tutorials]({{ '/projects/hw-ml-tutorials/' | relative_url }}). The [complete repository directory]({{ '/repositories/' | relative_url }}) includes the tools, exercises, and future architecture plans beyond these selected projects.

<div class="projects">
{% if site.enable_project_categories and page.display_categories %}
  <!-- Display categorized projects -->
  {% for category in page.display_categories %}
  <h2 class="category" id="{{ category | slugify }}">{{ category }}</h2>
  {% assign categorized_projects = site.projects | where: "category", category %}
  {% assign sorted_projects = categorized_projects | sort: "importance" %}
  <!-- Generate cards for each project -->
  {% if page.horizontal %}
  <div class="container">
    <div class="row row-cols-1 row-cols-md-2">
    {% for project in sorted_projects %}
      {% include projects_horizontal.liquid %}
    {% endfor %}
    </div>
  </div>
  {% else %}
  <div class="row row-cols-1 row-cols-md-3">
    {% for project in sorted_projects %}
      {% include projects.liquid %}
    {% endfor %}
  </div>
  {% endif %}
  {% endfor %}

{% else %}

<!-- Display projects without categories -->

{% assign sorted_projects = site.projects | sort: "importance" %}

  <!-- Generate cards for each project -->

{% if page.horizontal %}

  <div class="container">
    <div class="row row-cols-1 row-cols-md-2">
    {% for project in sorted_projects %}
      {% include projects_horizontal.liquid %}
    {% endfor %}
    </div>
  </div>
  {% else %}
  <div class="row row-cols-1 row-cols-md-3">
    {% for project in sorted_projects %}
      {% include projects.liquid %}
    {% endfor %}
  </div>
  {% endif %}
{% endif %}
</div>
