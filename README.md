# HelloWorldRedisDocker

Testing Docker multi-container app implementation, modified example from http://www.fig.sh

Assumptions:
- Docker Fig is installed on the running host
- Fig installation instructions: http://www.fig.sh/install.html

Files:
- Dockerfile - Dockerfile to build web-tier container
- fig.yml - Fig file describing the multi-container app environment
- requirements.txt - File describing pip dependencies for web container build
- /code/HelloWorldRedis.py - 'Hello World' Python Flask web app that increments counter in Redis and prints it out

To run:
fig up

Note:
- Lowercase repo/encasing folder name is required to avoid an issue that causes the web container build from the Dockerfile to fail
  - Issue reference: https://github.com/docker/fig/issues/655
