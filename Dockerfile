FROM python:3.12

COPY . /population_ui

RUN pip install --no-cache-dir --upgrade -r /population_ui/requirements.txt \
    && pip install --no-cache-dir --upgrade -r /population_ui/tests/requirements.txt

WORKDIR /population_ui

EXPOSE 8501

CMD ["python3.12", "-m", "streamlit", "run", "--server.port", "8501", "./src/Population.py"]