# Student Portal

> A Django service that wraps **17+ academic-record APIs** into a single portal: graduation checks, grades, credit audits, honors/minors tracking, and more.

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-092E20?style=flat&logo=django&logoColor=white)

## What it does

Aggregates scattered academic endpoints behind one service so students (and the academic team) can query degree progress without touching the ERP directly:

- 🎓 Graduation check · mandatory requirements · 32-credits audit
- 📚 Course work, grades, incomplete grades, online-course rules
- 🏅 Honors, minors, economics major (core + electives)
- 🔐 IP & access info

## Quick start

```bash
git clone https://github.com/Aditi21372/Student_portal.git
cd Student_portal/student_portal
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt

cp .env.example .env    # set API_BASE_URL, DEBUG, ALLOWED_HOSTS
python manage.py migrate
python manage.py runserver
```

The application will be available at `http://127.0.0.1:8000/student_api/api/`

## Configuration

| Variable       | Default                  | Purpose                        |
|----------------|--------------------------|--------------------------------|
| `API_BASE_URL` | `http://localhost:3002…` | Upstream academic API server   |
| `DEBUG`        | `False`                  | Django debug mode              |
| `ALLOWED_HOSTS`|:                        | Comma-separated allowed hosts  |

## Development notes

- All endpoints live in `student_app/student_api/`
- Runs `setup.sh` / `setup.bat` for a one-command environment bootstrap

---

Built by [@Aditi21372](https://github.com/Aditi21372) · [More projects](https://github.com/Aditi21372?tab=repositories)
