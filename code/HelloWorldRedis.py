from flask import Flask
from redis import Redis
import os

app = Flask(__name__)
redis = Redis(host="redis", port=6379)

@app.route('/')

def hello():
  redis.incr('count')
  return 'Hello World! My count now is: %s' "\n" % redis.get('count')

if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)