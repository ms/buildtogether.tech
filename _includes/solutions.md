{%- comment -%}
  Include solutions from exercises.
{%- endcomment -%}
<h2 id="{{ include.entry.slug }}">{{ include.entry.title }}</h2>

{% for exercise in include.entry.exercises %}
{% assign path = include.entry.slug | append: '/' | append: exercise %}
{%- capture content -%}{% include {{ path }} solution=true %}{%- endcapture -%}
{{ content | markdownify }}
{% endfor %}
