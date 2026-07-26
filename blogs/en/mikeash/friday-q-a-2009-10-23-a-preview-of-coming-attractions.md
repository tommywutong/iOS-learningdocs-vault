---
title: 'Friday Q&A 2009-10-23: A Preview of Coming Attractions'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2009-10-23-a-preview-of-coming-attractions.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:6764e413aa49b9fe'
translated: false
---

> 原文：[Friday Q&A 2009-10-23: A Preview of Coming Attractions](https://www.mikeash.com/pyblog/friday-qa-2009-10-23-a-preview-of-coming-attractions.html)　·　mikeash.com Friday Q&A

Posted at 2009-10-23 15:45 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [Friday Q&A 2009-10-30: Generators in Objective-C](https://www.mikeash.com/pyblog/friday-qa-2009-10-30-generators-in-objective-c.html)  
Previous article: [Friday Q&A 2009-10-16: Creating a Blocks-Based Object System](https://www.mikeash.com/pyblog/friday-qa-2009-10-16-creating-a-blocks-based-object-system.html)  
Tags: [fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [generators](https://www.mikeash.com/pyblog/?tag=generators)

Friday Q&A 2009-10-23: A Preview of Coming Attractions

by [Mike Ash](https://www.mikeash.com/)

MAGenerator is a library for building generators in Objective-C. These are much like the [generators found in Python](http://docs.python.org/tutorial/classes.html#generators), although with a slightly different interface. They are essentially functions which remember state between invocations, such that when you call them a second time, all local variables have the same value they did at the end of the first call, and execution resumes where it was when it returned from the first call.

There's complete, if terse, documentation found in the `MAGenerator.h` header, and some examples in the `GeneratorTests.m` file. I plan to release the code under an MIT license if you'd actually like to use it somewhere. Unlike my [blocks-based object system](https://www.mikeash.com/pyblog/friday-qa-2009-10-16-creating-a-blocks-based-object-system.html) from last week, I think this code could actually be used in a practical sense, even though the implementation is still pretty much evil.

Next week I'll go through how it all works, why it's built the way it is, and how to use it. Until then, enjoy the code. And as always, [keep your suggestions for topics coming](mailto:mike@mikeash.com). I'm already booked for next week but am always happy to hang on to ideas for later.

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

Comments:

---

[Comments RSS feed for this page](https://www.mikeash.com/commentsrss.py?page=pyblog/friday-qa-2009-10-23-a-preview-of-coming-attractions.html)

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.
