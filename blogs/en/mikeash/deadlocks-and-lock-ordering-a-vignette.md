---
title: 'Deadlocks and Lock Ordering: a Vignette'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/deadlocks-and-lock-ordering-a-vignette.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:7ea9d4eb35fa3e1d'
translated: false
---

> 原文：[Deadlocks and Lock Ordering: a Vignette](https://www.mikeash.com/pyblog/deadlocks-and-lock-ordering-a-vignette.html)　·　mikeash.com Friday Q&A

Posted at 2012-02-13 04:26 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [Friday Q&A 2012-02-17: Ring Buffers and Mirrored Memory: Part II](https://www.mikeash.com/pyblog/friday-qa-2012-02-17-ring-buffers-and-mirrored-memory-part-ii.html)  
Previous article: [Friday Q&A 2012-02-03: Ring Buffers and Mirrored Memory: Part I](https://www.mikeash.com/pyblog/friday-qa-2012-02-03-ring-buffers-and-mirrored-memory-part-i.html)  
Tags: [evil](https://www.mikeash.com/pyblog/?tag=evil) [objectivec](https://www.mikeash.com/pyblog/?tag=objectivec) [threading](https://www.mikeash.com/pyblog/?tag=threading)

Deadlocks and Lock Ordering: a Vignette

by [Mike Ash](https://www.mikeash.com/)

The solution to this conundrum is to enforce a lock order. Sometimes there's a natural ordering, like parent and child. But sometimes you just have two locks and you need to take both. Code like this can be dangerous:

```
    @synchronized(a)
    {
        @synchronized(b)
        {
            // do stuff
        }
    }
```

If two threads have opposite ideas of what `a` and `b` are, this carries the potential for deadlock. Some way needs to be found to ensure that every thread locks the same object first. In the absence of any other way to do it, an ordering can be imposed on these objects by comparing their addresses. If we always lock the one with the lower address first, we'll never deadlock, even with multiple threads grabbing the objects from different sources and not communicating with each other.

Fortunately, this comparison is easy, since C allows using the comparison operators on pointers of the same type:

```
    id min, max;
    if(a < b)
        min = a, max = b;
    else
        min = b, max = a;

    @synchronized(min)
    {
        @synchronized(max)
        {
            // do stuff, safely
        }
    }
```

This eliminates the risk of deadlock. Hooray!

You might notice that the code for finding the object with the lower address looks sort of like the code you might write for finding the smaller integer from two different `int` varibables. Sort of _exactly_ like the equivalent code for integers, in fact. The only difference is the types.

Thus the punchline: Cocoa's `MIN` and `MAX` variables, being written in a completely type-generic fashion, work on object pointers just as well as they do integers and floats. They can be used to solve this problem a little more nicely:

```
    @synchronized(MIN(a, b))
    {
        @synchronized(MAX(a, b))
        {
            // do stuff, safely
        }
    }
```

This code is equivalent to the above, but much more compact without sacrificing any readability or safety. Except for the part where you use `MIN` and `MAX` on pointers, you might consider that to sacrifice readability. Depends on personal taste.

This works with other locking constructs as well. For example:

```
    NSLock *aLock = [[NSLock alloc] init];
    NSLock *bLock = [[NSLock alloc] init];

    ...

    [MIN(aLock, bLock) lock];
    [MAX(aLock, bLock) lock];
    // do stuff, safely
    [MAX(aLock, bLock) unlock];
    [MIN(aLock, bLock) unlock];
```

It's a little crazy to see a `MIN` macro as the target of an Objective-C message send expression, but it works just fine. Even pthread mutexes and spinlocks can use this, as long as you apply it to their pointers, and not to the values themselves.

If you ever find yourself needing to acquire two locks at once, first, think very hard to see if you can avoid doing so. But if you must, the `MIN` and `MAX` macros make for an easy way to ensure a consistent, deadlock-free lock ordering across all of your various threads.

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

Comments:

---

[Comments RSS feed for this page](https://www.mikeash.com/commentsrss.py?page=pyblog/deadlocks-and-lock-ordering-a-vignette.html)

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.

Code syntax highlighting thanks to [Pygments](http://pygments.org/).
