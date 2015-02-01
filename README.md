# HelloWorldRedisDocker

Testing Docker multi-container app implementation using Fig and container linking.
Modified example from http://www.fig.sh

Assumptions:
- Docker and Fig is installed on the running host
- Docker installation instructions: https://docs.docker.com/installation/
- Fig installation instructions: http://www.fig.sh/install.html

Files:
- Dockerfile - Dockerfile to build web-tier container
- fig.yml - Fig file describing the multi-container app environment
- requirements.txt - File describing pip dependencies for web container build
- /code/HelloWorldRedis.py - 'Hello World' Python Flask web app that increments counter in Redis and prints it out

To start:
fig up

To access:
curl ($ip):5000

Note:
- Lowercase repo/encasing folder name is required to avoid an issue that causes the web container build from the Dockerfile to fail
  - Issue reference: https://github.com/docker/fig/issues/655
