---
title: 'Friday Q&A 2013-08-16: Let''s Build Dispatch Groups'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2013-08-16-lets-build-dispatch-groups.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:a1f209eeb687030b'
translated: false
---

> 原文：[Friday Q&A 2013-08-16: Let's Build Dispatch Groups](https://www.mikeash.com/pyblog/friday-qa-2013-08-16-lets-build-dispatch-groups.html)　·　mikeash.com Friday Q&A

Posted at 2013-08-17 02:19 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [Friday Q&A 2013-08-30: Model Serialization With Property Lists](https://www.mikeash.com/pyblog/friday-qa-2013-08-30-model-serialization-with-property-lists.html)  
Previous article: [Friday Q&A 2013-08-02: Type-Safe Scalars with Single-Field Structs](https://www.mikeash.com/pyblog/friday-qa-2013-08-02-type-safe-scalars-with-single-field-structs.html)  
Tags: [fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [gcd](https://www.mikeash.com/pyblog/?tag=gcd) [letsbuild](https://www.mikeash.com/pyblog/?tag=letsbuild)

Friday Q&A 2013-08-16: Let's Build Dispatch Groups

by [Mike Ash](https://www.mikeash.com/)

**Overview**  
Dispatch groups provide four basic operations:

1. Enter, to indicate that a task has begun.
2. Exit, to indicate that a task has completed.
3. Notify, which invokes a block when every enter gets a corresponding exit.
4. Wait, which is like notify, but synchronous.

You can use this to spin off a bunch of parallel operations and wait for them to complete:

```
    dispatch_group_t group = dispatch_group_create();
    for(int i = 0; i < 100; i++)
    {
        dispatch_group_enter(group);
        DoAsyncWorkWithCompletionBlock(^{
            dispatch_group_leave(group);
        });
    }
    dispatch_group_wait(group, DISPATCH_TIME_FOREVER);
```

You can also use it to asynchronously invoke a block when they all complete:

```
    dispatch_group_t group = dispatch_group_create();
    for(int i = 0; i < 100; i++)
    {
        dispatch_group_enter(group);
        DoAsyncWorkWithCompletionBlock(^{
            dispatch_group_leave(group);
        });
    }
    dispatch_group_notify(group, dispatch_get_main_queue(), ^{
        UpdateUI();
    });
```

Given that it's part of GCD and we're talking about asynchronous operations, it should go without saying that a major feature of dispatch groups is that all operations are thread safe.

**Code**  
As usual, I have posted the full code for my reimplementation on GitHub here:

[https://github.com/mikeash/MADispatchGroup](https://github.com/mikeash/MADispatchGroup)

**Interface**  
The API for `ma_dispatch_group` closely mirrors that of `dispatch_group`:

```
    typedef struct ma_dispatch_group_internal *ma_dispatch_group_t;

    ma_dispatch_group_t ma_dispatch_group_create(void);
    void ma_dispatch_group_destroy(ma_dispatch_group_t group);
    void ma_dispatch_group_enter(ma_dispatch_group_t group);
    void ma_dispatch_group_leave(ma_dispatch_group_t group);
    void ma_dispatch_group_notify(ma_dispatch_group_t group, void (^block)(void));
    void ma_dispatch_group_wait(ma_dispatch_group_t group);
```

There are a few differences from the `dispatch_group` interface:

1. A `ma_dispatch_group_t` is not a dispatch object, so it doesn't use retain/release semantics, instead using a single `destroy` function to clean one up.
2. The `dispatch_group_async` functions are missing. These are just simple wrappers around `enter`, `leave`, and `dispatch_async`, so not all that important.
3. The `notify` function doesn't take a dispatch queue, and instead invokes the block immediately in the context of the last piece of code to call `leave`. It's trivial to wrap the block in a `dispatch_async`, so this is no major change.
4. The `wait` function doesn't take a timeout. This simplifies the code considerably while still illustrating the overall concept.

**Fields**  
The `struct ma_dispatch_group_internal` contains two fields, a counter and an action block:

```
    struct ma_dispatch_group_internal {
        uint32_t counter;
        void (^action)(void);
    };
```

The counter keeps track of how many times `enter` has been called without a corresponding `exit`. The action block is the action set by the `notify` function.

**Creation and Deletion**  
Creating a new group is extremely simple. Just allocate a chunk of memory, using `calloc` to ensure it's zeroed:

```
    ma_dispatch_group_t ma_dispatch_group_create(void)
    {
        ma_dispatch_group_t group = calloc(1, sizeof *group);
        return group;
    }
```

Destroying a group is likewise simple. I assume that any action set with `notify` always fires before a group is destroyed, and that the action block is destroyed as part of that. As such, there's no cleanup required in `destroy` beyond simply calling `free`:

```
    void ma_dispatch_group_destroy(ma_dispatch_group_t group)
    {
        free(group);
    }
```

**Enter**  
The implementation of `ma_dispatch_group_enter` is extremely simple. It's just an atomic increment, using an atomic compiler builtin:

```
    void ma_dispatch_group_enter(ma_dispatch_group_t group)
    {
        __sync_fetch_and_add(&group->counter, 1);
    }
```

Using the atomic builtin ensures that this is thread safe. The implementation of `ma_dispatch_group_leave` is a bit more complex. It first performs an atomic decrement:

```
    void ma_dispatch_group_leave(ma_dispatch_group_t group)
    {
        uint32_t newCounterValue = __sync_sub_and_fetch(&group->counter, 1);
```

The `__sync_sub_and_fetch` builtin first performs an atomic decrement, then returns the new value of the counter. If this was the last `leave` call, then `newCounterValue` will contain `0`, and it's time to execute the group's notification action.

```
        if(newCounterValue == 0)
        {
```

The action may not exist yet, for example if all `enter` calls were balanced with a `leave` before the call to `notify`, so check for that:

```
            if(group->action)
            {
```

If an action has been set, execute it:

```
                group->action();
```

Once it returns, destroy the block and set the action to `NULL`:

```
                Block_release(group->action);
                group->action = NULL;
            }
        }
    }
```

**Notify**  
The implementation of `ma_dispatch_group_notify` is interesting, but ultimately extremely simple. Conceptually, there are two completely separate cases to consider:

1. There are still pending `enter` calls that have not been balanced with a `leave`. In that case, set the group's `action` block.
2. All `enter` calls have been balanced with a `leave`. In that case, execute the block immediately.

Seems straightforward enough. However, a simple implementation of the first case creates a race condition. Consider the following sequence of events:

1. The `notify` function checks `count` and sees that it is non-zero.
2. The pending actions call `leave` and decrease the count to zero.
3. The action that decreases the count to zero checks the action. No action is set, so it does nothing.
4. The `notify` function sets the group's action.
5. The action never runs, because no code is left to run it.

There's an elegant solution that both fixes this race condition and consolidates both separate cases into a single code path. The solution is to wrap the assignment of the action in an `enter`/`leave` pair. This effectively eliminates the second case, since there's always at least one unbalanced `enter` when assigning the action. This also solves the potential race condition, since the assignment occurs before at least one of the pending `leave` calls. Here's what the function looks like:

```
    void ma_dispatch_group_notify(ma_dispatch_group_t group, void (^block)(void))
    {
        ma_dispatch_group_enter(group);
        group->action = Block_copy(block);
        ma_dispatch_group_leave(group);
    }
```

**Wait**  
The implementation of `ma_dispatch_group_wait` is simple in concept, although a bit complex in code. It uses `ma_dispatch_group_notify` for most of the work. The idea is simply to call `notify` with a block that notes when it gets run, then wait for that block to run. The trick is how to efficiently wait.

It's possible to not bother with efficiency and just poll. For example, this is a valid, albeit dumb, implementation:

```
    void ma_dispatch_group_wait(ma_dispatch_group_t group)
    {
        __block volatile int done = 0;
        ma_dispatch_group_notify(group, ^{
            done = 1;
        });

        while(!done)
            /* nothing */;
    }
```

However, spinning the CPU at 100% for no reason is a bad idea, so let's try to do better.

There are many different ways to implement this. I chose to use `pthread` condition variables. A condition variable pairs with a mutex and allows one thread to block and wait for another thread to signal it. In the signaling thread, you do:

```
    pthread_mutex_lock(&lock);
    // make your change
    pthread_cond_broadcast(&cond); // or _signal
    pthread_mutex_unlock(&lock);
```

The lock ensures that the change is atomic with respect to the waiting thread. The `cond_broadcast` call then informs any waiting threads that it's time to wake up.

In the waiting thread, you do:

```
    pthread_mutex_lock(&lock);
    while(!condition)
        pthread_cond_wait(&cond);
    pthread_mutex_unlock(&lock);
```

The lock insures that the check for the condition is atomic with respect to the signaling thread. The `while` loop serves two purposes. First, it's possible that the condition was already set beforehand. In this case, the `while` avoids calling `pthread_cond_wait`, which would end up waiting forever since the signal had already occurred previously. Second, it's possible for `pthread_cond_wait` to return even when nothing has signaled the condition variable. This is known as [spurious wakeup](http://en.wikipedia.org/wiki/Spurious_wakeup) and is a consequence of how condition variables are implemented internally. In the event of spurious wakeup, the while loop ensures that the waiting thread doesn't exit prematurely.

The `ma_dispatch_group_wait` function first declares and initializes a mutex and a condition variable:

```
    void ma_dispatch_group_wait(ma_dispatch_group_t group)
    {
        pthread_mutex_t mutex;
        pthread_cond_t cond;

        pthread_mutex_init(&mutex, NULL);
        pthread_cond_init(&cond, NULL);
```

Next, it grabs pointers to these variables:

```
        pthread_mutex_t *mutexPtr = &mutex;
        pthread_cond_t *condPtr = &cond;
```

This is done to work around an unfortunate collision with blocks. If the block passed to `notify` were to capture `mutex` and `cond` directly, they would be copied. These data types don't tolerate being copied. Specifically, `pthread_mutex_t` has some internal alignment checks, at least on some implementations. Rather than figure out how to force the compiler to meet the library's alignment needs, `pthread_mutex_t` is set up with some extra storage internally, and then the proper alignment for the internal storage is figured out when it's initialized. In essence, there's an internal field that has (at least) two possible positions, and the position is decided by `init`. When the variable is copied, that alignment may no longer be correct, and this can lead to a crash. By instead capturing pointers to these variables, the copy and potential crash are avoided.

A `done` variable is also declared to track when the block actually executes:

```
        __block int done = 0;
```

Now `notify` is called with a block that acquires the lock, sets `done`, notifies the waiting thread, and releases the lock:

```
        ma_dispatch_group_notify(group, ^{
            pthread_mutex_lock(mutexPtr);
            done = 1;
            pthread_cond_broadcast(condPtr);
            pthread_mutex_unlock(mutexPtr);
        });
```

With that in place, the function waits for `done` to be set:

```
        pthread_mutex_lock(mutexPtr);
        while(!done)
            pthread_cond_wait(condPtr, mutexPtr);
        pthread_mutex_unlock(mutexPtr);
    }
```

That's everything!

**Conclusion**  
Dispatch groups are an extremely useful API that makes it easy to coordinate multiple asynchronous actions and execute followup code once they all complete. The API is bare, but highly functional. Such a useful facility is relatively simple to implement. With the right idea, a little code can go a long way.

That's it for today. Come back next time for more wacky adventures. Friday Q&A is driven by reader suggestions so, in the meantime, please [send in your ideas for topics to cover](mailto:mikeash.com).

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

Comments:

---

[Comments RSS feed for this page](https://www.mikeash.com/commentsrss.py?page=pyblog/friday-qa-2013-08-16-lets-build-dispatch-groups.html)

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.

Code syntax highlighting thanks to [Pygments](http://pygments.org/).
