import redis
from os import system
from time import sleep
system('clear')  # Clear the console for better readability

def get_redis_connection(host: str = 'localhost', port: int = 6379, db: int = 0, decode_responses: bool = True) -> redis.Redis:
    """
    Establishes a connection to the Redis server.

    Args:
        host (str): Redis server hostname.
        port (int): Redis server port.
        db (int): Redis database number.
        decode_responses (bool): If True, responses are decoded to strings.

    Returns:
        redis.Redis: Redis connection object.
    """
    return redis.Redis(host=host, port=port, db=db, decode_responses=decode_responses)

# STRINGS
def string_crud(r: redis.Redis, key: str, value: str) -> None:
    """
    Demonstrates CRUD operations for Redis Strings.

    Args:
        r (redis.Redis): Redis connection.
        key (str): Key name.
        value (str): Value to set.

    Returns:
        None
    """
    print("\n--------------------------------------------------")
    # Create/Update
    r.set(key, value)
    print(f"Set {key} = {value}")

    # Read
    val = r.get(key)
    print(f"Get {key} = {val}")

    # Update
    r.set(key, value + "_updated")
    print(f"Updated {key} = {r.get(key)}")

    # Delete
    r.delete(key)
    print(f"Deleted {key}, now get returns: {r.get(key)}")

# HASHES
def hash_crud(r: redis.Redis, key: str, mapping: dict) -> None:
    """
    Demonstrates CRUD operations for Redis Hashes.

    Args:
        r (redis.Redis): Redis connection.
        key (str): Hash key.
        mapping (dict): Dictionary to store.

    Returns:
        None
    """
    # Create/Update
    print("\n--------------------------------------------------")
    r.hset(key, mapping=mapping)
    print(f"Set hash {key}: {mapping}")

    # Read
    data = r.hgetall(key)
    print(f"Get hash {key}: {data}")

    # Update a field
    r.hset(key, "field1", "new_value")
    print(f"Updated hash {key}: {r.hgetall(key)}")

    # Delete a field
    r.hdel(key, "field2")
    print(f"Deleted field from hash {key}: {r.hgetall(key)}")

    # Delete entire hash
    r.delete(key)
    print(f"Deleted hash {key}, now get returns: {r.hgetall(key)}")

# LISTS
def list_crud(r: redis.Redis, key: str, values: list) -> None:
    """
    Demonstrates CRUD operations for Redis Lists.

    Args:
        r (redis.Redis): Redis connection.
        key (str): List key.
        values (list): List of values to store.

    Returns:
        None
    """
    print("\n--------------------------------------------------")
    # Create
    r.delete(key)  # Clear existing
    r.rpush(key, *values)
    print(f"Created list {key}: {r.lrange(key, 0, -1)}")

    # Read
    print(f"Read list {key}: {r.lrange(key, 0, -1)}")

    # Update (set index 0)
    r.lset(key, 0, "updated_value")
    print(f"Updated list {key}: {r.lrange(key, 0, -1)}")

    # Delete (pop)
    popped = r.lpop(key)
    print(f"Popped {popped} from {key}: {r.lrange(key, 0, -1)}")

    # Delete entire list
    r.delete(key)
    print(f"Deleted list {key}, now get returns: {r.lrange(key, 0, -1)}")

# SETS
def set_crud(r: redis.Redis, key: str, values: set) -> None:
    """
    Demonstrates CRUD operations for Redis Sets.

    Args:
        r (redis.Redis): Redis connection.
        key (str): Set key.
        values (set): Set of values to store.

    Returns:
        None
    """
    print("\n--------------------------------------------------")
    # Create
    r.delete(key)
    r.sadd(key, *values)
    print(f"Created set {key}: {r.smembers(key)}")

    # Read
    print(f"Read set {key}: {r.smembers(key)}")

    # Update (add new member)
    r.sadd(key, "new_member")
    print(f"Updated set {key}: {r.smembers(key)}")

    # Delete (remove member)
    r.srem(key, "new_member")
    print(f"Removed member from set {key}: {r.smembers(key)}")

    # Delete entire set
    r.delete(key)
    print(f"Deleted set {key}, now get returns: {r.smembers(key)}")

# SORTED SETS
def sorted_set_crud(r: redis.Redis, key: str, mapping: dict) -> None:
    """
    Demonstrates CRUD operations for Redis Sorted Sets.

    Args:
        r (redis.Redis): Redis connection.
        key (str): Sorted set key.
        mapping (dict): Dict of {member: score}.

    Returns:
        None
    """
    print("\n--------------------------------------------------")
    # Create
    r.delete(key)
    r.zadd(key, mapping)
    print(f"Created sorted set {key}: {r.zrange(key, 0, -1, withscores=True)}")

    # Read
    print(f"Read sorted set {key}: {r.zrange(key, 0, -1, withscores=True)}")

    # Update (change score)
    r.zincrby(key, 10, list(mapping.keys())[0])
    print(f"Updated sorted set {key}: {r.zrange(key, 0, -1, withscores=True)}")

    # Delete (remove member)
    r.zrem(key, list(mapping.keys())[0])
    print(f"Removed member from sorted set {key}: {r.zrange(key, 0, -1, withscores=True)}")

    # Delete entire sorted set
    r.delete(key)
    print(f"Deleted sorted set {key}, now get returns: {r.zrange(key, 0, -1, withscores=True)}")

# SET WITH EXPIRY
def set_with_expiry(r: redis.Redis, key: str, value: str, seconds: int) -> None:
    """
    Sets a key with an expiry time, prints its value, waits 5 seconds, and prints again.

    Args:
        r (redis.Redis): Redis connection.
        key (str): Key name.
        value (str): Value to set.
        seconds (int): Expiry time in seconds.

    Returns:
        None
    """
    print("\n--------------------------------------------------")
    r.set(key, value, ex=seconds)
    print(f"Set {key} = {r.get(key)} (expires in {seconds} seconds)")

    sleep(5)
    val_after_sleep = r.get(key)
    print(f"After 5 seconds, {key} = {val_after_sleep}")

# TRANSACTIONS
def transaction_example(r: redis.Redis) -> None:
    """
    Demonstrates a Redis transaction using pipelines.

    Args:
        r (redis.Redis): Redis connection.

    Returns:
        None
    """
    pipe = r.pipeline()
    pipe.set('trans:key1', 'value1')
    pipe.set('trans:key2', 'value2')
    pipe.get('trans:key1')
    pipe.get('trans:key2')
    responses = pipe.execute()
    print(responses)  # [True, 'Alice']
    print("Transaction executed: trans:key1 and trans:key2 set.")

# CACHE
def cache_example(r: redis.Redis, key: str, value: str, ttl: int = 60) -> None:
    """
    Simple cache set/get example.

    Args:
        r (redis.Redis): Redis connection.
        key (str): Cache key.
        value (str): Value to cache.
        ttl (int): Time to live in seconds.

    Returns:
        None
    """
    r.set(key, value, ex=ttl)
    print(f"Cached {key} for {ttl} seconds: {r.get(key)}")

def listen_to_topic(r: redis.Redis, topic: str) -> None:
    """
    Subscribes to a Redis topic and prints messages as they arrive.

    Args:
        r (redis.Redis): Redis connection.
        topic (str): The topic/channel to subscribe to.

    Returns:
        None
    """
    pubsub = r.pubsub()
    pubsub.subscribe(topic)
    print(f"Subscribed to topic '{topic}'. Waiting for messages...")
    for message in pubsub.listen():
        # Redis sends a subscription confirmation message first
        if message['type'] == 'message':
            print(f"Received message on '{topic}': {message['data']}") 

def publish_to_topic(r: redis.Redis, topic: str, message: str) -> None:
    """
    Publishes a message to a Redis topic.

    Args:
        r (redis.Redis): Redis connection.
        topic (str): The topic/channel to publish to.
        message (str): The message to send.

    Returns:
        None
    """
    r.publish(topic, message)
    print(f"Published message to '{topic}': {message}")            


r = get_redis_connection()
print(r.ping())  # Should print True if the connection is successful
# string_crud(r, "example_key", "example_value")
# hash_crud(r, "example_hash", {"field1": "value1", "field2": "value2"})
# list_crud(r, "example_list", ["value1", "value2", "value3"])
# set_crud(r, "example_set", {"value1", "value2", "value3"})
# sorted_set_crud(r, "example_sorted_set", {"member1": 1, "member3": 3, "member2": 2})
# set_with_expiry(r, "example_expiry_key", "example_value", 5)  # Set with expiry of 5 seconds
# transaction_example(r)  # Uncomment to test transactions
# cache_example(r, "example_cache_key", "example_cache_value", 10)  # Cache for 10 seconds
# publish_to_topic(r, "example_topic", "Hello, Redis!")  # Publish a message to a topic
# listen_to_topic(r, "example_topic")  # Uncomment to listen to a topic