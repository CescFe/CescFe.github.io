---
layout: page
title: col·leccions
permalink: /col-leccions/
description: un llistat amb les diferents col·leccions de Denes
nav: true
nav_order: 4
display_categories:
  [
    diccionaris,
    edicions de la guerra (poesia),
    calabria,
    contes de tots,
    contes del cocodril,
    estudis,
    bàsica,
    contaralles de la meua terra,
    Costumeta,
    investigació Francesc Ferrer Pastor,
    rent,
    altres
  ]
horizontal: true
---

<!-- pages/books.md -->
<div class="projects">
{% if site.enable_project_categories and page.display_categories %}
  <!-- Display categorized books -->
  {% for category in page.display_categories %}
  <a id="{{ category }}" href=".#{{ category }}">
    <h2 class="category">{{ category }}</h2>
  </a>
  {% assign categorized_books = site.books | where: "category", category %}
  {% assign sorted_books = categorized_books | sort: "importance" %}
  <!-- Generate cards for each book -->
  {% if page.horizontal %}
  <div class="container">
    <div class="row row-cols-1 row-cols-md-2">
    {% for book in sorted_books %}
      {% include books_horizontal.liquid %}
    {% endfor %}
    </div>
  </div>
  {% else %}
  <div class="row row-cols-1 row-cols-md-3">
    {% for book in sorted_books %}
      {% include books.liquid %}
    {% endfor %}
  </div>
  {% endif %}
  {% endfor %}

{% else %}

<!-- Display books without categories -->

{% assign sorted_books = site.books | sort: "importance" %}

  <!-- Generate cards for each collection -->

{% if page.horizontal %}

  <div class="container">
    <div class="row row-cols-1 row-cols-md-2">
    {% for book in sorted_books %}
      {% include books_horizontal.liquid %}
    {% endfor %}
    </div>
  </div>
  {% else %}
  <div class="row row-cols-1 row-cols-md-3">
    {% for book in sorted_books %}
      {% include books.liquid %}
    {% endfor %}
  </div>
  {% endif %}
{% endif %}
</div>
