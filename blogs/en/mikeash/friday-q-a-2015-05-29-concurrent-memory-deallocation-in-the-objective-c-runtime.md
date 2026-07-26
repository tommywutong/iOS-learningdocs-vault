---
title: 'Friday Q&A 2015-05-29: Concurrent Memory Deallocation in the Objective-C Runtime'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2015-05-29-concurrent-memory-deallocation-in-the-objective-c-runtime.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:cae950de9698cb90'
translated: false
---

> 原文：[Friday Q&A 2015-05-29: Concurrent Memory Deallocation in the Objective-C Runtime](https://www.mikeash.com/pyblog/friday-qa-2015-05-29-concurrent-memory-deallocation-in-the-objective-c-runtime.html)　·　mikeash.com Friday Q&A

Posted at 2015-06-05 13:06 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [I Do Not Agree To Your Terms](https://www.mikeash.com/pyblog/i-do-not-agree-to-your-terms.html)  
Previous article: [Friday Q&A 2015-05-01: Fuzzing with afl-fuzz](https://www.mikeash.com/pyblog/friday-qa-2015-05-01-fuzzing-with-afl-fuzz.html)  
Tags: [fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [objectivec](https://www.mikeash.com/pyblog/?tag=objectivec) [threading](https://www.mikeash.com/pyblog/?tag=threading)

Friday Q&A 2015-05-29: Concurrent Memory Deallocation in the Objective-C Runtime

by [Mike Ash](https://www.mikeash.com/)

**Message Sending in Concept**  
`objc_msgSend` works by looking up the appropriate method implementation for the method being sent, and then jumping to it. Conceptually, looking up the method works like this:

```
    IMP lookUp(id obj, SEL selector) {
        Class c = object_getClass(obj);

        while(c) {
            for(int i = 0; i < c->numMethods; i++) {
                Method m = c->methods[i];
                if(m.selector == selector) {
                    return m.imp;
                }
            }

            c = c->superclass;
        }

        return _objc_msgForward;
    }
```

Some names have been changed to protect the innocent. If you're interested in seeing the real code, check out the Objective-C runtime source code:

[http://www.opensource.apple.com/source/objc4/](http://www.opensource.apple.com/source/objc4/)

**Method Cache**  
Most Objective-C code sends messages all over the place. If the full message search was performed for each one, it would be unbelievably slow.

The solution to this is a cache. Each class has a hash table attached to it which maps selectors to method implementations. The hash table is built for maximum read efficiency, and `objc_msgSend` uses carefully tuned assembly language code to perform the hash table lookup quickly. This gets a message send in the cached case down to single-digit nanoseconds. The first use of any given message is still unbelievably slow, but after that it's fast.

When we think of a cache, it's usually something with a limited size that's intended to speed up multiple accesses to recently used resources. For example, you might cache images that you load from the internet so that two fetches in quick succession don't hit the network twice. You don't want to use too much memory, though, so you might cap the number of images you keep in the cache at any given time, and throw away the oldest image when a new one comes in after it fills up.

This is a fine approach for many problems but it can have unfortunate performance implications. For example, if you set your image cache to store 40 images, and you run into a case where your application is constantly cycling through 41 images, your cache suddenly becomes completely useless.

For our own apps we can test and tune the caches to avoid this, but the Objective-C runtime doesn't have this option. Because the method cache is so critical to performance, and because each entry is relatively small, the runtime doesn't impose any size limit on the caches, and expands them as necessary to cache all messages that have been sent.

Note that the caches _do_ sometimes get flushed; any time something happens that might cause the cached data to become stale, such as loading new code into the process or modifying a class's method lists, the appropriate caches are destroyed and allowed to refill.

**Resizing, Deallocation, and Threads**  
Resizing the cache is pretty simple in concept. It looks something like:

```
    bucket_t *newCache = malloc(newSize);
    copyEntries(newCache, class->cache);
    free(class->cache);
    class->cache = newCache;
```

The Objective-C runtime actually takes a small shortcut here: it doesn't even copy the old entries into the new cache! It's just a cache, after all, and there's no _requirement_ to preserve the data it contains. Entries refill as messages are sent. So it's really just:

```
    free(class->cache);
    class->cache = malloc(newSize);
```

In a single-threaded environment, this would be all you need, and this article would be short. But of course the Objective-C runtime has to support multithreaded code, and that means that all of this code has to be thread safe. Any given class's cache can be accessed simultaneously from multiple threads, so this code has to take care to ensure that it tolerates that scenario.

As written here, it won't. There's a window of opportunity after freeing the old cache and before assigning the new cache where another thread might access an invalid cache pointer. This could cause it to see garbage data, or even just crash immediately if the underlying memory was unmapped.

How can we solve this problem? The typical approach to protecting shared data like this is to use a lock. The code would then look like:

```
    lock(class->lock);
    free(class->cache);
    class->cache = malloc(newSize);
    unlock(class->lock);
```

All accesses must be gated by the lock, including reads, for this to work. That means that `objc_msgSend` would have to acquire the lock, look in the cache, and release the lock. Acquiring and releasing the lock each time would add a _lot_ of overhead, considering that the cache lookup itself only takes a few nanoseconds. The performance impact is just too high.

We might try to close the window in some other way. For example, what if we allocated and assigned the new cache _first_, and then deallocated the old cache?

```
    bucket_t *oldCache = class->cache;
    class->cache = malloc(newSize);
    free(oldCache);
```

This helps, but it doesn't solve the problem. Another thread might retrieve the old cache pointer, then get preempted by the system before it can access the contents. The old cache could then be destroyed before the other thread runs again, causing the same problems as before.

What if we put in a delay? Something like:

```
    bucket_t *oldCache = class->cache;
    class->cache = malloc(newSize);
    after(5 /* seconds */, ^{
        free(oldCache);
    });
```

This is almost certain to work. But it's still conceivable that a thread might get preempted at just the right moment and stay preempted for long enough that the five-second delay fires first. This makes the crash extremely unlikely, but doesn't completely eliminate it.

Rather than an arbitrary delay, how about waiting until the window is surely clear? Let's add a counter to `objc_msgSend` so that it looks something like:

```
    gInMsgSend++;
    lookUpCache(class->cache);
    gInMsgSend--;
```

A proper thread safe version would need to use atomics for the counter and appropriate memory barriers to make sure the dependent loads/stores show up properly. For the purposes of this article, just imagine that stuff is there.

With the counter, cache reallocation would look like:

```
    bucket_t *oldCache = class->cache;
    class->cache = malloc(newSize);
    while(gInMsgSend)
        ; // spin
    free(oldCache);
```

Note that there is no need to _block_ execution of `objc_msgSend` for this to work properly. Once the cache free code is sure that nothing is in `objc_msgSend` at any particular moment after it has replaced the cache pointer, it can go ahead and free the old one. Another thread might call out to `objc_msgSend` while the old cache pointer is being deallocated, but this new call can't possibly see the old pointer anymore, so it's safe.

Spinning is inefficient and inelegant. It's not particularly urgent to free these caches. It's nice to deallocate the memory, but it's not terrible if it takes some time. Rather than spinning, let's keep a list of unfreed caches, and each time something is freed, try to clear everything that's pending:

```
    bucket_t *oldCache = class->cache;
    class->cache = malloc(newSize);

    append(gOldCachesList, oldCache);
    if(!gInMsgSend) {
        for(cache in gOldCachesList) {
            free(cache);
        }
        gOldCachesList.clear();
    }
```

If a message send is in progress then this won't immediately free the old cache, but that's not a problem. The next time through it will be cleared, or the time after that, or at _some_ point in the future.

This version is pretty close to how the Objective-C runtime actually does it.

**Zero-Cost Flags**  
There's an extreme asymmetry here between the two interacting parts. The `objc_msgSend` side runs potentially millions of times each second and really needs to be as fast as possible. The best case running time for a single call is just a few nanoseconds. On the other hand, resizing the cache is a rare operation that will typically get less and less common as an app continues to run. Once the app reaches a steady state, no longer loading new code or editing message lists and with the caches as big as they need to be, it'll never happen. Before that, it may happen some hundreds or thousands of times as the caches grow to the size they need, but it's extremely rare in comparison to `objc_msgSend` and vastly less performance sensitive.

Because of this asymmetry, it's best to put as little as possible on the message send side, even if it makes the cache freeing part much slower. Shaving off one CPU cycle in `objc_msgSend` at the cost of a million CPU cycles in each cache free operation is a net win, by a huge margin.

Even a global counter is too costly. That's two additional memory accesses within `objc_msgSend` which would still add a great deal of overhead. They would need to be atomic and use memory barriers which makes it even worse. Fortunately, the Objective-C runtime has a technique for reducing the cost on the `objc_msgSend` side to zero, at the expense of making the cache free code much slower.

The purpose of the hypothetical global counter is to track when any thread is within a particular region of code. Threads already have something that tracks what code they're currently running: the program counter. This is the CPU register which tracks the memory address of the current instruction. Instead of a global counter, we could check each thread's program counter to see if it's within `objc_msgSend`. If all threads are outside, then it's safe to free the old caches. Here's what that implementation would look like:

```
    BOOL ThreadsInMsgSend(void) {
        for(thread in GetAllThreads()) {
            uintptr_t pc = thread.GetPC();
            if(pc >= objc_msgSend_startAddress && pc <= objc_msgSend_endAddress) {
                return YES;
            }
        }
        return NO;
    }

    bucket_t *oldCache = class->cache;
    class->cache = malloc(newSize);

    append(gOldCachesList, oldCache);
    if(!ThreadsInMsgSend()) {
        for(cache in gOldCachesList) {
            free(cache);
        }
        gOldCachesList.clear();
    }
```

Then `objc_msgSend` doesn't have to do anything special at all. It can access the caches directly without worrying about flagging that access. It just does:

```
    lookUpCache(class->cache);
```

The cache free code is pretty inefficient because it needs to examine the state of every thread in the process. But `objc_msgSend` is as efficient as it would be if it were written for a single-threaded environment, and that's a tradeoff well worth making. This is ultimately how Apple's runtime code works.

**The Real Code**  
Apple's implementation of this technique can be found in the runtime function `_collecting_in_critical` located in [objc-cache.mm](http://www.opensource.apple.com/source/objc4/objc4-646/runtime/objc-cache.mm).

The critical PC locations are stored in global variables:

```
    OBJC_EXPORT uintptr_t objc_entryPoints[];
    OBJC_EXPORT uintptr_t objc_exitPoints[];
```

There are actually multiple `objc_msgSend` implementations (for things like `struct` returns), and the internal `cache_getImp` function also accesses the cache directly. They all need to be checked in order to safely deallocate caches.

The function itself takes no parameters and returns `int`, which is just used as a boolean flag to indicate whether any threads are in one of the critical functions or not:

```
    static int _collecting_in_critical(void)
    {
```

I'm going to skip over the less interesting bits of code in this function in the interest of concentrating on the best parts. If you want to see the whole thing, take a look at [opensource.apple.com](http://www.opensource.apple.com/source/objc4/objc4-646/runtime/objc-cache.mm).

The APIs for getting thread information lie at the mach level. `task_threads` gets a list of all threads in a given task (mach's term for a process), and this code uses it to get the threads in its own process:

```
        ret = task_threads(mach_task_self(), &threads, &number);
```

That returns an array of `thread_t` values in `threads`, and the number of threads in `number`. Then it loops over them:

```
        for (count = 0; count < number; count++)
        {
```

Fetching the PC for a thread is done in a separate function, which we'll look at shortly:

```
            pc = _get_pc_for_thread (threads[count]);
```

It then loops over the entry and exit points and compares with each one:

```
            for (region = 0; objc_entryPoints[region] != 0; region++)
            {
                if ((pc >= objc_entryPoints[region]) &&
                    (pc <= objc_exitPoints[region])) 
                {
                    result = TRUE;
                    goto done;
                }
            }
        }
```

After the loop, it returns the result to the caller:

```
        return result;
    }
```

How does `_get_pc_for_thread` work? It's a relatively simple bit of code that calls `thread_get_state` to get the register state of the target thread. The main reason it's in a separate function is because the register state structures are architecture-specific, since each architecture has different registers. That means this function needs a separate implementation for each supported architecture, although the implementations are almost identical. Here's the implementation for `x86-64`:

```
    static uintptr_t _get_pc_for_thread(thread_t thread)
    {
        x86_thread_state64_t            state;
        unsigned int count = x86_THREAD_STATE64_COUNT;
        kern_return_t okay = thread_get_state (thread, x86_THREAD_STATE64, (thread_state_t)&state, &count);
        return (okay == KERN_SUCCESS) ? state.__rip : PC_SENTINEL;
    }
```

Note that `rip` is the register name of the PC on `x86-64`; the R stands for "register," and the IP stands for "instruction pointer."

The entry and exit points themselves are defined in the assembly language file where the functions in question are defined. They look like this:

```
    .private_extern _objc_entryPoints
    _objc_entryPoints:
        .quad   _cache_getImp
        .quad   _objc_msgSend
        .quad   _objc_msgSend_fpret
        .quad   _objc_msgSend_fp2ret
        .quad   _objc_msgSend_stret
        .quad   _objc_msgSendSuper
        .quad   _objc_msgSendSuper_stret
        .quad   _objc_msgSendSuper2
        .quad   _objc_msgSendSuper2_stret
        .quad   0

    .private_extern _objc_exitPoints
    _objc_exitPoints:
        .quad   LExit_cache_getImp
        .quad   LExit_objc_msgSend
        .quad   LExit_objc_msgSend_fpret
        .quad   LExit_objc_msgSend_fp2ret
        .quad   LExit_objc_msgSend_stret
        .quad   LExit_objc_msgSendSuper
        .quad   LExit_objc_msgSendSuper_stret
        .quad   LExit_objc_msgSendSuper2
        .quad   LExit_objc_msgSendSuper2_stret
        .quad   0
```

`_collecting_in_critical` is used much like in the hypothetical examples above. It's called before the code that frees leftover cache garbage. The runtime actually has two separate modes: one which leaves the garbage for the next time if other threads are in a critical function, and one which spins in a loop until the coast is clear, and always deallocates the garbage:

```
    // Synchronize collection with objc_msgSend and other cache readers
    if (!collectALot) {
        if (_collecting_in_critical ()) {
            // objc_msgSend (or other cache reader) is currently looking in
            // the cache and might still be using some garbage.
            if (PrintCaches) {
                _objc_inform ("CACHES: not collecting; "
                              "objc_msgSend in progress");
            }
            return;
        }
    } 
    else {
        // No excuses.
        while (_collecting_in_critical()) 
            ;
    }

    // free garbage here
```

The first mode, which leaves garbage for the next time, is used for normal cache resizes. The spin mode that always frees garbage is used in the runtime method that flushes all caches for all classes as this would typically generate a large amount of garbage. As best I can tell from examining the code, this only happens when enabling a debug logging facility that logs all message sends to a file. It flushes caches because the message cache interferes with the logging.

**Conclusion**  
Performance and thread safety are often at odds with each other. Often there is asymmetry in how different parts of code access shared data, which allows more efficient thread safety. A global flag or counter that indicates when a mutating action is unsafe can be one way to exploit this. In the Objective-C runtime, Apple takes this a step further and uses the program counter of each thread as an implicit indication of when a thread is taking unsafe action. This is a specialized case and it's hard to see where else the technique could be useful, but it's fascinating to take apart.

That's it for today. Check back next time for more exciting action. Friday Q&A is driven by reader ideas, so if you have an idea you'd like to see covered here, please [send it in](mailto:mike@mikeash.com)!

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

Comments:

---

Comments RSS feed for this page

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.

Code syntax highlighting thanks to [Pygments](http://pygments.org/).
