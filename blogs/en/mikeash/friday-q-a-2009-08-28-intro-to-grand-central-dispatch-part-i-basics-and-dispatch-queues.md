---
title: 'Friday Q&A 2009-08-28: Intro to Grand Central Dispatch, Part I: Basics and Dispatch Queues'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2009-08-28-intro-to-grand-central-dispatch-part-i-basics-and-dispatch-queues.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:6a7f7ec4e5b73876'
translated: false
---

> 原文：[Friday Q&A 2009-08-28: Intro to Grand Central Dispatch, Part I: Basics and Dispatch Queues](https://www.mikeash.com/pyblog/friday-qa-2009-08-28-intro-to-grand-central-dispatch-part-i-basics-and-dispatch-queues.html)　·　mikeash.com Friday Q&A

Posted at 2009-08-28 14:16 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [Objective-C Runtime Podcast Episode at Mobile Orchard](https://www.mikeash.com/pyblog/objective-c-runtime-podcast-episode-at-mobile-orchard.html)  
Previous article: [Unicode Comments Support](https://www.mikeash.com/pyblog/unicode-comments-support.html)  
Tags: [fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [gcd](https://www.mikeash.com/pyblog/?tag=gcd) [performance](https://www.mikeash.com/pyblog/?tag=performance)

Friday Q&A 2009-08-28: Intro to Grand Central Dispatch, Part I: Basics and Dispatch Queues

by [Mike Ash](https://www.mikeash.com/)

**What Is It?**  
 Grand Central Dispatch, or GCD for short, is a low level API which introduces a new way to perform concurrent programming. For basic functionality it's a bit like NSOperationQueue, in that it allows a program's work to be divided up into individual tasks which are then submitted to work queues to run concurrently or serially. It's lower level and higher performance than NSOperationQueue, and is not part of the Cocoa frameworks.

In addition to the facilities for parallel execution of code, GCD also provides a fully integrated event handling system. Handlers can be set up to respond to events on file descriptors, mach ports, and processes, to timers and signals, and to user-generated events. These handlers are executed through the GCD facilities for concurrent execution.

GCD's API is heavily based around blocks, which I talked about in previous Friday Q&A's, first to [introduce the basics of blocks](https://www.mikeash.com/pyblog/friday-qa-2008-12-26.html) and then to [discuss the practical aspects of using blocks in real-world code](https://www.mikeash.com/pyblog/friday-qa-2009-08-14-practical-blocks.html). While GCD can be used without blocks, by using the traditional C mechanism of providing a function pointer and a context pointer, it's vastly easier to use and ultimately more capable, from a practical standpoint, when used with blocks.

For documentation on GCD, start with `man dispatch` on a Snow Leopard machine.

**Why Use It?**  
 GCD offers many advantages over traditional multi-threaded programming:

1. **Ease of use:** GCD is much easier to work with than threads. Because it's based around work units rather than threads of computation, it can take care of common tasks such as waiting for work to finish, monitoring file descriptors, executing code periodically, and suspending work. The blocks-based APIs make it extremely easy to pass context between different sections of code.
2. **Efficiency:** GCD is implemented in a lightweight manner which makes it practical and fast to use GCD in many places where creating dedicated threads is too costly. This ties into ease of use: part of what makes GCD so easy to use is that for the most part you can just use it, and not worry too much about using it efficiently.
3. **Performance:** GCD automatically scales its use of threads according to system load, which in turn leads to fewer context switches and more computational efficiency.

**Dispatch Objects**  
 Although pure C, GCD is built in an object-oriented style. GCD objects are called dispatch objects. Dispatch objects are reference counted, much like Cocoa objects. The `dispatch_retain` and `dispatch_release` functions can be used to manipulate the reference count of dispatch objects for the purposes of memory management. Note that unlike Cocoa objects, dispatch objects do _not_ participate in garbage collection, so you will have to manage GCD objects manually even if you have GC enabled.

Dispatch queues and dispatch sources (more on what these are later) can be suspended and resumed, can have an arbitrary context pointer associated with them, and can have a finalizer function associated with them. For more information on these facilities, see `man dispatch_object`.

**Dispatch Queues**  
 A fundamental concept in GCD is that of the dispatch queue. A dispatch queue is an object which accepts jobs and which executes them in the order in which they arrive. A dispatch queue can either be concurrent or serial. A concurrent queue will execute many jobs simultaneously, as appropriate for system load, much like NSOperationQueue. A serial queue will only execute a single job at a time.

There are three main types of queues in GCD:

1. **The main queue:** Analogous to the main thread. In fact, jobs submitted to the main queue execute on the main thread of the process. The main queue can be obtained by calling `dispatch_get_main_queue()`. Since the main queue is inherently tied to the main thread, it is a serial queue.
2. **Global queues:** Global queues are concurrent queues shared through the entire process. Three global queues exist: a high, a default, and a low priority queue. Global queues can be accessed by calling `dispatch_get_global_queue` and telling it which priority you want.
3. **Custom queues:** Custom queues (GCD does not call them this, but doesn't have a specific name for these, so I call them "custom") are queues created with the `dispatch_queue_create` function. These are serial queues which only execute one job at a time. Because of this, they can be used as a synchronization mechanism, much like a mutex in a traditional threaded program.

**Creating Queues**  
 If you want to use a custom queue, you'll have to create one. To do this, just call `dispatch_queue_create`. The first parameter is a label, which is purely for debugging purposes. Apple recommends using reverse-DNS naming to give the queue a unique name, like `"com.yourcompany.subsystem.task"`. These names show up in crash logs and can be queried from the debugger and will help a lot when trying to see where things went wrong. The second argument is an attribute argument which is currently unsupported, so pass `NULL`.

**Submitting Jobs**  
 Submitting a job to a queue is easy: call the `dispatch_async` function, and pass it a queue and a block. The queue will then execute that block when it's that block's turn to execute. Here is an example of executing some long-running job in the background using a global queue:

```
    dispatch_async(dispatch_get_global_queue(DISPATCH_QUEUE_PRIORITY_DEFAULT, 0), ^{
        [self goDoSomethingLongAndInvolved];
        NSLog(@"Done doing something long and involved");
    });
```

`dispatch_async` returns immediately, and then the block will execute asynchronously in the background.

Of course, it's not really very useful to perform an `NSLog` when the work is done. In a typical Cocoa application, you probably want to update a part of your GUI, and that in turn means running code on the main thread. You can easily accomplish this by using nested dispatches, with the outer one performing the background work, and then from within the background block dispatching onto the main queue, like this:

```
    dispatch_async(dispatch_get_global_queue(DISPATCH_QUEUE_PRIORITY_DEFAULT, 0), ^{
        [self goDoSomethingLongAndInvolved];
        dispatch_async(dispatch_get_main_queue(), ^{
            [textField setStringValue:@"Done doing something long and involved"];
        });
    });
```

There is also a `dispatch_sync` function, which does the same thing but which waits for the block to complete before returning. In conjunction with the `__block` type qualifier, this can be used to get a value back from the executing block. For example, you may have some code running on a background thread (or better yet, a non-main dispatch queue) which needs to get a value from a GUI control. You can do this easily by using `dispatch_sync` and `dispatch_get_main_queue`:

```
    __block NSString *stringValue;
    dispatch_sync(dispatch_get_main_queue(), ^{
        // __block variables aren't automatically retained
        // so we'd better make sure we have a reference we can keep
        stringValue = [[textField stringValue] copy];
    });
    [stringValue autorelease];
    // use stringValue in the background now
```

It can be better to use a more asynchronous programming style, however. Rather than block background processing to fetch the GUI value, you can use nested blocks to terminate background processing, execute your fetch on the main thread, and then simply submit further processing back in the background. You can write code like this instead:

```
    dispatch_queue_t bgQueue = myQueue;
    dispatch_async(dispatch_get_main_queue(), ^{
        NSString *stringValue = [[[textField stringValue] copy] autorelease];
        dispatch_async(bgQueue, ^{
            // use stringValue in the background now
        });
    });
```

Depending on your needs, `myQueue` could be a custom queue or it could just be one of the global queues.

**Replacing Locks**  
 Custom queues can be used as a synchronization mechanism in place of locks. In traditional multi-threaded programming, you might have an object which is designed to be usable from multiple threads. In order to accomplish this, it protects all accesses to shared data using a lock, which you might find in an instance variable:

```
    NSLock *lock;
```

Then accesses look like this:

```
    - (id)something
    {
        id localSomething;
        [lock lock];
        localSomething = [[something retain] autorelease];
        [lock unlock];
        return localSomething;
    }
    
    - (void)setSomething:(id)newSomething
    {
        [lock lock];
        if(newSomething != something)
        {
            [something release];
            something = [newSomething retain];
            [self updateSomethingCaches];
        }
        [lock unlock];
    }
```

Using GCD, you can replace the instance variable with a queue:

```
    dispatch_queue_t queue;
```

In order to be used as a synchronization mechanism, the queue must be a custom queue, not a global queue, so you would initialize it using `dispatch_queue_create`. You would then wrap all code accessing shared data in `dispatch_async` or `dispatch_sync`:

```
    - (id)something
    {
        __block id localSomething;
        dispatch_sync(queue, ^{
            localSomething = [something retain];
        });
        return [localSomething autorelease];
    }
    
    - (void)setSomething:(id)newSomething
    {
        dispatch_async(queue, ^{
            if(newSomething != something)
            {
                [something release];
                something = [newSomething retain];
                [self updateSomethingCaches];
            }
        });
    }
```

Note that dispatch queues are extremely lightweight so it's entirely reasonable to use them just as often as you would use a lock.

At this point you may be asking, this is all well and good, but what's the point? I just switched code from one mechanism to another mechanism that looks pretty much the same. Why would you do this?

There are actually several advantages to the GCD approach:

1. **Parallelism:** Notice how `-setSomething:` uses `dispatch_async` in the second version of the code. This means that the call to `-setSomething:` will return right away, and then the bulk of the work will happen in the background. This could be a significant win if `updateSomethingCaches` is a costly operation and the caller will be doing something processor intensive as well.
2. **Safety:** It's impossible to accidentally write a code path that doesn't unlock the lock using GCD. In normal locked code it's not unusual to inadvertently put a return statement in the middle of the lock, or conditionalize the exit, or something equally unfortunate. With GCD, the queue always continues to run and you can't help but return control to it normally.
3. **Control:** It's possible to suspend and resume dispatch queues at will, which cannot easily be done with a locks-based approach. It's also possible to point a custom queue at another dispatch queue, making it inherit the attributes of that other dispatch queue. Using this, the priority of the queue can be adjusted by making it point to the different global queues, and the queue can even be made to execute code on the main thread if this were required for some reason.
4. **Integration:** The GCD event system integrates with dispatch queues. Any events or timers that the object needs to use can be pointed at the object's queue, causing the handlers to automatically run on that queue, making them automatically synchronized with the object.

**Conclusion**  
 Now you know the basics of Grand Central Dispatch, how to create dispatch queues, how to submit jobs to dispatch queues, and how to use queues as a substitute for locks in multithreaded programs. Next week I'll show you techniques for using GCD to write code which performs parallel processing to extract more performance out of multi-core systems. And in the coming weeks, I'll discuss more of GCD in depth, including the event system and queue targeting.

That wraps up this week's Friday Q&A. Come back next week for more GCD goodness. And just because I have a subject mapped out for a few weeks doesn't mean I don't need your suggestions. Quite the contrary: Friday Q&A is driven by your suggestions, and the more I have, the better posts I'll be able to make when I get to the end of this series. If you have a suggestion for a topic to cover, please post it in the comments or [e-mail it directly to me](mailto:mike@mikeash.com).

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

Comments:

---

[Comments RSS feed for this page](https://www.mikeash.com/commentsrss.py?page=pyblog/friday-qa-2009-08-28-intro-to-grand-central-dispatch-part-i-basics-and-dispatch-queues.html)

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.

Code syntax highlighting thanks to [Pygments](http://pygments.org/).
