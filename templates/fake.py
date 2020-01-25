{% extends "base.html" %}

{% load bootstrap3 %}

{% block content %}


<div class="content-section">
    <div class="media">
        <img class="rounded-circle account-img" src="{{ user.userprofile.image.url }}">
        <div class="media-body">
            <h2 class="account-heading">
                <h3>Username:{{user.username}}</h3>

            </h2>
            <p class="text-secondary">{{ user.email }}</p>
        </div>
    </div>
    <div>
        <a href="{% url 'core:order_detail' %}">Your Orders:{{orders}}</p>

            <div>
                {% if grant %}
                <a href="{% url 'corporate:corporate_home' %}">Sign in</a>
                {% elif process %}
                <h1>Processing your request</h1>
                {% else %}
                <a href="{% url 'corporate:contact_form' %}">Apply for Contact Form</a>
                {% endif %}
            </div>

    </div>
    <form method="POST" enctype="multipart/form-data">
        {% csrf_token %}
        <fieldset class="form-group">
            <legend class="border-bottom mb-4">Profile Info</legend>
            {% bootstrap_form form %}

        </fieldset>
        <div class="form-group">
            <button class="btn btn-outline-info" type="submit">Update</button>
        </div>
    </form>
</div>

{% endblock content %}