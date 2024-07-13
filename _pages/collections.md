---
layout: page
title: col·leccions
permalink: /col-leccions/
description: un llistat amb les diferents col·leccions de Denes
nav: true
nav_order: 4
display_categories: [infantil, adult, altres]
horizontal: true
---

<!-- pages/collections.md -->
<div class="projects">
{% if site.enable_project_categories and page.display_categories %}
  <!-- Display categorized collections -->
  {% for category in page.display_categories %}
  <a id="{{ category }}" href=".#{{ category }}">
    <h2 class="category">{{ category }}</h2>
  </a>
  {% assign categorized_collections = site.collections | where: "category", category %}
  {% assign sorted_collections = categorized_collections | sort: "importance" %}
  <!-- Generate cards for each collection -->
  {% if page.horizontal %}
  <div class="container">
    <div class="row row-cols-1 row-cols-md-2">
    {% for collection in sorted_collections %}
      {% include collections_horizontal.liquid %}
    {% endfor %}
    </div>
  </div>
  {% else %}
  <div class="row row-cols-1 row-cols-md-3">
    {% for collection in sorted_collections %}
      {% include collections.liquid %}
    {% endfor %}
  </div>
  {% endif %}
  {% endfor %}

{% else %}

<!-- Display collections without categories -->

{% assign sorted_collections = site.collections | sort: "importance" %}

  <!-- Generate cards for each collection -->

{% if page.horizontal %}

  <div class="container">
    <div class="row row-cols-1 row-cols-md-2">
    {% for collection in sorted_collections %}
      {% include collections_horizontal.liquid %}
    {% endfor %}
    </div>
  </div>
  {% else %}
  <div class="row row-cols-1 row-cols-md-3">
    {% for collection in sorted_collections %}
      {% include collections.liquid %}
    {% endfor %}
  </div>
  {% endif %}
{% endif %}
</div>
