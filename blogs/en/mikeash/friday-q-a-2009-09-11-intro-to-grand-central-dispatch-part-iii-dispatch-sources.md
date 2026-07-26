---
title: 'Friday Q&A 2009-09-11: Intro to Grand Central Dispatch, Part III: Dispatch Sources'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2009-09-11-intro-to-grand-central-dispatch-part-iii-dispatch-sources.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:66bed6781cfc2da7'
translated: false
---

> 原文：[Friday Q&A 2009-09-11: Intro to Grand Central Dispatch, Part III: Dispatch Sources](https://www.mikeash.com/pyblog/friday-qa-2009-09-11-intro-to-grand-central-dispatch-part-iii-dispatch-sources.html)　·　mikeash.com Friday Q&A

Posted at 2009-09-11 15:28 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [GCD Is Not Blocks, Blocks Are Not GCD](https://www.mikeash.com/pyblog/gcd-is-not-blocks-blocks-are-not-gcd.html)  
Previous article: [Friday Q&A 2009-09-04: Intro to Grand Central Dispatch, Part II: Multi-Core Performance](https://www.mikeash.com/pyblog/friday-qa-2009-09-04-intro-to-grand-central-dispatch-part-ii-multi-core-performance.html)  
Tags: [fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [gcd](https://www.mikeash.com/pyblog/?tag=gcd) [performance](https://www.mikeash.com/pyblog/?tag=performance)

Friday Q&A 2009-09-11: Intro to Grand Central Dispatch, Part III: Dispatch Sources

by [Mike Ash](https://www.mikeash.com/)

Note that I assume you've already read the first two posts in this series. The first post is particularly important, the second one less so. If you have not, go read them now.

Before I go any further, there's been some great news this week: [GCD has been open sourced](http://libdispatch.macosforge.org/)! This is a very nice move on Apple's part. The source is relatively clean and very interesting to read through.

**What Are Dispatch Sources**  
 In short, a dispatch source is an object which monitors for some type of event. When the event occurs, it automatically schedules a block for execution on a dispatch queue.

That's kind of vague. What kind of events are we talking about?

Here is the full list of events supported by GCD in 10.6.0:

1. Mach port send right state changes.
2. Mach port receive right state changes.
3. External process state change.
4. File descriptor ready for read.
5. File descriptor ready for write.
6. Filesystem node event.
7. POSIX signal.
8. Custom timer.
9. Custom event.

That's a lot of useful stuff. It's basically everything

supports, plus mach ports, plus built-in support for timers (instead of having to build your own using the timeout parameter), plus custom events.

**Custom Events**  
 Most of these events are pretty much self explanatory, but you may be wondering what a custom event is. In short, this is an event which you signal yourself by calling the `dispatch_source_merge_data` function.

This is a bit of an odd name for a function that signals an event. The reason it's named this way is because GCD will automatically coalesce multiple events that happen before the event handler has a chance to run. You can "merge" data into the dispatch source as many times as you want, and if the dispatch queue was busy for this whole period, GCD will only invoke the event handler once.

Two types of custom events are available, `DISPATCH_SOURCE_TYPE_DATA_ADD` and `DISPATCH_SOURCE_TYPE_DATA_OR`. A custom event source has an `unsigned long data` attribute, and you also pass an `unsigned long` to `dispatch_source_merge_data`. When using the `_ADD` variant, events are coalesced by adding all of the numbers together. When using the `_OR` variant, events are coalesced by doing a logical or. When the event handler executes, it can access the current value using `dispatch_source_get_data`, and the data is then reset to 0.

Let's look at a scenario where this could be useful. Imagine some asynchronous code performing some work that needs to update a progress bar. Since the main thread is just another dispatch queue to GCD, we can push the GUI work onto the main queue. However, there may be a lot of events, and we don't want to make redundant updates to the GUI; it's much better to coalesce all of the changes as much as possible if the main thread is busy with other work.

Dispatch sources are perfect for this, using the `DISPATCH_SOURCE_TYPE_DATA_ADD` type. We can merge the amount of work done, and then the main thread code can find out how much work has been performed since the last event, and update the progress indicator by that amount.

Enough talk, here's some code:

```
    dispatch_source_t source = dispatch_source_create(DISPATCH_SOURCE_TYPE_DATA_ADD, 0, 0, dispatch_get_main_queue());
    dispatch_source_set_event_handler(source, ^{
        [progressIndicator incrementBy:dispatch_source_get_data(source)];
    });
    dispatch_resume(source);
    
    dispatch_apply([array count], globalQueue, ^(size_t index) {
        // do some work on data at index
        dispatch_source_merge_data(source, 1);
    });
```

(I want to make one note about this code, about something that stymied me to no end when I first started working with dispatch sources. It bothered me enough that I'm going to put it in bold.

)

Assuming you've configured the progress indicator to have the correct min/max value, this will all work perfectly. The data will be processed in parallel. As each chunk of data finishes, it signals the dispatch source and adds 1 to the dispatch source data, which we treat as the number of work units completed. The event handler increments the progress indicator by the number of work units that have been completed since the last time it ran. If the main thread is idle and work units complete slowly, the event handler will be called for every work unit completion, giving real time results. If the main thread is busy or work units complete quickly, completion events will be coalesced and the progress indicator will only be updated one time each time the main thread becomes available to process it.

At this point you may be thinking, this all sounds great, but what if I don't _want_ my events to be coalesced? Sometimes you just want every signal to cause an action, without any smarts going on behind the scenes. Well, this is actually really easy, you just need to think a bit outside the box. If you want every signal to cause an action, use `dispatch_async` instead of a dispatch source. That's what it does, after all: schedules a block to be executed on the queue in question. In fact, the only reason to use a dispatch source instead of `dispatch_async` is to take advantage of coalescing.

**Built-In Events**  
 That's how to use a custom event, how about a built-in event? Let's look at an example of reading from standard input using GCD:

```
    dispatch_queue_t globalQueue = dispatch_get_global_queue(DISPATCH_QUEUE_PRIORITY_DEFAULT, 0);
    dispatch_source_t stdinSource = dispatch_source_create(DISPATCH_SOURCE_TYPE_READ,
                                                           STDIN_FILENO,
                                                           0,
                                                           globalQueue);
    dispatch_source_set_event_handler(stdinSource, ^{
        char buf[1024];
        int len = read(STDIN_FILENO, buf, sizeof(buf));
        if(len > 0)
            NSLog(@"Got data from stdin: %.*s", len, buf);
    });
    dispatch_resume(stdinSource);
```

This is pretty easy! Since we used a global queue, the handler automatically runs in the background, in parallel to the rest of the application, meaning an automatic parallel speed boost if the application is doing anything else at the time the event comes in.

This also has a nice benefit over the standard UNIX way of doing things in that there's no need to write a loop. With typical calls to `read`, you always have to be wary because it can return less data than requested, and can also suffer from transient "errors" like `EINTR` (interrupted system call). With GCD, you can just bail out in those cases and not do anything. If you leave unread data on the file descriptor, GCD will just invoke your handler a second time.

For standard input it's not a problem, but for other file descriptors you need to consider how to clean up once you're done reading from (or writing to) the descriptor. You must not close the descriptor while the dispatch source is still active. If another file descriptor is created (perhaps from another thread) and happens to get the same number, your dispatch source will suddenly be reading from (or writing to) something it shouldn't be. This will not be fun to debug.

The way to properly implement cleanup is to use `dispatch_source_set_cancel_handler` and give it a block which closes your file descriptor. You can then use `dispatch_source_cancel` to cancel the dispatch source, causing the handler to be invoked and the file descriptor to be closed.

Using other dispatch source types is much the same. In general, you give the identifier of the source (mach port, file descriptor, process ID, etc.) as the dispatch source handle. The mask argument is usually unused, but for `DISPATCH_SOURCE_TYPE_PROC` indicates what kind of process events you're interested in receiving. Then just provide a handler, resume the source, and off you go. These dispatch sources also provide source-specific data which can be accessed using the `dispatch_source_get_data` function. For example, file descriptors will give the rough number of bytes available on the descriptor as the dispatch source data. Process sources will give a mask of events which occurred since the last call. For a complete listing of what the data means for each type of source, see the man page.

**Timers**  
 Timer events are a bit different. They don't use the handle/mask arguments, but instead use a separate function, `dispatch_source_set_timer`, to configure the timer. This function takes three separate parameters to control when the timer fires:

The `start` parameter controls when the timer first fires. This parameter is of type `dispatch_time_t`, which is an opaque type that you can't manipulate directly. The functions `dispatch_time` and `dispatch_walltime` can be used to create them, and the constants `DISPATCH_TIME_NOW` and `DISPATCH_TIME_FOREVER` can be used if those are the values you're after.

The `interval` argument is an integer and is self explanatory. The `leeway` argument is an interesting one. This argument tells the system how much precision you want on your timer firing. Timers are never guaranteed to be absolutely 100% precise, but this argument lets you tell the system how hard you want it to try. If you want a timer to fire every 5 seconds and be as exact as possible, you would pass 0. On the other hand, consider a periodic task like checking for new e-mail. You want to check every 10 minutes, but this doesn't have to be exact. You might pass a leeway of 60 seconds, telling the system that you'll accept the timer running up to 60 seconds later than the scheduled time.

What's the point of this? In short, reduced power consumption. It's more energy efficient if the OS can let the CPU sleep for as long as possible, and then accomplish a bunch of things at once when it wakes up, rather than cycling between sleep and wake constantly to accomplish tasks in a spread-out manner. By giving a large leeway to your timer, you allow the system to lump your timer with other actions in order to group tasks together like this.

**Conclusion**  
 Now you know how to use GCD's dispatch source facilities to monitor file descriptors, run timers, coalesce custom events, and other similar activities. Because dispatch sources are fully integrated with dispatch queues, you can use any dispatch queue you have available. You can have a dispatch source run its handler on the main thread, in parallel on one of the global queues, or serialized with respect to a particular module of your program by using a custom queue.

That's it for this week. Come back next week as I wrap up the discussion of Grand Central Dispatch and talk about how to suspend, resume, and retarget dispatch queues, how to use dispatch semaphores, and how to use GCD's one-time initialization facility. As always, if you have a suggestion for a topic to cover for a future Friday Q&A, please post it in the comments or [e-mail it directly to me](mailto:mike@mikeash.com).

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

Comments:

---

Comments RSS feed for this page

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.

Code syntax highlighting thanks to [Pygments](http://pygments.org/).
