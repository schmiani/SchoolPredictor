from flask import Flask
app = Flask(__name__)

from flask import render_template
from flask import jsonify
import MySQLdb as mdb

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")


@app.route("/schools_json")
def schools_json():
    db= mdb.connect('localhost', 'root', 'password', 'school');
    with db:
        cur = db.cursor()
        cur.execute("SELECT School, School_Type, 2013_14_GRADE_PRED, \
            2012_13_GRADE, 2011_12_GRADE, 2010_11_GRADE, 2009_10_GRADE, 2008_09_GRADE, 2007_08_GRADE, 2006_07_GRADE, \
            2012_13_PERF_PERC, 2011_12_PERF_PERC, 2010_11_PERF_PERC, 2009_10_PERF_PERC, 2008_09_PERF_PERC, 2007_08_PERF_PERC, 2006_07_PERF_PERC \
            FROM Final ORDER BY School")
        query_results = cur.fetchall()
    schools = []
    for result in query_results:
        schools.append(dict(school=result[0], schooltype=result[1], grade2014=result[2], \
            grade2013=result[3], grade2012=result[4], grade2011=result[5], grade2010=result[6], grade2009=result[7], grade2008=result[8], grade2007=result[9],\
            perc2013=result[10], perc2012=result[11], perc2011=result[12], perc2010=result[13], perc2009=result[14], perc2008=result[15], perc2007=result[16])), 
    return jsonify(dict(schools=schools))


if __name__ == "__main__":
    app.run(host='0.0.0.0')
