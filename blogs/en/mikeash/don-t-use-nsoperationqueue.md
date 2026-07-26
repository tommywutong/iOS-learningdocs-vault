---
title: 'Don''t Use NSOperationQueue'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/dont-use-nsoperationqueue.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:47d9df4dafc7fb38'
translated: false
---

> 原文：[Don't Use NSOperationQueue](https://www.mikeash.com/pyblog/dont-use-nsoperationqueue.html)　·　mikeash.com Friday Q&A

Posted at 2008-11-30 23:36 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [RAOperationQueue, an open-source replacement for NSOperationQueue](https://www.mikeash.com/pyblog/raoperationqueue-an-open-source-replacement-for-nsoperationqueue.html)  
Previous article: [Key-Value Observing Done Right](https://www.mikeash.com/pyblog/key-value-observing-done-right.html)  
Tags: [nsoperationqueue](https://www.mikeash.com/pyblog/?tag=nsoperationqueue) [osbug](https://www.mikeash.com/pyblog/?tag=osbug)

Don't Use NSOperationQueue

by [Mike Ash](https://www.mikeash.com/)

**The Bug**

The bug can be demonstrated very easily with this code:

```
    #import <Foundation/Foundation.h>
    
    @interface Tester : NSObject
    {
        NSOperationQueue *_queue;
    }
    
    - (void)test;
    
    @end
    
    @implementation Tester
    
    - (id)init
    {
        if((self = [super init]))
        {
            _queue = [[NSOperationQueue alloc] init];
            [_queue setMaxConcurrentOperationCount:1];
        }
        return self;
    }
    
    - (void)test
    {
        NSInvocationOperation *op = [[NSInvocationOperation alloc]
    initWithTarget:self selector:_cmd object:nil];
        [_queue addOperation:op];
        [op release];
    }
    
    @end
    
    int main(int argc, char **argv)
    {
        [NSAutoreleasePool new];
    
        NSMutableArray *testers = [NSMutableArray array];
        int i;
        for(i = 0; i < 10; i++)
            [testers addObject:[[[Tester alloc] init] autorelease]];
    
        for(Tester *tester in testers)
            [tester test];
    
        while(1) sleep(1000);
    }
```

On my machine this will die within 10 seconds, throwing this exception:

```
    *** -[NSInvocationOperation start]: receiver has already started or finished
```

Which is thrown with this backtrace:

```
    #0  0x96480ff4 in ___TERMINATING_DUE_TO_UNCAUGHT_EXCEPTION___ ()
    #1  0x9207ee3b in objc_exception_throw ()
    #2  0x92db74de in -[NSOperation start] ()
    #3  0x92db7112 in __runop ()
    #4  0x902ae1f7 in _pthread_wqthread ()
    #5  0x902ae0aa in start_wqthread ()
```

Note that the bug appears to be hardware-dependent. A bunch of people have tried this code and nobody has ever made it crash on a PowerPC machine yet, so it seems that it's Intel-only.

The bug is also very rare. I discovered it in some audio processing code that was enqueueing roughly 500 NSOperations per second. It would take about an hour to crash. This was, as you can imagine, a whole lot of fun to debug.

The crash will still happen even if the above code is modified to enqueue NSOperations separately rather than doing that unusual trick of having one NSOperation enqueue a new one. Leaving off the call to `setMaxConcurrentOperationCount:` also doesn't help. Indeed, just about the only thing that seems to help is to only have a single NSOperationQueue running at a time. Since you can't prevent framework code from running its own NSOperationQueue, this is an untenable solution.

**The Cause**

NSOperationQueue works by managing a thread pool. The pool is global, which is to say that it's shared among all NSOperationQueues in a process. NSOperationQueue uses a private API to examine system load and spawn more worker threads or kill excess ones as needed to keep the system fully utilized without too much overhead.

From what I was able to determine from examining a crashed program, it appears that there's a race condition in the worker thread pool. They dequeue NSOperations from a set of internal queues, and it appears that when the timing is just wrong, the same NSOperation can get dequeued by two worker threads simultaneously. Since this is never supposed to happen, havoc ensues.

**What You Can Do About It**

Unfortunately the answer is, "not much". The bug is firmly in Apple's code and at this point it's doubtful that they'll fix it in Leopard. Your options are:

1. **File a bug.** Apple probably won't fix it for Leopard, but if enough people complain maybe they'll change their mind. If you do file a bug, you can reference my bug, which is bug ID [6332143](rdar://6332143).
2. **Wait for 10.6.**. It appears likely that 10.6 will not share this bug. If you can wait for 10.6 to ship, writing your software to require 10.6 is an easy "fix" for this bug.
3. **Go back to older concurrency models.** Switch to raw threads and you'll (mostly) only have your own bugs to contend with, not Apple's. Depending on your needs, it may not be difficult to implement an NSOperationQueue workalike which supports the subset of NSOperationQueue's capabilities that you need. For the software which led me to find this bug, I wrote my own queue subclass which offered prioritized access to a single worker thread in about a day, and made it [lockless](https://www.mikeash.com/pyblog/late-night-cocoa.html) to boot.
4. **Eliminate concurrency.** Sometimes NSOperation is used just as an optimization to take advantage of multiple cores, or to avoid blocking a thread. In those cases it may be reasonable to simply drop back to a slower serialized method or to simply block until the work is complete.

This bug is really unfortunate, as NSOperation/NSOperationQueue present a fairly nice API (although far too dependent on [KVO](https://www.mikeash.com/pyblog/key-value-observing-done-right.html)) and there's no decent workaround and a low probability of a fix before Snow Leopard ships. But at least now you know about it!

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

Comments:

---

[Comments RSS feed for this page](https://www.mikeash.com/commentsrss.py?page=pyblog/dont-use-nsoperationqueue.html)

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.

Code syntax highlighting thanks to [Pygments](http://pygments.org/).
