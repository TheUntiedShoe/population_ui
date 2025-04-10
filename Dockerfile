FROM python:3.12.9

COPY . /population_ui

RUN pip install --no-cache-dir --upgrade -r /population_ui/requirements.txt \
    && pip install --no-cache-dir --upgrade -r /population_ui/tests/requirements.txt

WORKDIR /population_ui

CMD ["python", "src/Population.py"]