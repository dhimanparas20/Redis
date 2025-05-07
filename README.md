---

# Redis Python Demo (`main.py`)

Welcome! This project is a hands-on, beginner-friendly guide to using **Redis** with Python. It demonstrates all the most common Redis data types and features, including CRUD operations, transactions, caching, and pub/sub messaging.

## Table of Contents

- [What is Redis?](#what-is-redis)
- [What Does This Script Do?](#what-does-this-script-do)
- [Prerequisites](#prerequisites)
- [Setup Instructions](#setup-instructions)
- [How to Use](#how-to-use)
- [Feature Demos](#feature-demos)
  - [1. Strings](#1-strings)
  - [2. Hashes](#2-hashes)
  - [3. Lists](#3-lists)
  - [4. Sets](#4-sets)
  - [5. Sorted Sets](#5-sorted-sets)
  - [6. Key Expiry](#6-key-expiry)
  - [7. Transactions](#7-transactions)
  - [8. Caching](#8-caching)
  - [9. Pub/Sub (Publish/Subscribe)](#9-pubsub-publishsubscribe)
- [Tips and Troubleshooting](#tips-and-troubleshooting)
- [Learning More](#learning-more)

---

## What is Redis?

**Redis** is a super-fast, in-memory key-value data store. It’s often used for caching, real-time analytics, message brokering, and more. Redis supports several data types: strings, hashes, lists, sets, and sorted sets.

---

## What Does This Script Do?

This script (`main.py`) is a **learning playground** for Redis in Python. It provides easy-to-understand functions for:

- Creating, reading, updating, and deleting (CRUD) data in Redis
- Exploring all major Redis data types
- Using advanced features like key expiry, transactions, caching, and pub/sub messaging

Each function is well-documented and prints out what it’s doing, so you can follow along and learn by example.

---

## Prerequisites

- **Python 3.7+** installed
- **Redis server** running locally (default: `localhost:6379`)
- **Python packages:**  
  - `redis` (install with `pip install redis`)

---

## Setup Instructions

1. **Install Redis**

   - On Linux/macOS:  
     ```bash
     sudo apt install redis-server
     # or
     brew install redis
     ```
   - On Windows:  
     Download from [https://github.com/microsoftarchive/redis/releases](https://github.com/microsoftarchive/redis/releases)

   - Start Redis server:  
     ```bash
     redis-server
     ```

2. **Install Python dependencies**

   ```bash
   uv add redis
   ```

3. **Clone or Download this Repository**

   Place `main.py` in your working directory.

---

## How to Use

1. **Open `main.py` in your code editor.**

2. **Uncomment** the function calls at the bottom of the file to try different demos.  
   For example, to try the string demo, uncomment:
   ```python
   string_crud(r, "example_key", "example_value")
   ```

3. **Run the script:**
   ```bash
   uv run python main.py
   ```

4. **Watch the output!**  
   The script prints each step and the results, so you can see exactly what’s happening in Redis.

---

## Feature Demos

Below are the features you can try. Uncomment the relevant lines at the bottom of `main.py` to run each demo.

### 1. Strings

```python
string_crud(r, "example_key", "example_value")
```
- Shows how to set, get, update, and delete a string value in Redis.

---

### 2. Hashes

```python
hash_crud(r, "example_hash", {"field1": "value1", "field2": "value2"})
```
- Demonstrates storing and manipulating a dictionary-like structure.

---

### 3. Lists

```python
list_crud(r, "example_list", ["value1", "value2", "value3"])
```
- Shows how to work with ordered lists (push, pop, update, delete).

---

### 4. Sets

```python
set_crud(r, "example_set", {"value1", "value2", "value3"})
```
- Demonstrates adding, removing, and reading unique values.

---

### 5. Sorted Sets

```python
sorted_set_crud(r, "example_sorted_set", {"member1": 1, "member3": 3, "member2": 2})
```
- Shows how to store items with a score and retrieve them in order.

---

### 6. Key Expiry

```python
set_with_expiry(r, "example_expiry_key", "example_value", 5)
```
- Sets a key with an expiry time (in seconds), prints its value, waits 5 seconds, and prints again to show it has expired.

---

### 7. Transactions

```python
transaction_example(r)
```
- Demonstrates how to execute multiple commands atomically using a Redis transaction (pipeline).

---

### 8. Caching

```python
cache_example(r, "example_cache_key", "example_cache_value", 10)
```
- Shows how to use Redis as a cache with a time-to-live (TTL).

---

### 9. Pub/Sub (Publish/Subscribe)

**To try Pub/Sub, open two terminals:**

- **Terminal 1 (Subscriber):**
  ```python
  listen_to_topic(r, "example_topic")
  ```
  This will wait and print any messages published to `"example_topic"`.

- **Terminal 2 (Publisher):**
  ```python
  publish_to_topic(r, "example_topic", "Hello, Redis!")
  ```
  This sends a message to the topic. The subscriber will print it.

---

## Tips and Troubleshooting

- **Redis server not running?**  
  Make sure you started Redis with `redis-server`.

- **Connection errors?**  
  Check that your Redis server is running on `localhost:6379` or update the connection parameters in `get_redis_connection()`.

- **Want to try multiple features?**  
  Uncomment multiple function calls, or run them one at a time for clarity.

- **Clearing the console:**  
  The script clears the console at the start for readability. Remove or comment out `system('clear')` if you don’t want this.

---

## Learning More

- [Redis Official Documentation](https://redis.io/documentation)
- [redis-py Python Client Docs](https://redis-py.readthedocs.io/en/stable/)
- [Awesome Redis Use Cases](https://redis.io/use-cases/)

---

**Happy Learning!**  
Feel free to experiment, break things, and learn how Redis works with Python.  
If you have questions or want to add more features, just edit `main.py` and try new things!
