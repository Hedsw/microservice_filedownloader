from flask import Flask, render_template, request
from trmmfiledownloader import starter as trmm_downloader
from converter import starter as nc4convstarter
from trmmfiledownloader import xml_trmm_rt_file as xml_trmm_rt_file
import time

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def main():
    return render_template('index.html', my_string="Successfully connected", my_list=[0,1,2,3,4,5])

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

@app.route('/schedular', methods =['GET', 'POST'])
def schedular():
    url = xml_trmm_rt_file()
    
    if request.method == 'POST':
        period = request.form['periodfrom']
        period1 = request.form['periodto']
        lists = request.form['lists']
        yearfrom, monthfrom, yearto, monthto = parse(period, period1)
        #print(yearfrom, monthfrom, yearto, monthto)
        #url = url + "/" + lists + "/" + yearfrom + "/" + monthfrom
        
        months = []
        trmmsignal = False
        for i in range(int(monthfrom), int(monthto)+1):
            url = xml_trmm_rt_file()
            if i < 10:
                j = "0" + str(i)
                url = url + "/" + lists + "/" + yearfrom + "/" + j
            else:
                url = url + "/" + lists + "/" + yearfrom + "/" + str(i)
            #print(url)
            trmmsignal = trmm_downloader(url)
        if trmmsignal == True:
            nc4convstarter()
            return render_template('index.html')

    elif request.method == 'GET':
        return render_template('index.html')

def parse(period1, period2):
    tmp = period1.split('-')
    tmp2 = period2.split('-')
    # year and month return
    #print(tmp[0],tmp[1])
    return tmp[0], tmp[1], tmp2[0], tmp2[1]

app.run(host='0.0.0.0', port=5001)


