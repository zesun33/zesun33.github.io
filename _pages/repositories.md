---
layout: page
permalink: /repositories/
title: Repositories
description: A complete directory of my hardware tools, GPU studies, tutorials, and architecture plans, with first tasks and current scope.
nav: true
nav_order: 4
---

{% if site.data.repositories.github_users %}

## GitHub profile

<div class="repositories d-flex flex-wrap flex-md-row flex-column justify-content-between align-items-center">
  {% for user in site.data.repositories.github_users %}
    {% include repository/repo_user.liquid username=user %}
  {% endfor %}
</div>

---

{% if site.repo_trophies.enabled %}
{% for user in site.data.repositories.github_users %}
{% if site.data.repositories.github_users.size > 1 %}

  <h4>{{ user }}</h4>
  {% endif %}
  <div class="repositories d-flex flex-wrap flex-md-row flex-column justify-content-between align-items-center">
  {% include repository/repo_trophies.liquid username=user %}
  </div>

---

{% endfor %}
{% endif %}
{% endif %}

## Choose a practical starting point

[Follow the tutorials]({{ '/projects/hw-ml-tutorials/' | relative_url }}), browse [featured project stories]({{ '/projects/' | relative_url }}#open-source-tools), or open the [portfolio getting-started guide]({{ site.data.portfolio.getting_started_url }}).

Each code project keeps its own repository. Labels distinguish usable tools, measured experiments, learning exercises, architecture drafts, and roadmap-only projects. The Rust entry contains public curriculum metadata; its basics remain private.

{% include portfolio_directory.liquid %}

## Website source

[This academic website](https://github.com/zesun33/zesun33.github.io) uses Jekyll and the al-folio theme. [The portfolio catalog]({{ site.data.portfolio.catalog_url }}) supplies the descriptions and scope used in this directory.
