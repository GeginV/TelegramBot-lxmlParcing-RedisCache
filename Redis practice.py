import redis

redis_cloud = redis.Redis(
    host='redis-15498.c259.us-central1-2.gce.cloud.redislabs.com',
    port=15498,
    password='lujMHFFTVIu6oPdlGtD3AI8AmyZL98Pf'
)

print("I can: write, read, delete, stop")

while True:
    action = input('What do I do? : ')
    if action == 'write':
        name = input('Name? : ')
        phone = input("Phone? : ")
        redis_cloud.set(name, phone)
    elif action == 'read':
        name = input('Whose number are you looking for? : ')
        phone = redis_cloud.get(name)
        if phone:
            print(f"{name}'s phone is {str(phone)}")
        else:
            print(f"{name} not found")
    elif action == 'delete':
        name = input('Whom to delete? : ')
        phone = redis_cloud.delete(name)
        if phone:
            print(f"{name}'s phone was deleted")
        else:
            print(f"{name} not found")
    elif action == 'stop':
        break
