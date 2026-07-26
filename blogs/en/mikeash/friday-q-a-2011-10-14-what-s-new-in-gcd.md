---
title: 'Friday Q&A 2011-10-14: What''s New in GCD'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2011-10-14-whats-new-in-gcd.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:3ce62b643792e9ce'
translated: false
---

> 原文：[Friday Q&A 2011-10-14: What's New in GCD](https://www.mikeash.com/pyblog/friday-qa-2011-10-14-whats-new-in-gcd.html)　·　mikeash.com Friday Q&A

Posted at 2011-10-14 12:01 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [Friday Q&A 2011-10-28: Generic Block Proxying](https://www.mikeash.com/pyblog/friday-qa-2011-10-28-generic-block-proxying.html)  
Previous article: [Friday Q&A 2011-09-30: Automatic Reference Counting](https://www.mikeash.com/pyblog/friday-qa-2011-09-30-automatic-reference-counting.html)  
Tags: [fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [gcd](https://www.mikeash.com/pyblog/?tag=gcd)

Friday Q&A 2011-10-14: What's New in GCD

by [Mike Ash](https://www.mikeash.com/)

**Prerequisite Reading**  
If you're new to GCD, you'll want to become familiar with the basics before diving into the new features in Lion. There are many good references out there, including my own series which starts off with [Intro to Grand Central Dispatch, Part I: Basics and Dispatch Queues](https://www.mikeash.com/pyblog/friday-qa-2009-08-28-intro-to-grand-central-dispatch-part-i-basics-and-dispatch-queues.html).

**Overview**  
GCD is still the same great library that we know and love, but now has a bunch more goodies.

First, there's a new global queue available, which can be accessed by passing `DISPATCH_QUEUE_PRIORITY_BACKGROUND`. This queue runs at an extremely low priority and disk IO is throttled. This makes it suitable for ongoing tasks which need to have a minimal impact on the system's interactive use.

Next, we now have the ability to create custom concurrent queues. Previously, custom queues were always serial, and the only concurrent queues supported by GCD were the global queues. Custom concurrent queues allow easy suspension of parallelized tasks. Alongside this, GCD now provides dispatch barriers, which allow a custom concurrent queue to be used much like a reader/writer lock.

Finally, we have the long-awaited GCD for IO. Dispatch IO objects can be created for paths or file descriptors. This not only provides a simpler interface for IO compared to the dispatch source API, but it also allows GCD to more intelligently coordinate IO activities to avoid disk thrashing. To go along with this, there's a new dispatch data type, which efficietly manages noncontiguous data.

There isn't really much more to say about the new global background queue, so let's jump straight to....

**Custom Concurrent Queues and Barriers**  
Creating a custom concurrent queue is easy: pass `DISPATCH_QUEUE_CONCURRENT` to the `dispatch_queue_create` function. Serial queues can still be obtained by passing `NULL` or `DISPATCH_QUEUE_SERIAL`.

Once created, a concurrent queue acts just as you'd expect. Multiple blocks submitted to it can run in parallel if system load and capabilities permit. Unlike the global queues, you can still suspend/resume custom concurrent queues, making it useful for managing a set of parallel operations.

Dispatch barriers go along with custom concurrent queues. They can be used with two functions: `dispach_barrier_async` and `dispatch_barrier_sync`. These work just like `dispatch_async` and `dispatch_sync` except that, if used on a custom concurrent queue, the block that's submitted with the `barrier` function doesn't run concurrently with other work on that queue. Instead, it waits until anything currently executing on the queue is finished, then blocks everything else on the queue while the barrier block executes. Once the barrier completes, execution resumes normally.

Note that these barrier functions are pointless on a serial queue, since every unit of work blocks other work on such a queue. They are non-functional when used on the global queues, where they simply do a non-barrier `dispatch_async` or `dispatch_sync`. This is because the global queues are a shared resource and it doesn't make sense to allow a single component to block them for everybody.

Custom concurrent queues and barriers allow for the efficient manipulation of data structures which can be read but not written concurrently. If you're familiar with them, they allow essentially the same capabilities as reader/writer locks from more traditional multithreading techniques.

As an example, let's imagine that we have a `NSMutableDictionary` that's being used as a cache. `NSMutableDictionary` is thread safe for reading, but doesn't allow any concurrent access while modifying its contents, not even if the other access is simple reading.

This can easily be done using a custom concurrent queue and barriers. First, we'll create the dictionary and the queue:

```
    _cache = [[NSMutableDictionary alloc] init];
    _queue = dispatch_queue_create("com.mikeash.cachequeue", DISPATCH_QUEUE_CONCURRENT);
```

To read from the cache, we can just use a `dispatch_sync`:

```
    - (id)cacheObjectForKey: (id)key
    {
        __block obj;
        dispatch_sync(_queue, ^{
            obj = [[_cache objectForKey: key] retain];
        });
        return [obj autorelease];
    }
```

Because the queue is concurrent, this allows for concurrent access to the cache, and therefore no contention between multiple threads in the common case.

To write to the cache, we need a barrier:

```
    - (void)setCacheObject: (id)obj forKey: (id)key
    {
        dispatch_barrier_async(_queue, ^{
            [_cache setObject: obj forKey: key];
        });
    }
```

Because this uses the `barrier` function, it ensures exclusive access to the cache while the block runs. Not only does it exclude all other writes to the cache while it runs, but it also excludes all other reads, making the modification safe.

The gain for such a simple dictionary isn't too compelling, but for more complicated use cases, where the readers need to carry out an expensive sequence of atomic operations, it can make it easy to write fast, safe concurrent code.

**Dispatch Data**  
Dispatch data objects are clearly included to facilitate dispatch IO, but they stand on their own and can be used as general purpose data containers as well. Dispatch data objects are much like `NSData` objects, in that they're simple object wrappers around a raw pointer and length. What the data means and how you use it is completely up to you.

There's a major difference from `NSData`, though, which is that dispatch data objects can be _noncontiguous_. Fundamentally, an `NSData` is a single buffer. A dispatch data object is a collection of potentially many such buffers. This can dramatically increase performance because there's often no need to copy data around at all. For example, when concatenating two `NSData` objects together, at least one of the buffers needs to be copied, and likely both. When concatenating dispatch data objects, nothing needs to be copied. Internally, this is implemented by creating a tree of dispatch data objects, with the leaves containing a single contiguous buffer, and others pointing to the objects that contain the individual buffers.

Of course, a lot of code wants to work with contiguous data, but fortunately GCD makes it easy to squash a dispatch data object together so that it becomes a single buffer. For code that's more flexible, it's easy to iterate over the individual buffers contained within the data object.

To create a basic dispatch data object, use the `dispatch_data_create` function. It takes a pointer, a length, a destructor block, and a queue on which to run the destructor. By requesting the default destructor, the data will be immediately copied into storage that's managed by GCD:

```
    dispatch_data_t data = dispatch_data_create(buffer, length, NULL, DISPATCH_DATA_DESTRUCTOR_DEFAULT);
    // buffer can now be freed
```

Of course, the whole point of this stuff is to avoid copies, so it's better to provide an explicit destructor that will free the memory so that it can avoid being copied. A common case is memory allocated with `malloc`, and the `DISPATCH_DATA_DESTRUCTOR_FREE` destructor will call `free`:

```
    void *buffer = malloc(length);
    // fill out buffer
    dispatch_data_t data = dispatch_data_create(buffer, length, NULL, DISPATCH_DATA_DESTRUCTOR_FREE);
    // buffer will now be freed when data is destroyed
```

For other types of buffers, we can provide a custom block to do whatever is necessary. For example, here's a simple function that creates a dispatch data object wrapping an `NSData` object:

```
    dispatch_data_t CreateDispatchDataFromNSData(NSData *nsdata)
    {
        // copy the data object here, in case it's mutable
        // this will just be a retain if it's immutable
        nsdata = [nsdata copy];

        dispatch_queue_t queue = dispatch_get_global_queue(0, 0);
        return dispatch_data_create([nsdata bytes], [nsdata length], queue, ^{
            // balance the copy at the top
            [nsdata release];
        });
    }
```

To concatenate two dispatch data objects, just use `dispatch_data_create_concat`. To extract a piece of a data object, `dispatch_data_create_subrange` will grab an exact subrange, and `dispatch_data_copy_region` will grab a region around a specific location, which gives GCD more flexibility to be efficient.

To access the contents of a data object, the simplest way is to call `dispatch_data_create_map` which concatenates all of the data into a single contiguous buffer:

```
    const void *buffer;
    size_t length;
    dispatch_data_t tmpData = dispatch_data_create_map(data, &buffer, &length);
    // use buffer and length here
    dispatch_release(tmpData);
```

However, this may need to copy the individual data pieces in order to create a contiguous buffer, which is just what this whole system is trying to avoid. For more efficient access to the contents, `dispatch_data_apply` is available and will walk through the individual pieces, calling a block on each one.

For example, here is a function which transforms a data object containing ASCII data into an `NSString` using `dispatch_data_apply` to avoid unnecessary copies:

```
    NSString *StringFromDispatchData(dispatch_data_t data)
    {
        NSMutableString *s = [NSMutableString stringWithCapacity: dispatch_data_get_size(data)];
        dispatch_data_apply(data, ^(dispatch_data_t region, size_t offset, const void *buffer, size_t size) {
            [s appendFormat: @"%.*s", size, buffer];
            return (_Bool)true;
        });
        return s;
    }
```

Note that the applier block returns a boolean indicating whether the apply operation should continue. Since this block continues unconditionally, it just returns `true`, with some typecasting to placate the compiler.

**Dispatch IO**  
Now we reach the really big new feature in GCD. The original GCD API could integrate with IO through dispatch sources. A dispatch source could be used to monitor a file descriptor and run a handler when data could be read or written. However, this approach still left a lot up to the programmer, who had to manually read and write the data in question and manage file descriptor lifetime. By handing more responsibility over to GCD, it's also able to more intelligently manage multiple concurrent IO operations to reduce thrash and resource contention.

Dispatch IO objects are called channels. A channel wraps a file descriptor. To create one, use the `dispatch_io_create` function, which takes a channel type (stream or random access), the file descriptor, a queue to associate with the channel, and a cleanup handler. Here's a quick example of making a channel for standard input:

```
    dispatch_io_t stdinChannel = dispatch_io_create(DISPATCH_IO_STREAM, STDIN_FILENO, dispatch_get_global_queue(0, 0), ^(int error) {
        if(error)
            fprintf(stderr, "got an error from stdin: %d (%s)\n", error, strerror(error));
    });
```

We'll want to read from this channel, but first we need to configure it. We can tell GCD how often we want data by setting high and low water values for the channel. The low water value sets how much data GCD will try to gather before invoking a read handler. Standard input is often interactive, in which case we want GCD to invoke the read handler when any data comes in no matter how small, so we'll set the low water mark to just one byte:

```
    dispatch_io_set_low_water(stdinChannel, 1);
```

There's no reason to limit the maximum amount of data, so we'll leave the high water value at the default of `SIZE_MAX`, which is essentially infinite. If we had to limit this for some reason, we'd just call `dispatch_io_set_high_water`.

There's also a `dispatch_io_set_interval` function, which tells GCD to call the read handler periodically, allowing the code to monitor the progress of the IO operations. This is also unnecessary for simply reading from standard input.

Now that the channel is configured, we'll tell GCD to read from it using `dispatch_io_read`. This function takes a channel, an offset (ignored in the case of stream channels like this one), a length, a queue, and a handler block:

```
    dispatch_io_read(stdinChannel, 0, SIZE_MAX, dispatch_get_global_queue(0, 0), ^(bool done, dispatch_data_t data, int error) {
        if(data)
        {
            // process data
        }
        if(error)
        {
            // handle an error, or just let the channel's handler take care of it
        }
        if(done)
        {
            // we've processed all of stdin, so exit
            exit(0);
        }
    });
```

Similarly, we can write to a channel using `dispatch_io_write`. By creating another channel and inserting a bit of code into the above handler, the program turns into a simple echo tool:

```
    dispatch_io_t stderrChannel = dispatch_io_create(DISPATCH_IO_STREAM, STDERR_FILENO, dispatch_get_global_queue(0, 0), ^(int error) {
        if(error)
            fprintf(stderr, "got an error from stdout: %d (%s)\n", error, strerror(error));
    });

    dispatch_io_read(stdinChannel, 0, SIZE_MAX, dispatch_get_global_queue(0, 0), ^(bool done, dispatch_data_t data, int error) {
        if(data)
        {
            dispatch_io_write(stderrChannel, 0, data, dispatch_get_global_queue(0, 0), ^(bool done, dispatch_data_t data, int error) {});
        }
        ...
```

In addition to simply dealing with raw file descriptors, GCD also provides `dispatch_io_create_with_path`, a convenience function for directly getting an IO channel to a file on disk. This essentially combines `dispatch_io_create` and `open`, with the convenience of only having to handle errors in one spot.

When done with an IO channel, simply call `dispatch_io_close` to explicitly close the channel, and don't forget a `dispatch_release` to balance the create call.

For simple use cases, GCD also provides `dispatch_read` and `dispatch_write` calls, which do simple, GCD-based IO from a file descriptor without having to set up channels. This makes it simple to just read a chunk of data all at once, although for more complicated uses, creating a channel is more efficient and easier to work with.

Dispatch IO channels can talk to just about any kind of file descriptor, making this API useful not only for manipulating files, but also sockets and pipes.

**Conclusion**  
Lion and iOS 5 bring some exciting and long-awaited additions to GCD. The new global background queue is useful for long-running, low impact tasks. The ability to create custom concurrent queues allows much better management of parallelized tasks, and barriers allow for safe parallel access to shared data while reading and exclusive access for writing. Finally, the dispatch IO API brings GCD's smarts and system-wide integration to file access and networking.

That's it for today. You may now return to waiting for your shiny new iPhone. Friday Q&A is driven by reader ideas, so if you happen to come up with something you'd like to see covered here while you're playing with your new toy, [send it in](mailto:mike@mikeash.com:)!

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

Comments:

---

[Comments RSS feed for this page](https://www.mikeash.com/commentsrss.py?page=pyblog/friday-qa-2011-10-14-whats-new-in-gcd.html)

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.

Code syntax highlighting thanks to [Pygments](http://pygments.org/).
