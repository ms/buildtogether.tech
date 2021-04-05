---
---

{% for entry in site.chapters %}
{% if entry.appendix %}{% break %}{% endif %}
{% if entry.exercises %}
{% include solutions.md entry=entry solution=true %}
{% endif %}
{% endfor %}
