from flask import Flask, request, jsonify
from flask_caching import Cache
import redis
import json

app = Flask(__name__)

cache = Cache(app, config={
    'CACHE_TYPE': 'RedisCache',
    'CACHE_REDIS_URL': 'redis://redis:6379/0'
})

redis_client = redis.StrictRedis(host='redis', port=6379, db=0)

def get_cache_key(user_id):
    return f"user_cache:{user_id}"

@app.route('/get-data', methods=['GET'])
def get_user_data():
    user_id = request.args.get('user_id')
    cache_key = get_cache_key(user_id)

    if (cached := redis_client.get(cache_key)):
        return jsonify({"source": "cache", "data": json.loads(cached)})

    db_data = {"records": [f"record_{i}" for i in range(100000)]}
    redis_client.set(cache_key, json.dumps(db_data), ex=300)
    return jsonify({"source": "db", "data": db_data})

@app.route('/update-data', methods=['POST'])
def update_user_data():
    user_id = request.args.get('user_id')
    new_data = request.json.get("data")
    cache_key = get_cache_key(user_id)
    redis_client.set(cache_key, json.dumps(new_data), ex=300)
    return jsonify({"message": "Cache updated", "cache_key": cache_key})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
