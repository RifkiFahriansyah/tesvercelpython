from flask import Flask, render_template
from typing import Union
app = Flask(__name__)

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

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug = True)