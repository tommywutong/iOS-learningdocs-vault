---
title: Unicode Comments Support
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/unicode-comments-support.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:c2de6cfb9e652001'
translated: false
---

> 原文：[Unicode Comments Support](https://www.mikeash.com/pyblog/unicode-comments-support.html)　·　mikeash.com Friday Q&A

Posted at 2009-08-22 20:55 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [Friday Q&A 2009-08-28: Intro to Grand Central Dispatch, Part I: Basics and Dispatch Queues](https://www.mikeash.com/pyblog/friday-qa-2009-08-28-intro-to-grand-central-dispatch-part-i-basics-and-dispatch-queues.html)  
Previous article: [Reading Between the Lines of Apple's FCC Reply](https://www.mikeash.com/pyblog/reading-between-the-lines-of-apples-fcc-reply.html)  
Tags: [meta](https://www.mikeash.com/pyblog/?tag=meta) [python](https://www.mikeash.com/pyblog/?tag=python) [unicode](https://www.mikeash.com/pyblog/?tag=unicode)

Unicode Comments Support

by [Mike Ash](https://www.mikeash.com/)

What was the solution, you ask? Easy: give up on MySQL and switch everything to SQLite. SQLite is fully Unicode-aware and makes everything related to non-ASCII text easy. I had to do some hacking in my Python code to get it to do the conversions at the right place, but it was fairly minor work. Dumping all the old comments over took a fairly short script, and now I'm up and running on the new system. Overall SQLite was really nice to work with, a big contrast from MySQL. I realize they're targeted at different types of work, but the fact is that with the low amount of traffic I get, and especially the small number of comments that are posted, I don't need the performance, multiuser facilities, or other capabilities offered by MySQL.

Anyway, it's done, it appears to work, so enjoy. If you see any problems, [let me know](mailto:mike@mikeash.com). (Or post a comment if you can!)

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

Comments:

---

Comments RSS feed for this page

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.
