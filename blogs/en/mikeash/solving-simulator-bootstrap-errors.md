---
title: Solving Simulator Bootstrap Errors
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/solving-simulator-bootstrap-errors.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:167a4d4fae7e6278'
translated: false
---

> 原文：[Solving Simulator Bootstrap Errors](https://www.mikeash.com/pyblog/solving-simulator-bootstrap-errors.html)　·　mikeash.com Friday Q&A

Posted at 2012-05-07 20:06 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [Friday Q&A 2012-05-18: A Tour of PLWeakCompatibility: Part I](https://www.mikeash.com/pyblog/friday-qa-2012-05-18-a-tour-of-plweakcompatibility-part-i.html)  
Previous article: [Friday Q&A 2012-05-04: PLCrashReporter and Unwinding the Stack With DWARF, Part 2](https://www.mikeash.com/pyblog/friday-qa-2012-05-04-plcrashreporter-and-unwinding-the-stack-with-dwarf-part-2.html)  
Tags: [apple](https://www.mikeash.com/pyblog/?tag=apple) [hack](https://www.mikeash.com/pyblog/?tag=hack) [xcode](https://www.mikeash.com/pyblog/?tag=xcode)

Solving Simulator Bootstrap Errors

by [Mike Ash](https://www.mikeash.com/)

This occasionally happens when using Xcode to run iOS apps in the simulator. Although the error really gives no indication of it, it's apparently a hung `launchd` job that somehow doesn't get cleaned up. The above command lists out all `launchd` jobs, searches for one with `UIKitApplication` in the name (which will be the job corresponding to your app that's improperly sticking around), extracts the name, and tells `launchd` to get rid of that job.

I'm still not sure exactly why this error happens. And, as far as I know, the above can't be used on the actual device, so you still have to reboot those to solve it when it happens there, although that's much less painful than rebooting your development Mac. But the above works just fine as a workaround until Apple can get their act together on this problem. I saved the command into a shell script called `unfuckbootstrap` that I can use whenever Xcode decides to screw up.

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

Comments:

---

Comments RSS feed for this page

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.
