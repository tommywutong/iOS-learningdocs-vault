---
title: introduced PLWeakCompatibility
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/introducing-plweakcompatibility.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:c9f845c848d73125'
translated: false
---

> 原文：[introduced PLWeakCompatibility](https://www.mikeash.com/pyblog/introducing-plweakcompatibility.html)　·　mikeash.com Friday Q&A

Posted at 2012-03-31 03:09 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [Friday Q&A 2012-04-13: Nib Memory Management](https://www.mikeash.com/pyblog/friday-qa-2012-04-13-nib-memory-management.html)  
Previous article: [Friday Q&A 2012-03-16: Let's Build NSMutableDictionary](https://www.mikeash.com/pyblog/friday-qa-2012-03-16-lets-build-nsmutabledictionary.html)  
Tags: [arc](https://www.mikeash.com/pyblog/?tag=arc) [code](https://www.mikeash.com/pyblog/?tag=code) [hack](https://www.mikeash.com/pyblog/?tag=hack) [objectivec](https://www.mikeash.com/pyblog/?tag=objectivec) [sourcecode](https://www.mikeash.com/pyblog/?tag=sourcecode)

Introducing PLWeakCompatibility

by [Mike Ash](https://www.mikeash.com/)

Using PLWeakCompatibility is easy. Add one file to your Xcode project, add two compiler flags, and you're off to the races. If you have [MAZeroingWeakRef](https://github.com/mikeash/MAZeroingWeakRef) in your app already, then PLWeakCompatibility will use it to handle weak references on older OSes. If you don't, then it will use its own implementation, which is considerably simpler but somewhat slower. When your app runs on a newer OS with built in weak reference support, PLWeakCompatibility passes all calls through to the native support.

As you can probably tell from the prefix, PLWeakCompatibility comes from my employer, [Plausible Labs](http://plausible.coop/). I had a hand in writing it, but I didn't do it alone! You can now use `__weak` on any OS where you can deploy ARC, so grab [PLWeakCompatibility on GitHub now](https://github.com/plausiblelabs/PLWeakCompatibility)!

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

Comments:

---

[Comments RSS feed for this page](https://www.mikeash.com/commentsrss.py?page=pyblog/introducing-plweakcompatibility.html)

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.
