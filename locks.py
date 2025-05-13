import redis
import time

# Connect to your local Redis instance
client = redis.StrictRedis(host='localhost', port=6379, db=0)

# Create a lock object with a unique name
lock = client.lock(
    name='resource_lock',      # Unique lock name
    timeout=10,                # Lock expires after 10 seconds (prevents deadlocks)
    sleep=0.2,                 # Sleep 200ms between retries
    blocking=True,             # Block until the lock is acquired
    blocking_timeout=5,        # Wait up to 5 seconds to acquire the lock
    thread_local=True          # Lock token is stored per-thread
)

def critical_section():
    print("Performing critical section work...")
    time.sleep(3)
    print("Done with critical section.")

# Try to acquire the lock
if lock.acquire(blocking=True, blocking_timeout=5):
    try:
        print("Lock acquired!")
        critical_section()
    finally:
        lock.release()
        print("Lock released.")
else:
    print("Could not acquire lock.")

# This automatically acquires and releases the lock
with client.lock('resource_lock', timeout=10):
    print("Lock acquired via context manager.")
    critical_section()
print("Lock released via context manager.")

# Acquire the lock first
if lock.acquire():
    print("Lock acquired for extension demo.")
    # Extend the lock by 5 more seconds
    lock.extend(5)
    print("Lock extended by 5 seconds.")
    lock.release()
    print("Lock released after extension.")

def demo_redis_lock():
    lock = client.lock('resource_lock', timeout=5)
    print("Trying to acquire lock...")
    if lock.acquire(blocking=True, blocking_timeout=3):
        try:
            print("Lock acquired!")
            # Extend the lock by 5 seconds
            lock.extend(5)
            print("Lock extended by 5 seconds.")
            # Do some work
            critical_section()
        finally:
            lock.release()
            print("Lock released.")
    else:
        print("Could not acquire lock.")

    # Using context manager
    print("Trying context manager...")
    with client.lock('resource_lock', timeout=5):
        print("Lock acquired in context manager.")
        critical_section()
    print("Lock released in context manager.")

demo_redis_lock()
