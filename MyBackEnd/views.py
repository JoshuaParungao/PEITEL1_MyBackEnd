from django.shortcuts import render, redirect

# Simple homepage view
def homepage_view(request):
    return render(request, 'homepage.html')


# Basic login view using the project's `UserRegistration` model.
# This is a minimal, compatible implementation so the form at
# `login.html` can POST email/password and authenticate against
# the `registration.UserRegistration` table. It stores the
# user's id in the session on success.
#
# NOTE: currently passwords are stored in plain text in the
# `UserRegistration` model. For production you should use
# Django's built-in User model and password hashing.
def login_view(request):
    error = None
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        # Lazy import to avoid circular imports at project startup
        from registration.models import UserRegistration
        try:
            user = UserRegistration.objects.get(email=email, password=password)
            # mark user as logged in via session
            request.session['user_id'] = user.id
            request.session['user_email'] = user.email
            return redirect('home_html')
        except UserRegistration.DoesNotExist:
            error = 'Invalid email or password'

    return render(request, 'login.html', {'error': error})