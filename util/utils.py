import secrets
import string
import re
from django.http import JsonResponse

# Generate a secure password
def generate_password():
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(characters) for _ in range(12))
    return JsonResponse({"generated_password": password})

# Check password strength on backend
def check_password_strength(request):
    password = request.GET.get('password', '')
    points = 0

    if len(password) >= 8:
        points += 1
    if re.search(r"[a-z]", password):
        points += 1
    if re.search(r"[A-Z]", password):
        points += 1
    if re.search(r"[\d]", password):
        points += 1
    if re.search(r"[!@#$%^&*(){}|<>,./?\-+=`~]", password):
        points += 1

    strength_levels = ["Needs Improvement", "Bad", "Average", "Good", "Perfect"]
    strength = strength_levels[points - 1] if points > 0 else "Invalid Password"

    return JsonResponse({"strength": strength, "points": points})
