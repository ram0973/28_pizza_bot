Ваш заказ:

{% for pizza in pizzas -%}
*{{ pizza.title }} #{{pizza.id}}*
Цена: {{ pizza.price }} руб.
{{ pizza.description }}
{% endfor %}
*Стоимость заказа: {{order_total}} руб.*
