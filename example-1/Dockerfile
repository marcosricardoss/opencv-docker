FROM marcosricardoss/opencv-python

RUN pip install --upgrade pip
RUN pip install numpy

WORKDIR /usr/src/app
ADD requirements.txt ./requirements.txt
RUN pip install -r requirements.txt