---
layout: about
permalink: /
title: about
social: true # includes social icons at the bottom of the page
---

<div class="post">

  <div style="text-align: center;">
    <img src="{{ site.about_banner | prepend: '/assets/img/' | relative_url }}" alt="Banner Image" style="max-width: 100%; height: auto;">
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
          <i class="fa-solid fa-hashtag fa-sm"></i> <a href="{{ tag | slugify | prepend: '/' | relative_url }}">{{ tag }}</a>
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
          <i class="fa-solid fa-tag fa-sm"></i> <a href="{{ category | slugify | prepend: '/' | relative_url }}">{{ category }}</a>
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

{{ site.about_content }}

<br>
<div style="text-align: center; margin-top: 20px;">
  <img src="{{ site.about_logo | prepend: '/assets/img/' | relative_url }}" alt="Logo Denes" style="max-width: 30%; height: auto;">
</div>
<br>

<p style="text-align: center;">{{ site.contact_info }}</p>
