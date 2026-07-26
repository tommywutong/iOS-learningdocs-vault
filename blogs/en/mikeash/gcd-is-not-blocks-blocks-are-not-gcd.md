---
title: GCD Is Not Blocks, Blocks Are Not GCD
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/gcd-is-not-blocks-blocks-are-not-gcd.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:6271459d90b7cd54'
translated: false
---

> 原文：[GCD Is Not Blocks, Blocks Are Not GCD](https://www.mikeash.com/pyblog/gcd-is-not-blocks-blocks-are-not-gcd.html)　·　mikeash.com Friday Q&A

Posted at 2009-09-11 21:27 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [The iPhone Development Story: One Year Later](https://www.mikeash.com/pyblog/the-iphone-development-story-one-year-later.html)  
Previous article: [Friday Q&A 2009-09-11: Intro to Grand Central Dispatch, Part III: Dispatch Sources](https://www.mikeash.com/pyblog/friday-qa-2009-09-11-intro-to-grand-central-dispatch-part-iii-dispatch-sources.html)  
Tags: [gcd](https://www.mikeash.com/pyblog/?tag=gcd) [rant](https://www.mikeash.com/pyblog/?tag=rant)

GCD Is Not Blocks, Blocks Are Not GCD

by [Mike Ash](https://www.mikeash.com/)

**Blocks**  
 Blocks are a new C/C++/Objective-C language feature designed and developed by Apple. They were first released to the public as part of the [clang project](http://clang.llvm.org/). This summer saw a nice packaged blocks-capable compiler in the form of [PLBlocks](http://code.google.com/p/plblocks/), and they gained official Apple support in 10.6.

Blocks are what other languages commonly call lambdas or closures. They are anonymous inner functions which capture enclosing scope and which can live beyond the lifetime of that enclosing scope. In essence, they allow writing inline code which can then be passed to other functions or modules instead of being executed immediately.

Blocks are officially supported by Apple on 10.6 and up. Programs targeting 10.5 can use blocks if they use PLBlocks. Programs written for other platforms can probably use blocks if they are compiled with clang, but I'm not certain on the status of this work.

**Grand Central Dispatch**  
 GCD, also known as libdispatch, is a Mac OS X multiprocessing framework new in 10.6. Its major feature is an efficient system-aware thread pool implementation. "System-aware" means that it will automatically and dynamically scale the number of threads in the pool in response to system load, the number of CPU cores in the computer, and the state of the threads currently executing in the pool. GCD also offers other multiprocessing features such as an events system and semaphores.

As of this week, the GCD [is now open source](http://libdispatch.macosforge.org/). The system awareness of GCD requires kernel integration which may make it more difficult to port to other platforms, and for now GCD remains a purely Mac OS X 10.6 library.

**Why the Confusion?**  
 Reading the above, I think that anyone can see that these two entities are very different. They really have nothing in common. So why is there so much confusion about what's what?

The answer is pretty simple: GCD is built around callbacks. You pass it a callback for an event trigger, or to execute a work unit, or as a cancellation handler, or for many other things.

Callbacks in C have always been clunky. Blocks make callbacks much easier to use. Since GCD is so heavily based on callbacks, the solution was easy: add blocks-based APIs to GCD. Thus, most GCD examples you see out there include blocks as well, as in this example from the `dispatch_async` man page:

```
     dispatch_async(my_queue, ^{
             // critical section
     });
```

The confusion is understandable, but it's important to understand the distinction between the two. You can use blocks without GCD, and in fact many new blocks-based Cocoa APIs in 10.6 do just that. You can use GCD without blocks, via the `_f` variants provided for every GCD function that takes a block. They go great together, but they are in fact completely different technologies.

And now you know the rest of the story.

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

Comments:

---

[Comments RSS feed for this page](https://www.mikeash.com/commentsrss.py?page=pyblog/gcd-is-not-blocks-blocks-are-not-gcd.html)

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.

Code syntax highlighting thanks to [Pygments](http://pygments.org/).
