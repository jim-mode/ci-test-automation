FROM cimg/python:3.8

    ## Install Packages & Google Chrome
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | sudo apt-key add - \
        && sudo sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list' \
        && sudo apt -y update \
        && sudo apt install -yqq unzip default-jre google-chrome-stable \
        && sudo rm -rf /var/lib/apt/lists/*

    # Install Web Driver
RUN wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE`/chromedriver_linux64.zip \
        && sudo unzip /tmp/chromedriver.zip chromedriver -d /usr/local/bin/ \
        && rm /tmp/chromedriver.zip

    # Download Allure
RUN wget -O /tmp/allure.zip https://github.com/allure-framework/allure2/releases/download/2.17.1/allure-2.17.1.zip \
        && unzip /tmp/allure.zip -d /tmp/ \
        && mkdir -p /home/circleci/allure/ \
        && mv /tmp/allure-2.*/* /home/circleci/allure/ \
        && rm -rf /tmp/allure*
