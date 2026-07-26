---
title: Performance Comparisons of Common Operations
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/performance-comparisons-of-common-operations.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:3384a32f64fd5ce7'
translated: false
---

> 原文：[Performance Comparisons of Common Operations](https://www.mikeash.com/pyblog/performance-comparisons-of-common-operations.html)　·　mikeash.com Friday Q&A

Posted at 2007-08-25 00:00 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [Don't use strnstr](https://www.mikeash.com/pyblog/dont-use-strnstr.html)  
Previous article: [Subtle Bugs](https://www.mikeash.com/pyblog/subtle-bugs.html)  
Tags: [cocoa](https://www.mikeash.com/pyblog/?tag=cocoa) [objectivec](https://www.mikeash.com/pyblog/?tag=objectivec) [performance](https://www.mikeash.com/pyblog/?tag=performance)

Performance Comparisons of Common Operations

by [Mike Ash](https://www.mikeash.com/)

I put together a Cocoa program to compute timings of a bunch of different operations. You can download that program [here](http://www.mikeash.com/perf.mm).  
   
 I ran the program on my 2.66GHz Mac Pro with 3GB of RAM and the stock hard drive. I didn't bother to shut down any other apps because I'm lazy and because I have lots of idle CPU. Disk timings may have been affected by background activity. This produced the following chart:

| Name | Iterations | Total time (sec) | Time per (ns) |
|---|---|---|---|
| IMP-cached message send | 1000000000 | 0.9 | 0.9 |
| C++ virtual method call | 1000000000 | 1.4 | 1.4 |
| Integer division | 1000000000 | 2.3 | 2.3 |
| Objective-C message send | 1000000000 | 5.0 | 5.0 |
| Float division with int conversion | 100000000 | 0.9 | 9.2 |
| Floating-point division | 100000000 | 0.9 | 9.3 |
| 16 byte memcpy | 100000000 | 2.9 | 29.5 |
| 16 byte malloc/free | 100000000 | 5.2 | 52.5 |
| NSInvocation message send | 10000000 | 1.6 | 160.7 |
| NSObject alloc/init/release | 10000000 | 1.9 | 186.6 |
| NSAutoreleasePool alloc/init/release | 10000000 | 3.0 | 300.0 |
| NSButtonCell creation | 1000000 | 5.2 | 5219.2 |
| 16MB malloc/free | 100000 | 1.0 | 10211.3 |
| Read 16-byte file | 100000 | 2.0 | 19905.4 |
| Zero-second delayed perform | 100000 | 3.0 | 30374.1 |
| NSButtonCell draw | 100000 | 7.6 | 76167.0 |
| pthread create/join | 10000 | 1.1 | 114887.3 |
| 1MB memcpy | 10000 | 1.2 | 124217.6 |
| Write 16-byte file | 10000 | 5.0 | 503798.5 |
| Write 16-byte file (atomic) | 10000 | 9.9 | 989662.0 |
| NSTask process spawn | 1000 | 5.5 | 5504646.1 |
| Read 16MB file | 100 | 2.9 | 29116230.5 |
| Write 16MB file | 30 | 10.0 | 334185067.2 |
| Write 16MB file (atomic) | 30 | 10.0 | 334293782.2 |

All file operations use NSData. The APIs used by the rest are hopefully obvious.

In general few of these results are surprising. However, some of them are still instructive.

IMP cached messaging is the fastest. This is no shock: it's just a call through a C function pointer. C++ virtual dispatch is close behind, about 50% slower, which is to be expected since it just incurs one additional array lookup before calling through a C function pointer.

Objective-C message sends are slower as one would think, but still very reasonable. At 5 nanoseconds each, this comes out to an average of just over 13 cycles per message send, which is fantastically fast.

Malloc/free is considerably more expensive as expected. There is a good amount of bookkeeping which takes place there. However, at 53ns per allocation, this isn't something which must be slavishly avoided.

NSInvocation is ridiculously slow, but once again it comes as no surprise. It has to do a lot more and the extra indirection it provides comes with a price, namely taking about 30 times longer than a straight message send.

The creation and destruction of an NSObject is significantly more expensive than a malloc/free but still just peanuts in the grand scheme of things. NSAutoreleasePool takes little more time to create and destroy, but

you already knew that

.

Allocating large chunks of memory is considerably more expensive than small chunks. This is because once you hit a certain threshold, every allocation goes straight to the kernel and you pay for that in the form of syscall overhead. Ten microseconds is still pretty fast but you might consider caching huge blocks of memory if you use a ton of them in a tight loop.

As expected, anything which hits the disk is tremendously slow. The fastest one, a 16-byte file read which no doubt stayed entirely in RAM cache for the entire test, still took 20 microseconds per read on average.

Delayed performs come in as surprisingly costly at 30 microseconds. Even so, this will support around 30,000 of them per second, hopefully you won't need anywhere near that many.

Creating threads is slow, over 100 microseconds. There's a reason we have

thread pools

.

The large memcpy works out to about 8GB/sec. I believe the Mac Pro has a theoretical max memory bandwidth of about 20GB/sec, but of course the memcpy hits the bus with the data in both directions, so I am willing to call this extremely impressive performance.

Filling in the end of the table are all of the remaining file operations. We can see the cost of using the "atomic" flag for NSData writes; since the amount of data for a 16-byte file is trivial, the write can be thought of as a single operation and the atomic swap adds a second operation, which doubles the time needed for the write. As expected, the cost for "atomic" becomes basically invisible for large files. The large write test comes in at 48.7MB/s which is quite respectable. The large read test comes in at 550MB/s which is obviously a result of OS caching.

A surprise entry near the end of the table is the process spawn test. At over 5 milliseconds per spawn, this is a very expensive operation. This is definitely not one for tight loops.

Soundbite lessons to take away:

- Don't fear ObjC messages, they're really quick.
- Don't fear creating ObjC objects, even in pretty tight loops, it's fast.
- Try not to allocate huge chunks of memory continuously in tight loops.
- Don't do synchronous disk operations if you need high speed.
- Creating new threads is pretty slow, if you're going to be doing it a thousand times a second then it may pay to create pools.
- Intel Macs have bone-crushing memory bandwidth.
- As always, code for correctness and clarity first, then profile if necessary, and only when you have identified a critical bottleneck should you optimize.

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

Comments:

---

Comments RSS feed for this page

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.
