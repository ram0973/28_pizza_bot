Пицца из нашего меню:

{% for pizza in pizzas -%}
*{{ pizza.title }} #{{pizza.id}}*
Цена: {{ pizza.price }} руб.
{{ pizza.description }}
{% endfor %}
