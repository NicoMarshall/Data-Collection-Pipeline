FROM python:3.8-slim-buster
COPY waterstones_scraping.py . 
COPY requirements.txt . 
RUN pip install -r requirements.txt
RUN  apt-get -y update \
  && apt-get install -y wget \
  && apt-get install -y gnupg \
  && apt-get install -y curl
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \ 
  && echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list
RUN apt-get -y update \
  && apt-get install -y google-chrome-stable \
  && CHROMEDRIVER_VERSION=`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE`\
  && curl -sS -o /tmp/chromedriver_linux64.zip http://chromedriver.storage.googleapis.com/$CHROMEDRIVER_VERSION/chromedriver_linux64.zip
RUN apt-get install -yqq unzip && unzip /tmp/chromedriver_linux64.zip chromedriver -d /usr/local/bin/
CMD ["python", "waterstones_scraping.py"]

