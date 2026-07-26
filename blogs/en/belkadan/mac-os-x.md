---
title: Mac OS X
source: Belkadan (Jordan Rose, 前 Swift 编译器工程师)
source_key: belkadan
source_url: 'https://belkadan.com/blog/tags/mac-os-x'
original_language: en
published: ''
status: active
license: Copyright 2012–2020 Jordan Rose → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:221a4042ef49b997'
translated: false
---

> 原文：[Mac OS X](https://belkadan.com/blog/tags/mac-os-x)　·　Belkadan (Jordan Rose, 前 Swift 编译器工程师)

## [quasiquarantine](https://belkadan.com/blog/2019/12/Quasiquarantine/?tag=mac-os-x)

24 December 2019

In Apple’s TN2206, “[macOS Code Signing in Depth](https://developer.apple.com/library/archive/technotes/tn2206/)”, there’s a section about “[Checking Gatekeeper Compliance](https://developer.apple.com/library/archive/technotes/tn2206/_index.html#//apple_ref/doc/uid/DTS40007919-CH1-TNTAG211)”.

> - Package your program the way you ship it, such as in a disk image.
> - Download it from its website, or mail it to yourself, or send it to yourself using AirDrop or Message. This will quarantine the downloaded copy. This is necessary to trigger the Gatekeeper check as Gatekeeper only checks quarantined files the first time they’re opened.
> - Drag-install your app and launch it.

I figured jumping through a “download” or “send” step was overkill. Surely there’s a way to get the same effect programmatically, right?

[(Continue reading…)](https://belkadan.com/blog/2019/12/Quasiquarantine/?tag=mac-os-x)

Posted in [Technical](https://belkadan.com/blog/technical). Tags: [Mac OS X](https://belkadan.com/blog/tags/mac-os-x), [Source code](https://belkadan.com/blog/tags/source-code)

## [Keyboard Adventures](https://belkadan.com/blog/2012/04/Keyboard-Adventures/?tag=mac-os-x)

26 April 2012

The best utility for making custom keyboard layouts on Mac OS X has long been [Ukelele](http://scripts.sil.org/cms/scripts/page.php?site_id=nrsi&id=ukelele) (sic). Sure, Apple came up with an [XML format](https://developer.apple.com/library/mac/technotes/tn2056) for keyboard layouts, but when you want a variant of an existing keyboard, it’s a lot easier to just _copy the existing keyboard_ in Ukelele and modify the keys you want to change.

A few years ago I took a class on Phonetics and Phonology, and found myself needing to type in [IPA](http://en.wikipedia.org/wiki/International_Phonetic_Alphabet) quite often. So I fired up Ukelele and made a copy of the standard Dvorak keyboard and got to work. I didn’t…

[(Continue reading…)](https://belkadan.com/blog/2012/04/Keyboard-Adventures/?tag=mac-os-x)

Posted in [Technical](https://belkadan.com/blog/technical). Tags: [Mac OS X](https://belkadan.com/blog/tags/mac-os-x), [Text](https://belkadan.com/blog/tags/text)

## [rm vs. Time Machine](https://belkadan.com/blog/2011/07/rm-vs-Time-Machine/?tag=mac-os-x)

22 July 2011

Public Service Announcement: if a Time Machine backup fails, it will leave behind a file with an extension of `inprogress`. (It’s actually a folder.) If you have a hard time deleting it, **do not** use `rm`! It will erase files from **all** backups, instead of just the one in progress. Instead, trash the `inprogress` file from the Finder and Empty Trash as usual. It might take a while, but it will Do The Right Thing.

You could also leave the file alone and just try to backup again; Time Machine will clear out the failed `inprogress` file when the next backup succeeds.

[(Continue reading…)](https://belkadan.com/blog/2011/07/rm-vs-Time-Machine/?tag=mac-os-x)

Posted in [Technical](https://belkadan.com/blog/technical). Tags: [Mac OS X](https://belkadan.com/blog/tags/mac-os-x), [Unix](https://belkadan.com/blog/tags/unix), [Time Machine](https://belkadan.com/blog/tags/time-machine), [Filesystems](https://belkadan.com/blog/tags/filesystems)

## Older Posts

1. 2011-07-14[Priorities](https://belkadan.com/blog/2011/07/Priorities/?tag=mac-os-x)
2. 2011-06-03[Chrome vs. Safari](https://belkadan.com/blog/2011/06/Chrome-vs-Safari/?tag=mac-os-x)
3. 2011-05-31[User-Side Troubleshooting](https://belkadan.com/blog/2011/05/User-Side-Troubleshooting/?tag=mac-os-x)
4. 2009-06-26[Garbage Collectors and Stack Drawers](https://belkadan.com/blog/2009/06/Garbage-Collectors-and-Stack-Drawers/?tag=mac-os-x)

### Possibly Related Tags

- [Apple](https://belkadan.com/blog/tags/apple)
- [Book](https://belkadan.com/blog/tags/book)
- [Chrome](https://belkadan.com/blog/tags/chrome)
- [Filesystems](https://belkadan.com/blog/tags/filesystems)
- [Keystone](https://belkadan.com/blog/tags/keystone)
- [Programming languages](https://belkadan.com/blog/tags/programming-languages)
- [Safari](https://belkadan.com/blog/tags/safari)
- [Source code](https://belkadan.com/blog/tags/source-code)
- [Text](https://belkadan.com/blog/tags/text)
- [Time Machine](https://belkadan.com/blog/tags/time-machine)
- [Unix](https://belkadan.com/blog/tags/unix)
- [User experience](https://belkadan.com/blog/tags/user-experience)
- [Webmailer](https://belkadan.com/blog/tags/webmailer)
- [Windows](https://belkadan.com/blog/tags/windows)
