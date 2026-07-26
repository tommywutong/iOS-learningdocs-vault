---
title: More Fun With Autorelease
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/more-fun-with-autorelease.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:232fc62df018d55d'
translated: false
---

> 原文：[More Fun With Autorelease](https://www.mikeash.com/pyblog/more-fun-with-autorelease.html)　·　mikeash.com Friday Q&A

Posted at 2007-02-08 00:00 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [How To Shrink Your Source Code](https://www.mikeash.com/pyblog/how-to-shrink-your-source-code.html)  
Previous article: [Why CoreAudio is Hard](https://www.mikeash.com/pyblog/why-coreaudio-is-hard.html)  
Tags: [autorelease](https://www.mikeash.com/pyblog/?tag=autorelease) [bug](https://www.mikeash.com/pyblog/?tag=bug) [cocoa](https://www.mikeash.com/pyblog/?tag=cocoa) [objectivec](https://www.mikeash.com/pyblog/?tag=objectivec)

More Fun With Autorelease

by [Mike Ash](https://www.mikeash.com/)

The key word is "event loop". In Apple's infinite wisdom, things that aren't real actual NSEvents don't trigger the pool.

I'm currently working on an app that spends a lot of time in the background doing dark, unspeakable things with NSStreams on the main thread. I encountered a bug where one of my objects can get destroyed in the middle of handling a stream event, which left it open to getting other stream events after it was deallocated. (Apparently NSStreams can still send you stream events even after you've closed them, released them, and set their delegate to

, but that's an entirely different problem for another day.)

The obvious fix was to simply do

before making the problem call. And fix it it did, except instead of my

happening in the middle of my event handler, it

.

Until I clicked on my app's dock icon.

At least the solution was easy. Post an

event in the stream event handler, and autoreleased objects get destroyed on schedule.

The amazing part is that, from what I've heard, this bug has been there for a long time. I haven't used it, but it seems like CFRunLoopObserver would make it trivial to hook into the runloop at such a low level that you could drain the current pool if anything so much as

. And as we all know,

Autorelease is Fast

, so there should be no penalty in doing this.

How many of our apps sit quietly ticking away in the background, accumulating ever larger autorelease pools that only get drained once we bring them forward? It makes you wonder.

Hopefully this will be fixed in Leopard. I'm afraid to file a bug lest I get a "Behaves Correctly".

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

Comments:

---

Comments RSS feed for this page

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.
