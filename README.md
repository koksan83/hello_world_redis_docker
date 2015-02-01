# HelloWorldRedisDocker

Assumptions:
- Docker Fig is installed on the running host
- Fig installation instructions please refer to: http://www.fig.sh/install.html

Testing Docker multi-container app implementation, modified example from http://www.fig.sh

To run:
fig up

Note:
- Lowercase repo/encasing folder name is required to avoid an issue that causes the web container build from the Dockerfile to fail
  - Issue reference: https://github.com/docker/fig/issues/655
