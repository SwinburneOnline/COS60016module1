from django.test import TestCase

from django.test import Client
from django.urls import reverse
import json
import pytest

# Create your tests here.


pytestmark = pytest.mark.django_db
def test_create_book_view():
    client = Client()
    mimetype = 'application/json;charset=UTF-8'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype
    }
    data = '{"title": "Random Books", "description": "This is an awesome random book", "author": "John Doe"}'
    response = client.post(reverse(viewname='create_book'), data=json.loads(data), headers=headers)
    assert response.status_code == 200




def test_create_member_view():
    client = Client()
    mimetype = 'application/json;charset=UTF-8'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype
    }
    data = '{"first_name": "Clara", "last_name": "Clark"}'
    response = client.post(reverse(viewname='create_member'), data=json.loads(data), headers=headers)
    assert response.status_code == 200




def test_create_staff_view():
    client = Client()
    mimetype = 'application/json;charset=UTF-8'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype
    }
    data = '{"first_name": "Laura", "last_name": "Clark", "age": "27", "position": "librarian"}'
    response = client.post(reverse(viewname='create_staff'), data=json.loads(data), headers=headers)
    assert response.status_code == 200





def test_create_book_status_view():
    client = Client()
    mimetype = 'application/json;charset=UTF-8'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype
    }
    data = '{"status01": "Rented", "status02": "Rented", "book_title": "Random Books", "staff_name": "Laura", "staff_last_name": "Clark", "member_name": "Clara", "member_last_name": "Clark"}'
    response = client.post(reverse(viewname='book_status'), data=json.loads(data), headers=headers)
    assert response.status_code == 200
