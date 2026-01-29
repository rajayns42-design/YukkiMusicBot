FROM nikolaik/python-nodejs:python3.11-nodejs19
RUN rm -f /etc/apt/sources.list.d/yarn.list && \
    printf "deb http://deb.debian.org/debian bullseye main\ndeb http://deb.debian.org/debian bullseye-updates main\ndeb http://security.debian.org/debian-security bullseye-security main" > /etc/apt/sources.list && \
    apt-get update && \
    apt-get install -y --no-install-recommends ffmpeg aria2 && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*
COPY . /app/
WORKDIR /app/
RUN python3 -m pip install --no-cache-dir --upgrade pip
RUN pip3 install --no-cache-dir --upgrade -r requirements.txt
CMD bash start
