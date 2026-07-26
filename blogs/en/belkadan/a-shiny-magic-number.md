---
title: A Shiny Magic Number
source: Belkadan (Jordan Rose, 前 Swift 编译器工程师)
source_key: belkadan
source_url: 'https://belkadan.com/blog/2019/02/A-Shiny-Magic-Number/'
original_language: en
published: 2019-02-21
status: active
license: Copyright 2012–2020 Jordan Rose → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:e04fe59324584983'
translated: false
---

> 原文：[A Shiny Magic Number](https://belkadan.com/blog/2019/02/A-Shiny-Magic-Number/)　·　Belkadan (Jordan Rose, 前 Swift 编译器工程师)

« [Misleading Metrics and UX Tradeoffs](https://belkadan.com/blog/2018/04/Misleading-Metrics/)

[\> go east](https://belkadan.com/blog/2019/08/go-east/) »

« ["FIXME" Doesn't Always Mean "Fix Me"](https://belkadan.com/blog/2018/04/FIXME/?tag=swift)

[Leaving Apple](https://belkadan.com/blog/2019/11/Leaving-Apple/?tag=swift) »

## [A Shiny Magic Number](#)

Now that a particular code name for Swift has been [leaked from a Definitive Source](https://oleb.net/2019/chris-lattner-swift-origins/), I’ll point out a little easter egg I put in: the “magic number” for swiftmodule files is `E2 9C A8 0E`. Those first three bytes are UTF-8 for ✨ (U+2728 SPARKLES).

The last byte is also relevant: as a character it’s U+000E SHIFT OUT, a basically-unused ASCII control code. It’s also “14” in decimal, as in “2014”, the year we were hoping would see the release of Swift 1. (IIRC it was 2013 when I made this.)

I kind of regret this in retrospect because it’s better if a magic number for a binary format isn’t valid UTF-8 at all, but the next four bytes start the LLVM bitstream format, which is pretty much guaranteed to have the latter two bytes be 00 00. So it’s not confusable for text.

And now I’m working on the format that will replace swiftmodule files (in certain circumstances, see [https://forums.swift.org/t/plan-for-module-stability/14551](https://forums.swift.org/t/plan-for-module-stability/14551)). The sparkles will stick around in the related swiftdoc files, though (`E2 9C A8 07`), which turned out to be a binary format worth stabilizing.

Thanks to [Harlan Haskins](https://mastodon.social/@harlan) for the push to tell this story. (He’s also a collaborator on the module stability effort.)

P.S. If you don’t know what a “magic number” is in this context, it’s your lucky day! Check out [https://en.wikipedia.org/wiki/File_format#Magic_number](https://en.wikipedia.org/wiki/File_format#Magic_number), which includes the delightful phrase “magic database”.

_Originally posted [on Twitter](https://twitter.com/UINT_MIN/status/1098628355539124224)._

This entry was posted on [February](https://belkadan.com/blog/2019/02) 21, [2019](https://belkadan.com/blog/2019) and is filed under [Technical](https://belkadan.com/blog/technical). Tags: [Swift](https://belkadan.com/blog/tags/swift), [Social media import](https://belkadan.com/blog/tags/social-media-import)
