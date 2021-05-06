import json
import time
from datetime import datetime
from flask import make_response, redirect, render_template, request, url_for, Response
from . import APP_SERVER_BLUEPRINT, ERROR_HANDLER_BLUEPRINT
from app.app_db.devices_database import DevicesDatabase
from app.app_server.read_temperature import ReadTemperature

DB = DevicesDatabase('Devices.db')


def get_temperature(device_data) -> str:
    """
    This method call class ReadTemperature(this class save and convert temperature from bytes to string) to get
    temperature near by device.
    """
    return ReadTemperature(device_ip=device_data[0][1], device_port=device_data[0][2],
                           ssh_login=device_data[0][3],
                           ssh_password=device_data[0][4]).read_temperature()


@APP_SERVER_BLUEPRINT.route('/', methods=['GET', 'POST'])
def index():
    """
    Start Page
    """
    return render_template('index.html'), 200


@APP_SERVER_BLUEPRINT.route('/get_device_data_from_db', methods=['POST'])
def get_device_data_from_db():
    """
    This method get all device data from database. After getting data app will try to get temperature near by device.
    """
    global device_data
    device_ip = request.form['device_ip']
    device_data = DB.select_data_from_chosen_device(device_ip)
    return redirect(url_for('.show_chart'))


@APP_SERVER_BLUEPRINT.route('/show_chart', methods=['GET'])
def show_chart():
    """
    This method render template with the current temperature.
    """
    return render_template('show_chart.html'), 200


@APP_SERVER_BLUEPRINT.route('/convert_chart_data')
def convert_chart_data():
    """
    This method converting temperature and date to json format. This method also updating temperature and date each
    ten seconds.
    """

    def jsonify_data():
        while True:
            json_data = json.dumps(
                {'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                 'value': get_temperature(device_data)})
            yield f"data:{json_data}\n\n"
            time.sleep(device_data[0][5])

    return Response(jsonify_data(), mimetype='text/event-stream')


@ERROR_HANDLER_BLUEPRINT.errorhandler(400)
def bad_request():
    """
    Bad request.
    """
    return make_response(render_template("400.html", title='400', content='Page not found.'), 400)


@ERROR_HANDLER_BLUEPRINT.errorhandler(404)
def page_not_found(not_found):
    """
    Page not found.
    """
    return make_response(render_template('404.html', title='404', content='Page not found.'), 404)


@ERROR_HANDLER_BLUEPRINT.errorhandler(500)
def server_error():
    """
    Internal server error.
    """
    return make_response(render_template("500.html", title='500', content='Internal server error.'), 500)
