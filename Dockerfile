FROM python:3.9-slim
WORKDIR /app
RUN pip install matplotlib numpy pandas datetime scipy faker
COPY . . 
ENTRYPOINT ["python"]
CMD ["urun_analiz.py"]