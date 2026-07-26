---
title: Mail Aliases
source: Belkadan (Jordan Rose, 前 Swift 编译器工程师)
source_key: belkadan
source_url: 'https://belkadan.com/blog/freebies/Mail-Aliases/'
original_language: en
published: ''
status: active
license: Copyright 2012–2020 Jordan Rose → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:247a0707b3026a06'
translated: false
---

> 原文：[Mail Aliases](https://belkadan.com/blog/freebies/Mail-Aliases/)　·　Belkadan (Jordan Rose, 前 Swift 编译器工程师)

« [Header Anchors: A Safari Extension](https://belkadan.com/blog/freebies/Header-Anchors/)

## [Mail Aliases](#)

Even though I’m the developer of [Webmailer](http://belkadan.com/webmailer), I mostly use Apple Mail for e-mail these days. Sometimes it’s nice to be able to send e-mails using different identities; for Belkadan Software tech support I’m “Jordy Rose”, but for school-related communication I’d prefer my name to show up as “Jordan Rose” and use my school e-mail address. Mail supports this, but doesn’t actually have a preference for it without creating separate accounts.[1](#fn:names) You have to edit the settings file manually.

So I wrote **[Mail Aliases](https://github.com/downloads/belkadan/Mail-Aliases/Mail%20Aliases.zip)**, a little app that can edit this data for you.more It’s not particularly polished, but it might come in handy for some of you. Note that this comes WITHOUT WARRANTY, so if you’re at all worried, back up your Mail account settings in `~/Library/Mail/V2/MailData/Accounts.plist`.

Mail Aliases has been tested on Mac OS X v10.7 (Lion), but should work with 10.6 (Snow Leopard) as well. You can check out the source [on Github](https://github.com/belkadan/Mail-Aliases).

---

By the way, if you wondering why the blog has been silent so long, there are two reasons. First, I’ve been moving away from Cocoa development into lower-level stuff, specifically contributing to [Clang](http://clang.llvm.org) in my free time. (Don’t worry, Webmailer and Keystone are still being supported!) Second, I spent several months after graduation teaching English abroad, and during that time I tried to stay away from software for a while. I’m hoping to start posting again soon about nifty programming things I come across, but (like every other blog on the internet) no promises!

1. You can have multiple e-mail addresses associated with a single account by separating them with commas, but you can only have one “Full Name” per account. [↩︎](#fnref:names)

This entry was posted on [April](https://belkadan.com/blog/2012/04) 10, [2012](https://belkadan.com/blog/2012) and is filed under [Freebies](https://belkadan.com/blog/freebies). Tags: [Mail.app](https://belkadan.com/blog/tags/mailapp)
