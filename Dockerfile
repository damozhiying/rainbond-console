FROM goodrain.me/debian:jessie_122901
MAINTAINER qisy@goodrain.com

RUN echo "Asia/Shanghai" > /etc/timezone;dpkg-reconfigure -f noninteractive tzdata

RUN apt-get update \
    && apt-get install -y curl wget python2.7 python2.7-dev libzmq3 libzmq3-dev python-zmq libmysqlclient-dev python-yaml python-crypto python-mysqldb


RUN curl https://bootstrap.pypa.io/get-pip.py | python -
RUN apt-get install -y libmemcached-dev python-pylibmc libjpeg-dev python-pil

ENV REGION_TAG console
ENV PORT 5000
ENV WORK_DIR /app

EXPOSE $PORT

RUN mkdir -pv $WORK_DIR

RUN echo "upgrad packages UPDATE_POINT"
ADD requirements.txt $WORK_DIR/requirements.txt
RUN pip install -r $WORK_DIR/requirements.txt -i https://pypi.doubanio.com/simple

COPY . $WORK_DIR
RUN python -c "import compileall;compileall.compile_dir('$WORK_DIR')" \
    && find $WORK_DIR -name '*.py' -type f -delete \
    && find $WORK_DIR/goodrain_web/conf -type f ! -name '__init__.pyc' -delete

RUN rm -f $WORK_DIR/{Dockerfile, release.sh, struct.txt, entrypoint.sh}
ADD entrypoint.sh /entrypoint.sh

USER rain
WORKDIR $WORK_DIR
ENTRYPOINT ["/entrypoint.sh"]