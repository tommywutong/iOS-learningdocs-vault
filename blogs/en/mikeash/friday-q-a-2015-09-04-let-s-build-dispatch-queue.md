---
title: 'Friday Q&A 2015-09-04: Let''s Build dispatch_queue'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2015-09-04-lets-build-dispatch_queue.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:1f8bd4561ee19432'
translated: false
---

> 原文：[Friday Q&A 2015-09-04: Let's Build dispatch_queue](https://www.mikeash.com/pyblog/friday-qa-2015-09-04-lets-build-dispatch_queue.html)　·　mikeash.com Friday Q&A

Posted at 2015-09-04 13:22 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [Friday Q&A 2015-09-18: Building a Gear Warning System](https://www.mikeash.com/pyblog/friday-qa-2015-09-18-building-a-gear-warning-system.html)  
Previous article: [Friday Q&A 2015-08-14: An Xcode Plugin for Unsmoothed Text](https://www.mikeash.com/pyblog/friday-qa-2015-08-14-an-xcode-plugin-for-unsmoothed-text.html)  
Tags: [fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [gcd](https://www.mikeash.com/pyblog/?tag=gcd) [letsbuild](https://www.mikeash.com/pyblog/?tag=letsbuild)

Friday Q&A 2015-09-04: Let's Build dispatch_queue

by [Mike Ash](https://www.mikeash.com/)

**Overview**  
A dispatch queue is a queue of jobs backed by a global thread pool. Typically, jobs submitted to a queue are executed asynchronously on a background thread. All threads share a single pool of background threads, which makes the system more efficient.

That is the essence of the API which I'll replicate. There are a number of fancy features provided by GCD which I'll ignore for the sake of simplicity. For example, the number of threads in the global pool scales up and down with the amount of work to be done and the CPU utilization of the system. If you have a bunch of jobs hitting the CPU hard and you submit another job, GCD will avoid creating another worker thread for it, because it's already running at 100% and another thread will just make things less efficient. I'll skip over this and just use a hardcoded limit on the number of threads. I'll skip other fancy features like target queues and barriers on concurrent queues as well.

The goal is to concentrate on the essence of dispatch queues: they can be serial or concurrent, they can dispatch jobs synchronously or asynchronously, and they're backed by a shared global thread pool.

**Code**  
As usual, the code for today's article is available on GitHub here:

[https://github.com/mikeash/MADispatchQueue](https://github.com/mikeash/MADispatchQueue)

If you'd like to follow along as you read, or just want to explore on your own, you can find it all there.

**Interface**  
GCD is a C API. Although GCD objects have turned into Objective-C objects on more recent OS releases, the API remains pure C (plus Apple's blocks extension). This is great for a low-level API, and GCD presents a remarkably clean interface, but for my own purposes I prefer to write my reimplementation in Objective-C.

The Objective-C class is called `MADispatchQueue` and it only has four calls:

1. A method for getting a shared global queue. GCD has multiple global queues with different priorities, but we'll just have one for simplicity.
2. An initializer which can create the queue as either concurrent or serial.
3. An async dispatch call.
4. A sync dispatch call.

Here's the interface declaration:

```
    @interface MADispatchQueue : NSObject

    + (MADispatchQueue *)globalQueue;

    - (id)initSerial: (BOOL)serial;

    - (void)dispatchAsync: (dispatch_block_t)block;
    - (void)dispatchSync: (dispatch_block_t)block;

    @end
```

The goal, then, is to implement these methods to actually do what they say they do.

**Thread Pool Interface**  
The thread pool that backs the queues has a simpler interface. It will do the grunt work of actually running the submitted jobs. The queues will then be responsible for submitting their enqueued jobs at the right time to maintain the queue's guarantees.

The thread pool has a single job: submit some work to be run. Accordingly, its interface has just a single method:

```
    @interface MAThreadPool : NSObject

    - (void)addBlock: (dispatch_block_t)block;

    @end
```

Since this is the core, let's implement it first.

**Thread Pool Implementation**  
Let's look at instance variables first. The thread pool is going to be accessed from multiple threads, both internally and externally, and so needs to be thread safe. While GCD goes out of its way to use fast atomic operations whenever possible, for my conceptual rebuilding I'm going to stick with good old-fashioned locks. I need the ability to wait and signal on this lock, not just enforce mutual exclusion, so I'm using an `NSCondition` rather than a plain `NSLock`. If you're not familiar with it, `NSCondition` is basically a lock and a single condition variable wrapped into one:

```
    NSCondition *_lock;
```

In order to know when to spin up new worker threads, I need to know how many threads are in the pool, how many are actually busy doing work, and the maximum number of threads I can have:

```
    NSUInteger _threadCount;
    NSUInteger _activeThreadCount;
    NSUInteger _threadCountLimit;
```

Finally, there's a list of blocks to execute. This is an `NSMutableArray`, treated as a queue by appending new blocks to the end and removing whem from the front:

```
    NSMutableArray *_blocks;
```

Initialization is simple. Initialize the lock, initialize the blocks array, and set the thread count limit to an arbitrarily-chosen 128:

```
    - (id)init {
        if((self = [super init])) {
            _lock = [[NSCondition alloc] init];
            _blocks = [[NSMutableArray alloc] init];
            _threadCountLimit = 128;
        }
        return self;
    }
```

The worker threads run a simple infinite loop. As long as the blocks array is empty, it will wait. Once a block is available, it will dequeue it from the array and execute it. When doing so, it will increment the active thread count, then decrement it again when done. Let's get started:

```
    - (void)workerThreadLoop: (id)ignore {
```

The first thing it does is acquire the lock. Note that it does this _before_ the loop begins. The reason will become clear at the end of the loop:

```
        [_lock lock];
```

Now loop forever:

```
        while(1) {
```

If the queue is empty, wait on the lock:

```
            while([_blocks count] == 0) {
                [_lock wait];
            }
```

Note that this is done with a loop, not just an `if` statement. The reason for this is [spurious wakeup](https://en.wikipedia.org/wiki/Spurious_wakeup). In short, `wait` can potentially return even though nothing signaled, so for correct behavior the condition being checked needs to be reevaluated when `wait` returns.

Once a block is available, dequeue it:

```
            dispatch_block_t block = [_blocks firstObject];
            [_blocks removeObjectAtIndex: 0];
```

Indicate that this thread is now doing something by incrementing the active thread count:

```
            _activeThreadCount++;
```

Now it's time to execute the block, but we have to release the lock first, otherwise we won't get any concurrency and we'll have all sorts of entertaining deadlocks:

```
            [_lock unlock];
```

With the lock safely relinquished, execute the block:

```
            block();
```

With the block done, it's time to decrement the active thread count. This must be done with the lock held to avoid race conditions, and that's the end of the loop:

```
            [_lock lock];
            _activeThreadCount--;
        }
    }
```

Now you can see why the lock had to be acquired before entering the loop above. The last act in the loop is to decrement the active thread count, which requires the lock to be held. The first thing at the top of the loop is to check the blocks queue. By performing the first lock outside of the loop, subsequent iterations can use a single lock operation for both operations, rather than locking, unlocking, and immediately locking again.

Now for `addBlock:`

```
    - (void)addBlock: (dispatch_block_t)block {
```

Everything here needs to be done with the lock acquired:

```
        [_lock lock];
```

The first task is to add the new block to the blocks queue:

```
        [_blocks addObject: block];
```

If there's an idle worker thread ready to take this block, then there isn't much to do. If there aren't enough idle worker threads to handle all the outstanding blocks, and the number of worker threads isn't yet at the limit, then it's time to create a new one:

```
        NSUInteger idleThreads = _threadCount - _activeThreadCount;
        if([_blocks count] > idleThreads && _threadCount < _threadCountLimit) {
            [NSThread detachNewThreadSelector: @selector(workerThreadLoop:)
                                     toTarget: self
                                   withObject: nil];
            _threadCount++;
        }
```

Now everything is ready for a worker thread to get started on the block. In case they're all sleeping, wake one up:

```
        [_lock signal];
```

Then relinquish the lock and we're done:

```
        [_lock unlock];
    }
```

That gives us a thread pool that can spawn worker threads up to a pre-set limit to service blocks as they come in. Now to implement queues with this as the foundation.

**Queue Implementation**  
Like the thread pool, the queue will use a lock to protect its contents. Unlike the thread pool, it doesn't need to do any waiting or signaling, just basic mutual exclusion, so it uses a plain `NSLock`:

```
    NSLock *_lock;
```

Like the thread pool, it maintains a queue of pending blocks in an `NSMutableArray`:

```
    NSMutableArray *_pendingBlocks;
```

The queue knows whether it's serial or concurrent:

```
    BOOL _serial;
```

When serial, it also tracks whether it currently has a block running in the thread pool:

```
    BOOL _serialRunning;
```

Concurrent queues behave the same whether anything is running or not, so they don't track this.

The global queue is stored in a global variable, as is the underlying shared thread pool. They're both created in `+initialize`:

```
    static MADispatchQueue *gGlobalQueue;
    static MAThreadPool *gThreadPool;

    + (void)initialize {
        if(self == [MADispatchQueue class]) {
            gGlobalQueue = [[MADispatchQueue alloc] initSerial: NO];
            gThreadPool = [[MAThreadPool alloc] init];
        }
    }
```

The `+globalQueue` method can then just return the variable, since `+initialize` is guaranteed to have created it:

```
    + (MADispatchQueue *)globalQueue {
        return gGlobalQueue;
    }
```

This is just the sort of thing that calls for `dispatch_once`, but it felt like cheating to use a GCD API when I'm reimplementing a GCD API, even if it's not the same one.

Initializing a queue consists of allocating the lock and the pending blocks queue, and setting the `_serial` variable:

```
    - (id)initSerial: (BOOL)serial {
        if ((self = [super init])) {
            _lock = [[NSLock alloc] init];
            _pendingBlocks = [[NSMutableArray alloc] init];
            _serial = serial;
        }
        return self;
    }
```

Before we get to the remaining public API, there's an underlying method to build which will dispatch a single block on the thread pool, and then potentially call itself to run another block:

```
    - (void)dispatchOneBlock {
```

Its entire purpose in life is to run stuff on the thread pool, so it dispatches there:

```
        [gThreadPool addBlock: ^{
```

Then it grabs the first block in the queue. Naturally, this must be done with the lock held to avoid catastrophic explosions:

```
            [_lock lock];
            dispatch_block_t block = [_pendingBlocks firstObject];
            [_pendingBlocks removeObjectAtIndex: 0];
            [_lock unlock];
```

With the block in hand and the lock relinquished, the block can safely be executed on the background thread:

```
            block();
```

If the queue is concurrent, then that's all it needs to do. If it's serial, there's more:

```
            if(_serial) {
```

On a serial queue, additional blocks will build up, but can't be invoked until preceding blocks complete. When a block completes here, `dispatchOneBlock` will see if any other blocks are pending on the queue. If there are, it calls itself to dispatch the next block. If not, it sets the queue's running state back to `NO`:

```
                [_lock lock];
                if([_pendingBlocks count] > 0) {
                    [self dispatchOneBlock];
                } else {
                    _serialRunning = NO;
                }
                [_lock unlock];
            }
        }];
    }
```

With this method, implementing `dispatchAsync:` is relatively easy. Add the block to the queue of pending blocks, then set state and invoke `dispatchOneBlock` as appropriate:

```
    - (void)dispatchAsync: (dispatch_block_t)block {
        [_lock lock];
        [_pendingBlocks addObject: block];
```

If a serial queue is _idle_ then set its state to running and call `dispatchOneBlock` to get things moving:

```
        if(_serial && !_serialRunning) {
            _serialRunning = YES;
            [self dispatchOneBlock];
```

If the queue is concurrent, then call `dispatchOneBlock` unconditionally. This makes sure the new block is executed as soon as possible even if another block is already running, since multiple blocks are allowed to run concurrently:

```
        } else if (!_serial) {
            [self dispatchOneBlock];
        }
```

If a serial queue is already running then nothing more needs to be done. The existing run of `dispatchOneBlock` will eventually get to the block that was just added to the queue. Now release the lock:

```
        [_lock unlock];
    }
```

On to `dispatchSync:`. GCD is smart about this and runs the block directly on the calling thread, while stopping other blocks from running on the queue (if it's serial). We won't try to be so smart. Instead, we'll just use `dispatchAsync:`, and wrap it to wait for execution to complete.

It does this using a local `NSCondition`, plus a `done` variable to indicate when the block has completed:

```
    - (void)dispatchSync: (dispatch_block_t)block {
        NSCondition *condition = [[NSCondition alloc] init];
        __block BOOL done = NO;
```

Then it dispatches a block asynchronously. This block calls the passed-in one, then sets `done` and signals the `condition`:

```
        [self dispatchAsync: ^{
            block();
            [condition lock];
            done = YES;
            [condition signal];
            [condition unlock];
        }];
```

Out in the original calling thread, it waits on the `condition` for `done` to be set, then returns.

```
        [condition lock];
        while (!done) {
            [condition wait];
        }
        [condition unlock];
    }
```

At this point, the block's execution has completed. Success! That's the last bit of API needed for `MADispatchQueue`.

**Conclusion**  
A global thread pool can be implemented with a queue of worker blocks and a bit of intelligent spawning of threads. Using a shared global thread pool, a basic dispatch queue API can be built that offers basic serial/concurrent and synchronous/asynchronous dispatch. This rebuild lacks many of the nice features of GCD and is certainly much less efficient, but even so it gives a nice glimpse into what the inner workings of such a thing might be like, and shows that it's not really magic after all. (Except for [`dispatch_once`](https://www.mikeash.com/pyblog/friday-qa-2014-06-06-secrets-of-dispatch_once.html). That's all magic.)

That's it for today. Come back next time for more fun, games, and fun. Friday Q&A is driven by reader ideas so if you have something you'd like to see discussed here next time or in the future, please [let me know](mailto:mike@mikeash.com)!

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

Comments:

---

Comments RSS feed for this page

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.

Code syntax highlighting thanks to [Pygments](http://pygments.org/).
