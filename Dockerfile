FROM debian:10
WORKDIR /application
ENV PYTHONPATH="$PYTHONPATH:/"
ADD https://github.com/xcollantes/test-world.git

CMD ["python3", "-m", "initiate"]
