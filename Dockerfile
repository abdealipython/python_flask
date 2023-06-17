FROM python:3.8
RUN pip install flask flask-mysql
WORKDIR /app
COPY uat_app.py .
COPY templates . 
ENV FLASK_APP=uat_app.py
EXPOSE 5000 
CMD ["flask", "run", "--host=0.0.0.0"]
