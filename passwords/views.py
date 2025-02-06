from django.shortcuts import render
from util.utils import generate_password, check_password_strength  # Import the functions

def home(request):
    return render(request, "index.html")

def process_data(request):
    user_input = None
    password_strength = None
    generated_password = None

    if request.method == "POST":
        # Get the user input
        user_input = request.POST.get("user_input")

        # Check if user wants to generate a password
        if user_input == "generate":
            generated_password = generate_password()
            user_input = f"Generated Password: {generated_password}"

        # If the user enters a password, check its strength
        elif user_input and user_input != "generate":
            password_strength = check_password_strength(user_input)
            user_input = f"Your password strength is: {password_strength}"

    return render(request, "index.html", {"user_input": user_input, "generated_password": generated_password, "password_strength": password_strength})
