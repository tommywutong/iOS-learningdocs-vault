---
title: Copyrightable APIs Are Not a Good Thing
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2014/01/copyrightable-apis-not-a-good-thing/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:7f45c65c31bafb2b'
translated: false
---

> 原文：[Copyrightable APIs Are Not a Good Thing](https://oleb.net/blog/2014/01/copyrightable-apis-not-a-good-thing/)　·　Ole Begemann

# Copyrightable APIs Are Not a Good Thing

[Florian Mueller reports](http://www.fosspatents.com/2014/01/api-copyrightability-to-be-confirmed.html) on the [Oracle vs. Google case](https://en.wikipedia.org/wiki/Oracle_v._Google) that the appeals court agrees with Oracle’s claim that Google violated Oracle’s copyright when it copied large parts of the Java API for Android:

> As far as the copyrightability of Oracle’s Java API declaring code is concerned, I would go even further: it’s practically inconceivable that the district court’s non-copyrightability holding will be upheld considering that the circuit judges made perfectly clear that District Judge Alsup confused “fair use” and copyrightability issues and that Google’s whole non-copyrightability theory, which Judge Alsup adopted in its entirety, rests on a complete misreading of two key cases (_Sega_ and _Sony_).

Just to be clear, this is not about outright copying of the Java codebase.^[1](#fn:1) The judges of the appeals court seem to hold the opinion that the [design of the Java API](https://en.wikipedia.org/wiki/Structure,_sequence_and_organization) itself—and not just its implementation—is copyrightable, at least in cases where the API in question is substantial enough to be deemed a considerable creative effort, which the Java API undoubtedly is.

To Florian Mueller, this is a good thing:

> The fact of the matter is that, unless you’re Google or close to Google, there’s no reason at all to be concerned. On the contrary, it would really have been a threat to software development if the appellate hearing had worked out more favorably for Google because this would have made it very easy for large companies to hijack APIs developed by small, innovative players.

I disagree. What does it even mean to “hijack APIs”? I can’t remember a single case of a large company crushing a small developer solely by copying their innovative API. You don’t lure users away from a platform just by offering the same API. You get users for your API by offering a superior platform.

> As long as there is a sufficient creativity threshold, honest software developers are protected, not threatened, by copyright law. They are not threatened because if such code is reasonably creative, none of us will write the same code independently by happenstance: infringement will, in practical terms, require willfulness.

It is true that accidental infringement is not an issue here. What Mueller misses, though, is that there are lots of examples where developers with nothing but good intentions willfully copy the design of another API to the benefit of large audiences:

- The mission of the [GNUstep](http://www.gnustep.org) project is to reimplement Apple’s [Cocoa APIs](https://en.wikipedia.org/wiki/Cocoa_%28API%29) in order to make them available on other platforms.
- [Mono](http://www.mono-project.com/), an open-source implementation of [Microsoft’s .NET](https://en.wikipedia.org/wiki/.NET_Framework). [Xamarin.iOS](http://xamarin.com/ios) (formerly MonoTouch) combines the two to make iOS development accessible to .NET developers.
- [Cappuccino](http://www.cappuccino-project.org) is a web framework that is based on the design ideas of Cocoa.
- [Wine](http://www.winehq.org), an implementation of the Windows API for Linux and Unix systems.
- [ReactOS](http://www.reactos.org), a free operating system whose goal is to be binary compatible with Windows.
- Microsoft’s [Bing Maps SDK for iOS](https://www.bing.com/blogs/site_blogs/b/maps/archive/2011/05/05/new-bing-maps-ios-sdk.aspx) closely mimics Apple’s MapKit API to make it easier for developers to get started.
- Innumerable open-source developers willfully base the design of their libraries and components on the APIs of the “parent” platform for the same reason.

I am certainly not an expert in U.S. copyright law. Legally, the appeals court may be right that sufficiently creative APIs are copyrightable. And I do understand that the “infringed” parties in the above examples often have a commercial interest in prohibiting the use of their designs by competitors. But intellectually, I think they should not be allowed to prohibit this. Apple should not be able to stop Microsoft from adopting the MapKit API, nor should it be able to stop Google from copying the entire structure, sequence and organization of Cocoa if Google so chose.

The software world would be poorer for it.

1. Google did that, too, but only in a few relatively minor instances. [↩︎](#fnref:1)
