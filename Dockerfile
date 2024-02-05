FROM bentoml/model-server:0.11.0-py310
MAINTAINER ersilia

RUN pip install rdkit
RUN pip install git+https://github.com/bp-kelley/descriptastorus
RUN pip install tqdm>=4.62.2
RUN pip install typed-argument-parser==1.6.1
RUN pip install scikit-learn
RUN pip install torch
RUN pip install pandas
RUN pip install tensorboardX==2.
RUN pip install hyperopt

WORKDIR /repo
COPY . /repo

WORKDIR /repo
COPY . /repo