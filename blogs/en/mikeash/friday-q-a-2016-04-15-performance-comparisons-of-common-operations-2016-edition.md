---
title: 'Friday Q&A 2016-04-15: Performance Comparisons of Common Operations, 2016 Edition'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2016-04-15-performance-comparisons-of-common-operations-2016-edition.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:565d3b306e761ed7'
translated: false
---

> 原文：[Friday Q&A 2016-04-15: Performance Comparisons of Common Operations, 2016 Edition](https://www.mikeash.com/pyblog/friday-qa-2016-04-15-performance-comparisons-of-common-operations-2016-edition.html)　·　mikeash.com Friday Q&A

Posted at 2016-04-15 13:20 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [Good News, Bad News, and Ugly News](https://www.mikeash.com/pyblog/good-news-bad-news-and-ugly-news.html)  
Previous article: [Friday Q&A 2016-03-04: Swift Asserts](https://www.mikeash.com/pyblog/friday-qa-2016-03-04-swift-asserts.html)  
Tags: [cocoa](https://www.mikeash.com/pyblog/?tag=cocoa) [fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [iphone](https://www.mikeash.com/pyblog/?tag=iphone) [objectivec](https://www.mikeash.com/pyblog/?tag=objectivec) [performance](https://www.mikeash.com/pyblog/?tag=performance)

Friday Q&A 2016-04-15: Performance Comparisons of Common Operations, 2016 Edition

by [Mike Ash](https://www.mikeash.com/)

**Previous Articles**  
If you'd like to compare with decades past, here are the links to the previous articles:

- Mac (10.5)
- Mac (10.4)
- iPhone OS 1

(Note that the name of Apple's mobile OS didn't become "iOS" until 2010.)

**Overview**  
Performance testing can be dangerous. Tests are usually highly artificial, unless you have a specific application with a real-world workload you can test. These particular tests are certainly artificial, and the results may not reflect how things actually perform in your own programs. The idea is just to give you a feel for the rough order of magnitude, not put a precise number on everything.

It's particularly difficult to measure extremely fast operations, like an Objective-C message send or a simple arithmetic operation. Modern CPUs are heavily pipelined and parallel, and the time such an operation takes in isolation may not correspond with the time it takes when in the context of a real program. Adding one of these operations into the middle of other code may not increase the running time of that code at all, if it's sufficiently independent that the CPU can run it in parallel. On the other hand, it could increase the running time a lot if it ties up important resources.

Performance also depends on external factors. Many modern CPUs will run faster when cold, and throttle down as they get hot. Filesystem performance will depend on the storage hardware and the state of the filesystem. Even relative performance can differ.

If something is performance critical, you always want to measure and profile it so you can see exactly what takes time in your code and know where to concentrate your efforts. It can and will surprise you to find out what's actually slow in working code.

All that said, it's still really useful to have a rough idea of how fast various things are compared to each other. It's worth a little effort to avoid writing a ton of data to the filesystem if you don't have to. It's probably not worth a little effort to avoid a single message send. In between, it depends.

**Methodology**  
The code used for these tests is available on GitHub:

[https://github.com/mikeash/PerformanceTest](https://github.com/mikeash/PerformanceTest)

The code is written in Objective-C++, with the core performance measuring code written in C. I don't yet have a good enough handle on how Swift performs to feel like I could do a good job of this in Swift.

The basic technique is simple: run the operation in question in a loop for a few seconds. Divide the total running time by the number of loop iterations to get the time per operation. The number of iterations is hardcoded, and I chose that number by experiment to make the test run for a reasonable amount of time.

I attempt to account for the overhead of the loop itself. This overhead is completely unimportant for the slower operations, but is substantial for the faster ones. To do this, I time an empty loop, then subtract the time per iteration from the times measured for the other tests.

For some tests, the test code appears to get pipelined in with the loop code. This produces amazingly low times for those tests, but the results are false. To compensate for this, all of the fast operations are manually unrolled so that a single loop iteration executes the test ten times, which I hope produces a more realistic result.

The tests are compiled and run _without_ optimizations. This is contrary to what we normally do in the real world, but I think it's the best choice here. For operations which mostly depend on external code, like working with files or decoding JSON, it makes little difference. For short operations like arithmetic or method calls, it's difficult to write a test that doesn't just get optimized away entirely as the compiler realizes that the test doesn't do anything that's externally visible. Optimization will also change how the loop is compiled, making it hard to account for loop overhead.

The Mac tests were run on my 2013 Mac Pro, with a 3.5GHz Xeon E5 running OS X 10.11.4. The iOS tests were run on an iPhone 6s running iOS 9.3.1.

**The Mac Tests**  
Here are the Mac numbers. Each test lists what it tested, how many iterations the test runs, the total time it took to run the test, and the per-operation time. All times are listed with loop overhead subtracted.

| Name | Iterations | Total time (sec) | Time per (ns) |
|---|---|---|---|
| 16 byte memcpy | 1000000000 | 0.7 | 0.7 |
| C++ virtual method call | 1000000000 | 1.5 | 1.5 |
| IMP-cached message send | 1000000000 | 1.6 | 1.6 |
| Objective-C message send | 1000000000 | 2.6 | 2.6 |
| Floating-point division with integer conversion | 1000000000 | 3.7 | 3.7 |
| Floating-point division | 1000000000 | 3.7 | 3.7 |
| Integer division | 1000000000 | 6.2 | 6.2 |
| ObjC retain and release | 100000000 | 2.3 | 23.2 |
| Autorelease pool push/pop | 100000000 | 2.5 | 25.2 |
| Dispatch_sync | 100000000 | 2.9 | 29.0 |
| 16-byte malloc/free | 100000000 | 5.5 | 55.4 |
| Object creation | 10000000 | 1.0 | 101.0 |
| NSInvocation message send | 10000000 | 1.7 | 174.3 |
| 16MB malloc/free | 10000000 | 3.2 | 317.1 |
| Dispatch queue create/destroy | 10000000 | 4.1 | 411.2 |
| Simple JSON encode | 1000000 | 1.4 | 1421.0 |
| Simple JSON decode | 1000000 | 2.7 | 2659.5 |
| Simple binary plist decode | 1000000 | 2.7 | 2666.1 |
| NSView create/destroy | 1000000 | 3.3 | 3272.1 |
| Simple XML plist decode | 1000000 | 5.5 | 5481.6 |
| Read 16 byte file | 1000000 | 6.4 | 6449.0 |
| Simple binary plist encode | 1000000 | 8.8 | 8813.2 |
| Dispatch_async and wait | 1000000 | 9.3 | 9343.5 |
| Simple XML plist encode | 1000000 | 9.5 | 9480.9 |
| Zero-zecond delayed perform | 100000 | 2.0 | 19615.0 |
| pthread create/join | 100000 | 2.8 | 27755.3 |
| 1MB memcpy | 100000 | 5.6 | 56310.6 |
| Write 16 byte file | 10000 | 1.7 | 165444.3 |
| Write 16 byte file (atomic) | 10000 | 2.4 | 237907.9 |
| Read 16MB file | 1000 | 3.4 | 3355650.0 |
| NSWindow create/destroy | 1000 | 10.6 | 10590507.9 |
| NSTask process spawn | 100 | 6.7 | 66679149.2 |
| Write 16MB file (atomic) | 30 | 2.8 | 94322686.1 |
| Write 16MB file | 30 | 3.1 | 104137671.1 |

The first thing that stands out in this table is the first entry in it. The 16-byte `memcpy` test takes less than a nanosecond per call. Looking at the generated code, the compiler is smart enough to turn the call to `memcpy` into a sequence of `mov` instructions, even with optimizations off. This is an interesting lesson: just because you write a function call doesn't mean the compiler has to generate one.

A C++ virtual method call and an ObjC message send with a cached IMP both take about the same amount of time. They're essentially the same operation: an indirect function call through a function pointer.

A normal Objective-C message send is a bit slower, as we'd expect. Still, the speed of `objc_msgSend` continues to astound me. Considering that it performs a full hash table lookup followed by an indirect jump to the result, the fact that it runs in 2.6 nanoseconds is amazing. That's about 9 CPU cycles. In the 10.5 days it was a dozen or more, so we've seen a nice improvement. To turn this number upside down, if you did nothing but Objective-C message sends, you could do about 400 million of them per second on this computer.

Using `NSInvocation` to call a method is much slower, as expected. `NSInvocation` has to construct the message at runtime, doing the work that the compiler does at compile time for each call. Fortunately, `NSInvocation` is rarely a bottleneck in real programs. It appears to have slowed down since 10.5, with an `NSInvocation` call taking about twice as much time in this test compared to the old one, even though this test is running on faster hardware.

A retain and release pair take about 23 nanoseconds together. Modifying an object's reference count must be thread safe, so it requires an atomic operation which is relatively expensive when we're down at the nanosecond level counting individual CPU cycles.

Autorelease pools have become quite a bit faster than they used to be. In the old test, creating and destroying an autorelease pool took well over 300ns. Here, it shows up at 25ns. The implementation of autorelease pools has been completely redone and the new implementation is a lot faster, so this is no surprise. Pools used to be instances of the `NSAutoreleasePool` class, but now they're done using runtime functions which just do some pointer manipulation. At 25ns, you can afford to sprinkle `@autoreleasepool` anywhere you even suspect you might accumulate some autoreleased objects.

Allocating and freeing 16 bytes costs much like before, but larger allocations have become significantly faster. Allocating and freeing 16MB took about 4.5 microseconds back in the day, but only took about 300 nanoseconds here. Typical apps do tons of memory allocations, so this is a great improvement.

Objective-C object creation also got a nice speedup, from almost 300ns to about 100ns. Obviously, the typical app creates and destroys a _lot_ of Objective-C objects, so this is really useful. On the flip side, consider that you can send an existing object about 40 messages in the same amount of time it takes to create and destroy a new object, so it's still a significantly more expensive operation, especially considering that most objects will take more time to create and destroy than a simple `NSObject` instance does.

The `dispatch_queue` tests show an interesting contrast between the various operations. A `dispatch_sync` on an uncontended queue is extremely fast, under 30ns. GCD is smart and doesn't do any cross-thread calls for this case, so it ends up just acquiring and then releasing a lock. `dispatch_async` takes a lot longer, since it has to find a worker thread to use, wake it up, and get the call over to it. Creating and destroying a `dispatch_queue` is pretty cheap, with a time comparable to creating an Objective-C object. GCD is able to share all of the heavyweight threading stuff, so the individual queues don't contain very much.

I added tests for JSON and property list serialization and deserialization, which I didn't test the last time around. With the rise of the iPhone, these things became a lot more prominent. These tests encode or decode a simple three-element dictionary. As expected, it's relatively slow compared to simple, low-level stuff like message sends, but it's still in the microseconds range. It's interesting that JSON outperforms property lists, even binary property lists, which I expected would be the fastest. This could be because JSON sees more use and so gets more attention, or it might just be that the JSON format is actually faster to parse. Or it might be that testing with a three-element dictionary isn't realistic, and the relative speeds would look different for something larger.

Zero-second delayed performs come in pretty heavyweight, relatively speaking, at about twice the cost of a `dispatch_async`. Runloops have a lot of work to do, it seems.

Creating a pthread and then waiting for it to terminate is another relatively heavyweight operation, taking a bit under 30 microseconds. We can see why GCD uses a thread pool and tries not to create new threads unless it's necessary. However, this is one test which got a lot faster since the old days. This same test took well over 100 microseconds in the old test.

Creating an `NSView` instance is fast, at about 3 microseconds. In constrast, creating an `NSWindow` is much slower, taking about 10 _milliseconds_. `NSView` is really a relatively light structure that represents an area of a window, while an `NSWindow` represents a chunk of pixel buffer in the window server. Creating one involves communicating with the window server to have it create the necessary structures, and it also requires a lot of work to set up all the various internal objects an NSWindow needs, like views for the title bar. You can go crazy with the views, but you might want to go easy on the windows.

File access is, as always, pretty slow. SSDs make it a lot faster, but there's still a ton of stuff going on there. Do it if you have to, try not to do it if you don't have to.

**The iOS Tests**  
Here are the iOS results.

| Name | Iterations | Total time (sec) | Time per (ns) |
|---|---|---|---|
| C++ virtual method call | 1000000000 | 0.8 | 0.8 |
| IMP-cached message send | 1000000000 | 1.2 | 1.2 |
| Floating-point division with integer conversion | 1000000000 | 1.5 | 1.5 |
| Integer division | 1000000000 | 2.1 | 2.1 |
| Objective-C message send | 1000000000 | 2.7 | 2.7 |
| Floating-point division | 1000000000 | 3.5 | 3.5 |
| 16 byte memcpy | 1000000000 | 5.3 | 5.3 |
| Autorelease pool push/pop | 100000000 | 1.5 | 14.7 |
| ObjC retain and release | 100000000 | 3.7 | 36.9 |
| Dispatch_sync | 100000000 | 7.9 | 79.0 |
| 16-byte malloc/free | 100000000 | 8.6 | 86.2 |
| Object creation | 10000000 | 1.2 | 119.8 |
| NSInvocation message send | 10000000 | 2.7 | 268.3 |
| Dispatch queue create/destroy | 10000000 | 6.4 | 636.0 |
| Simple JSON encode | 1000000 | 1.5 | 1464.5 |
| 16MB malloc/free | 10000000 | 15.2 | 1524.7 |
| Simple binary plist decode | 1000000 | 2.4 | 2430.0 |
| Simple JSON decode | 1000000 | 2.5 | 2515.9 |
| UIView create/destroy | 1000000 | 3.8 | 3800.7 |
| Simple XML plist decode | 1000000 | 5.5 | 5519.2 |
| Simple binary plist encode | 1000000 | 7.6 | 7617.7 |
| Simple XML plist encode | 1000000 | 10.5 | 10457.4 |
| Dispatch_async and wait | 1000000 | 18.1 | 18096.2 |
| Zero-zecond delayed perform | 100000 | 2.4 | 24229.2 |
| Read 16 byte file | 1000000 | 27.2 | 27156.1 |
| pthread create/join | 100000 | 3.7 | 37232.0 |
| 1MB memcpy | 100000 | 11.7 | 116557.3 |
| Write 16 byte file | 10000 | 20.2 | 2022447.6 |
| Write 16 byte file (atomic) | 10000 | 30.6 | 3055743.8 |
| Read 16MB file | 1000 | 6.2 | 6169527.5 |
| Write 16MB file (atomic) | 30 | 1.6 | 52226907.3 |
| Write 16MB file | 30 | 2.3 | 78285962.9 |

The most remarkable thing about this is how similar it looks to the Mac results above. Looking back at the old tests, the iPhone was orders of magnitude slower. An Objective-C message send, for example, was about 4.9ns on the Mac, but it took an eternity on the iPhone at nearly 200ns. A simple C++ virtual method call took a bit over a nanosecond on the Mac, but 80ns on the iPhone. A small malloc/free at around 50ns on the Mac took about 2 _microseconds_ on the iPhone.

Comparing the two today, and things have clearly changed a lot in the mobile world. Most of these numbers are just slightly worse than the Mac numbers. Some are actually faster! For example, autorelease pools are substantially faster on the iPhone. I guess ARM64 is better at doing the stuff that the autorelease pool code does.

Reading and writing small files stands out as an area where the iPhone is substantially slower. The 16MB file tests are comparable to the Mac, but the iPhone takes nearly ten times longer for the 16-byte file tests. It appears that the iPhone's storage has excellent throughput but suffers somewhat in latency compared to the Mac's.

**Conclusion**  
An excessive focus on performance can interfere with writing good code, but it's good to keep in mind the rough performance of the common operations we perform in your programs. That performance changes as software and hardware improves. The Mac has seen some nice improvements over the years, but the progress on the iPhone is remarkable. In eight years, it's gone from being almost a hundred times slower to being roughly on par with the Mac.

That's it for today. Come back next time for more fun stuff. Friday Q&A is driven by reader suggestions, so if you have a topic you'd like to see covered next time or some other time, please [send it in](mailto:mike@mikeash.com)!

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

Comments:

---

Comments RSS feed for this page

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.
