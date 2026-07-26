---
title: 'Space is time: how your CS theory class lied to you'
source: Hamster Emporium (Greg Parker)
source_key: sealiesoftware
source_url: 'http://sealiesoftware.com/blog/archive/2008/10/14/Space_is_time_how_your_CS_theory_class_lied_to_you.html'
original_language: en
published: 2008-10-14
status: frozen
license: 未声明 → 保守视为保留所有权利，仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:b0fffecc6b15c2c3'
translated: false
---

> 原文：[Space is time: how your CS theory class lied to you](http://sealiesoftware.com/blog/archive/2008/10/14/Space_is_time_how_your_CS_theory_class_lied_to_you.html)　·　Hamster Emporium (Greg Parker)

[![](http://sealiesoftware.com/hamster.jpg)](http://sealiesoftware.com/blog/index.html)  
  
 **blog**  
 [recent](http://sealiesoftware.com/blog/index.html)  
 [archive](http://sealiesoftware.com/blog/archive/index.html)  
 [twitter](http://twitter.com/gparker)  
   
 **projects**  
 [Mac OS X](http://www.apple.com/macosx/)  
 [Keyboard](http://sealiesoftware.com/keyboard/index.html)  
 [backlight](http://sealiesoftware.com/keyboard/index.html)  
 [CSC Menu](http://sealiesoftware.com/cscmenu/index.html)  
 [Valgrind](http://sealiesoftware.com/valgrind/index.html)  
 [Fringe Player](http://sealiesoftware.com/fringe/index.html)  
 [pssh](http://sealiesoftware.com/pssh/index.html)  
 [Peal](http://sealiesoftware.com/peal/index.html)  
 [Frankenmouse](http://sealiesoftware.com/frankenmouse/index.html)

## Hamster Emporium archive

\<\< [updated: Valgrind for Mac OS X](http://sealiesoftware.com/blog/archive/2008/10/27/updated_Valgrind_for_Mac_OS_X.html) | [archive](http://sealiesoftware.com/blog/archive/index.html) | [updated: Valgrind for Mac OS X](http://sealiesoftware.com/blog/archive/2008/10/01/updated_Valgrind_for_Mac_OS_X.html) \>\>

[![(link)](http://sealiesoftware.com/link.gif)](http://sealiesoftware.com/blog/archive/2008/10/14/Space_is_time_how_your_CS_theory_class_lied_to_you.html)

**Space is time: how your CS theory class lied to you** ([2008-10-14 1:04 AM](http://sealiesoftware.com/blog/archive/2008/10/14/Space_is_time_how_your_CS_theory_class_lied_to_you.html))

In your computer science algorithms course, you learned about space-time tradeoffs. An algorithm that requires lots of time can often be changed to take less time but more space. A wide range of performance optimizations work this way, from caching to memoization to loop unrolling.

But the "tradeoff" is a lie. Space _is_ time.

Every use of space incurs a time cost. In your theory class, the time cost of space is swept under the big-O rug. On your big-iron machine running a single computational workload or CPU benchmark, the time cost of space is small compared to the other time costs involved. But in the real world of consumer-grade devices, with limited memory and power, the time cost of space is tremendous. A performance optimization that tries to trade less time for more space often ends up requiring more time and more space.

The `gcc` compiler uses a garbage collector to manage its memory. To save time, `gcc` does not even start to collect any garbage until its memory size is quite large. "That's fine", you might say, "my new machine has gigabytes of memory". But the kernel needs a big chunk of memory just to keep track of the rest of the memory. And you're running a web browser, and an email client, and an IDE, and music and chat and clock and search and sync and backup and everything else you didn't have a decade or two ago. And your build system runs multiple `gcc` commands in parallel because your machine has multiple cores. Now your memory capacity isn't so big after all, the system starts paging to disk, and your compiler performance falls off a cliff and the web browser is sluggish too. In this memory-constrained environment, trying to use less time (skipping GC) and more space (accumulating garbage) has backfired badly.

Space _is_ time. An optimization that is faster on a well-endowed device may be much slower everywhere else. Assume your customer's machines have less memory than yours, and design and test accordingly.

At one modern extreme, the iPhone has only 128 MB of memory. Ever seen iPhone Safari "forget" a web page and re-download it after you switched tabs or apps? The system ran out of memory and Safari had to throw the page away. On the iPhone, your favorite space-time tradeoff in your own program may sacrifice the user's web page, requiring a repeat download across a slow network. Good for your program, perhaps, but bad for the user.

Space _is_ time. An optimization that makes _your program_ faster may make _the user's system_ slower overall. Play well with others.

Most of Mac OS X is compiled with `-Os` instead of `-O3`, to reduce code size. Mac OS X's memory allocator is slower than other allocators under some workloads, because it tries to avoid hoarding unused memory where other processes can't use it. Mac OS X uses dynamic shared libraries exclusively, then combines multiple shared libraries into a single shared cache, then carefully re-processes that shared cache, all to save space across multiple processes. Many ideas for faster cross-library calls or accelerated Objective-C method dispatch or JIT-based optimization have been abandoned because they need too much space and do not save enough time.

CPU-focused optimization can be just as evil as the infamous premature optimization. Space _is_ time.

Sealie Software
