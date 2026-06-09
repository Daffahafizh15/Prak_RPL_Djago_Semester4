from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def login_view(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)

            # Setelah login masuk ke halaman utama
            return redirect('daftar_mahasiswa')

        else:
            messages.error(
                request,
                'Username atau Password salah!'
            )

    return render(request, 'akun/login.html')


def logout_view(request):
    logout(request)

    # Setelah logout kembali ke halaman login
    return redirect('login')