FROM python:3

RUN apt-get update

# 音声ファイルをpythonで扱うために入れる必要がある
RUN apt-get -y install libsndfile1

RUN mkdir /workdir
WORKDIR /workdir
ADD . /workdir

# 音声分析用のファイルをpipでインストール
RUN pip install --upgrade pip
RUN pip install numba==0.48.0
RUN pip install librosa
