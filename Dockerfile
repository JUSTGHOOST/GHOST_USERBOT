FROM theteamultroid/ultroid:main

# set timezone
ENV TZ=Africa/Cairo
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

#clonning repo 
RUN git clone https://github.com/Mahmoud7100/GHOST_USERBOT /root/sbb_b
#working directory 
WORKDIR /root/sbb_b

# Install requirements
RUN pip3 install --no-cache-dir -r requirements.txt

ENV PATH="/home/sbb_b/bin:$PATH"

CMD ["python3","-m","sbb_b"]
