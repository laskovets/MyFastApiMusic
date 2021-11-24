FROM python:3.8
COPY . ~/MyFastApiMusic
WORKDIR "~/MyFastApiMusic/app"
RUN pip install -r ../requirements.txt
ENTRYPOINT [ "python" ]
CMD ["main.py"]
