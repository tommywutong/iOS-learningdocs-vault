---
title: 'There''s a Garbage Collection ninja hiding in the project templates | Cocoa with Love'
source: Cocoa with Love (Matt Gallagher)
source_key: cocoawithlove
source_url: 'https://www.cocoawithlove.com/2009/12/there-garbage-collection-ninja-hiding.html'
original_language: en
published: ''
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-26
content_hash: 'sha256:ee6b377e57555250'
translated: false
---

> 原文：[There's a Garbage Collection ninja hiding in the project templates | Cocoa with Love](https://www.cocoawithlove.com/2009/12/there-garbage-collection-ninja-hiding.html)　·　Cocoa with Love (Matt Gallagher)

Not all Xcode project templates are alike. Especially the Core Data Command Line Tool...

## An unwanted feature jumped out and attacked me!

In [yesterday's post on implementing a CSV parser](https://www.cocoawithlove.com/2009/11/writing-parser-using-nsscanner-csv.html), I briefly mentioned that the parser took around 0.28 seconds to parse the test data that I provided. I consider this a good time for the parser to take but my first run was not so quick.

The first timing test I ran gave a parsing time of 1.15 seconds. This was slightly shocking to me, since I had already run a "control" test — where I just used `componentsSeparatedByString:` to break into lines and then into fields — that took just 0.95 seconds.

Had I really spent all that time writing code that was 20% slower (albeit more functional) than a clumsy, brute force approach?

No. As it turns out, the Xcode Project Template I had used for the test project, the:

project has Garbage Collection enabled by default.

The only real hint that this template is different is the `objc_startCollectorThread()` line in the default `main()` function — of course, I never saw this line because I always replace the source files in the templates with my own versions that follow my own formatting style.

Anyway, I turned Garbage Collection off and... _boom_ 4 times faster.

I'd ask for more warning about these major — but subtle — changes to templates in the future but you know... ninjas, what can you do?
