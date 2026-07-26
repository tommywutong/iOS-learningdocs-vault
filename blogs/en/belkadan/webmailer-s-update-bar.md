---
title: 'Webmailer''s Update Bar'
source: Belkadan (Jordan Rose, 前 Swift 编译器工程师)
source_key: belkadan
source_url: 'https://belkadan.com/blog/2016/05/Webmailer-Update-Bar/'
original_language: en
published: 2016-05-29
status: active
license: Copyright 2012–2020 Jordan Rose → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:94aeb713cb7d4b94'
translated: false
---

> 原文：[Webmailer's Update Bar](https://belkadan.com/blog/2016/05/Webmailer-Update-Bar/)　·　Belkadan (Jordan Rose, 前 Swift 编译器工程师)

« [So You Want to Be a (Compiler) Wizard](https://belkadan.com/blog/2016/05/So-You-Want-To-Be-A-Compiler-Wizard/)

[Pronoun Buttons](https://belkadan.com/blog/2016/06/Pronoun-Buttons/) »

« ["Little Big Details"](https://belkadan.com/blog/2011/08/Little-Big-Details/?tag=user-experience)

[Misleading Metrics and UX Tradeoffs](https://belkadan.com/blog/2018/04/Misleading-Metrics/?tag=user-experience) »

« [Priorities](https://belkadan.com/blog/2011/07/Priorities/?tag=webmailer)

## [Webmailer's Update Bar](#)

A few weeks ago longtime Mac developer [Daniel Jalkut](http://bitsplitting.org) said something on Twitter that struck a chord with me.

> Now to get back to making my own software more Mac-like.
> 
> — Daniel Jalkut (@danielpunkass)
> 
> May 3, 2016

This reminded me of a particular time when I spent days working on the experience for a feature that no one would really care about, and might not even see: the “update available” notification for one of my pre-employment programs, Webmailer. So I decided to ~~show off~~ post about it.

---

Webmailer’s job was to forward `mailto` URLs to your particular webmail system; as such, it didn’t really need a whole _application._ It just launched on demand when you clicked a `mailto` link, opened your webmail with the right parameters filled in, and exited. I _could_ have put the settings for that in the app itself, but at the time it felt more natural to treat it as part of the system and put them in System Preferences using a [custom preference pane](https://developer.apple.com/library/mac/documentation/UserExperience/Conceptual/PreferencePanes/PreferencePanes.html).

This worked pretty well! You downloaded Webmailer, double-clicked the prefpane, and were taken to the settings; once everything was set up, you were good.

At the time, the standard (and best) way to add update support to a Mac program was the [Sparkle](https://sparkle-project.org/) framework, originally by [Andy Matuschak](https://andymatuschak.org).[1](#fn:sparkle) Sparkle put a lot of value on the user experience; for example, it wouldn’t ask you whether you wanted automatic updates until the _second_ time you launched a program.

The problem with Sparkle was that all of its interaction with the user was through dialog panels. In a normal application that’s fine: you might have many windows open, and the Sparkle panel would be on top of them. But OS X’s System Preferences is an all-in-one-window app, so much so that closing the window causes the app to quit. Having another window pop up just felt wrong.

So I ended up doing this:

I spent a lot of time working out the details there: tweaking the background gradient (which goes from “dark grey” to “slightly lighter dark grey”), adjusting the download arrow icon, changing the text and button baseline to be pixel-exact where I wanted them, trying different animation lengths, seeing if it looked better to _reveal_ the bar’s contents or having the whole thing slide in…not to mention figuring out what text and buttons I wanted to have, based on the original Sparkle dialog.

---

It’s a small thing, really, in the grand scheme of things. Most Webmailer users probably never even saw it, because you had to go back into the preference pane to check for updates. (It seemed too intrusive to do it whenever you happened to click on a `mailto` link.) But I was proud of it, and to be honest I’m still proud of it.

These are the kind of details you don’t notice, but which nevertheless make an app a _good_ app. Even if I [don’t work on GUI apps anymore](https://swift.org), I still appreciate the thought and design that goes into them.

1. Sparkle is still in use today by pretty much every Mac app that isn’t distributed through the Mac App Store. [↩︎](#fnref:sparkle)

This entry was posted on [May](https://belkadan.com/blog/2016/05) 29, [2016](https://belkadan.com/blog/2016) and is filed under [Technical](https://belkadan.com/blog/technical). Tags: [User experience](https://belkadan.com/blog/tags/user-experience), [Webmailer](https://belkadan.com/blog/tags/webmailer)
