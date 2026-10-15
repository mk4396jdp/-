from flask import Flask, request, render_template, send_file
import os
from werkzeug.utils import secure_filename
import csv
from datetime import datetime
from omr.omr import score_paper

UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), '..', 'uploads')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    files = request.files.getlist('files')
    if not files:
        return '没有上传文件', 400
    results_all = []
    time_prefix = datetime.now().strftime('%Y%m%d_%H%M%S')
    out_dir = os.path.join(UPLOAD_FOLDER, time_prefix)
    os.makedirs(out_dir, exist_ok=True)
    csv_rows = []
    for f in files:
        filename = secure_filename(f.filename)
        if filename == '': continue
        path = os.path.join(out_dir, filename)
        f.save(path)
        annotated_path = os.path.join(out_dir, 'annot_' + filename)
        try:
            res = score_paper(path, save_annotated_path=annotated_path)
        except Exception as e:
            res = {'error': str(e), 'file': filename}
            results_all.append(res)
            csv_rows.append([filename, 'ERROR', str(e)])
            continue
        entry = {'file': filename, 'total': res['total'], 'max': res['max'], 'per_question': res['per_question'], 'annotated': os.path.relpath(annotated_path, start=os.path.dirname(__file__)), 'saved_path': os.path.relpath(path, start=os.path.dirname(__file__))}
        results_all.append(entry)
        perq_str = ';'.join([f"{p['q']}:{p['choice']}:{p['status']}" for p in res['per_question']])
        csv_rows.append([filename, res['total'], res['max'], perq_str])
    csv_path = os.path.join(out_dir, 'results.csv')
    with open(csv_path, 'w', newline='', encoding='utf-8') as cf:
        writer = csv.writer(cf)
        writer.writerow(['file', 'score', 'max', 'per_question'])
        writer.writerows(csv_rows)
    return render_template('index.html', results=results_all, csv_path=os.path.relpath(csv_path, start=os.path.dirname(__file__)))

@app.route('/download/<path:csv_relpath>')
def download(csv_relpath):
    base = os.path.dirname(__file__)
    abs_path = os.path.join(base, csv_relpath)
    if not os.path.exists(abs_path):
        return '文件不存在', 404
    return send_file(abs_path, as_attachment=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
