---
title: UIKonf 2014 Talks
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2014/07/uikonf-2014-talks/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:5e5d9f4236890d22'
translated: false
---

> 原文：[UIKonf 2014 Talks](https://oleb.net/blog/2014/07/uikonf-2014-talks/)　·　Ole Begemann

# UIKonf 2014 Talks

The [UIKonf](http://www.uikonf.com) folks have published [the recordings of all talks](https://www.youtube.com/playlist?list=PLdr22uU_wISq-xmSdu1QQ4OJxr68qnJ54) of the May 2014 edition of the conference. These have been my favorites.

# Nick Lockwood: Image Performance

An in-depth discussion of the various ways to load, decode and draw images on iOS. Includes live performance comparisons that Nick ingeniously embedded directly in his presentation by driving it from a custom-built app that ran on an iPad. It’s a great technique for technical talks. Nick gives out some highly valuable information that I hadn’t read about anywhere else before. The [code for the presentation is available on GitHub](https://github.com/nicklockwood/Presentations/tree/master/ImagePerformance). Make sure to run it on an actual device and not in the simulator for useful results.

[The video on YouTube](https://www.youtube.com/watch?v=khoabTSgOFA&list=PLdr22uU_wISq-xmSdu1QQ4OJxr68qnJ54&index=10) (30:46 min)  
 [The iOS app used for slides and live benchmarks](https://github.com/nicklockwood/Presentations/tree/master/ImagePerformance)  
 [Nick Lockwood on Twitter](https://twitter.com/nicklockwood)

# Rachel Andrew: We’re Not “Doing a Startup”

Rachel shares her experiences in creating something on the side of your main work and slowly building it into a profitable product that can become your main business over time. Which ideas are worth pursuing as a bootstrapper with limited time and money? How do you distinguish between advice applicable to funded startups and bootstrapped businesses? How do you deal with procastination when working on your own? How do you build an audience? It is a really inspiring talk that reminded me of the [37signals](http://37signals.com) story.

[The video on YouTube](https://www.youtube.com/watch?v=TI0RDxyUmvo&list=PLdr22uU_wISq-xmSdu1QQ4OJxr68qnJ54&index=12) (41:04 min)  
 [The slides](https://speakerdeck.com/rachelandrew/uikonf-were-not-doing-a-startup) and [resources](http://rachelandrew.co.uk/presentations/not-doing-a-startup)  
 [Rachel Andrew on Twitter](https://twitter.com/rachelandrew)

# Luis Solano: Techniques to write DSLs in Objective-C

Designing a [domain-specific language](https://en.wikipedia.org/wiki/Domain-specific_language) can be a useful tool to make the purpose of certain parts of your code clearer or to allow non-programmers to work with it. The topic of this talk is how to use Objective-C language features to write DSLs in Objective-C. I liked it not just for the specific topic (which I don’t have an immediate application for), but because Luis shares some highly valuable Objective-C tricks and coding habits that are useful in a very general way, not just for writing DSLs. I think Luis found a good balance in sharing tricks that are not quite mainstream and not totally outlandish, either. There is also already version of this talk that takes Swift into account, held by Luis at AltConf 2014 ([video](https://www.youtube.com/watch?v=a3rR5XVA22w), [slides](https://speakerdeck.com/luisobo/techniques-to-write-dsls-in-swift)).

[The video on YouTube](https://www.youtube.com/watch?v=vv88YvH6Eqs&list=PLdr22uU_wISq-xmSdu1QQ4OJxr68qnJ54&index=6) (29:37 min)  
 [The slides](https://speakerdeck.com/luisobo/techniques-to-write-dsls-in-objective-c)  
 [Luis Solano on Twitter](https://twitter.com/luisobo)

# Max Seelemann: TextKit for the Rest of Us

Good overview of the components of TextKit and how they relate to each other. For everybody who’s been struggling with where to hook into `NSTextStorage`, `NSLayoutManager`, and `NSTextContainer` to add custom functionality. I found this very useful even though I had read about TextKit before. I sort of already knew the concepts, but it was really helpful to have an expert talk through some concrete examples.

[The video on YouTube](https://www.youtube.com/watch?v=cNUsaJ3Tmuo&list=PLdr22uU_wISq-xmSdu1QQ4OJxr68qnJ54&index=14) (31:37 min)  
 [The slides](https://speakerdeck.com/macguru17/uikonf-14-textkit-for-the-rest-of-us)  
 [Max Seelemann on Twitter](https://twitter.com/macguru17)

# Max Bazaliy: Reverse Engineering iOS Apps

Max knows a lot about iOS internals, and it really shows in this talk. I learned about a bunch of reverse engineering techniques that I had only known vaguely or not at all. Granted, you won’t need to know most of this in your day-to-day work as an app developer, but it can be useful at times, be it to check how another app implements a certain feature or to harden your own code against attackers. [Just keep this in mind](https://www.google.com/search?q=with+great+power+comes+great+responsibility).

[The video on YouTube](https://www.youtube.com/watch?v=vlaIIYpZUnM&list=PLdr22uU_wISq-xmSdu1QQ4OJxr68qnJ54&index=8) (32:06 min)  
 [The slides](https://speakerdeck.com/mbazaliy/reverse-engineering-ios-apps-lessons-learned-1)  
 [Max Bazaliy on Twitter](https://twitter.com/mbazaliy)

# David Rönnqvist: OpenGL (ES) Demystified

David does a really good job explaining the concepts behind OpenGL for people how are not used to the API. I am glad it is not another intro to 3D graphics maths but specifically about getting into OpenGL. This is another presentation built from a fully custom app, this time leveraging SceneKit.^[1](#fn:1)

[The video on YouTube](https://www.youtube.com/watch?v=8OHYX2RxBuo&list=PLdr22uU_wISq-xmSdu1QQ4OJxr68qnJ54&index=9) (29:30 min)  
 [The slides](https://speakerdeck.com/ronnqvist/opengl-es-demystified) and the [OS X app to drive the live presentation](https://www.dropbox.com/s/bpzckb5064vwqta/OpenGL%20%28ES%29%20Demysified%20Presentation.zip)  
 [David Rönnqvist on Twitter](https://twitter.com/davidronnqvist)

# Sally Shepard: Beyond VoiceOver

Good overview and live demos of the accessibility features in iOS. [The VoiceOver demo turns hilarious at one point](https://www.youtube.com/watch?v=OC_pmEW_GjE&list=PLdr22uU_wISq-xmSdu1QQ4OJxr68qnJ54&index=11t=7m5s) when the device receives a bunch of push notifications while VoiceOver is on, but I thought this incident actually made a great point: situations like this are what users of our apps are going to have to put up with if we do not test how they behave when used with accessibility features turned on. Also, [Cylon mode](https://www.youtube.com/watch?v=OC_pmEW_GjE&list=PLdr22uU_wISq-xmSdu1QQ4OJxr68qnJ54&index=11&t=23m28s).

[The video on YouTube](https://www.youtube.com/watch?v=OC_pmEW_GjE&list=PLdr22uU_wISq-xmSdu1QQ4OJxr68qnJ54&index=11) (34:10 min)  
 [Sally Shepard on Twitter](https://twitter.com/mostgood)

# Steven Kabbes: Cross-Platform iOS and Android Development at Dropbox

See [my earlier article on this one](https://oleb.net/blog/2014/05/how-dropbox-uses-cplusplus-cross-platform-development/). Unfortunately, this talk was not recorded because it took place on a side stage.

1. I had a very, very small part in this talk as it was apparently inspired by [a tweet of mine](https://twitter.com/olebegemann/status/410778117670977537). [↩︎](#fnref:1)
