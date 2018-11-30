from functools import wraps

from flask import Flask, render_template, redirect, session, request, url_for
from webapp.cmds.docker_cmd import DockerCmd
from webapp import app
from webapp.login_decorate import LoginDecorate


def login_decorate(f):
    @wraps(f)
    def wrapped_decorate(*args, **kwargs):
        print(session.get('Username'))
        if not session.get('Username'):
            print('To Login')
            return redirect('/login')
        else:
            print('Do Action')
            return f(*args, **kwargs)

    return wrapped_decorate


@app.route('/')
@app.route('/index')
@LoginDecorate()
def index():
    # if session.get('Username'):
    return render_template('index.html', docker_server_list=DockerCmd().get_running_docker())


# else:
#     url = url_for('login')
#     return redirect(url)


@app.route('/container/<string:id>/<string:name>')
@LoginDecorate()
def container(id, name):
    docker = DockerCmd()
    all_devices = docker.get_all_devices()
    connected_device = docker.get_connected_devices(id)
    return render_template('device.html', container=id, name=name, all_devices=all_devices,
                           connected_device=connected_device)


@app.route('/container/start/<string:id>')
@LoginDecorate()
def start_container(id):
    print('Into Start')
    DockerCmd().start_container(id)
    return redirect('/')


@app.route('/container/stop/<string:id>')
@LoginDecorate()
def stop_container(id):
    DockerCmd().stop_container(id)
    return redirect('/')


@app.route('/connect/<string:container>/<string:device_id>')
@LoginDecorate()
def connect_device(container, device_id):
    DockerCmd().connect_device(container, device_id)
    return redirect('/')


@app.route('/disconnect/<string:container>/<string:device_id>')
@LoginDecorate()
def disconnect_device(container, device_id):
    DockerCmd().disconnect_device(container, device_id)
    return redirect('/')


@app.route('/container/logs/<string:container>')
@LoginDecorate()
def container_logs(container):
    out = DockerCmd().show_container_logs(container)
    return render_template('logs.html', logs=out)


@app.route('/login', methods=['POST', 'GET'], endpoint='login')
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        username = request.values.get('Username')
        password = request.values.get('Password')
        if username == 'admin' and password == 'strikingly':
            session['Username'] = username
            return redirect('/')
        else:
            return redirect('/login')
