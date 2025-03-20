import threading
import paho.mqtt.client as mqtt
import time
import sys

# Konfigurasi MQTT
broker = "test.mosquitto.org"
topic_data = "mahen/data/sensor/dht22"
topic_request = "sensor/request"

# Variabel global
waiting_response = False
timeout_handler = None
start_time = None


# Callback ketika terhubung ke broker
def on_connect(client, userdata, flags, rc, properties):
    if rc == 0:
        print("✅ Terhubung ke MQTT broker!")
        client.subscribe(topic_data)
        print(f"📡 Berhasil subscribe ke topik: {topic_data}")
        tanya_pengguna()
    else:
        print(f"❌ Gagal terhubung ke broker dengan kode: {rc}")


# Callback ketika menerima pesan
def on_message(client, userdata, msg):
    global waiting_response, start_time

    if msg.topic == topic_data:
        if start_time:
            end_time = time.time()
            runtime_in_ms = (end_time - start_time) * 1000
            print(f"⏱️  Waktu Respons: {runtime_in_ms:.2f} ms")
        else:
            print("⚠️  start_time tidak ditemukan, perhitungan waktu respons dilewati.")

        raw_data = msg.payload.decode().strip()
        print(f"\n📥 Data Sensor Diterima: {raw_data}")

        if len(raw_data) == 8:
            suhu = float(raw_data[:4]) / 100
            kelembaban = float(raw_data[4:8]) / 100

            print(f"🌡️  Suhu       : {suhu:.2f}°C")
            print(f"💧 Kelembaban : {kelembaban:.2f}%\n")
        else:
            print("⚠️  Format data tidak valid!\n")

        waiting_response = False
        if timeout_handler:
            timeout_handler.cancel()

        tanya_pengguna()


# Callback ketika terjadi error
def on_error(client, userdata, rc):
    print(f"❌ Terjadi kesalahan MQTT: {rc}")


# Callback ketika koneksi terputus
def on_disconnect(client, userdata, rc):
    print("🔴 Koneksi ke broker MQTT terputus! Mencoba reconnect...")
    time.sleep(5)
    client.reconnect()


# Fungsi untuk meminta input pengguna
def tanya_pengguna():
    global waiting_response, start_time, timeout_handler

    if waiting_response:
        return

    jawaban = input("📝 Ketik '1' untuk mendapatkan data sensor: ")
    if jawaban.lower() == "1":
        print("📨 Meminta data ke Publisher...\n")
        start_time = time.time()  # Inisialisasi start_time di sini
        client.publish(topic_request, "REQ")
        waiting_response = True

        # Set timeout 10 detik
        timeout_handler = threading.Timer(10, timeout_callback)
        timeout_handler.start()
    else:
        print("⏳ Perintah tidak dikenali, silakan ketik '1'.\n")
        tanya_pengguna()


# Callback ketika timeout
def timeout_callback():
    global waiting_response
    print("⏳ Tidak ada respons dari publisher dalam 10 detik. Coba lagi.\n")
    waiting_response = False
    tanya_pengguna()


# Membuat client MQTT menggunakan MQTT v5
client = mqtt.Client(protocol=mqtt.MQTTv5)

client.on_connect = on_connect
client.on_message = on_message
client.on_disconnect = on_disconnect

# Terhubung ke broker
client.connect(broker, 1883, 60)

# Mulai loop MQTT
client.loop_start()


# Fungsi untuk menangani exit program
def on_exit():
    print("🔴 Program dihentikan.")
    client.disconnect()
    sys.exit(0)


# Jalankan program
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    on_exit()
