FROM python:3.6.5
ENV PATH /usr/local/bin:$PATH
ADD . /home/spider/python_graphql/
RUN pip install --no-cache-dir -r /home/spider/python_graphql/requirements.txt
WORKDIR /home/spider/python_graphql/
EXPOSE 31211/tcp
CMD ["python", "app.py"]