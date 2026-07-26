---
title: Swift Regrets
source: Belkadan (Jordan Rose, 前 Swift 编译器工程师)
source_key: belkadan
source_url: 'https://belkadan.com/blog/2021/09/Swift-Regrets/'
original_language: en
published: 2021-09-10
status: active
license: Copyright 2012–2020 Jordan Rose → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:ba1ddefb7eb3b8ae'
translated: false
---

> 原文：[Swift Regrets](https://belkadan.com/blog/2021/09/Swift-Regrets/)　·　Belkadan (Jordan Rose, 前 Swift 编译器工程师)

« [Swift Regret: Unapplied Instance Methods](https://belkadan.com/blog/2021/09/Swift-Regret-Unapplied-Instance-Methods/)

[Swift Regret: Subscript Argument Label Rules](https://belkadan.com/blog/2021/09/Swift-Regret-Subscript-Argument-Label-Rules/) »

« [Swift Regret: Unapplied Instance Methods](https://belkadan.com/blog/2021/09/Swift-Regret-Unapplied-Instance-Methods/?tag=swift)

[Swift Regret: Subscript Argument Label Rules](https://belkadan.com/blog/2021/09/Swift-Regret-Subscript-Argument-Label-Rules/?tag=swift) »

« [Swift Regret: Unapplied Instance Methods](https://belkadan.com/blog/2021/09/Swift-Regret-Unapplied-Instance-Methods/?tag=swift-regrets)

[Swift Regret: Subscript Argument Label Rules](https://belkadan.com/blog/2021/09/Swift-Regret-Subscript-Argument-Label-Rules/?tag=swift-regrets) »

« [Many-to-Many Protocols](https://belkadan.com/blog/2018/02/Many-to-Many-Protocols/?tag=programming-languages)

[Swift Regrets: Wrap-up](https://belkadan.com/blog/2021/12/Swift-Regrets-Wrap-up/?tag=programming-languages) »

## [Swift Regrets](#)

For the past few weeks I’ve been writing Twitter threads on “Swift regrets”, things I wish we’d done differently early on in Swift’s development. I’ve been doing them on Twitter rather than as blog posts because of my [RSI](https://belkadan.com/blog/2021/07/Keyboard-Pants/)—short-form on my phone is easier than long-form at a keyboard when I spend so much time on a keyboard for work. But I’m mirroring them here, lightly edited, so they don’t get lost in the eternal history of Twitter. You can find them under the [Swift regrets](https://belkadan.com/blog/tags/swift-regrets/) tag.

I worked on Swift [at Apple](https://belkadan.com/blog/2019/11/Leaving-Apple/) from pre-release to Swift 5.1. I’m at least partly responsible for many things people like about Swift and many things people hate about Swift. This list is something I started collecting around when I left Apple, and I’m putting them up so other language designers can learn from our mistakes. These are all things that would be hard to change in Swift today, because they’d break tons of people’s code. [That’s what happens with real-world languages and libraries: the more users you have, the fewer breaking changes you can make.](https://mobile.twitter.com/UINT_MIN/status/1426402680763600900)

That said, I don’t want people to think “oh, Jordan hates Swift” or “gosh, look at all these issues in Swift, why can’t they get it right”. That’s definitely _not_ the takeaway here. I love Swift. Every language has warts, mistakes, compromises, I promise you. And a lot of what Swift did wasn’t new; it was borrowing and maybe improving on ideas from other languages. So future languages should improve on Swift, but also I decided to stir in “Swift delights”, things I want other languages to borrow. They’re not things only Swift does, but they _are_ things I appreciate in Swift and that I’d like to see in future languages as well.

Obviously I expect people to disagree with me on many of these; heck, for many of them Past Me would disagree too, and that’s why things are the way they are! Also, please feel free to ask questions. (And if one interests you in particular, I suggest checking out the Twitter thread to see what other people added.)

This entry was posted on [September](https://belkadan.com/blog/2021/09) 10, [2021](https://belkadan.com/blog/2021) and is filed under [Technical](https://belkadan.com/blog/technical). Tags: [Swift](https://belkadan.com/blog/tags/swift), [Swift regrets](https://belkadan.com/blog/tags/swift-regrets), [Programming languages](https://belkadan.com/blog/tags/programming-languages)
