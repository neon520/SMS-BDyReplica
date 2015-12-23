FROM ubuntu
RUN mkdir /home/SMS_BD
COPY ./ /home/SMS_BD
RUN cd /home/SMS_BD && chmod a+x docker_run
RUN cd /home/SMS_BD && make install
CMD cd /home/SMS_BD/SMS_BD && python __main__.py
