FROM python

EXPOSE 8000

WORKDIR /usr/local/image_board

COPY dist/requirements.txt .
copy cfg.json .
COPY ImageBoard ./ImageBoard
COPY manage.py .

RUN pip install -r requirements.txt

RUN python3 manage.py migrate
RUN python3 manage.py collectstatic --noinput

RUN groupadd -r image_board
RUN useradd -r -g image_board -s /sbin/nologin -d /usr/local/image_board image_board

USER image_board:image_board

CMD ["gunicorn", "ImageBoard.wsgi", "--bind", "0.0.0.0:8000"]
