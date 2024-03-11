---
template: blog_post.html
layout: post
title: "asyncio python"
alias: asyncio
tags:
  - python
  - asyncio
  - coroutine
term:
  - asyncio queues are designed to be similar to classes of the [queue](https://docs.python.org/3/library/queue.html#module-queue) module. Although asyncio queues are not thread-safe
  - they are designed to be used specifically in async/await code.
desc:
  - Each event loop contains a number of tasks
  - and every coroutine that is executing is doing so inside a task.
id: 6512ae22-02c0-42c1-bb30-97094aae783d
constructor: asyncio
def: asyncio.Queue(maxsize=0)
date: 2023-12-20
---

- History
  - greenlet
  - yield
  - python3.4 asyncio
    - `yield from asyncio.sleep(1)` `yield` allow switch to other coroutines if blocked on IO
  - python3.5 (async, await), 3.7(run)
    - await, async

      ```python
      import asyncio

      async def main():
          print('Hello ...')
          await asyncio.sleep(1)
          print('... World!')

      asyncio.run(main())
      ```
  - python 3.7 Task
  - python 3.11 TaskGroup
- Asynchronous Programming
  - event loop

    ```python
    import asyncio
    loop = asyncio.get_event_loop()
    loop.run_until_complete([task1, task2])
    ```
  - Basic of coroutines
  - ![A diagram showing the difference between subroutine and coroutine calling](https://bbc.github.io/cloudfit-public-docs/images/asyncio/SubVsCoRoutines.png){:height
    181, :width 346}
  - async
    - coroutine function and coroutine object

      ```python
      async def cotask():  # a coroutine task
        yield from asyncio.sleep(1)
      result = cotask()      # a coroutine object
      asyncio.get_event_loop().run_until_complete(cotask())  # run the task

      asyncio.run(cotask())  # python 3.7
      ```
  - await
    - If Python encounters an `await f()` expression in the scope of `g()`, `await` tells the event loop, “Suspend
      execution of `g()` until whatever I’m waiting on —the result of `f()` —is returned. In the meantime, go let
      something else run."
    - Waitable objects can be:
      - coroutine object
      - ((6512ae22-02c0-42c1-bb30-97094aae783d))
      - Task object
    - Two coroutines depends on each other

      ```python
      import asyncio
      async def others()
        await async.sleep(1)
      async def others1()
        await async.sleep(1)
      async def dep_others():
        await others()
        await other1()
      asyncio.run(dep_others())
      ```
  - Future
    - Future is an [awaitable](https://docs.python.org/3/glossary.html#term-awaitable) object. Coroutines can await on
      Future objects until they either have a result or an exception set, or until they are cancelled. A Future can be
      awaited multiple times and the result is same.
    - Typically Futures are used to enable low-level callback-based code (e.g. in protocols implemented using
      asyncio [transports](https://docs.python.org/3/library/asyncio-protocol.html#asyncio-transports-protocols)) to
      interoperate with high-level async/await code.
    - example

      ```python
      async def main():
      	loop = asyncio.get_running_loop() # current evloop
          future = loop.create_future()  # an empty future object/task
          await future # wait until future object/task finished in this case it will wait for ever
      asyncio.run(main())
      ```
    - Set a future

      ```python
      async def set_future(future):
      	await asyncio.sleep(1)
          future.set_result("666")
      async def main():
      	loop = asyncio.get_running_loop() # current evloop
          future = loop.create_future()  # an empty future object/task
          await loop.create_task(set_future(future))
          data = await future # wait until future object/task finished in this case it will wait for ever
          print(data) # 666
      asyncio.run(main())
      ```
    - concurrent.futures
      - The `concurrent.futures` module is part of the Python standard library starting from Python 3.2. It provides a
        high-level interface for asynchronously executing callable objects using threads or processes. It builds upon
        the concepts of threading and multiprocessing but offers a simpler, more abstracted interface.
        ThreadPoolExecutor example

        ```python
        import concurrent.futures

        # Define a simple function to be executed
        def task(n):
            return n ** 2

        # Create a ThreadPoolExecutor with maximum 2 worker threads
        with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
            # Submit tasks to the executor
            results = [executor.submit(task, i) for i in range(5)]

            # Retrieve results as they become available
            for future in concurrent.futures.as_completed(results):
                result = future.result()
                print(result)

        # Create a ProcessPoolExecutor with maximum 2 worker processes
        with concurrent.futures.ProcessPoolExecutor(max_workers=2) as executor:
            # Submit tasks to the executor
            results = [executor.submit(task, i) for i in range(5)]

            # Retrieve results as they become available
            for future in concurrent.futures.as_completed(results):
                result = future.result()
                print(result)
        ```
      - asyncio object are not thread safe and it should not use together with multithread object. Here is a hack to
        convert a concurrent future to a asyncio feature

        ```python
        import requests  # doesnt support asyncio feature
        import asyncio
        async def download(url):
        	loop = asyncio.get_event_loop()
            feautre=loop.run_in_executor(None, request.get, url)
            response = await future
            print(response)
        task = [download(url) for url in rul_list]
        loop = asyncio.get_event_loop()
        loop.run_until_complete(asyncio.wait(tasks))
        ```
        reference:
        [Executing code in thread or process pools](https://docs.python.org/3/library/asyncio-eventloop.html#id14)
      - `run_in_executor`
        - if a io request does not support asyncio API. It can be wrapped with `run_in_executor`
        - Above create a task The _executor_ argument should be
          an [concurrent.futures.Executor](https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.Executor) instance.
          The default executor is used if _executor_ is None.
      -
  - Tasks
    - Syntax

      ```python
      class asyncio.Task(coro, *, loop=None, name=None, context=None)
      ```
    - Tasks are used to run/schedule coroutines in event loops. If a coroutine awaits on a
      ((6512ae22-02c0-42c1-bb30-97094aae783d)) , the Task suspends the execution of the coroutine and waits for the
      completion of the Future. When the Future is /done/, the execution of the wrapped coroutine resumes.
    - If a coroutine awaits on a Future, the Task suspends the execution of the coroutine and waits for the completion
      of the Future. When the Future is _done_, the execution of the wrapped coroutine resumes.
    - Event loops use cooperative scheduling: an event loop runs one Task at a time. While a Task awaits for the
      completion of a Future, the event loop runs other Tasks, callbacks, or performs IO operations.
    - Use the high-level [[https://docs.python.org/3/library/asyncio-task.html#asyncio.create_task][]] function to
      create Tasks, or the
      low-level [[https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.create_task][]] or [[https://docs.python.org/3/library/asyncio-future.html#asyncio.ensure_future][]] functions.
      Manual instantiation of Tasks is discouraged. `create_task` is equal to create+scheduleToRun. You do not need to
      kickoff the task
    - The method `create_task` takes a coroutine object as a parameter and returns a `Task` object, which inherits from
      `asyncio.Future`. The call creates the task inside the event loop for the current thread, and starts the task
      executing at the beginning of the coroutine’s code-block. The returned future will be marked as `done()` only when
      the task has finished execution. As you might expect the return value of the coroutine’s code block is the
      `result()` which will be stored in the future object when it is finished (and if it raises then the exception will
      be caught and stored in the future).
    - Example:

      ```python
      import asyncio

      async def counter(name: str):
          for i in range(0, 100):
              print(f"{name}: {i!s}")
              await asyncio.sleep(0)

      async def main():
          tasks = []
          for n in range(0, 4):
              tasks.append(asyncio.create_task(counter(f"task{n}")))
          while True:
              tasks = [t for t in tasks if not t.done()]
              if len(tasks) == 0:
                  return
              await tasks[0]
          #another way to wait
          done, pending = await asyncio.wait(tasks, timeout=None)
          # and you can also try this
      	asyncio.run(asyncio.wait([counter('a'), counter('b')]))

      asyncio.run(main())
      ```
    - Video resource
      {{video(https://www.bilibili.com/video/BV1NA411g7yf?p=7&vd_source=3beef1bd86c86cf14f277319e599dab9)}}
  - Async Queue
  - Asynchronous Iterators
    - ((65137d16-a06a-40e4-b28e-5fa4474017d5))
    - Sample

      ```python
      class Ticker:
          """Yield numbers from 0 to `to` every `delay` seconds."""
          def __init__(self, delay, to):
              self.delay = delay
              self.i = 0
              self.to = to

          def __aiter__(self):
              return self

          async def __anext__(self):
              i = self.i
              if i >= self.to:
                  raise StopAsyncIteration
              self.i += 1
              if i:
                  await asyncio.sleep(self.delay)
              return i
      async def ticker(delay, to):
          """Yield numbers from 0 to `to` every `delay` seconds."""
          for i in range(to):
              yield i
              await asyncio.sleep(delay)
      ```
  - Asynchronous contex manager
    - async ctx mgr provide a context manager that can be suspended when entering and exiting. This is achieved by using
      `async with`. It is same way as `with` been used in other python expressions (e.g. file open)
    - How to use

      ```python
      # create and use an asynchronous context manager
      async with AsyncContextManager() as manager:
          ...
      # Same as:
      # create or enter the async context manager
      manager = await AsyncContextManager()
      try:
      	# ...
      finally:
      	# close or exit the context manager
      	await manager.close()
      ```
    - It must be used inside a coroutine `async def`
  - uvloop
    - uvloop [GitHub - MagicStack/uvloop: Ultra fast asyncio event loop.](https://github.com/magicstack/uvloop) is 2~3
      times faster than asyncio
    - Using uvloop

      ```python
      import asyncio
      import sys

      import uvloop

      async def main():
          # Main entry-point.
          ...

      if sys.version_info >= (3, 11):
          with asyncio.Runner(loop_factory=uvloop.new_event_loop) as runner:
              runner.run(main())
      else:
          uvloop.install()
          asyncio.run(main())
      ```
    - It used by asgi uvicorn
  - Practical examples
    - redis

      ```python
      import redis.asyncio as redis

      r = await redis.from_url("redis://localhost")
      async with r.pipeline(transaction=True) as pipe:
          ok1, ok2 = await (pipe.set("key1", "value1").set("key2", "value2").execute())
      assert ok1
      assert ok2

      # pubsub
      import asyncio
      import redis.asyncio as redis
      STOPWORD = "STOP"
      async def reader(channel: redis.client.PubSub):
          while True:
              message = await channel.get_message(ignore_subscribe_messages=True)
              if message is not None:
                  print(f"(Reader) Message Received: {message}")
                  if message["data"].decode() == STOPWORD:
                      print("(Reader) STOP")
                      break

      r = redis.from_url("redis://localhost")
      async with r.pubsub() as pubsub:
          await pubsub.subscribe("channel:1", "channel:2")

          future = asyncio.create_task(reader(pubsub))

          await r.publish("channel:1", "Hello")
          await r.publish("channel:2", "World")
          await r.publish("channel:1", STOPWORD)

          await future

      import asyncio_redis
      @asyncio.coroutine
      def example():
          # Create Redis connection
          connection = yield from asyncio_redis.Connection.create(host='127.0.0.1', port=6379)
          # Set a key
          yield from connection.set('my_key', 'my_value')
          # When finished, close the connection.
          connection.close()

      if __name__ == '__main__':
          loop = asyncio.get_event_loop()
          loop.run_until_complete(example())
      ```
    - Mysql with aiomysql

      ```python
      import asyncio
      import sqlalchemy as sa
      from aiomysql.sa import create_engine
      metadata = sa.MetaData()
      tbl = sa.Table('tbl', metadata,
                     sa.Column('id', sa.Integer, primary_key=True),
                     sa.Column('val', sa.String(255)))

      async def go(loop):
          engine = await create_engine(user='root', db='test_pymysql',
                                       host='127.0.0.1', password='', loop=loop)
          async with engine.acquire() as conn:
              await conn.execute(tbl.insert().values(val='abc'))
              await conn.execute(tbl.insert().values(val='xyz'))

              async for row in conn.execute(tbl.select()):
                  print(row.id, row.val)

          engine.close()
          await engine.wait_closed()

      loop = asyncio.get_event_loop()
      loop.run_until_complete(go(loop))
      ```
-
-
-
-
-
-
- References
  - [协程到底是咋回事？asyncio大佬给你彻底讲明白。](https://www.bilibili.com/video/BV11T4y117Jo)
  - [Python Asyncio Part 2 – Awaitables, Tasks, and Futures | cloudfit-public-docs](https://bbc.github.io/cloudfit-public-docs/asyncio/asyncio-part-2.html)
  - [Python Asyncio Part 3 – Asynchronous Context Managers and Asynchronous Iterators | cloudfit-public-docs](https://bbc.github.io/cloudfit-public-docs/asyncio/asyncio-part-3)
  - [Async IO in Python: A Complete Walkthrough – Real Python](https://realpython.com/async-io-python/)
-
-
