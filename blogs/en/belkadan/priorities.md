---
title: Priorities
source: Belkadan (Jordan Rose, 前 Swift 编译器工程师)
source_key: belkadan
source_url: 'https://belkadan.com/blog/2011/07/Priorities/'
original_language: en
published: ''
status: active
license: Copyright 2012–2020 Jordan Rose → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:f8e1a857dc111808'
translated: false
---

> 原文：[Priorities](https://belkadan.com/blog/2011/07/Priorities/)　·　Belkadan (Jordan Rose, 前 Swift 编译器工程师)

« [git add](https://belkadan.com/blog/2011/06/git-add/)

[rm vs. Time Machine](https://belkadan.com/blog/2011/07/rm-vs-Time-Machine/) »

["Little Big Details"](https://belkadan.com/blog/2011/08/Little-Big-Details/?tag=user-experience) »

« [Chrome vs. Safari](https://belkadan.com/blog/2011/06/Chrome-vs-Safari/?tag=mac-os-x)

[rm vs. Time Machine](https://belkadan.com/blog/2011/07/rm-vs-Time-Machine/?tag=mac-os-x) »

« [Z shell](https://belkadan.com/blog/2009/06/Z-shell/?tag=unix)

[rm vs. Time Machine](https://belkadan.com/blog/2011/07/rm-vs-Time-Machine/?tag=unix) »

[Recommendations](https://belkadan.com/blog/2015/11/Recommendations/?tag=book) »

« [“Several New Features”](https://belkadan.com/blog/2009/05/Several-New-Features/?tag=apple)

[Big News](https://belkadan.com/blog/2012/05/Big-News/?tag=apple) »

[Webmailer's Update Bar](https://belkadan.com/blog/2016/05/Webmailer-Update-Bar/?tag=webmailer) »

« [Hacking Safari 4...for Great Convenience](https://belkadan.com/blog/2009/04/Hacking-Safari-4-for-Great-Convenience/?tag=keystone)

## [Priorities](#)

From [_Effective UI_](http://amzn.com/059615478X):

> The point of software isn’t necessarily to engross your users in the experience of using the software, it is to keep them focused on the ultimate goals they’re trying to accomplish in using the software, rather than on the actual use of the software itself. […] To be truly and unobtrusively useful, software must clear the straightest, most frictionless path to the accomplishment of the user’s goals.

_Effective UI_ is a very good book, one of the few instances where a discussion of UI (or UX, “user experience”) doesn’t drive me up a wall. This is not because I don’t care about UX, but rather because I care about _very strongly_. Utility software that does not “get out of my way” is no good. Productivity software that does not make easy things easy and hard things possible is no good. I make an exception for [GIMP](http://gimp.org) over [Photoshop](http://adobe.com/products/photoshop.html) because it’s free, but I prefer my old-but-registered copy of [Acorn](http://flyingmeat.com/acorn/) (or even [Preview](http://en.wikipedia.org/wiki/Preview_(software))) whenever my task is simple enough. The fact that other developers don’t make UX as high a priority as I do drives me crazy sometimes.

Both of Belkadan Software’s current products have been designed to “get out of your way” as much as possible. Webmailer has two pieces of UI: a preference pane calmly sitting in System Preferences, and a window for choosing a destination other than your default, which only appears if you ask for it. Even the “update available” notification slides in as a bar at the top of the preference pane, rather than presenting a dialog.

Keystone, likewise, tries to make a minimal intrusion into Safari’s location bar and preferences. Its completions only appear when the user types something that looks like a query. The autodiscovery UI tries to act as much like the normal “add bookmark” sheet as possible. And while it uses the traditional dialog for “update available” notifications, it takes advantage of [Sparkle](http://sparkle.andymatuschak.org/)’s ability to delay such notifications until the second time you run Safari with Keystone installed, in order to make a better impression and _reduce friction_ on the first run.

What I’ve come to decide, however, is that the different priorities are at least partially correlated with the primary platform you develop for.

- Mac OS X (and iOS) programmers, including Apple, place _user experience_ first. If there’s a choice between “better for the user” and “better for the program”, the user usually wins, and something that feels half-baked is better off unreleased.
- Unix/Linux/BSD programmers place _composability_ and _configurability_ first. Your program should do one thing very well, and make it easy to take input and output from other programs; after all, the package manager has a program or library for everything.
- Windows programmers place _features_ first. The program should be able to handle all use cases – after all, someday someone’s going to want to rotate an image through an angle that’s not a multiple of 90°. And besides, it gives you a leg up on the competition. (This is the most nebulous since I actually know very few Windows programmers.)
- Android seems to be a funny mix of all three of the other platforms’ priorities – but usually not in the same program.

These are, of course, generalizations, and I’ve known developers for all these platforms that break the stereotypes I’m laying down here. But I think it may be more important how the customer ecosystem for each platform affects its priorities in a feedback loop. Pro Mac users tend to value user experience, pro Windows users (and many enterprise organizations) place value on features, and pro Unix users usually have uniquely-configured systems tweaked towards optimality. Is it any surprise, then, that experienced developers on each platform try to play towards their target consumer base?

In any case, it is important to see that all three platforms’ criteria are valuable. “Bad UX”, “proprietary formats”, “no customization”, and “missing features” are all reasons why I’ve given up on various apps throughout the years. So I’m always on the lookout for suggestions on how to improve my programs.

What are _your_ priorities?

This entry was posted on [July](https://belkadan.com/blog/2011/07) 14, [2011](https://belkadan.com/blog/2011) and is filed under [Technical](https://belkadan.com/blog/technical). Tags: [User experience](https://belkadan.com/blog/tags/user-experience), [Mac OS X](https://belkadan.com/blog/tags/mac-os-x), [Unix](https://belkadan.com/blog/tags/unix), [Windows](https://belkadan.com/blog/tags/windows), [Book](https://belkadan.com/blog/tags/book), [Apple](https://belkadan.com/blog/tags/apple), [Webmailer](https://belkadan.com/blog/tags/webmailer), [Keystone](https://belkadan.com/blog/tags/keystone)
