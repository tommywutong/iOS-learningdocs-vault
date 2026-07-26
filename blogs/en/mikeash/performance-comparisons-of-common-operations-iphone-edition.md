---
title: Performance Comparisons of Common Operations, iPhone Edition
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/performance-comparisons-of-common-operations-iphone-edition.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:1eb6964cef389d6c'
translated: false
---

> 原文：[Performance Comparisons of Common Operations, iPhone Edition](https://www.mikeash.com/pyblog/performance-comparisons-of-common-operations-iphone-edition.html)　·　mikeash.com Friday Q&A

Posted at 2008-03-19 21:40 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [Deconstructing the iPhone SDK: Malware](https://www.mikeash.com/pyblog/deconstructing-the-iphone-sdk-malware.html)  
Previous article: [Use strnstr](https://www.mikeash.com/pyblog/use-strnstr.html)  
Tags: [cocoa](https://www.mikeash.com/pyblog/?tag=cocoa) [iphone](https://www.mikeash.com/pyblog/?tag=iphone) [objectivec](https://www.mikeash.com/pyblog/?tag=objectivec) [performance](https://www.mikeash.com/pyblog/?tag=performance)

Performance Comparisons of Common Operations, iPhone Edition

by [Mike Ash](https://www.mikeash.com/)

For comparison, you may wish to see the original [Performance Comparisons of Common Operations](https://www.mikeash.com/pyblog/performance-comparisons-of-common-operations.html) and its followup, [Performance Comparisons of Common Operations, Leopard Edition](https://www.mikeash.com/pyblog/performance-comparisons-of-common-operations-leopard-edition.html). The source code used in this test can be obtained [here](http://www.mikeash.com/perf_iphone.mm).

Here are the times:

| Name | Iterations | Total time (sec) | Time per (ns) |
|---|---|---|---|
| C++ virtual method call | 1000000000 | 80.8 | 80.8 |
| IMP-cached message send | 1000000000 | 85.4 | 85.4 |
| Floating-point division | 100000000 | 13.4 | 134.4 |
| Integer division | 1000000000 | 139.5 | 139.5 |
| 16 byte memcpy | 100000000 | 17.6 | 175.7 |
| Objective-C message send | 1000000000 | 192.9 | 192.9 |
| Float division with int conversion | 100000000 | 19.3 | 193.0 |
| NSInvocation message send | 10000000 | 19.0 | 1899.0 |
| 16 byte malloc/free | 100000000 | 198.8 | 1988.4 |
| NSObject alloc/init/release | 10000000 | 118.8 | 11883.6 |
| NSAutoreleasePool alloc/init/release | 10000000 | 172.7 | 17272.9 |
| 16MB malloc/free | 100000 | 3.1 | 30754.5 |
| Read 16-byte file | 100000 | 51.1 | 511041.3 |
| Zero-second delayed perform | 100000 | 67.5 | 674994.5 |
| pthread create/join | 10000 | 8.0 | 802160.2 |
| Write 16-byte file (atomic) | 10000 | 51.5 | 5153943.7 |
| Write 16-byte file | 10000 | 80.9 | 8089726.2 |
| 1MB memcpy | 10000 | 81.3 | 8130009.1 |
| Read 16MB file | 100 | 137.6 | 1376092573.3 |
| Write 16MB file (atomic) | 30 | 143.8 | 4793527088.9 |
| Write 16MB file | 30 | 151.2 | 5038515361.1 |

Note that this test suite is somewhat reduced compared to the original. NSTask and NSButtonCell don't exist, so those tests were removed. Conceivably they could be replaced with substitutes, but I didn't bother.

The first thing that stands out is the large speed difference for low-level operations compared to the Mac Pro used in the original tests. Of course I wouldn't expect a handheld device to compete against a modern desktop machine, but the contrast is still striking. The worst is the IMP-cached message send, which is over one hundred times slower on the iPhone.

It's also interesting to note that C++ virtual method calls have a better time than IMP-cached message sends. I'll assume that the difference is within the margin of error and that they are both actually the same speed. This is still an interesting result, since the C++ virtual method call involves more indirection than calling an IMP. I would guess that the ARM architecture includes an instruction which natively handles this indirection; anyone familiar with ARM care to comment?

Another interesting pairing is integer and floating-point division. Again these appear to be the same speed on the iPhone, but floating-point division is roughly 3.5 times slower on the Mac Pro. This makes floating-point division on the iPhone merely 15 times slower.

The results also show the atomic file writes to be faster than the non-atomic ones. I have no explanation for this other than testing error, but the difference in timing for the 16-byte file is pretty huge. The 5-8ms time to write the 16-byte file is interestingly large. At that size seek time should completely dominate, and flash memory has effectively no seek time, so I don't understand why this number would be so large. Perhaps CPU performance ends up costing this one so much. The 16MB test shows about a 3MB/s sustained write speed, not too bad.

The 1MB memcpy test reveals roughly 120MB/s of available memory bandwidth. I'm a bit surprised that it's this low, given the [on-die RAM](http://www.semiconductor.com/resources/reports_database/view_device.asp?sinumber=18016), but this is roughly comparable to the rest of the system even so.

Overall, this little machine isn't going to be substituting for a Mac Pro anytime soon, but it's not bad for a pocket-sized computer with such constraints on cost, battery usage, and heat. Now if only Apple [would let me put software on it](http://www.rogueamoeba.com/utm/2008/03/07/code-signing-and-you/).

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

Comments:

---

[Comments RSS feed for this page](https://www.mikeash.com/commentsrss.py?page=pyblog/performance-comparisons-of-common-operations-iphone-edition.html)

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.
