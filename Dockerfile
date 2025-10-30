FROM bentoml/model-server:0.11.0-py310
MAINTAINER ersilia
RUN pip install rdkit==2023.9.4
RUN pip install git+https://github.com/bp-kelley/descriptastorus@da9760932ab9a78b116bc697795dd9e1798f087a
RUN pip install tqdm==4.66.1
RUN pip install typed-argument-parser==1.6.1
RUN pip install scikit-learn==1.4.0
RUN pip install torch==2.2.0
RUN pip install pandas==2.2.0
RUN pip install tensorboardX==2.0
RUN pip install hyperopt==0.2.7
RUN pip install protobuf==3.20.0
#---dependencyes from descriptastorus
RUN pip install packaging==24.2
RUN pip install pandas-flavor==0.6.0
RUN pip install xarray==2024.3.0
RUN conda install -c conda-forge xorg-libxrender=0.9.12
RUN conda install -c conda-forge xorg-libxtst=1.2.5
WORKDIR /repo
COPY . /repo
