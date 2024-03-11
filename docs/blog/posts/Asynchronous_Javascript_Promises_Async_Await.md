---
layout: post
template: blog_post.html
title: "Asynchronous Javascript"
author: "Ray"
header-style: text
template: blog_post.html
tags:
  - Docker
date: 2024-02-20
---

- Promise
  - The **~~Promise~~** object represents the eventual completion (or failure) of an asynchronous operation and its
    resulting value. A **~~Promise~~** is a proxy for a value not necessarily known when the promise is created. It
    allows you to associate handlers with an asynchronous action's eventual success value or failure reason. This lets
    asynchronous methods return values like synchronous methods: instead of immediately returning the final value, the
    asynchronous method returns a /promise/ to supply the value at some point in the future.
    ```javascript
    let promise = new Promise(function (resolve, reject) {
      resolve("done");

      reject(new Error("…")); // ignored
      setTimeout(() => resolve("…")); // ignored
    });
    ```
  - Essentially, a promise is a returned object to which you attach callbacks, instead of passing callbacks into a
    function. Imagine a function, ~~createAudioFileAsync()~~, which asynchronously generates a sound file given a
    configuration record and two callback functions: one called if the audio file is successfully created, and the other
    called if an error occurs.
  - A ~~Promise~~ is in one of these states:
    - _pending_: initial state, neither fulfilled nor rejected.
    - _fulfilled_: meaning that the operation was completed successfully.
    - _rejected_: meaning that the operation failed.
    - ![Flowchart showing how the Promise state transitions between pending, fulfilled, and rejected via then/catch handlers.](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/promises.png)
      - A pending promise can become either fulfilled or rejected. If fulfilled, the "on fulfillment" handler, or first
        parameter of the ((64e03d90-eea8-4b2f-8c4d-ed3ba949fa39)) method, is executed and carries out further
        asynchronous actions. If rejected, the error handler, either passed as the second parameter of the then() method
        or as the sole parameter of the catch() method, gets executed
  - then id:: 64e03d90-eea8-4b2f-8c4d-ed3ba949fa39
    ```javascript
    promise.then(
      function (result) {/* handle a successful result */},
      function (error) {/* handle an error */},
    );
    ```
    ```javascript
    const myPromise = new Promise((resolve, reject) => {
      setTimeout(() => {
        resolve("foo");
      }, 300);
    });

    myPromise
      .then(handleFulfilledA, handleRejectedA)
      .then(handleFulfilledB, handleRejectedB)
      .then(handleFulfilledC, handleRejectedC);

    let promise2 = new Promise(function (resolve, reject) {
      // after 1 second signal that the job is finished with an error
      setTimeout(() => reject(new Error("Whoops!")), 1000);
    });

    let promise = new Promise(function (resolve, reject) {
      setTimeout(() => resolve("done!"), 1000);
    });

    // resolve runs the first function in .then
    promise.then(
      (result) => alert(result), // shows "done!" after 1 second
      (error) => alert(error), // doesn't run
    );

    promise = new Promise(function (resolve, reject) {
      setTimeout(() => reject(new Error("Whoops!")), 1000);
    });

    // reject runs the second function in .then
    promise.then(
      (result) => alert(result), // doesn't run
      (error) => alert(error), // shows "Error: Whoops!" after 1 second
    );
    ```
    - This shows a common pattern of using `Promise`. Create a new promise object and use `then` to execute callbacks,
      aka ((64e026ee-513e-4459-a698-6ad09de202d7))
    -
  - [Chained Promises](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise#chained_promises)
    id:: 64e026ee-513e-4459-a698-6ad09de202d7
    - The
      methods [[https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/then][]], [[https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/catch][]],
      and [[https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/finally][]] are
      used to associate further action with a promise that becomes settled. As these methods return promises, they can
      be chained.
    - while the value `then()` returns is not a promise (can be string, number etc), the `.then()` method itself wraps
      that value in a resolved promise, allowing for further chaining.
    - The ~~.then()~~ method takes up to two arguments;
      - a callback function for the fulfilled case of the promise
      - a callback function for the rejected case.
      - Each ~~.then()~~ returns a newly generated promise object, which can optionally be used for chaining; for
        example:
        ```javascript
        new Promise(function (resolve, reject) {
          setTimeout(() => resolve(1), 1000); // (*)
        }).then(function (result) { // (**)
          alert(result); // 1
          return result * 2;
        }).then(function (result) { // (***)  result*2=2
          alert(result); // 2
          return result * 2;
        }).then(function (result) {
          alert(result); // 4
          return result * 2;
        });
        ```
      - Then can return a promise.When you return a value from a `.then()` callback, the next `.then()` in the chain
        receives that value as its argument. If you return a promise (or thenable) from a `.then()` callback, the next
        `.then()` waits for that promise to resolve and receives its resolved value.
      - Example2, Load json form web/local

        ```javascript
        fetch("/article/promise-chaining/user.json")
          .then((response) => response.json())
          .then((user) => fetch(`https://api.github.com/users/${user.name}`))
          .then((response) => response.json())
          .then((githubUser) =>
            new Promise(function (resolve, reject) { // (*)
              let img = document.createElement("img");
              img.src = githubUser.avatar_url;
              img.className = "promise-avatar-example";
              document.body.append(img);

              setTimeout(() => {
                img.remove();
                resolve(githubUser); // (**)
              }, 3000);
            })
          )
          // triggers after 3 seconds
          .then((githubUser) => alert(`Finished showing ${githubUser.name}`));
        ```
  - catch() method
    - use ~~.catch(errorHandlingFunction)~~ to handle errors. The `then` between error throw and `catch` will not be
      executed, but `then` after `catch will be executed`. To make sure skip all `then` put `catch` at end. `catch` set
      the promise to pending state
    - cache can be used catch error any place in the chain.
      ```javascript
      let promise = new Promise((resolve, reject) => {
        setTimeout(() => reject(new Error("Whoops!")), 1000);
      });

      // .catch(f) is the same as promise.then(null, f)
      promise.catch(alert); // shows "Error: Whoops!" after 1 second
      ```
  - finally()
    - Used to cleanup / finalizing The call ~~.finally(f)~~ is similar to ~~.then(f, f)~~ in the sense that ~~f~~ runs
      always, when the promise is settled: be it resolve or reject.
    - the ~~finally~~ handler has no arguments, and the promise outcome is handled by the next handler.
    - A ~~finally~~ handler “passes through” the result or error to the next suitable handler.
    - For instance, here the result is passed through ~~finally~~ to ~~then~~:
    - [promise](https://javascript.info/promise-basics#)
      ```javascript
      new Promise((resolve, reject) => {
        setTimeout(() => resolve("value"), 2000);
      })
        .finally(() => alert("Promise ready")) // triggers first
        .then((result) => alert(result)); // <-- .then shows "value"
      ```
    - As you can see, the ~~value~~ returned by the first promise is passed through ~~finally~~ to the next ~~then~~.
    - That’s very convenient, because ~~finally~~ is not meant to process a promise result. As said, it’s a place to do
      generic cleanup, no matter what the outcome was.
    - And here’s an example of an error, for us to see how it’s passed through ~~finally~~ to ~~catch~~:
      ```javascript
      new Promise((resolve, reject) => {
        throw new Error("error");
      })
        .finally(() => alert("Promise ready")) // triggers first
        .catch((err) => alert(err)); // <-- .catch shows the error
      ```
    - A ~~finally~~ handler also shouldn’t return anything. If it does, the returned value is silently ignored.
    - The only exception to this rule is when a ~~finally~~ handler throws an error. Then this error goes to the next
      handler, instead of any previous outcome.
  - Promise states and `finally`
    - PENDING => Promise is doing work, neither then() nor catch() executes at this moment
    - RESOLVED > Promise is resolved > then() executes
    - REJECTED > Promise was rejected > catch() executes
    - When you have another then() block after a catch() or then() block, the promise re-enters PENDING mode (keep in
      mind: then() and catch() always return a new promise - either not resolving to anything or resolving to what you
      return inside of then()). Only if there are no more then() blocks left, it enters a new, final mode: SETTLED.
    - Once SETTLED, you can use a special block - finally() - to do final cleanup work. finally() is reached no matter
      if you resolved or rejected before.
    - Here's an example:
      ```javascript
      somePromiseCreatingCode()
        .then((firstResult) => {
          return "done with first promise";
        })
        .catch((err) => {
          // would handle any errors thrown before
          // implicitly returns a new promise - just like then()
        })
        .finally(() => {
          // the promise is settled now - finally() will NOT return a new promise!
          // you can do final cleanup work here
        });
      ```
      You don't have to add a finally() block (indeed we haven't in the lectures).
- Async/await
  - special syntax to work with promises in a more comfortable fashion.
  - Async
    - `async` ensures that the function returns a promise, and wraps non-promises in
      ```javascript
      async function f() {
        return 1;
        // same as return Promise.resolve(1);
      }

      f().then(alert); // 1
      ```
  - Await
    - The keyword ~~await~~ makes JavaScript wait until that promise settles and returns its result.
      `await`只能放在~async~函数里面，如果不放在里面，代码会直接报错，不能运行。它会暂停代码在该行上，直到 promise
      完成，然后返回结果值。在暂停的同时，其他正在等待执行的代码就有机会执行了。这个行为不会耗费任何 CPU 资源，因为
      JavaScript 引擎可以同时处理其他任务：执行其他脚本，处理事件等。
      ```javascript
      async function hello() {
        return greeting = await Promise.resolve("Hello");
      }
      hello().then(alert); // Hello

      async function foo() {
        await 1;
      }
      // same as
      function foo() {
        return Promise.resolve(1).then(() => undefined);
      }
      ```
    - compare async/await and promise
      ```javascript
      function loadJson(url) {
        return fetch(url)
          .then((response) => response.json());
      }

      function loadGithubUser(name) {
        return loadJson(`https://api.github.com/users/${name}`);
      }

      function showAvatar(githubUser) {
        return new Promise(function (resolve, reject) {
          let img = document.createElement("img");
          img.src = githubUser.avatar_url;
          img.className = "promise-avatar-example";
          document.body.append(img);

          setTimeout(() => {
            img.remove();
            resolve(githubUser);
          }, 3000);
        });
      }

      // 使用它们：
      loadJson("/article/promise-chaining/user.json")
        .then((user) => loadGithubUser(user.name))
        .then(showAvatar)
        .then((githubUser) => alert(`Finished showing ${githubUser.name}`));
      // ...
      async function showAvatar() {
        // 读取我们的 JSON
        let response = await fetch("/article/promise-chaining/user.json");
        let user = await response.json();
        // 读取 github 用户信息
        let githubResponse = await fetch(`https://api.github.com/users/${user.name}`);
        let githubUser = await githubResponse.json();
        // 显示头像
        let img = document.createElement("img");
        img.src = githubUser.avatar_url;
        img.className = "promise-avatar-example";
        document.body.append(img);
        // 等待 3 秒
        await new Promise((resolve, reject) => setTimeout(resolve, 3000));
        img.remove();
        return githubUser;
      }

      showAvatar();

      // coffee
      fetch("coffee.jpg")
        .then((response) => response.blob())
        .then((myBlob) => {
          let objectURL = URL.createObjectURL(myBlob);
          let image = document.createElement("img");
          image.src = objectURL;
          document.body.appendChild(image);
        })
        .catch((e) => {
          console.log(e.message);
        });

      // write with async/await
      async function myFetch() {
        let response = await fetch("coffee.jpg");
        let myBlob = await response.blob();

        let objectURL = URL.createObjectURL(myBlob);
        let image = document.createElement("img");
        image.src = objectURL;
        document.body.appendChild(image);
      }

      myFetch().catch((e) => {
        console.log(e.message);
      });

      // split await
      async function myFetch() {
        let response = await fetch("coffee.jpg");
        return await response.blob();
      }

      myFetch().then((blob) => {
        let objectURL = URL.createObjectURL(blob);
        let image = document.createElement("img");
        image.src = objectURL;
        document.body.appendChild(image);
      }).catch((e) => console.log(e));
      ```
  - AsyncGenerator
    - The **AsyncGenerator** object is returned by
      an [async generator function](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/async_function*) and
      it conforms to both
      the [async iterable protocol and the async iterator protocol](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols#the_async_iterator_and_async_iterable_protocols).
    - Async generator methods always
      yield [[https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise][]] objects.
    - `AsyncGenerator` is a subclass of the
      hidden [[https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/AsyncIterator][]] class.
    - JavaScript Demo: Expressions - Async Function Asterisk

      ```javascript
      async function* foo() {
        yield await Promise.resolve("a");
        yield await Promise.resolve("b");
        yield await Promise.resolve("c");
      }

      let str = "";

      async function generate() {
        for await (const val of foo()) {
          str = str + val;
        }
        console.log(str);
      }

      generate();
      // Expected output: "abc"
      ```
    - Constractor
      - The ~~AsyncGenerator~~ constructor is not available globally. Instances of ~~AsyncGenerator~~ must be returned
        from [async generator functions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/async_function*)

        ```javascript
        async function* createAsyncGenerator() {
          yield await Promise.resolve(1);
          yield await Promise.resolve(2);
          yield await Promise.resolve(3);
        }
        const asyncGen = createAsyncGenerator();
        asyncGen.next().then((res) => console.log(res.value)); // 1
        ```
- Loading javascript **defer** and **async**
  - Defer: tell the browser to load the js code asynchronously but not parse it until html is fully loaded. The order of
    multiple defered js code is guaranteed
  - async: tell the browser to download and parse the js asynchronously, used to load library that does not need the
    html body been parse correctly. The order can not be guaranteed and depends on when the js is downloaded
    ```html
    <head>
      <title>Defer and async</title>
      <script src="assert/scripts/vendor.js" async> </script>
      <script src="assert/scripts/app.js" defer> </script>
    </head>
    ```
