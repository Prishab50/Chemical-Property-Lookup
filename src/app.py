from flask import Flask, render_template, request, jsonify
from models import filter_cmpd_info
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', result=None, compound=None)


@app.route('/health')
def health():
    return jsonify({"status": "ok"}), 200


@app.route('/lookup', methods=['POST'])
def lookup():
    result = {}
    compound = request.form.get('compound')
    query = request.form.getlist('query')

    if not query:
        result = filter_cmpd_info(compound=compound)
    else:
        result = filter_cmpd_info(compound=compound, query=query)

    return render_template('index.html', compound=compound, result=result)

if __name__ == '__main__':

    app.run(host='0.0.0.0', port=port=int(os.environ.get("PORT", 5000))
