From python:3.10

WORKDIR /app

# Copy requirements file
COPY . /app

#Install dependencies
RUN pip install -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable
ENV NAME World

# Run app.py when the container launches
CMD ["python", "chat.py"]


# docker build -t my-ml-model .
# docker run -p 4000:80 my-ml-model