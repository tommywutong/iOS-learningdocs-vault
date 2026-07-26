---
title: Misleading Metrics and UX Tradeoffs
source: Belkadan (Jordan Rose, 前 Swift 编译器工程师)
source_key: belkadan
source_url: 'https://belkadan.com/blog/2018/04/Misleading-Metrics/'
original_language: en
published: ''
status: active
license: Copyright 2012–2020 Jordan Rose → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:a43495adb7477590'
translated: false
---

> 原文：[Misleading Metrics and UX Tradeoffs](https://belkadan.com/blog/2018/04/Misleading-Metrics/)　·　Belkadan (Jordan Rose, 前 Swift 编译器工程师)

« ["FIXME" Doesn't Always Mean "Fix Me"](https://belkadan.com/blog/2018/04/FIXME/)

[A Shiny Magic Number](https://belkadan.com/blog/2019/02/A-Shiny-Magic-Number/) »

« [Webmailer's Update Bar](https://belkadan.com/blog/2016/05/Webmailer-Update-Bar/?tag=user-experience)

[Soft Orders of Magnitude](https://belkadan.com/blog/2023/10/Soft-Orders-of-Magnitude/?tag=user-experience) »

## [Misleading Metrics and UX Tradeoffs](#)

Imagine you have a search feature, and you find that basically no one is using it. That is, the number of loads you get on the dedicated search page is tiny. You make a tweak to your UI, and suddenly way more people are going to the search page! Sounds like a win, right?

Except…the tweak to the UI was that previously you had search results loading inline in the search bar, and now it’s just doing _completions._ And your product is Facebook, which means that most searches are for people or pages that the searcher already knows; they’re just using the search bar for quick navigation (like [Spotlight](https://en.wikipedia.org/wiki/Spotlight_(software)) or the Start menu). And this change happened a year or two ago, but it still annoys me every time.

When I search for “mark” on Facebook, I _used to_ be able to jump straight to one of my friends named Mark. Now, Facebook still completes their name, but takes me to a search page first if I _choose_ that completion. I have to click on the first result to actually get to the friend.

![(here's what that looks like)](https://belkadan.com/blog/2018/04/Misleading-Metrics/mark.jpg)

What’s worse is that they clearly still have the old UI, where you can jump directly to a person or page, because that’s what they use for Recent Searches. (You can see this by clicking in the search bar and deleting all the text; no image here because blacking it out would mostly defeat the point.)

I called this post “Misleading Metrics” because I felt like this _had_ to have been a metrics-based decision. **[It turns out I was wrong](https://medium.com/@justahl/simplifying-facebook-search-8a555dbef4ad).** Facebook _did_ do qualitative user studies as part of making this change. But the design they settled on clashes horribly with how I actually use Facebook, and likely many others as well.

My original takeaway was that metrics give you numbers, but they don’t give you _reasons,_ and you should always try to think of multiple reasons why the numbers could be what they are—and even to mix your metrics with some in-person user studies and qualitative feedback. That’s still a good lesson, but maybe I need a better example.

(I’m picking on Facebook because I use Facebook^[1](#fn:me) and because they’re big enough to stand this kind of critique, but this is the kind of thing any company could do. Also, feedback submitted via [https://www.facebook.com/help/feedback](https://www.facebook.com/help/feedback).)

1. Please don’t try to find me on Facebook unless we’re friends or coworkers offline, or at least Twitter mutuals. Separate persona. [↩︎](#fnref:me)

This entry was posted on [April](https://belkadan.com/blog/2018/04) 29, [2018](https://belkadan.com/blog/2018) and is filed under [Technical](https://belkadan.com/blog/technical). Tags: [User experience](https://belkadan.com/blog/tags/user-experience), [Rant](https://belkadan.com/blog/tags/rant)
