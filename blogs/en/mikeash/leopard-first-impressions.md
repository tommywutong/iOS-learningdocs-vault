---
title: 'Leopard: First Impressions'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/leopard-first-impressions.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:aa6320b566622108'
translated: false
---

> 原文：[Leopard: First Impressions](https://www.mikeash.com/pyblog/leopard-first-impressions.html)　·　mikeash.com Friday Q&A

Posted at 2007-11-30 23:12 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [The Cults of Programming](https://www.mikeash.com/pyblog/the-cults-of-programming.html)  
Previous article: [Algorithmic Optimizations: a Case Study](https://www.mikeash.com/pyblog/algorithmic-optimizations-a-case-study.html)  
Tags: [cocoa](https://www.mikeash.com/pyblog/?tag=cocoa) [leopard](https://www.mikeash.com/pyblog/?tag=leopard) [objectivec](https://www.mikeash.com/pyblog/?tag=objectivec) [rant](https://www.mikeash.com/pyblog/?tag=rant)

Leopard: First Impressions

by [Mike Ash](https://www.mikeash.com/)

I won't be discussing Leopard from the user's perspective. Suffice it to say that it seems solid, and I haven't regretted upgrading from Tiger yet.

Now on to the meat of the post. Here's a list of new features I've worked with and how they've worked out for me so far:

- This is the great big granddaddy of all the new Leopard features. Apple added GC to Objective-C, a task many thought impossible, and many more thought would be doomed to mediocrity. But Apple forged a path right down the middle, carefully limiting the collector's scope to protect it from many of the more painful aspects of C while still making it useful for typical Objective-C use. There are a few painful corner cases but then again, there were painful corner cases with the old style of memory management too. Overall it makes writing new code pretty nice.

  Verdict:
- Considering the rest of Apple's additions to Objective-C, I am forced to cry out in a Homer-Simpson-like voice: booooooring! Properties are unexciting syntactic sugar, and the C++-like overloading of the = operator is mildly disturbing. The new for loop syntax is nice but doesn't do anything significant that my own home-rolled foreach macro hasn't done for me for years. And the rest... wait, there's nothing else! Compare this with the features Apple/NeXT has added to the language before

  changing the name: built-in exceptions and synchronization, protocols, categories.

  Verdict:
- Just like moving from Project Builder to Xcode, moving up to Xcode 3 is made out to be a big event, but then you arrive and discover that it's the same old app with a new coat of paint. After tweaking my settings a bit the first day, I can hardly tell the difference from Xcode 2. Refactoring seems pretty useless. Snapshots bring nothing to the table that version control hasn't done for decades, and if you aren't using version control then you're just asking for pain. Apple claims the editor is faster, which is good, but my machine is too fast and my files too small to notice. Inline error and warning messages are alternately great and tremendously annoying. It's still buggy and weird and it's still better than anything else on the Mac for making Cocoa apps.

  Verdict:
- Now this one actually deserves the name. It's a big change from IB2. Most of the change is even good. A lot of weird bugs and stupid limitations in IB2 are gone. The new inspector is good once you get used to it. The searchable palette is nice, although I think it's slightly harder to navigate than the old palette when not using the search box. Automatic synchronization with changes in Xcode is a definite plus. The new xib format could be better but even so it should solve a lot of problems with using nibs in group projects.

  Verdict:
- Apple's shiny new all-in-one instrumenting application replaces a bunch of separate applications that I've known and loved for a long time. It takes some getting used to, but overall I think the change is a good one. The main downside is that Instruments can get

  resource hungry when given the right stuff to monitor. It's made me glad I have 7GB of RAM because I have seen this single application use more than half of it all by itself.

  Verdict:
- Animator proxies are a great idea and make basic use of CoreAnimation roughly sixteen times simpler than NSViewAnimation. I haven't used any of the actual CA classes yet but they look to be very powerful. On the downside, the promise of transparent animation, where we could use the animator proxy to update a property, and internally it would update instantly while visually it would animate to the new value, appears to have been broken despite still existing in the AppKit release notes. This may simply be a bug in the frameworks, or it may be that Apple changed their minds. If the latter it's pretty disappointing. I've filed this as

  rdar://5614088

  .

  Verdict:
- This one probably prompts a "huh?" from the readership.

  CFStringTokenizer

  does just what it says on the label: you feed it a string and it feeds you tokens. These tokens can be paragraphs, line breaks, sentences, and even individual words. That may not sound impressive until you realize that it will do this even for languages like Chinese and Japanese which don't use spaces. You can also feed it a blob of text and it will tell you what language the text is written in. Probably not something a lot of people will really use but personally it's a really nice, simple interface to some powerful stuff.

  Verdict:
- Leopard brings a host of small improvements to Cocoa, such as the newly exposed NSCodition class, the ability to manually schedule NSURLConnections, NSBundle unloading, threading and multiprocessing enhancements, NSTrackingArea, NSGradient, and many more. These little additions fill gaps and add nice, easy new functionality.

  Verdict:
- This one isn't all that important yet, but it's getting there. Apple has been shipping 64-bit computers for years, and every Mac shipping today is 64-bit. The 4GB address space which once seemed to be limitless is now getting to be pretty small. Instruments could definitely stand to be a 64-bit app right now, and a lot of other useful applications for it will undoubtedly appear. The lack of Carbon GUI support is unfortunate but not too surprising. The way Apple handled it, by promising Carbon 64-bit and then changing their minds a year later was a total kick in the pants to everyone with a Carbon app, but the writing has been on the wall for a while.

  Verdict:

So there you have it. Although most of the code I write must remain Tiger-compatible for quite some time, I look forward to when I can take advantage of the new OS more completely.

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

Comments:

---

Comments RSS feed for this page

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.
