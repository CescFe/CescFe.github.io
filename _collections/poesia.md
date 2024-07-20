---
layout: page
title: edicions de la guerra
description: la col·lecció de poesia d'editorial Denes
img: assets/img/collection_preview/collection_poesia.png
importance: 1
category: adult
related_publications: false
---

<!-- pages/books.md -->
<div class="projects">
  <!-- Display "poesia" books -->
  {% assign categorized_books = site.books | where: "category", "poesia" %}
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
