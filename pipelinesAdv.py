import redis

r = redis.Redis(decode_responses=True)
pipe = r.pipeline()

# Batch set multiple keys
for i in range(1, 6):
    pipe.set(f"user:{i}", f"name_{i}")

# Batch get multiple keys
for i in range(1, 6):
    pipe.get(f"user:{i}")

results = pipe.execute()
print(results)  # [True, True, True, True, True, 'name_1', 'name_2', ...]


pipe = r.pipeline()
pipe.incr("counter:1")
pipe.incr("counter:2")
pipe.incr("counter:3")
pipe.get("counter:1")
pipe.get("counter:2")
pipe.get("counter:3")
results = pipe.execute()
print(results)  # [new_value1, new_value2, new_value3, new_value1, new_value2, new_value3]


pipe = r.pipeline()
pipe.multi()  # Optional, starts a transaction block
pipe.set("balance:alice", 100)
pipe.set("balance:bob", 50)
pipe.incrby("balance:alice", -10)
pipe.incrby("balance:bob", 10)
pipe.get("balance:alice")
pipe.get("balance:bob")
results = pipe.execute()
print(results)
