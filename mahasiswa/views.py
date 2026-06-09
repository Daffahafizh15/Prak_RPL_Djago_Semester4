from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Mahasiswa


def index(request):
    context = {
        'judul': 'Halaman Mahasiswa',
        'deskripsi': 'Contoh halaman index menggunakan Django.'
    }

    return render(request, 'mahasiswa/index.html', context)


@login_required(login_url='/akun/login/')
def daftar_mahasiswa(request):
    mahasiswas = Mahasiswa.objects.all()

    return render(
        request,
        'mahasiswa/daftar.html',
        {'mahasiswas': mahasiswas}
    )


@login_required(login_url='/akun/login/')
def tambah_mahasiswa(request):
    if request.method == 'POST':
        nim = request.POST['nim']
        nama = request.POST['nama']
        programstudi = request.POST['programstudi']
        angkatan = request.POST['angkatan']

        Mahasiswa.objects.create(
            nim=nim,
            nama=nama,
            programstudi=programstudi,
            angkatan=angkatan
        )

        return redirect('daftar_mahasiswa')

    return render(request, 'mahasiswa/tambah.html')


@login_required(login_url='/akun/login/')
def edit_mahasiswa(request, id):
    mhs = Mahasiswa.objects.get(id=id)

    if request.method == 'POST':
        mhs.nim = request.POST['nim']
        mhs.nama = request.POST['nama']
        mhs.programstudi = request.POST['programstudi']
        mhs.angkatan = request.POST['angkatan']
        mhs.save()

        return redirect('daftar_mahasiswa')

    return render(request, 'mahasiswa/edit.html', {'mhs': mhs})


@login_required(login_url='/akun/login/')
def hapus_mahasiswa(request, id):
    mhs = Mahasiswa.objects.get(id=id)
    mhs.delete()

    return redirect('daftar_mahasiswa')