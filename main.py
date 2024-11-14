from flask import Flask, render_template,request,redirect,url_for
from typing import Union
import os # Diperlukan untuk menyimpan file
import time # Diperlukan untuk membuat timestamp

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads/' #Path folder upload

# 1 Router 1 Fungsi
Number = Union[int, float]
@app.route('/')
def hello():
    return render_template('main.html')

@app.route('/aboutme/<name>')
def about(name):
    return 'Halo {}!' .format(name)
    
# Menampilkan umur 
@app.route('/umur/<int:age>')
def umur(age):
    return 'Umur saya adalah {} tahun' .format(age)

# Menampilkan IPK @app.route('/ipk/<ipk>')
def ipk(ipk : Number):
    return 'IPK saya adalah {}' .format(ipk)

# Menampilkan Route  prodi, contact, fakultas
@app.route('/fakultas')
def fakultas():
    fakultas = ["FIKR", "FEB"]
    return render_template('fakultas.html', fakultas = fakultas)

@app.route('/prodi')
def prodi():
    prodi = [
    {"nama": "Informatika", "fakultas": "FIKR"},
    {"nama": "Sistem Informasi", "fakultas": "FIKR"},
    {"nama": "Manajemen", "fakultas": "FEB"},
    ]
    for data in prodi:
        if data["fakultas"] == "FIKR":
            data["ukt"] = "8.000.000"
        elif data["fakultas"] == "FEB":
            data["ukt"] = "6.000.000"
    return render_template('prodi.html', prodi = prodi)

@app.route('/contact', methods = ['GET', 'POST'])
def contact():
    if request.method == 'POST':
        nama = request.form['nama'] #Ambil data dari form dengan name=nama
        email = request.form['email'] #Ambil data dari form dengan name=email
        pesan = request.form['pesan'] #Ambil data dari form dengan name=pesan
        #Tampilkan di terminal
        print(f"Nama : {nama}, Email : {email}, Pesan : {pesan}")
        # return redirect(url_for('fakultas'))
        confirmation_message = f"Thankyou, {nama}. Pesanmu sudah kami terima "

        return render_template('contact.html', confirmation_message=confirmation_message, nama=nama, email=email, pesan=pesan)
    
    return render_template('contact.html')

@app.route('/registrasi', methods = ['GET', 'POST'])
def registrasi():
    if request.method == 'POST':
        nisn = request.form['nisn']
        nama = request.form['nama']
        email = request.form['email']
        tglLahir = request.form['tglLahir']
        asalSekolah = request.form['asalSekolah']
        prodi = request.form['prodi']
        # Cek file yg diunggah
        foto = request.files['foto']
        if foto:
            #Mengambil timestamp saat ini untuk menambahkan ke nama file
            timestamp = str(int(time.time()))

            # Mengambil ekstensi file asli
            ext = foto.filename.split('.')[-1]

            # Menambahkan ekstensi ke nama file unik
            unique_filename = f"{timestamp}.{ext}"

            # Menyimpan file dengan nama unik
            foto_path = os.path.join(app.config['UPLOAD_FOLDER'], unique_filename)
            foto.save(foto_path)
            foto_path = f'uploads/{unique_filename}'  # Menyimpan path relatif dengan menggunakan '/uploads/'
        else:
            foto_path = None

        # Tes 
        print(f"Nama : {nama}, Email : {email}, Asal Sekolah : {asalSekolah}")
        # Pesan Konfirmasi
        pesanKonfirmasi = f"Terimakasih {nama} sudah mendaftar"
        
        return render_template('registrasi.html',pesanKonfirmasi=pesanKonfirmasi, nisn=nisn, nama=nama, email=email, tglLahir=tglLahir, asalSekolah=asalSekolah, prodi=prodi, foto=foto_path)
    
    return render_template("registrasi.html")

if __name__ == '__main__':
    app.run(debug = True)