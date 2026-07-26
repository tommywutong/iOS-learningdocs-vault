---
title: Performance Comparisons of Common Operations, Leopard Edition
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/performance-comparisons-of-common-operations-leopard-edition.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:7709d4b7f9f8a713'
translated: false
---

> 原文：[Performance Comparisons of Common Operations, Leopard Edition](https://www.mikeash.com/pyblog/performance-comparisons-of-common-operations-leopard-edition.html)　·　mikeash.com Friday Q&A

Posted at 2008-01-12 21:01 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [A Tool for Editing Version-Controlled Bundles](https://www.mikeash.com/pyblog/a-tool-for-editing-version-controlled-bundles.html)  
Previous article: [The Cults of Programming](https://www.mikeash.com/pyblog/the-cults-of-programming.html)  
Tags: [cocoa](https://www.mikeash.com/pyblog/?tag=cocoa) [leopard](https://www.mikeash.com/pyblog/?tag=leopard) [objectivec](https://www.mikeash.com/pyblog/?tag=objectivec) [performance](https://www.mikeash.com/pyblog/?tag=performance)

Performance Comparisons of Common Operations, Leopard Edition

by [Mike Ash](https://www.mikeash.com/)

You can see the original article [here](https://www.mikeash.com/pyblog/performance-comparisons-of-common-operations.html). I used the exact same program as before, which you can get [here](http://www.mikeash.com/perf.mm). There is one change to the hardware, in that the computer now has 7GB of RAM instead of 3GB. I do not expect this to influence much. It still has the 2.66GHz CPUs and the stock 250GB hard drive. Here's the new chart:

| Name | Iterations | Total time (sec) | Time per (ns) |
|---|---|---|---|
| IMP-cached message send | 1000000000 | 0.7 | 0.7 |
| C++ virtual method call | 1000000000 | 1.1 | 1.1 |
| Integer division | 1000000000 | 2.4 | 2.4 |
| Objective-C message send | 1000000000 | 4.9 | 4.9 |
| Float division with int conversion | 100000000 | 0.9 | 9.0 |
| Floating-point division | 100000000 | 0.9 | 9.2 |
| 16 byte memcpy | 100000000 | 2.9 | 28.9 |
| 16 byte malloc/free | 100000000 | 5.6 | 56.0 |
| NSInvocation message send | 10000000 | 0.8 | 77.3 |
| NSObject alloc/init/release | 10000000 | 2.9 | 290.5 |
| NSAutoreleasePool alloc/init/release | 10000000 | 3.6 | 357.7 |
| 16MB malloc/free | 100000 | 0.4 | 4485.2 |
| NSButtonCell creation | 1000000 | 6.6 | 6640.5 |
| Read 16-byte file | 100000 | 2.1 | 21219.3 |
| Zero-second delayed perform | 100000 | 4.2 | 42211.8 |
| pthread create/join | 10000 | 0.6 | 56633.2 |
| NSButtonCell draw | 100000 | 6.9 | 69400.5 |
| 1MB memcpy | 10000 | 1.2 | 123001.8 |
| Write 16-byte file | 10000 | 4.9 | 492040.5 |
| Write 16-byte file (atomic) | 10000 | 8.7 | 867380.7 |
| NSTask process spawn | 1000 | 6.1 | 6096478.5 |
| Read 16MB file | 100 | 2.9 | 28619582.6 |
| Write 16MB file (atomic) | 30 | 10.7 | 356168718.8 |
| Write 16MB file | 30 | 10.9 | 361767086.5 |

As you would expect, the low-level stuff that doesn't touch the OS is pretty much unaffected, and any changes are well within the margin of error. Things like Objective-C message sends really can't get much faster than they already are, and are unchanged. However, there are some interesting changes from the Tiger numbers.

Sending a message with NSInvocation on Tiger took about 160ns per message, but on Leopard it took only 77ns. That's over a factor of two faster. It's still over ten times slower than a straight message send, but it's much better.

Allocating and destroying Objective-C objects has apparently become significantly slower. `[[[NSObject alloc] init] release]` on Tiger took under 190ns, but on Leopard it took 290ns. This is still well into ignorable territory in most situations, but taking 50% more time is not good. I'm not sure what changes would have been made to make this slower. The small malloc/free test was pretty much unaffected, so it's apparently something specific to Objective-C.

The 16MB malloc/free test ran in less than half the time on Leopard. At this size, malloc/free hit the kernel directly, so presumably there is some syscall or kernel memory management optimization at work.

Delayed performs are somewhat worse on Leopard, going from 30µs each to 42µs.

NSButtonCell drawing got a bit faster, although not significantly. Leopard probably has various drawing optimizations, since that's something that the OS does quite a lot of.

Pthread creation is about twice as fast on Leopard. It's still annoyingly slow, but now it's something you can do about 20,000 times a second instead of 10,000 times a second.

And lastly, the atomic 16-byte file write is a bit over 10% faster. Perhaps there are some filesystem optimizations affecting the atomic swap process that this uses.

**Update:** The above was compiled as 32-bit, and it was pointed out that it might be good to show 64-bit numbers as well:

| Name | Iterations | Total time (sec) | Time per (ns) |
|---|---|---|---|
| IMP-cached message send | 1000000000 | 0.8 | 0.8 |
| C++ virtual method call | 1000000000 | 1.1 | 1.1 |
| Integer division | 1000000000 | 2.4 | 2.4 |
| Objective-C message send | 1000000000 | 8.6 | 8.6 |
| Float division with int conversion | 100000000 | 0.9 | 9.0 |
| Floating-point division | 100000000 | 0.9 | 9.0 |
| 16 byte memcpy | 100000000 | 2.9 | 29.3 |
| 16 byte malloc/free | 100000000 | 5.3 | 52.7 |
| NSInvocation message send | 10000000 | 0.8 | 81.6 |
| NSAutoreleasePool alloc/init/release | 10000000 | 1.7 | 169.5 |
| NSObject alloc/init/release | 10000000 | 1.9 | 192.6 |
| 16MB malloc/free | 100000 | 0.3 | 2924.6 |
| NSButtonCell creation | 1000000 | 6.1 | 6069.9 |
| Read 16-byte file | 100000 | 1.7 | 17382.1 |
| Zero-second delayed perform | 100000 | 3.4 | 33858.4 |
| pthread create/join | 10000 | 0.6 | 56279.8 |
| NSButtonCell draw | 100000 | 6.5 | 64812.5 |
| 1MB memcpy | 10000 | 1.2 | 122725.0 |
| Write 16-byte file | 10000 | 4.9 | 486454.7 |
| Write 16-byte file (atomic) | 10000 | 8.6 | 859274.8 |
| NSTask process spawn | 1000 | 5.6 | 5551589.2 |
| Read 16MB file | 100 | 2.8 | 27785650.2 |
| Write 16MB file | 30 | 9.2 | 305342338.2 |
| Write 16MB file (atomic) | 30 | 9.2 | 306369990.9 |

There are definitely some interesting differences here. Objective-C object allocation is back down to the Tiger numbers. I have even less of an idea why it would only be slower on Leopard 32-bit but not 64-bit. The 16MB malloc/free is even faster under 64-bit, and delayed peforms are significantly faster as well. Everything else seems to be pretty much the same, with some margin of error.

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

Comments:

---

[Comments RSS feed for this page](https://www.mikeash.com/commentsrss.py?page=pyblog/performance-comparisons-of-common-operations-leopard-edition.html)

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.
