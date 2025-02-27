from django.test import TestCase
from intasend import APIService
from dotenv import load_dotenv
import requests, base64, json, re, os

# Create your tests here
# Load environment variables
load_dotenv()

publishable_key = "Bearer ISSecretKey_test_493e0ea5-c804-461f-ad31-f905b918ec64"
service = APIService(token=None, publishable_key=publishable_key, test=True)

Authorization = "Bearer ISSecretKey_test_493e0ea5-c804-461f-ad31-f905b918ec64"

response = service.collect.checkout(phone_number=254722424220,
                                    email="john@doe.com", amount=10, currency="KES", comment="Service Fees", redirect_url="http://example.com/thank-you")
print(response.get("url"))