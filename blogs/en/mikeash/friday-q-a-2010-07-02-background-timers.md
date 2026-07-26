---
title: 'Friday Q&A 2010-07-02: Background Timers'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2010-07-02-background-timers.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:4789c1578ab46965'
translated: false
---

> 原文：[Friday Q&A 2010-07-02: Background Timers](https://www.mikeash.com/pyblog/friday-qa-2010-07-02-background-timers.html)　·　mikeash.com Friday Q&A

Posted at 2010-07-02 16:45 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [Friday Q&A 2010-07-16: Zeroing Weak References in Objective-C](https://www.mikeash.com/pyblog/friday-qa-2010-07-16-zeroing-weak-references-in-objective-c.html)  
Previous article: [Blocks and GCD in Russian](https://www.mikeash.com/pyblog/blocks-and-gcd-in-russian.html)  
Tags: [blocks](https://www.mikeash.com/pyblog/?tag=blocks) [fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [gcd](https://www.mikeash.com/pyblog/?tag=gcd)

Friday Q&A 2010-07-02: Background Timers

by [Mike Ash](https://www.mikeash.com/)

**Periodic Cleanup**  
 To understand the usefulness of background timers, it's important to understand what kind of problem they're trying to solve.

It's common to have a class which needs to perform some sort of periodic cleanup or dumping. For example, buffered file IO (as done by e.g. `printf`) requires occasionally flushing the buffer to the file. A cache may want to occasionally evict old entries.

As one concrete example, consider an implementation of `NSMutableArray`. The array needs to manage storage for its contents, which it allocates with `malloc`. When an object is added that exceeds the current storage size, it uses `realloc` to grow the array. When it shrinks enough to justify it, it uses `realloc` to shrink the array.

The key is "enough to justify it". When is it enough?

One strategy would be to shrink it every time the current allocation was less than half full. However, imagine that you remove a lot of elements, but leave the array at one element over half full, then let it sit for a long time. You're wasting a lot of space! You could reduce the potential for wasted space by, say, shrinking any time the array is less than 90% full. But that can be inefficient if you're removing a lot of elements right away, or add and remove a lot of objects at a size that causes the array to constantly shrink and then re-grow.

Another strategy would be to shrink it every so many calls, say, every 100 calls. This could be combined with the above so that it would only shrink when there was enough wasted space to justify it. But this, too, could cause a lot of unnecessary shrinking and re-growing with an unfriendly access pattern, or a lot of wasted space if you suddenly leave the array idle on call #99.

Yet another strategy would be to base the decision not on fullness or calls, but on time. Check the array, say, once every half-second while it's in active use. If needed, resize the array. If the array isn't being used, nothing happens.

The natural way to implement this strategy would be with `NSTimer`. Whenever an object is removed from the array, check to see if a timer exists, and if it doesn't, create one with a half-second delay. When the timer fires, resize the array if it's necessary.

Trouble is, `NSTimer` requires an active runloop. If the array is manipulated a lot without returning to the runloop, it won't resize during that period. Worse, if the array is manipulated on a thread that doesn't have an active runloop, it will never resize.

To fix this, you'd want the timer to run on some sort of dedicated background thread. And you'd want to make sure that your normal array code was synchronized with that background thread so that all of your data access was safe.

Of course, Mac OS X already has an API that lets you do work on background threads and synchronize accesses with them: Grand Central Dispatch. GCD even includes timers, although they're not 100% what's wanted here.

Thus, I created a class, `MABGTimer`. It wraps GCD timers to provide the functionality needed to perform these periodic maintenance tasks based on time and in the background.

**Code**  
 As usual, you can get the code that goes along with this post from my public subversion repository:

```
    svn co http://mikeash.com/svn/BackgroundTimer/
```

Or just click on the link above to browse it.

**API**  
 The key public methods of `MABGTimer` are:

```
    - (void)afterDelay: (NSTimeInterval)delay do: (void (^)(id self))block;
    - (void)performWhileLocked: (void (^)(void))block;
    - (void)cancel;
```

After creating the timer, you set up a task by calling

. You give it a delay, and a block to perform after that delay passes. If you call this method multiple times before the delay expires, the timer is either extended or coalesced, depending on settings.

Notice that the block passed to `afterDelay:do:` takes a parameter called `self`. The idea is that `MABGTimer` is initialized with a pointer to the object it's supposed to operate on, and it then passes a pointer to that object as a parameter to the block.

You might wonder, what's the point? After all, the block could simply capture `self` from the enclosing scope. That's what blocks are all about, after all.

The reason for the `self` parameter is that capturing `self` from the enclosing scope sets up a retain cycle. The object will be kept alive by the block until the timer fires. `MABGTimer` keeps a _weak_ reference to the object, so that it can be destroyed at any time. When it is, the object can cancel the timer using the `cancel` method. This allows an object to set up long-term maintenance tasks and then cancel them early if the object is destroyed and no longer needs to perform them. `MABGTimer` then passes that weak reference into the block so it can use the original object without forcing a strong reference.

(Note: it is possible to give the block a weak reference to something in the enclosing scope by declaring a local variable with the `__block` qualifier and capturing that. However, that's more work than simply having a parameter passed in that you can use, so `MABGTimer` does a little extra work to make the client's job easier.)

As I mentioned above, since the timer executes in the background, synchronization is important. The `performWhileLocked:` method takes care of synchronization. Any time you do something with data that is also accessed in the timer block, wrap that code in a call to `performWhileLocked:`, and the timer will ensure that access is synchronized.

To clarify, here's an example of how these methods might be used:

```
    // do some work with non-shared data
    _someIvar++;
    [_someOtherIvar addObject: parameter];
    
    // do some work with timer-accessed data
    __block id resultObject;
    [_timer performWhileLocked: ^{
        // retain here to ensure the object stays live, since
        // this is multithreaded!
        resultObject = [[_cache objectForKey: parameter] retain];
    }];
    // balance the retain
    [resultObject autorelease];
    
    // clean the cache periodically
    [_timer afterDelay: 1.0 do: ^(id self) {
        // DON'T directly access ivars here
        // that will implicitly capture self, and cause a retain cycle
        [self _flushCache];
    }];
    
    return resultObject;
```

**Behaviors**  
 Each call to `afterDelay:do:` does not necessarily result in an invocation of the block passed in. If it's called multiple times before the timer fires, the block is only called once. This means that you should pass the same block each time; if they do different things, some of those things won't get done!

What exactly happens when you call it multiple times depends on how the timer was configured. This is done using _behaviors_, and I currently implement two.

When set with the **coalesce** behavior, the timer fires at the earliest time specified by the calls. In other words, calling with 2 seconds and then with 1 second will fire after 1 second. Calling with 10 seconds, then waiting 1 second, then calling with 5 seconds, will fire at the 6-second mark.

Coalesce is good for periodic maintenance tasks. You can call the timer many times, and it will fire periodically as needed. By passing different delays into the timer, you can handle events with varying urgency. For example, if you write some very low-priority data to a file handle, you might specify a 60-second delay. If you write high-priority data, you might specify a 0.1-second delay. `MABGTimer` will intelligently combine those so that high-priority data following low-priority data will flush the entire cache.

When set with the **delay** behavior, the timer's firing time is reset with each call. This essentially implements an idle timer. As long as your class is active, the timer will continue to reset, but after it's quiet for a while, it will fire. This could be used to implement a GUI control which refreshes an expensive view only when the mouse has stopped moving.

Behaviors are specified when creating the timer object using this method:

```
    - (id)initWithObject: (id)obj behavior: (MABGTimerBehavior)behavior;
```

There is also a convenience initializer:

```
    - (id)initWithObject: (id)obj;
```

This defaults to

behavior, because I think it's the more common one.

**Target Queue**  
 There's also one method for advanced GCD users:

```
    - (void)setTargetQueue: (dispatch_queue_t)target;
```

This allows you to specify a dispatch queue where the

will execute its code. This includes the timer block as well as the block passed to

.

By default, `MABGTimer` runs everything on a private queue targeted to the default-priority global queue. This method could be used to retarget it to a global queue of different priority, to another private queue (to manage suspension behavior) or even to the main queue so you can do GUI work in the timer.

**Implementation**  
 `MABGTimer` has the following instance variables, which should be self-explanatory:

```
    id _obj;
    dispatch_queue_t _queue;
    dispatch_source_t _timer;
    MABGTimerBehavior _behavior;
    NSTimeInterval _nextFireTime;
```

The initializers and

are also pretty simple:

```
    - (id)initWithObject: (id)obj
    {
        return [self initWithObject: obj behavior: MABGTimerCoalesce];
    }
    
    - (id)initWithObject: (id)obj behavior: (MABGTimerBehavior)behavior
    {
        if((self = [super init]))
        {
            _obj = obj;
            _behavior = behavior;
            _queue = dispatch_queue_create("com.mikeash.MABGTimer", NULL);
        }
        return self;
    }
    
    - (void)dealloc
    {
        if(_timer)
        {
            dispatch_source_cancel(_timer);
            dispatch_release(_timer);
        }
        dispatch_release(_queue);
        [super dealloc];
    }
```

And

and

just call through to the appropriate dispatch function:

```
    - (void)setTargetQueue: (dispatch_queue_t)target
    {
        dispatch_set_target_queue(_queue, target);
    }
    
    - (void)performWhileLocked: (dispatch_block_t)block
    {
        dispatch_sync(_queue, block);
    }
```

The

method calls through to an internal

method that's run on the queue. This ensures that cancellation is synchronized with timer activity:

```
    - (void)cancel
    {
        [self performWhileLocked: ^{
            [self _cancel];
        }];
    }
```

And the

method is also simple: if the timer is active, cancel it and destroy it:

```
    - (void)_cancel
    {
        if(_timer)
        {
            dispatch_source_cancel(_timer);
            dispatch_release(_timer);
            _timer = NULL;
        }
    }
```

The meat of the functionality is in

. The first thing it does is run everything synchronized to avoid race conditions and the like:

```
    - (void)afterDelay: (NSTimeInterval)delay do: (void (^)(id self))block
    {
        [self performWhileLocked: ^{
```

It then checks to see whether it needs to reset the timer or not. It needs to reset the timer if the GCD timer doesn't exist (no pending fire has been set up), if the timer is in delay mode, or if the timer is in coalesce mode and the new fire time is before the previous fire time:

```
            BOOL hasTimer = _timer != nil;
            
            BOOL shouldProceed = NO;
            if(!hasTimer)
                shouldProceed = YES;
            else if(_behavior == MABGTimerDelay)
                shouldProceed = YES;
            else if(_behavior == MABGTimerCoalesce && [self _now] + delay < _nextFireTime)
                shouldProceed = YES;
```

Next, if the timer needs to be reset and the GCD timer doesn't exist, create it:

```
            if(shouldProceed)
            {
                if(!hasTimer)
                    _timer = dispatch_source_create(DISPATCH_SOURCE_TYPE_TIMER, 0, 0, _queue);
```

Then it first sets the GCD timer and the

instance variable:

```
                dispatch_source_set_timer(_timer, dispatch_time(DISPATCH_TIME_NOW, delay * NSEC_PER_SEC), 0, 0);
                _nextFireTime = [self _now] + delay;
```

Then it sets the event handler on the timer. The event handler first calls the block that's passed in. Since GCD timers are always repeating, it then calls

to make sure it only fires once, and also to signal to any future calls that the timer is no longer active:

```
                dispatch_source_set_event_handler(_timer, ^{
                    block(_obj);
                    [self _cancel];
                });
```

Finally, if the timer was newly created, resume it so it can become active:

```
                if(!hasTimer)
                    dispatch_resume(_timer);
            }
        }];
    }
```

One last thing, we need an implementation of the

method. This is simple: call

, convert it to seconds:

```
    - (NSTimeInterval)_now
    {
        uint64_t t = mach_absolute_time();
        Nanoseconds nano = AbsoluteToNanoseconds(*(AbsoluteTime *)&t;);
        NSTimeInterval seconds = (double)*(uint64_t *)&nano / (double)NSEC_PER_SEC;
        return seconds;
    }
```

**Conclusion**  
 Background timers are a useful technique for decoupling the timing of calls to an API from the tasks it performs. The repository contains `BackgroundResizingArray`, an implementation of `NSMutableArray` which uses a background timer to implement resizing. Background timers can be useful for networking as well, especially on iOS devices where you want to batch up transmissions to reduce power usage on the cellular radio, or any case where you have a lot of non-urgent messages to send.

That's it for this Friday Q&A. Check back in another two weeks for more gooey goodness. Friday Q&A is driven by reader suggestions (mostly), so if you have an idea for a topic you would like to see covered here, [send it in](mailto:mike@mikeash.com)!

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

No comments have been posted.

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.

Code syntax highlighting thanks to [Pygments](http://pygments.org/).
