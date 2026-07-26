---
title: 'Header Anchors: A Safari Extension'
source: Belkadan (Jordan Rose, 前 Swift 编译器工程师)
source_key: belkadan
source_url: 'https://belkadan.com/blog/freebies/Header-Anchors/'
original_language: en
published: ''
status: active
license: Copyright 2012–2020 Jordan Rose → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:192c960551d65eb8'
translated: false
---

> 原文：[Header Anchors: A Safari Extension](https://belkadan.com/blog/freebies/Header-Anchors/)　·　Belkadan (Jordan Rose, 前 Swift 编译器工程师)

« [Quick Look in TextMate](https://belkadan.com/blog/2011/06/Quick-Look-in-TextMate/)

[Mail Aliases](https://belkadan.com/blog/freebies/Mail-Aliases/) »

« [Chrome vs. Safari](https://belkadan.com/blog/2011/06/Chrome-vs-Safari/?tag=safari)

## [Header Anchors: A Safari Extension](#)

![](https://belkadan.com/blog/freebies/Header-Anchors/icon)

Ever want to link to a specific part of a web page? Well-designed web pages have _anchors_ at the start of each section, which can serve as targets of links.[1](#fn:name) You’ve probably seen URLs that end in `#something`; that _fragment identifier_, or “frag-id”, refers to a specific anchor on the page.

What’s annoying, though, is that even if an author includes them, they’re hard to discover. Sometimes there’s a table of contents, sometimes not. What I really wanted was a way to just click on the nearest header and grab the link. So I wrote “Header Anchors”.more

Header Anchors is a [Safari extension](https://extensions.apple.com/) which turns any header into a link if it has an associated anchor. It won’t look like a link (that’s my preferred design choice) but if you mouse over a header that has an anchor, the cursor will change to the usual “click here” pointer. You can then grab or copy the URL as usual.

The quickest way to test this is to go to [a Wikipedia article](http://en.wikipedia.org/wiki/Never_Gonna_Give_You_Up). Each section on the page has a header (such as “References”) which has an associated anchor. With Header Anchors installed, clicking on “References” will show you the URL that refers to that part of the page in your location bar.

[Download Header Anchors](https://belkadan.com/blog/freebies/Header-Anchors/HeaderAnchors-1.0.safariextz). Requires Safari 5.

Header Anchors will never access personal data, other than any preferences it might have in the future. Header Anchors will never access the internet; it does all its work in the browser.

You can check out the source [on Github](https://github.com/belkadan/HeaderAnchors.safariextension). If anyone wants to port this to Chrome or Firefox, be my guest…and please tell me about it, so I can link to your port!

1. The term “anchor” is why the HTML tag for linking is called `a`; its other use was to introduce an anchor on the page. Today I think the standard way to do that is just to use an `id` attribute. [↩︎](#fnref:name)

This entry was posted on [August](https://belkadan.com/blog/2011/08) 14, [2011](https://belkadan.com/blog/2011) and is filed under [Freebies](https://belkadan.com/blog/freebies). Tags: [Safari](https://belkadan.com/blog/tags/safari), [Safari extensions](https://belkadan.com/blog/tags/safari-extensions)
