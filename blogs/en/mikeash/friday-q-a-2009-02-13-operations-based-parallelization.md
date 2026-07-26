---
title: 'Friday Q&A 2009-02-13: Operations-Based Parallelization'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2009-02-13-operations-based-parallelization.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:4b4ace7da346c541'
translated: false
---

> 原文：[Friday Q&A 2009-02-13: Operations-Based Parallelization](https://www.mikeash.com/pyblog/friday-qa-2009-02-13-operations-based-parallelization.html)　·　mikeash.com Friday Q&A

Posted at 2009-02-13 20:31 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [Friday Q&A 2009-02-20: The Good and Bad of Distributed Objects](https://www.mikeash.com/pyblog/friday-qa-2009-02-20-the-good-and-bad-of-distributed-objects.html)  
Previous article: [Late Night Cocoa: NSOperationQueue Problems](https://www.mikeash.com/pyblog/late-night-cocoa-nsoperationqueue-problems.html)  
Tags: [fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [nsoperationqueue](https://www.mikeash.com/pyblog/?tag=nsoperationqueue) [performance](https://www.mikeash.com/pyblog/?tag=performance)

Friday Q&A 2009-02-13: Operations-Based Parallelization

by [Mike Ash](https://www.mikeash.com/)

**What It's For**  
 Parallel processing is becoming more and more important. Right now, good parallelization can result in perhaps a factor of eight speedup to your application compared to a non-parallel implementation, on high-end hardware and with the right sort of computation. More realistically you'll probably see less than that, but even a 50% speedup is nothing to sneeze at, and it's not that hard to get significantly more on a Mac Pro. The future looks to be just more and more cores too, so today's 50% speedup on a dual-core machine might become much more on tomorrow's 32-core monster.

Splitting a program into discretely-executable chunks, or operations, is a good way to parallelize it. Apple introduced this idea on Mac OS X with NSOperationQueue, which provides a nice API for it. Unfortunately, they [totally screwed up the implementation](https://www.mikeash.com/pyblog/dont-use-nsoperationqueue.html) so you might not want to use it now, but the concept is still very useful, whether you're waiting for Apple to fix NSOperationQueue, using a similar API like [RAOperationQueue](http://www.rogueamoeba.com/utm/2008/12/01/raoperationqueue-an-open-source-replacement-for-nsoperationqueue/) or are just doing multithreading the old fashioned way.

**Design Approaches**  
 First, think about your program and what it does. A single-threaded program is a serialized list of actions, performed in order. Sometimes they're performed in order because the second action depends on the results of the first. But sometimes it's simply because the program has to do two things, and if you're single-threaded then you need to pick one to do first.

Try to find those unrelated actions where order doesn't matter. Loops are often a good candidate for this sort of thing. Imagine something like this:

```
    for(NSImage *image in images) {
        [self rotate:image];
        [self scale:image];
        [self save:image];
    }
```

There are no dependencies between those images, so each one can go into a separate operation. On the other hand, each individual method call within the loop depends on the previous one, so those can't be split out beneficially.

It can go beyond loops, too. Imagine some code like this:

```
    [self loadImage];
    [self parseDictionary];
    [self setupNetworkListener];
    [self getDirectoryListing];
```

If these methods have no interdependencies, as their names imply, then they too can be broken out into separate operations for parallel execution.

One question to ask here is whether you _should_ break them out. Is it a win?

The answer to that question will depend greatly on how long it takes to complete the operation. There's always going to be extra overhead for a parallel operation, and you don't want that overhead to overwhelm the gains you get. As a _general_ guideline (very general, overhead will vary a lot depending on what you're using to do parallel processing), figure that if your operation finishes in less than a millisecond it's probably not worth it. As always when it comes to performance optimization, measure before and after to see if you achieved a speedup, and profile to make sure you're hitting the parts that will do the most good.

It will also depend on exactly what your operations are doing. For example, if you have one I/O-bound operation (reading a bunch of stuff from a disk) and a bunch of CPU-bound operations, you'll benefit from having that I/O-bound operation sit in the background and let the CPU-bound operations get on with their tasks. You'll also benefit from running the CPU-bound operations simultaneously to benefit from multi-core machines. On the other hand, if all you have is a bunch of I/O bound operations, you're likely to make your performance _worse_ if you try to run many of them in parallel, due to disk contention.

The key to this style of parallel programming is functional programming. By that I mean programming in the style of mathematical functions. The key attrtibute of mathematical functions is that they always give the same result if you give them the same argument. For example, if `f(3) = 5` then `f(3)` will _always_ give you `5`. This means essentially, that there are no side effects. Side effects are death for parallel programming. Side effects means dealing with external data, which means _shared_ data, which means synchronization, locks, and all pain that brings. It's much better if you can write your operations in terms of computing a function based on some arguments but nothing else.

**Wrapping Up**  
 Parallel programming is challenging and rewarding, and has many complicating factors, but I hope this gives you some ideas to start with. While I don't recommend using NSOperationQueue in any shipping product, it can be a good learning tool, and if you're starting on something new that can require Snow Leopard it's probably a good bet. Even if you can't use it, doing your own custom multithreading in such a way as to deal with discrete operations like this can be a big help in avoiding the locking and concurrency hell that plagues so many multithreaded programs.

That wraps it up. Come back next week for the exciting conclusion, including what happened to the horse, where they hid the loot, and why are there so many pigeons in there anyway?

Leave your comments on this post below. Hate multithreading? Have your own battle story to share? Post it below. Also post any suggestions you might have for future editions of Friday Q&A, or [e-mail them directly](mailto:mike@mikeash.com) (tell me if you don't want your name to be used). Remember, Friday Q&A is fueled by your ideas, so send them in!

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

Comments:

---

Comments RSS feed for this page

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.

Code syntax highlighting thanks to [Pygments](http://pygments.org/).
