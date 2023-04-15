import json
import redis

redis_client = redis.StrictRedis(host='localhost', port=6379, db=1)

def publish_data_on_redis(json_data:dict, channel_name:str):
    redis_client.publish(channel_name, json.dumps(json_data))