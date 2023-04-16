import sys
import os
from time import ctime
import time
import datetime
import serial
import serial.tools.list_ports
from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QTimer
from ver6 import *

from haberlesme import GirisBilgileri, SunucuSaati, TelemetriVerisi, KilitlenmeBilgisi
from api_get_post import Api_Get, Api_Post

import serial.tools.list_ports
from pymavlink import mavutil
import json
import requests
import googlemaps
from gmplot import gmplot

from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtCore import QUrl

App = QApplication(sys.argv)
MainWindow = QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()

master = None
is_armed = False

adres_giris = "http://localhost:64559/api/giris" # post

response_giris = Api_Post(adres_giris,{
    "kadi" : "ikaruss7",
    "sifre" : "r7pr8zCywP"
}, "ikaruss7", "r7pr8zCywP")

ui.statusbar.showMessage(str(response_giris))

def PortConnection():
    port = str(ui.port.currentText())
    baud = str(ui.baudrate.currentText())
    global ser

    try:
        ser = serial.Serial(port, baudrate=baud, timeout=0)

        if ser.is_open:
            ui.statusbar.showMessage(" "*1+" Port açıldı...", 1500)
            global timer1
            timer1 = QtCore.QTimer()
            timer1.start(1000)
            timer1.timeout.connect()
    except:
        ui.statusbar.showMessage(" "*1 + " Port açılamadı!!! ")


def Screentimer():
    global time
    time = ctime()
    ui.systemTime_lbl.setText(time[10:19])


timer0 = QtCore.QTimer()
timer0.start(1000)
timer0.timeout.connect(Screentimer)

# COM port verisi
ports = list(serial.tools.list_ports.comports())
port_names = []
for port in ports:
    port_names.append(port.device)

ui.COM_cbox.addItems(port_names)
selected_port = ui.COM_cbox.currentText()

motor_timer = QTimer()


def button_arm_clicked():
    global master, is_armed
    msg = master.mav.command_long_encode(
        0,  # sistem ID
        0,  # Component ID
        mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM,
        0,  # Confirmation
        1,  # Arm
        0,  # Parametre 1
        0,  # Parametre 2
        0,  # Parametre 3
        0,  # Parametre 4
        0,  # Parametre 5
        0)  # Parametre 6

    # mavlink mesajını gönder
    master.mav.send(msg)
    is_armed = True

    # Plane'i arm etmeyi sağlayacak buton aktif hale gelir
    ui.arm_button.setEnabled(False)
    ui.disarm_button.setEnabled(True)
    # arm edince manuel moda geçiş yap
    master.mav.set_mode_send(
        master.target_system,
        mavutil.mavlink.MAV_MODE_FLAG_MANUAL_INPUT_ENABLED,
        0)
    ui.statusbar.showMessage("ARM EDİLDİ")


def button_disarm_clicked():
    global master, is_armed
    # MAVLink mesajı oluştur
    msg = master.mav.command_long_encode(
        0,  # Sistem ID
        0,  # Component ID
        mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM,  # Komut
        0,  # Confirmation
        0,  # Disarm
        0,  # Parametre 1
        0,  # Parametre 2
        0,  # Parametre 3
        0,  # Parametre 4
        0,  # Parametre 5
        0)  # Parametre 6
    master.mav.send(msg)
    is_armed = False

    # Plane'i arm etmeyi sağlayacak buton aktif hale gelir
    ui.arm_button.setEnabled(True)
    ui.disarm_button.setEnabled(False)
    ui.statusbar.showMessage("DISARM EDİLDİ")




def check_motor_status():
    global motor_status
    motor_status = motor_status + 1
    if motor_status > 20:
        motor_timer.stop()
        print('Motorlar çalışıyor.')
        ui.statusbar.showMessage("Motorlar çalışıyor.")


def irtifa():
    AltitudeMessage = master.recv_match(
        type="GLOBAL_POSITION_INT", blocking=True)
    alt = AltitudeMessage.relative_alt
    alt = alt / 1000

    if alt < 0.004:
        return 0.0
    else:
        return alt


def boylam():
    LongitudeMessage = master.recv_match(
        type="GLOBAL_POSITION_INT", blocking=True)
    lon = LongitudeMessage.lon
    lon = lon / 1e7
    return lon


def enlem():
    LatitudeMessage = master.recv_match(
        type="GLOBAL_POSITION_INT", blocking=True)
    lat = LatitudeMessage.lat
    lat = lat / 1e7
    return lat


def SystemInformation():
    global master
    counter = 0
    com = ui.COM_cbox.currentText()
    ui.arm_button.setEnabled(True)

    try:
        # baudrate girişi
        adress = "udpin:127.0.0.1:14550"
        # adress = "/dev/ttyUSB0"
        baudrate = 57600
        # connection=serial.Serial(adress, baudrate)
        master = mavutil.mavlink_connection(
            adress,
            baud=baudrate,
            source_system=255,
            source_component=0,
        )

        master.wait_heartbeat()
        master.mav.request_data_stream_send(master.target_system, master.target_component,
                                            mavutil.mavlink.MAV_DATA_STREAM_ALL, 10, 1)

        ui.team_ip_lbl_2.setText(adress)
        ui.baudrate_lbl_2.setText(str(baudrate))
        ui.status_lbl.setText("BAĞLANDI")
        ui.status_lbl.setStyleSheet("color: green")

        master.mav.command_long_send(master.target_system, master.target_component,
                                     mavutil.mavlink.MAV_CMD_NAV_TAKEOFF, 0, 0, 0, 0, 0, 0, 0, 0)  # ilk 0 onay

        start_lat = enlem()
        start_lon = boylam()

        ui.startPositionValue_lbl.setText(
            "{:.3f} {:.3f}".format(start_lat, start_lon))

        now = datetime.datetime.now()
        filename = "data/{}_{}_{}_{}_{}_{}.json".format(
            now.day, now.month, now.year, now.hour, now.minute, now.second)

        adres_telemetri = "http://localhost:64559/api/telemetri_gonder" # post
        sunucu_saati = "http://localhost:64559/api/sunucu_saati" # get
        adres_kilitlenme = "http://localhost:64559/api/kilitlenme_bilgisi" # post
        adres_kamikaze = "http://localhost:64559/api/kamikaze_bilgisi" # post
        adres_qr = "http://localhost:64559/api/qr_koordinatı" #get
        # çıkış isteği // get

        ui.statusbar.showMessage(
            "{0} altında log kayıtları tutulmaya başlandı...".format(filename[5:]))

        while True:

            msg = master.recv_match(type='HEARTBEAT', blocking=True)
            mode = mavutil.mode_string_v10(msg)
            ui.current_mode_lbl.setText("Mode : {0}".format(mode))

            counter = counter + 1
            ui.flightValue_lbl.setText("{} s".format(int(counter)))

            ThrottleMessage = master.recv_match(type='VFR_HUD', blocking=True)
            ui.throttle_value_lbl.setText(
                "{0} %".format(ThrottleMessage.throttle))

            SpeedMessage = master.recv_match(type='VFR_HUD', blocking=True)
            ui.speedValue_lbl.setText(
                "{:.2f} m/s".format(SpeedMessage.airspeed))

            WindMessage = master.recv_match(type='WIND', blocking=True)
            ui.windValue_lbl.setText("{:.2f} m/s".format(WindMessage.speed))

            Yaw_Pitch_RollMessage = master.recv_match(type='ATTITUDE', blocking=True)
            if Yaw_Pitch_RollMessage is not None:
                # Yaw, pitch ve roll değerlerini hesaplayın
                yaw = Yaw_Pitch_RollMessage.yaw
                pitch = Yaw_Pitch_RollMessage.pitch
                roll = Yaw_Pitch_RollMessage.roll

            current_lat = enlem()
            current_lon = boylam()
            current_alt = irtifa()
            ui.altitudeValue_lbl.setText(str(current_alt))
            ui.longitudeValue_lbl.setText(str(current_lon))
            ui.latitudeValue_lbl.setText(str(current_lat))

            api_key = "AIzaSyDxURw0nCQOM4o6w9kGkNUJAeXRcAq3v24"

            # API anahtarını kullanarak Google Maps istemcisini oluşturun
            gmap = googlemaps.Client(api_key)
            gmap = gmplot.GoogleMapPlotter(
                current_lat, current_lon, 13, apikey=api_key)
            gmap.marker(current_lat, current_lon)
            gmap.draw('map.html')

            ui.map_view.load(QUrl.fromLocalFile(os.path.abspath("map.html")))

            data_list = []

            # Her bir data sözlüğünü data_list listesine ekleyin
            data = {
                "giris_bilgileri": {
                    'kadi': "ikaruss7",
                    'sifre': "r7pr8zCywP"
                },
                "sistem_saati":{
                    "gun": datetime.datetime.now().day,
                    "saat": datetime.datetime.now().hour,
                    "dakika": datetime.datetime.now().minute,
                    "saniye": datetime.datetime.now().second,
                    "milisaniye": datetime.datetime.now().microsecond
                },
                # "sistem_saati":{
                #     "gun" : server_gun,
                #     "saat": server_saat,
                #     "dakika": server_dakika,
                #     "saniye": server_saniye,
                #     "milisaniye": server_milisaniye
                # },
                "telemetri_verisi": {
                    'takim_numarasi': 10,
                    'iha_enlem': current_lat,
                    'iha_boylam': current_lon,
                    'iha_irtifa': current_alt,
                    'iha_dikilme': pitch,   # pitch
                    'iha_yonelme': yaw,  # yaw
                    'iha_yatis': roll,  # roll
                    'iha_hiz': SpeedMessage.airspeed,
                    'iha_otonom': False if  ui.current_mode_lbl != "OTONOM" else True,
                    "iha_kilitlenme": "",
                    "hedef_merkez_x": "",
                    "hedef_merkez_y": "",
                    "hedef_genislik": "",
                    "hedef_yukseklik": "",

                "kilitlenme_bilgisi": {
                    "kilitlenmeBaslangicZamani": "",
                    "kilitlenmeBitisZamani": "",
                    "otonom_kilitlenme": ""
                },
                "kamikaze_bilgisi": {
                    "kamikazeBaslangicZamani": "",
                    "kamikazeBitisZamani": "",
                    "qr_metni": ""
                }
            }
        }
            response = Api_Get("https://savasaniha.baykartech.com/api/sunucusaati")
            temp = f"{response['gun']}:{response['saat']}:{response['dakika']}:{response['saniye']}:{response['milisaniye']}"
            ui.serverTime_lbl.setText(temp)
            server_gun = 0
            server_saat = 0
            server_dakika = 0
            server_saniye = 0
            server_milisaniye = 0
            server_gun = response["gun"]
            server_saat = response["saat"]
            server_dakika = response["dakika"]
            server_saniye = response["saniye"]
            server_milisaniye = response["milisaniye"]

            data_list.append(data)

            with open(filename, 'a') as file:
                if file.tell() == 0:
                    file.write('[')

                else:
                    file.seek(file.tell() - 1)
                    file.truncate()

                for data in data_list:
                    json.dump(data, file)
                    file.write(',')
                    file.write('\n')

                file.write(',')
                file.write('\n')
                file.seek(file.tell() - 2)
                file.truncate()
                file.write(']')

            # Response Request

            # Api_Post(adres_giris, data["giris_bilgileri"], ui.response_giris_lbl)
            # Api_Post(adres_telemetri, data["telemetri_verisi"], ui.response_telemetri_lbl)

            QApplication.processEvents()

    except Exception as e:
        ui.status_lbl.setText("BAĞLANTI KURULAMADI")
        ui.status_lbl.setStyleSheet("color: navy")
        ui.statusbar.showMessage("{}".format(str(e)))


ui.baudrate_connect_btn.clicked.connect(SystemInformation)

ui.arm_button.setEnabled(False)
ui.arm_button.clicked.connect(button_arm_clicked)

ui.disarm_button.setEnabled(False)
ui.disarm_button.clicked.connect(button_disarm_clicked)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    argv = sys.argv + ['--no-sandbox']  # sandbox modunu devre dışı bırakın
    # sandbox modunu devre dışı bırakın
    os.environ['QTWEBENGINE_DISABLE_SANDBOX'] = '1'
    ex = Ui_MainWindow()
    sys.exit(App.exec_())
