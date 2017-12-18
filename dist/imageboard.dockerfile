FROM python:3

EXPOSE 8000

WORKDIR /usr/local/imageboard

COPY dist/requirements.txt .
COPY ImageBoard ./ImageBoard
COPY board ./board
COPY users ./users
COPY templates ./templates
COPY manage.py .

RUN pip install --no-cache-dir -r requirements.txt

RUN groupadd -r imageboard
RUN useradd -r -g imageboard -s /sbin/nologin -d /usr/local/imageboard imageboard

RUN chown -R imageboard:imageboard ../imageboard

USER imageboard:imageboard

CMD ["gunicorn", "ImageBoard.wsgi", "--access-logfile", "-", "-w", "4", "--bind", "0.0.0.0:8000"]
