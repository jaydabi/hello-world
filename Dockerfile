FROM docker.pkg.github.com/jaydabi/garbageshell/garbageshell:latest
COPY app.py .
CMD ["gunicorn", "-b", "0.0.0.0:80", "-w", "1", "app:app"]
 
