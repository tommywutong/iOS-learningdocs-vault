---
title: 'Friday Q&A 2009-09-18: Intro to Grand Central Dispatch, Part IV: Odds and Ends'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2009-09-18-intro-to-grand-central-dispatch-part-iv-odds-and-ends.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:f720aa9e24094594'
translated: false
---

> 原文：[Friday Q&A 2009-09-18: Intro to Grand Central Dispatch, Part IV: Odds and Ends](https://www.mikeash.com/pyblog/friday-qa-2009-09-18-intro-to-grand-central-dispatch-part-iv-odds-and-ends.html)　·　mikeash.com Friday Q&A

Posted at 2009-09-18 17:23 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [Friday Q&A 2009-09-25: GCD Practicum](https://www.mikeash.com/pyblog/friday-qa-2009-09-25-gcd-practicum.html)  
Previous article: [The iPhone Development Story: One Year Later](https://www.mikeash.com/pyblog/the-iphone-development-story-one-year-later.html)  
Tags: [fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [gcd](https://www.mikeash.com/pyblog/?tag=gcd) [performance](https://www.mikeash.com/pyblog/?tag=performance)

Friday Q&A 2009-09-18: Intro to Grand Central Dispatch, Part IV: Odds and Ends

by [Mike Ash](https://www.mikeash.com/)

As with the previous weeks, I will assume that you've read all of the previous articles before reading this one, and are thus familiar with all aspects of GCD discussed up to this point. If you have not already read those articles, please do so now.

**Dispatch Queue Suspension**  
 Dispatch queues can be suspended and resumed at will. To suspend, use the `dispatch_suspend` function, and to resume, use `dispatch_resume`. These work pretty much the way you'd expect them to. Note that they also work on dispatch sources.

One caveat to dispatch queue suspension is that suspension is block-granular. In other words, suspending a queue does _not_ suspend the currently executing block. Instead what happens is that the block is allowed to run to completion, and then no further blocks are allowed to run until the queue (or source) is resumed.

One final note, straight from the man page: you _must_ resume a queue/source before destroying it if you have previously suspended it.

**Dispatch Queue Targeting**  
 All custom dispatch queues have the concept of a target queue. In essence, a custom dispatch queue doesn't actually execute any work, but passes work to its target queue for execution. Normally the target queue of a custom queue is the default-priority global queue.

The target queue of a custom queue can be set by using the `dispatch_set_target_queue` function. You can pass it any other dispatch queue, even another custom queue, so long as you never create a cycle. This function can be used to set the priority of a custom queue by simply setting its target queue to a different global queue. If you set your custom queue's target to be the low priority global queue, all work on your custom queue will execute with low priority, and the same with the high priority global queue.

Another potential use of this is to target a custom queue to the main queue. This will cause all blocks submitted to that custom queue to run on the main thread. The advantage of doing this instead of simply using the main queue directly is that your custom queue can be independently suspended and resumed, and could potentially be retargeted onto a global queue afterwards, although you'll have to be careful to ensure that all blocks which run after that point can tolerate being away from the main thread!

Yet another potential use is to target custom queues to other custom queues. This will force multiple queues to be serialized with respect to each other, and essentially creates a group of queues which can all be suspended and resumed together by suspending/resuming the queue that they target. For a way that this could be used, imagine an application which is scanning a set of directories and loading the files within. In order to avoid disk contention, you want to make sure that only one file loading task is active for each physical disk. However, multiple files can be read from physically separate disks simultaneously. To make this happen, all you have to do is build a dispatch queue structure which mirrors your disk structure.

First, you would scan the system and find the disks, and create a custom dispatch queue for each one. Then you would scan the filesystems and create a custom queue for each one of those as well, pointing their target queues at the queue of the appropriate disk. Finally, each directory scanner can have its own queue as well, pointing the target at the filesystem on which the directory resides. The directory scanners can enumerate their directories and submit a block for each file directly to their own queue. Due to how the system is set up, this will inherently serialize all access to each physical disk while allowing parallel access to separate disks, all without any manual intervention beyond the initial queue setup process.

**Semaphores**  
 Dispatch semaphores work just like any other semaphore and if you're familiar with semaphores from other multithreading systems, this will look entirely familiar to you.

A semaphore is basically an integer which has an initial count and supports two operations: signal and wait. When a semaphore is signaled, the count is incremented. When a thread waits on a semaphore, it will block, if necessary, until the count is greater than 0, and then decrement the count.

Dispatch semaphores are created using `dispatch_semaphore_create`, signaled using `dispatch_semaphore_signal`, and waited on using `dispatch_semaphore_wait`. The man page for these functions shows two good examples of how to use semaphores, one involving synchronizing work completion and one involving controlling access to a finite resource. Rather than make up my own, inferior examples, I encourage you to simply read the man page to see some potential uses for these objects.

**One-Time Initialization**  
 GCD also has support for one-time initialization, which if you're familiar with pthreads is pretty much the same as the `pthread_once` call. The main advantage of the GCD approach is that it uses blocks instead of function pointers, allowing for a more natural flow of code.

A major use of this is for lazily initializing singletons or other shared data in a thread-safe manner. The typical singleton initialization technique looks like this, for singletons that need to be thread safe:

```
    + (id)sharedWhatever
    {
        static Whatever *whatever = nil;
        @synchronized([Whatever class])
        {
            if(!whatever)
                whatever = [[Whatever alloc] init];
        }
        return whatever;
    }
```

This is fine, but expensive; every call to

incurs the expense of taking a lock, even though that lock is basically only needed once. There are fancier ways to approach this, using things like double-checked locking or atomic operations, but they're difficult and extremely error-prone.

Using GCD you can rewrite the above method using `dispatch_once` like so:

```
    + (id)sharedWhatever
    {
        static dispatch_once_t pred;
        static Whatever *whatever = nil;
        dispatch_once(&pred, ^{
            whatever = [[Whatever alloc] init];
        });
        return whatever;
    }
```

This is actually slightly simpler than the

method, and GCD makes sure to do these checks in a fast manner. It ensures that the code in the block will have run before any threads can pass beyond the call to

, but doesn't force code to take the hit of synchronization every time it uses this function. In fact, if you look at the header where this function is declared, you'll discover that the current implementation is actually a macro which performs the initial test inline, meaning that you don't even incur

overhead, much less synchronization overhead, for the common case.

**Conclusion**  
 That wraps up this series on Grand Central Dispatch. This week you saw how to suspend, resume, and retarget dispatch queues, and some uses for these facilities. You also saw how to use dispatch semaphores and one-time initialization facilities. In previous weeks you saw how to manage dispatch objects, how to create/access and use the different types of dispatch queues available for different tasks, strategies for taking advantage of multi-core systems, and how to monitor for events using GCD's events system. Now you have the complete picture of how GCD operates and how to use it, so go out there and write some great new software with it!

Come back next week for another exciting edition of Friday Q&A. As always, if you have a suggestion for a topic to cover, please post it in the comments or [e-mail it directly to me](mailto:mike@mikeash.com).

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

Comments:

---

Comments RSS feed for this page

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.

Code syntax highlighting thanks to [Pygments](http://pygments.org/).
