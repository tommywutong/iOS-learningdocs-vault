---
title: Fun With Beowulf Clusters
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/fun-with-beowulf-clusters.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:c964168c271dc02f'
translated: false
---

> 原文：[Fun With Beowulf Clusters](https://www.mikeash.com/pyblog/fun-with-beowulf-clusters.html)　·　mikeash.com Friday Q&A

Posted at 2005-07-13 00:00 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [Score!](https://www.mikeash.com/pyblog/score.html)  
Previous article: [Using FileMerge with subversion](https://www.mikeash.com/pyblog/using-filemerge-with-subversion.html)  
Tags: [rant](https://www.mikeash.com/pyblog/?tag=rant) [university](https://www.mikeash.com/pyblog/?tag=university)

Fun With Beowulf Clusters

by [Mike Ash](https://www.mikeash.com/)

Since this library is developed at my university, it was pretty much a given that I would use it for my project. So starting in March, I started reading up on it, looking over documentation and examples, and trying it out. There was even supposed to be a Mac OS X port!

Of course, nothing worked. I pretty much gave up on it for the time being sometime in April and concentrated on non-parallel simumlation and visualization. But this week, I had gone as far as I could go without parallelizing some code, so I hit the cluster room and buckled down to make it work.

So guess what, it still doesn't work! Now, this code is developed on Linux, and aimed for Linux. It has a Mac port, with Mac benchmarks. All of the code is supposed to work. As far as I can tell, all it does is compile. On the Mac, none of the dynamic libraries have their install names set, and so none of the binaries can execute. When I fix the install names, other issues crop up. I have no idea how this is supposed to be working code, yet that's what they say.

Monday was the big failure with the threading lib. While leaving campus, I was pretty upset with the whole deal. It's frustrating to be told to use a library which simply doesn't work no matter what you do. I'm the world's biggest advocate of using existing code and existing libraries, but I finally decided that I'd implement my own communications, at least as a stopgap. Maybe it wouldn't be as efficient or flexible, but it would work!

Monday was despair, Tuesday was implementation and Wednesday was success! Maybe it's just because my little simulation isn't big and complicated, but it really wasn't that hard to get things up and running. Of course, my thesis supervisor has no idea that I'm completely bypassing their favorite clustering library. I meet with her next Monday to give her the good news.

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

Comments:

---

Comments RSS feed for this page

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.
