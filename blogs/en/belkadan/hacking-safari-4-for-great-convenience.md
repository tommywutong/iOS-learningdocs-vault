---
title: Hacking Safari 4...for Great Convenience
source: Belkadan (Jordan Rose, 前 Swift 编译器工程师)
source_key: belkadan
source_url: 'https://belkadan.com/blog/2009/04/Hacking-Safari-4-for-Great-Convenience/'
original_language: en
published: ''
status: active
license: Copyright 2012–2020 Jordan Rose → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:9cd1ad0ec1607cfc'
translated: false
---

> 原文：[Hacking Safari 4...for Great Convenience](https://belkadan.com/blog/2009/04/Hacking-Safari-4-for-Great-Convenience/)　·　Belkadan (Jordan Rose, 前 Swift 编译器工程师)

« [Const Correctness](https://belkadan.com/blog/2009/03/Const-Correctness/)

[Safer Plugin Categories](https://belkadan.com/blog/2009/04/Safer-Plugin-Categories/) »

[Priorities](https://belkadan.com/blog/2011/07/Priorities/?tag=keystone) »

## [Hacking Safari 4...for Great Convenience](#)

For the last few years, I’ve been using a great little Safari plugin called “Sogudi” (“Safari, Sogudi”…get it?). Sogudi allows for keyword searching: you type something like “wiki Safari” and it goes to the Wikipedia page for Safari. This is something Firefox has had for a while, but Safari (and its lack of plugin support) really needed.

Sogudi was great, but I was disappointed to find that it no longer worked with the Safari 4 beta. Even worse, the author had stopped development, having unrecoverably lost the source code. (!) It only took a few weeks before I was fed up; my keyword search habits are quite ingrained by now.

So I went and [class-dumped](http://www.codethecode.com/projects/class-dump/) the code for Safari, poked around a little, and found that the completion system was handled by C++. Darn! But wait…the controller for the little menu was still Objective-C. Maybe I could tap into it there… (spoiler: you can).

At this point, someone might want to ask why I picked the completion system, instead of just catching the URL when the user hits Return. The answer is simple: I considered being able to see the expansion valuable; also, this lets you selectively ignore (or select) the new shortcuts when you have something that could be interpreted differently. An added bonus is that you can have two shortcuts for the same keyword, and select it in the completion list.

OK, back to the code. Normally, Safari completion items are wrapper objects around opaque C++ structs, which I did not want to reverse-engineer. Instead, I created a FakeCompletionItem class, which responded to the same attribute messages. By swizzling some of the completion controller’s methods, these fake items can be used exactly like the “real” ones.

From there it was simple; getting the completion items to take the query into account, loading and saving, etc. So part of this is a preview that, in a few weeks, there’ll be a Safari keyword completion plugin (a [SIMBL](http://www.culater.net/software/SIMBL/SIMBL.php) plugin) up on the Belkadan Software site.

The other part of the post, though, is that I’m making this completion-injection system modular enough for _anyone_ to add completions. Not sure how many people will be interested, but it’ll be out there, soon. Still need to iron out some bugs, add documentation, etc…but soon. It was a pretty cool quick project, and now I’ve got keyword search back.

By the way, people might be wondering why I’m not working on Dockyard. The answer is, I’d like to, but I don’t have the time. Dockyard is a _big_ project now, while this little plugin was just a single day’s work, plus refinements.

(If you really can’t wait for me to post this, there actually is a keyword search plugin available now, called Keywurl. I discovered this about two-thirds of the way through my own project. Like Sogudi, Keywurl performs its action on Return, and doesn’t allow multiple shortcuts with the same name, but it also has more flexible query string construction. In practice, I’ve very rarely wanted this extra flexibility.)

This entry was posted on [April](https://belkadan.com/blog/2009/04) 02, [2009](https://belkadan.com/blog/2009) and is filed under [Technical](https://belkadan.com/blog/technical). Tags: [Keystone](https://belkadan.com/blog/tags/keystone)
