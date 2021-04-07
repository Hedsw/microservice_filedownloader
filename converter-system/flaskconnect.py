from flask import Flask, render_template

from trmmfiledownloader import trmmfiledownloader as trmm_downloader
from converter import starter as nc4convstarter

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def main():
    #return "<h1> Flask Web Framework Fully Connencted"
    return render_template('index.html', my_string="Successfully connected", my_list=[0,1,2,3,4,5])

@app.route('/filedownloader/v1', methods=['GET'])
def downloader():
    result = trmm_downloader()
    if result == True:
        return "<h1> Download is finished"
    else:
        return "<h1> Download is failed"

@app.route('/converter/v1', methods=['GET'])
def nc4convertergeotif():
    result = nc4convstarter()
    if result == True:
        return "<h1> Converter is finished"
    else:
        return "<h1> Converter is failed"

@app.route('/one-shot/v1', methods=['GET'])
def oneshot():
    covertResult = False
    result = trmm_downloader()
    if result == True:
        covertResult = nc4convstarter()
        if covertResult == True:
            return "<h1> trmm downlaod is finished and converter is finished"
    else:
        return "<h1> trmm_downlaoder is failed"
    
    return "H"

app.run(host='0.0.0.0', port=5002)

