---
layout: about
permalink: /
title: about
social: true # includes social icons at the bottom of the page
---

<div class="post">

  <!-- Centered Image -->
  <div style="text-align: center;">
    <img src="{{ '/assets/img/about_banner.jpg' | relative_url }}" alt="Banner Image" style="max-width: 100%; height: auto;">
  </div>

{% assign blog_name_size = site.blog_name | size %}
{% assign blog_description_size = site.blog_description | size %}

{% if blog_name_size > 0 or blog_description_size > 0 %}

  <div class="header-bar">
    <h1>{{ site.blog_name }}</h1>
    <h2>{{ site.blog_description }}</h2>
  </div>
  {% endif %}

{% if site.display_tags or site.display_categories %}

  <div class="tag-category-list">
    <ul class="p-0 m-0">
      {% for tag in site.display_tags %}
        <li>
          <i class="fa-solid fa-hashtag fa-sm"></i> <a href="{{ tag | slugify | prepend: '/blog/tag/' | relative_url }}">{{ tag }}</a>
        </li>
        {% unless forloop.last %}
          <p>&bull;</p>
        {% endunless %}
      {% endfor %}
      {% if site.display_categories.size > 0 and site.display_tags.size > 0 %}
        <p>&bull;</p>
      {% endif %}
      {% for category in site.display_categories %}
        <li>
          <i class="fa-solid fa-tag fa-sm"></i> <a href="{{ category | slugify | prepend: '/blog/category/' | relative_url }}">{{ category }}</a>
        </li>
        {% unless forloop.last %}
          <p>&bull;</p>
        {% endunless %}
      {% endfor %}
    </ul>
  </div>
  {% endif %}

  <br>

</div>

Benvolgudes amigues i amics, aquesta és una primera versió de la nostra nova web. Actualment està en construcció i continuem treballant per actualitzar-la amb la informació del nostres diccionaris i vocabularis, els nostres autors i títols, el material de biblioteca i la resta del catàleg.

Podeu sol·licitar les comandes a les llibreries de la vostra confiança o per les distribuïdores especialitzades:

- [Exclusivas Graons](https://www.graons.com/).
- Nordest Llibres: tlf. 972 67 23 54, email: nordest@nordest.es
- Maidhisa: tlf. 91 670 21 29, email: ismaroto@hotmail.com

<br>
<div style="text-align: center; margin-top: 20px;">
  <img src="{{ '/assets/img/logo_denes_blue.gif' | relative_url }}" alt="Logo Denes" style="max-width: 30%; height: auto;">
</div>
<br>
