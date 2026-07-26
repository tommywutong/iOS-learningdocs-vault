---
title: Perform Better With Garbage Collection
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/perform_better_with_garbage_collection.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:a7811326026ceab7'
translated: false
---

> 原文：[Perform Better With Garbage Collection](https://www.mikeash.com/pyblog/perform_better_with_garbage_collection.html)　·　mikeash.com Friday Q&A

Posted at 2007-11-21 04:44 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [Algorithmic Optimizations: a Case Study](https://www.mikeash.com/pyblog/algorithmic-optimizations-a-case-study.html)  
Previous article: [IOCCC 2006 Winners](https://www.mikeash.com/pyblog/ioccc2006.html)  
Tags: [cocoa](https://www.mikeash.com/pyblog/?tag=cocoa) [garbagecollection](https://www.mikeash.com/pyblog/?tag=garbagecollection) [performance](https://www.mikeash.com/pyblog/?tag=performance)

Perform Better With Garbage Collection

by [Mike Ash](https://www.mikeash.com/)

First, the slowness: speed has been one of the big criticisms against garbage collection since the very beginning. A collector must obviously do more work than manual memory management, the logic goes, therefore it must be slower than doing the work yourself. This ignores the extra overhead that manual management imposes, but it was often true with early collectors. Modern collectors are usually very fast, and by eliminating the overhead of manual management (such as the reference counting and autorelease pools used so pervasively in Cocoa), can outperform it. Of course the manual code can be optimized, so it often comes down to getting decent performance for free or putting a lot of effort into great performance, just like so many things in programming.

The Cocoa garbage collector is claimed to be very fast. It certainly should be; although the fact that it has to live within a C world puts certain constraints on what it can do, such as not being able to compact the heap, it is shiny new and should be able to take advantage of many recent techniques. Apple has also wisely limited the scope of its collector, such that it only collects Objective-C objects and memory you explicitly ask it to collect; it does not try to be a general replacement for malloc/free. The impression I get from reading over Apple's literature about the collector is that it performs very well, although I haven't performed any tests.

But beyond basic speed, I think that the Cocoa collector has one big performance advantage that hasn't been discussed much: it is multithreaded.

The fact that it's multithreaded is discussed in Apple's literature, but mainly just to assure the programmer that the collector won't cause unsightly pauses while it works. Another common problem with older collectors was that they would halt the entire program while collecting, so that human-facing programs would be seen to lock up for visible periods when memory limits were reached, animation would stutter, etc. Apple's collector pauses individual threads in the program, but only for a very short period of time, and the major work of the collector is done with all of the app's threads running freely.

So what does this mean? Quite simple! The bulk of the garbage collector's work can run on a separate CPU core from the rest of your app.

In other words, by enabling garbage collection in your single-threaded Cocoa app, you've suddenly turned it into a multithreaded Cocoa app. Your code can run happily on one core while the collector churns away happily on another core. Since all shipping Macs have been multicore for quite a while now, this is very useful. In situations where your program is the only CPU eater on the system, the garbage collector is essentially free, and you get a performance boost by moving all the memory management work to a separate CPU core.

How much faster is it? I haven't worked up any benchmarks to measure, so right now this is entirely theoretical. But I was prompted to write this post after noticing that one of my Cocoa projects was using 200% CPU under garbage collection despite being completely single-threaded. I looked closer and, sure enough, the app's main thread was running full blast on one core while the garbage collector was running full blast picking up the pieces on the other. Most apps will probably not get a pure 50/50 split like this, but it seems clear that a lot of apps will gain at least some benefit.

Multithreaded programming is becoming more and more important as multicore machines have now become commonplace, and the average number of cores per machine seems set to increase without limit for the forseeable future. OS X is doing a good job of providing both explicit multithreaded services such as NSOperation as well as implicit services like CoreAnimation, which does all of its work in a separate thread but doesn't make the API user think about that fact. It seems that Cocoa garbage collection is another easy-to-overlook example of the implicit multiprocessing support that's being added to OS X, and it's something to think about when considering whether to GC-enable your new Cocoa project.

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

Comments:

---

Comments RSS feed for this page

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.
