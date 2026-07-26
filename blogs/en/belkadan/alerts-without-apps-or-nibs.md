---
title: Alerts Without Apps (or nibs)
source: Belkadan (Jordan Rose, 前 Swift 编译器工程师)
source_key: belkadan
source_url: 'https://belkadan.com/blog/2008/03/Alerts-Without-Apps/'
original_language: en
published: ''
status: active
license: Copyright 2012–2020 Jordan Rose → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:408dda6cce9714fe'
translated: false
---

> 原文：[Alerts Without Apps (or nibs)](https://belkadan.com/blog/2008/03/Alerts-Without-Apps/)　·　Belkadan (Jordan Rose, 前 Swift 编译器工程师)

« [NSNumber, CFNumber, and CFBoolean](https://belkadan.com/blog/2008/01/NSNumber-CFNumber-and-CFBoolean/)

[HTTPS and Name-based Virtual Hosting](https://belkadan.com/blog/2008/08/HTTPS-and-Name-based-Virtual-Hosting/) »

« [NSNumber, CFNumber, and CFBoolean](https://belkadan.com/blog/2008/01/NSNumber-CFNumber-and-CFBoolean/?tag=cocoa)

[Categories and +load](https://belkadan.com/blog/2009/03/Categories-and-load/?tag=cocoa) »

[Quick Look in TextMate](https://belkadan.com/blog/2011/06/Quick-Look-in-TextMate/?tag=source-code) »

## [Alerts Without Apps (or nibs)](#)

Quickie for today that some people might find handy. (I need to start posting _much_ more. And reorganize a bit.)

Just yesterday I found myself wondering what to do when Dockyard would crash. The new Dockyard uses the wonderfully transparent distributed objects of Cocoa, which become staggeringly destructive when the remote process crashes. If you only used the data in a few places, or transferred everything by-copy, then you can probably recover. But in the bindings-intensive AppKit world of Dockyard Manager, you’re going to crash before you can say `[[self window] close:nil]` (I tried.) The bindings all try to update and come back complaining about a broken connection. The only thing that worked was to bail out, but if I tried to show an NSAlert to _tell_ the user we had to bail out, the app got stuck in the modal loop. I have no idea why, but I can only assume it’s because the hordes of orphaned object proxies have destroyed all of the run loops by this point.

(I’d like to know why I can’t just use NSAlert, but I have no idea where to go from the bit of poking I did. Pausing during the alert reveals an apparently normal run loop, but the alert simply won’t close.)

So, I have decided instead to bail out as planned, but to show an alert after the application quits. (Huh‽) Rather than use AppleScript’s “display alert”, which doesn’t look as nice, requires twice as much space as my final solution, and (the clincher) doesn’t work on Panther outside of AppleScript Studio, I wrote a small application intended to be called with a property list file describing the parameters of the alert.

The application wouldn’t be so remarkable, except that it works and it’s nibless. Even if you don’t care about the app itself (to be fair it’s really odd to want to display an alert without having an application context already, and a better sudden death app might be needed in the end), you might still be a bit interested in how to write a nibless application.

Summary: nibless faceless application that displays alerts based on a property list file description. If you’re interested at all, you can e-mail me and I’ll send you the source for what I’ve named Alert Notifier. (It used to be online, but got lost when I changed hosts.)

This entry was posted on [March](https://belkadan.com/blog/2008/03) 08, [2008](https://belkadan.com/blog/2008) and is filed under [Technical](https://belkadan.com/blog/technical). Tags: [Cocoa](https://belkadan.com/blog/tags/cocoa), [Source code](https://belkadan.com/blog/tags/source-code)
