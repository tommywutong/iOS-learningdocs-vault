---
title: 'Friday Q&A 2009-09-04: Intro to Grand Central Dispatch, Part II: Multi-Core Performance'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2009-09-04-intro-to-grand-central-dispatch-part-ii-multi-core-performance.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:59746460e04f7c7b'
translated: false
---

> 原文：[Friday Q&A 2009-09-04: Intro to Grand Central Dispatch, Part II: Multi-Core Performance](https://www.mikeash.com/pyblog/friday-qa-2009-09-04-intro-to-grand-central-dispatch-part-ii-multi-core-performance.html)　·　mikeash.com Friday Q&A

Posted at 2009-09-04 01:51 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [Friday Q&A 2009-09-11: Intro to Grand Central Dispatch, Part III: Dispatch Sources](https://www.mikeash.com/pyblog/friday-qa-2009-09-11-intro-to-grand-central-dispatch-part-iii-dispatch-sources.html)  
Previous article: [Objective-C Runtime Podcast Episode at Mobile Orchard](https://www.mikeash.com/pyblog/objective-c-runtime-podcast-episode-at-mobile-orchard.html)  
Tags: [fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [gcd](https://www.mikeash.com/pyblog/?tag=gcd) [performance](https://www.mikeash.com/pyblog/?tag=performance)

Friday Q&A 2009-09-04: Intro to Grand Central Dispatch, Part II: Multi-Core Performance

by [Mike Ash](https://www.mikeash.com/)

**Concepts**  
 In order to take advantage of multiple CPU cores within a single process, it's necessary to use multiple threads. (I'm ignoring multi-process concurrency, because it's unrelated to GCD.) This is just as true in the GCD world as it is in the purely threaded world. At the low level, GCD global dispatch queues are just abstractions around a pool of worker threads. Blocks on those queues get dispatched onto the worker threads as they become available. Blocks submitted to custom queues end up going through global queues and into that same pool of worker threads. (Unless your custom queue is targeted at the main thread, but you would never do that for speed purposes!)

There are essentially two ways to extract multi-core performance out of GCD: by parallelizing a single task or a group of related tasks onto one of the global queues, and by parallelizing multiple unrelated or loosely related tasks onto multiple custom queues.

**Global Queues**  
 Imagine the following loop:

```
    for(id obj in array)
        [self doSomethingIntensiveWith:obj];
```

Assume that `-doSomethingIntensiveWith:` is thread safe and can be run in parallel with other uses of that same method. If this is true, and `array` regularly contains more than one object, it's easy to use GCD to parallelize this code:

```
    dispatch_queue_t queue = dispatch_get_global_queue(DISPATCH_QUEUE_PRIORITY_DEFAULT, 0);
    for(id obj in array)
        dispatch_async(queue, ^{
            [self doSomethingIntensiveWith:obj];
        });
```

Easy as that, you're running on multiple cores.

Of course code isn't always this nice. Sometimes you have code which manipulates an array like this, but then has to perform some work with the result:

```
    for(id obj in array)
        [self doSomethingIntensiveWith:obj];
    [self doSomethingWith:array];
```

The use of `dispatch_async` in the GCD example means that this doesn't work. And you can't solve it just by switching to `dispatch_sync`, because that will cause each individual iteration to block, destroying all parallelism.

One way to solve this problem is by using dispatch groups. A dispatch group is a way to group together multiple blocks, and either wait for them to complete or be notified once they complete. They are created using `dispatch_group_create`, and the `dispatch_group_async` function allows submitting a block to a dispatch queue and also adding it to the group. We could then rewrite this code to use GCD like so:

```
    dispatch_queue_t queue = dispatch_get_global_qeueue(DISPATCH_QUEUE_PRIORITY_DEFAULT, 0);
    dispatch_group_t group = dispatch_group_create();
    for(id obj in array)
        dispatch_group_async(group, queue, ^{
            [self doSomethingIntensiveWith:obj];
        });
    dispatch_group_wait(group, DISPATCH_TIME_FOREVER);
    dispatch_release(group);
    
    [self doSomethingWith:array];
```

If this work can be performed asynchronously relative to the calling code, then we can get even fancier than this, and run `-doSomethingWith:` in the background instead of waiting. To do this, we'll use `dispatch_group_async` to set a block to run when the group completes:

```
    dispatch_queue_t queue = dispatch_get_global_qeueue(DISPATCH_QUEUE_PRIORITY_DEFAULT, 0);
    dispatch_group_t group = dispatch_group_create();
    for(id obj in array)
        dispatch_group_async(group, queue, ^{
            [self doSomethingIntensiveWith:obj];
        });
    dispatch_group_notify(group, queue, ^{
        [self doSomethingWith:array];
    });
    dispatch_release(group);
```

Now not only will all of the work on the array objects run in parallel, but the final work will also run asynchronously with respect to the rest of the application, giving even more parallelism. Note that if `-doSomethingWith:` needed to run on the main thread, for example to manipulate the GUI, all you need to do is pass the main queue to `dispatch_group_notify` instead of a global queue.

For the synchronous case, GCD provides a nice shortcut with the `dispatch_apply` function. This function calls a single block multiple times in parallel and waits for it to complete, just like what we wanted:

```
    dispatch_queue_t queue = dispatch_get_global_qeueue(DISPATCH_QUEUE_PRIORITY_DEFAULT, 0);
    dispatch_apply([array count], queue, ^(size_t index){
        [self doSomethingIntensiveWith:[array objectAtIndex:index]];
    });
    [self doSomethingWith:array];
```

This is nice, but what about the asynchronous case? There's no asynchronous version of `dispatch_apply` that we can use. But we're using an API built around asynchronous invocation! We can just use `dispatch_async` to push the whole thing into the background:

```
    dispatch_queue_t queue = dispatch_get_global_qeueue(DISPATCH_QUEUE_PRIORITY_DEFAULT, 0);
    dispatch_async(queue, ^{
        dispatch_apply([array count], queue, ^(size_t index){
            [self doSomethingIntensiveWith:[array objectAtIndex:index]];
        });
        [self doSomethingWith:array];
    });
```

Easy!

The key to this approach is identifying code which is performing identical work on many different pieces of data at once. If you ensure that the work performed is done in a thread safe manner (beyond the scope of this post) then you can replace your loops with calls to GCD in order to achieve parallelism.

In order to see a performance gain, you need to be performing a fairly substantial amount of work. GCD is lightweight and low-overhead compared to threads, but it's still somewhat costly to submit a block to a queue. The block has to be copied and enqueued, and the appropriate worker thread somehow notified. Submitting a block for every pixel in an image is probably not going to be a win. On the other hand, submitting a block for each image when converting a collection of images is probably going to be a win. The point where GCD ceases to be profitable falls somewhere in the middle. When in doubt, experiment. Parallelizing applications is an optimization, and as such you should always measure before and after to make sure that your changes helped. (And to make sure that you're making the changes in the right place!)

**Subsystem Parallelism**  
 The previous section talked about taking advantage of multiple cores in a single subsystem of your application. It can also be useful to do this across multiple subsystems.

For example, imagine an application which opens a document containing metadata. The document data itself must be parsed and converted into model objects for display, as must the metadata. However, the document data and the metadata don't interact. You could create a dispatch queue for each one, then run both in parallel. The code for each piece of data parsing would be entirely serial within itself, and thread safety is not a concern (as long as you don't have shared data between them), but they will still run in parallel.

Once the document is open, the program needs to perform tasks in response to user actions. For example, it may need to perform spell checking, syntax highlighting, word counting, autosave, and other such things. If each one of these tasks is implemented using a separate dispatch queue, they will all run in parallel with respect to each other without many of the difficulties of multithreaded programming.

By using dispatch sources, something I'll cover next week, you can have GCD deliver events directly to a custom dispatch queue. A part of your program that monitors a network socket, for example, could be given its own dispatch queue which will then allow it to run in parallel with respect to the rest of the application. And again, by using a custom queue, this module will run serially with respect to itself, simplifying programming.

**Conclusion**  
 This week we saw how to use GCD to increase the performance of your applications and take advantage of modern multi-core systems. Although care must still be taken when writing parallel applications, GCD makes it easier than ever to take advantage of all available computing power.

That wraps up this week's Friday Q&A. Come back next week for the next part in the continuing series on GCD, when I will talk about dispatch sources, GCD's mechanism for monitoring internal and external events. As always, if you have a suggestion for a topic to cover, please post it in the comments or [e-mail it directly to me](mailto:mike@mikeash.com).

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

Comments:

---

[Comments RSS feed for this page](https://www.mikeash.com/commentsrss.py?page=pyblog/friday-qa-2009-09-04-intro-to-grand-central-dispatch-part-ii-multi-core-performance.html)

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.

Code syntax highlighting thanks to [Pygments](http://pygments.org/).
