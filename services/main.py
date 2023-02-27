from celery import Celery
from flask import Flask, jsonify

app = Flask(__name__)
celery_app = Celery(__name__ + '_app', broker='redis://192.168.18.206:14000/0', backend='redis://192.168.18.206:14000/0')


@app.route("/sum/<param1>/<param2>", methods=["GET"])
def calc(param1, param2):
    params = dict(param1=param1, param2=param2)
    result = celery_app.signature('task_sum', kwargs=params, ).delay().get()
    return jsonify(result)


if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0', threaded=True)
