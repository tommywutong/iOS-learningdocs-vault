---
title: Autorelease is Fast
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/autorelease-is-fast.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:ceb09e86f3f56091'
translated: false
---

> 原文：[Autorelease is Fast](https://www.mikeash.com/pyblog/autorelease-is-fast.html)　·　mikeash.com Friday Q&A

Posted at 2006-06-07 00:00 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [Using Evil for Good](https://www.mikeash.com/pyblog/using-evil-for-good.html)  
Previous article: [Making Xcode Better](https://www.mikeash.com/pyblog/making-xcode-better.html)  
Tags: [autorelease](https://www.mikeash.com/pyblog/?tag=autorelease) [cocoa](https://www.mikeash.com/pyblog/?tag=cocoa) [objectivec](https://www.mikeash.com/pyblog/?tag=objectivec) [performance](https://www.mikeash.com/pyblog/?tag=performance)

Autorelease is Fast

by [Mike Ash](https://www.mikeash.com/)

I wrote a quick test program to allocate a million NSObjects and record the amount of time taken. The program increases the number of autorelease pools used by a factor of ten each time. The first test uses only one pool for the whole run, the second test uses ten, etc. At the end, it uses one pool per object.

You can get the source code to the test program [here](http://mikeash.com/tmp/autorelease_test.m).

Here are the results, compiled with gcc4 and -Os, run on my PowerBook G4/1.5 with 10.4.6 while relatively unloaded:

| Objects | Objects per pool | Run time (seconds) |
|---|---|---|
| 1000000 | 1000000 | 1.65 |
| 1000000 | 100000 | 1.59 |
| 1000000 | 10000 | 1.48 |
| 1000000 | 1000 | 1.46 |
| 1000000 | 100 | 1.43 |
| 1000000 | 10 | 1.64 |
| 1000000 | 1 | 2.91 |

Interestingly enough, the run time actually goes down as the number of autorelease pools created goes up in the first part of the run. This is probably because more frequent pool creation means the program's memory footprint is smaller, and so less time is spent mucking about with page tables and the like.

At the end the runtime spikes up heavily. But notice that the worst runtime is only about twice as bad as the best runtime, and this makes sense because at the end we're allocating almost twice as many objects. The final run creates and destroys two million objects (one million NSObjects, one million NSAutoreleasePools), and the best run does only a hair over one million.

So what's the conclusion? Creating and destroying an NSAutoreleasePool is about as expensive as creating and autoreleasing an NSObject. This is really insanely cheap. You might as well create a new pool in every iteration of your loop. The only time playing games with your pool so it only gets destroyed and recreated every N iterations is if you're only creating a handful of objects per loop, and even then your best-case savings will only be 50%, and that's when you're creating a single object and doing nothing else in the loop. And why would you need that to be super ultra blazing fast anyway?

Premature optimization is the root of all evil. So many people who would otherwise agree with this statement still say things like "you may want to release the pool every 10th iteration". The next time you see someone saying something ilke that, gently correct them and point them to this post.

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

Comments:

---

[Comments RSS feed for this page](https://www.mikeash.com/commentsrss.py?page=pyblog/autorelease-is-fast.html)

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.
