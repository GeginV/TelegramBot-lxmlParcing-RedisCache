import redis
import json

redis_cloud = redis.Redis(
    host='redis-15498.c259.us-central1-2.gce.cloud.redislabs.com',
    port=15498,
    password='lujMHFFTVIu6oPdlGtD3AI8AmyZL98Pf'
)

redis_cloud.set('var1','test string')
print(redis_cloud.get('var1'))

dict1 = {'key1': 'value1', 'key2': 'value2'}

redis_cloud.set('dict1', json.dumps(dict1))

converted_dict = json.loads(redis_cloud.get('dict1'))

print(type(converted_dict))
print(converted_dict)

redis_cloud.delete('var1')
redis_cloud.delete('dict1')

print(redis_cloud.get('var1'))
print(redis_cloud.get('dict1'))