from flask import Flask, render_template, request
from trmmfiledownloader import starter as trmm_downloader
from converter import starter as nc4convstarter
import time

app = Flask(__name__)
app.config["DEBUG"] = True
url = "test"

@app.route('/', methods=['GET'])
def main():
    #return "<h1> Flask Web Framework Fully Connencted"
    return render_template('index.html', my_string="Successfully connected", my_list=[0,1,2,3,4,5])

@app.route('/filedownloader/v1', methods=['GET'])
def downloader():
    result = trmm_downloader(url)
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
    result = trmm_downloader(url)
    #print("H?") http://0.0.0.0:5001/one-shot/v1
    print("TRMM Is done")
    time.sleep(0.5)
    if result == True:
        covertResult = nc4convstarter()
        if covertResult == True:
            return "<h1> trmm download is finished and converter is finished"
    else:
        return "<h1> trmm_downloader is failed"
    
    return "<h1> File Downloaded"

@app.route('/urldownloader', methods=['POST'])
def urldownloader():
    url = request.form.get('trmmfilepath')
    print(url)
    render_template('index.html') # Need to check
    # https://disc2.gesdisc.eosdis.nasa.gov/data/TRMM_RT/TRMM_3B42RT_Daily.7/2002/01/
    covertResult = False
    result = trmm_downloader(url)
    if result == True:
        covertResult = nc4convstarter()
        if covertResult == True:
            return "<h1> trmm download is finished and converter is finished"
    else:
        return "<h1> trmm_downloader is failed"
    
    return render_template('index.html')
    
app.run(host='0.0.0.0', port=5001)



