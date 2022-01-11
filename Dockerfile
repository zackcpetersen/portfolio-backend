FROM python:3.7.4-alpine3.10

WORKDIR /app
RUN set -ex \
    && apk add --no-cache --virtual .build-deps postgresql-dev build-base \
#    && python -m venv /env \
    && /env/bin/pip install --upgrade pip \
#    && /env/bin/pip install --no-cache-dir -r /app/requirements.txt \
    && runDeps="$(scanelf --needed --nobanner --recursive /env \
        | awk '{ gsub(/,/, "\nso:", $2); print "so:" $2 }' \
        | sort -u \
        | xargs -r apk info --installed \
        | sort -u)" \
    && apk add --virtual rundeps $runDeps \
    && apk del .build-deps

ADD . .
RUN /env/bin/pip install --no-cache-dir -r requirements.txt

#ENV VIRTUAL_ENV /env
#ENV PATH /env/bin:$PATH

EXPOSE 8000