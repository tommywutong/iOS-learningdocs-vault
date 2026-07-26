---
title: WWDC 08 Followup
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/wwdc--followup.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:dc5bf3cc07ead304'
translated: false
---

> 原文：[WWDC 08 Followup](https://www.mikeash.com/pyblog/wwdc--followup.html)　·　mikeash.com Friday Q&A

Posted at 2008-06-23 01:33 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [Welcome to iPhone: Your Crappy Mac of Tomorrow, Today!](https://www.mikeash.com/pyblog/welcome-to-iphone-your-crappy-mac-of-tomorrow-today.html)  
Previous article: [Worst. Keynote. Ever.](https://www.mikeash.com/pyblog/worst-keynote-ever.html)  
Tags: [clang](https://www.mikeash.com/pyblog/?tag=clang) [gcd](https://www.mikeash.com/pyblog/?tag=gcd) [llvm](https://www.mikeash.com/pyblog/?tag=llvm) [opencl](https://www.mikeash.com/pyblog/?tag=opencl) [wwdc](https://www.mikeash.com/pyblog/?tag=wwdc)

WWDC 08 Followup

by [Mike Ash](https://www.mikeash.com/)

Due to the NDA I'm not going to talk about any specifics, so you're not going to get any juicy tidbits. I'm just going to discuss my reaction to the stuff I saw which is already publicly announced.

Ignoring iPhone stuff, which I don't really care about, the whole show was of course centered around Snow Leopard. The absurd rumor leading up to WWDC was that SL would have zero new features and would instead concentrate on security and stability. What a surprise when they turned out to be true!

You'd think this would be bad news, but it's really like Christmas in June for developers. You see, when Apple said "no new features" what they meant was _user_ features. Things like Spotlight, Time Machine, and Dashboard. Instead of adding silly user-facing fluff like that, they're adding a ton of fantastic developer-facing infrastructure.

The first such feature listed in Apple's press release (see, no NDA violation here!) is Grand Central. This is really going to change in some fundamental ways how applications are built for 10.6 and beyond. It's a way to get rid of a lot of fundamental difficulties and overhead associated with multithreaded programming so that we can really use all of these cores we have these days.

Another great speed feature listed is OpenCL. OpenCL is, essentially, a GPU programming framework that lets you code in C. This approach is vastly more flexible than the typical technique of using OpenGL with GLSL to use graphics APIs for general purpose computation. It's similar in concept to CUDA and CTM, but intended to be an open standard. Modern computers have an enormous amount of power that sits idle most of the time because it's sitting on the video card doing nothing, and OpenCL should help greatly in taking advantage of it.

LLVM and clang are really looking good too. If you aren't aware, LLVM is essentially a library for code generation, intended for use as a JIT compiler for a virtual machine but capable of a lot more. Clang is a C/C++/Objective-C parser that goes in front of LLVM. Together they make a full compiler suite that is completely independent of gcc. Personally I can't wait for the day when I can say goodbye to gcc once and for all. LLVM is already being used in OS X for things like OpenGL shaders and is in good shape. Clang is a bit earlier in development and isn't quite ready for prime time, but it's on the right track.

That's all I have time and non-NDA information for. Suffice it to say that Snow Leopard is shaping up to be the most exciting Mac OS X release in quite some time.

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

Comments:

---

[Comments RSS feed for this page](https://www.mikeash.com/commentsrss.py?page=pyblog/wwdc--followup.html)

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.
