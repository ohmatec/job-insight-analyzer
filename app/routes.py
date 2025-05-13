from flask import Blueprint, render_template

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/test-api')
def test_api():
    from .services.job_api import fetch_jobs
    data = fetch_jobs("Python Developer", "Bangkok")
    # แสดงผลบางส่วนในหน้าเว็บเพื่อทดสอบ
    jobs = data.get('results', [])[:5]
    return "<br>".join([job.get('title') for job in jobs])
