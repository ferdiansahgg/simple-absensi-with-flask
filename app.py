from flask import Flask, render_template, request, send_from_directory, url_for
from datetime import datetime, timedelta
import os

app = Flask(__name__)

# Pastikan folder static tersedia untuk menyimpan file absensi & lembur
os.makedirs("static", exist_ok=True)

def translate_day(day):
    days = {
        "Monday": "Senin",
        "Tuesday": "Selasa",
        "Wednesday": "Rabu",
        "Thursday": "Kamis",
        "Friday": "Jumat"
    }
    return days.get(day, day)

def generate_attendance(nama, tanggal_input, jam_masuk, jam_keluar, keterangan):
    try:
        input_date = datetime.strptime(tanggal_input, "%d-%m-%Y")
        start_date = input_date - timedelta(days=input_date.weekday())  # Geser ke Senin
    except ValueError:
        return None, "Format tanggal tidak valid. Gunakan DD-MM-YYYY."

    jam_masuk = jam_masuk or "08.00 AM"
    jam_keluar = jam_keluar or "17.00 PM"

    attendance_text = ""

    for i in range(5):  # Loop Senin-Jumat
        current_date = start_date + timedelta(days=i)
        formatted_date = current_date.strftime("%d-%m-%Y")
        day_name = translate_day(current_date.strftime("%A"))
        
        attendance_text += (f"Nama : {nama}\n"
                            f"\U0001F4C6 Kehadiran : {day_name} {formatted_date}\n"
                            f"\U000023F0 Masuk : {jam_masuk}\n"
                            f"\U0001F570 Keluar : {jam_keluar}\n")
        
        if keterangan:
            attendance_text += f"\U0001F4DD Keterangan : {keterangan}\n"
        
        attendance_text += "\n"

    filename = f"absensi-{nama}-{datetime.now().strftime('%d%m%Y')}.txt"
    file_path = os.path.join("static", filename)

    with open(file_path, "w", encoding="utf-8") as file:
        file.write(attendance_text)

    return filename, attendance_text

def generate_overtime(nama, tanggal_lembur, jam_masuk_lembur, jam_keluar_lembur, keterangan_lembur):
    try:
        datetime.strptime(tanggal_lembur, "%d-%m-%Y")
    except ValueError:
        return None, "Format tanggal tidak valid. Gunakan DD-MM-YYYY."

    jam_masuk_lembur = jam_masuk_lembur or "08.00 AM"
    jam_keluar_lembur = jam_keluar_lembur or "17.00 PM"

    overtime_text = (f"Nama : {nama}\n"
                     f"\U0001F4C6 Lembur : {tanggal_lembur}\n"
                     f"\U000023F0 Masuk : {jam_masuk_lembur}\n"
                     f"\U0001F570 Keluar : {jam_keluar_lembur}\n")

    if keterangan_lembur:
        overtime_text += f"\U0001F4DD Keterangan : {keterangan_lembur}\n"

    filename = f"lembur-{nama}-{datetime.now().strftime('%d%m%Y')}.txt"
    file_path = os.path.join("static", filename)

    with open(file_path, "w", encoding="utf-8") as file:
        file.write(overtime_text)

    return filename, overtime_text

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html", result="", filename=None)

@app.route("/generate_absen", methods=["POST"])
def generate_absen():
    nama = request.form.get("nama")
    tanggal = request.form.get("tanggal")
    jam_masuk = request.form.get("jam_masuk")
    jam_keluar = request.form.get("jam_keluar")
    keterangan = request.form.get("keterangan")

    filename, result = generate_attendance(nama, tanggal, jam_masuk, jam_keluar, keterangan)

    if not filename:
        return render_template("index.html", result=f"<p style='color:red;'>{result}</p>", filename=None)

    return render_template("index.html", result=result, filename=filename)

@app.route("/generate_lembur", methods=["POST"])
def generate_lembur():
    nama = request.form.get("nama")
    tanggal_lembur = request.form.get("tanggal_lembur")
    jam_masuk_lembur = request.form.get("jam_masuk_lembur")
    jam_keluar_lembur = request.form.get("jam_keluar_lembur")
    keterangan_lembur = request.form.get("keterangan_lembur")

    filename, result = generate_overtime(nama, tanggal_lembur, jam_masuk_lembur, jam_keluar_lembur, keterangan_lembur)

    if not filename:
        return render_template("index.html", result=f"<p style='color:red;'>{result}</p>", filename=None)

    return render_template("index.html", result=result, filename=filename)

@app.route("/download/<filename>")
def download(filename):
    return send_from_directory("static", filename, as_attachment=True)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
