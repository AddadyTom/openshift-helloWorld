import os
import socket
from uuid import uuid4
from flask import Flask

app = Flask(__name__)


@app.route('/hello')
def availability():
    pod_name = socket.gethostname()
    pod_ip = socket.gethostbyname(pod_name)
    return 'hello user... this is openshift pod named: {}, on IP: {}'.format(pod_name, pod_ip)


@app.route('/costum/<command>')
def costum_command(command):
    output_file = 'temp_output_{id}.txt'.format(id=uuid4().hex)
    os.system('{command} > {output_file}'.format(command=command, output_file=output_file))
    with open(output_file, 'r') as result_file:
        result = result_file.read()
    os.remove(output_file)
    return result
    

if __name__ == '__main__':
    app.run(port=8080)
