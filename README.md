# Flask-Nginx Docker depoly for Domitory system

## Using this project

This project is a template. We recommend the following workflow:

- Clone this repository.
- Start the Docker container:

```
$ docker build -t <TAG NAME> .
$ docker run -p 80:80 -d <IMAGE ID>.
```

- Verify that `<IP address of Docker machine>/flask-nginx` works, i.e. that Nginx is properly delegating to flask-nginx.
- Move your code into the flask-nginx application, renaming things as needed.

#### Developing locally

Nothing changes when you develop locally. Just use:

```
$ python run.py
```
