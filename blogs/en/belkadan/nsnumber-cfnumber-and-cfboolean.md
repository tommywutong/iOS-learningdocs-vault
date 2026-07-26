---
title: NSNumber, CFNumber, and CFBoolean
source: Belkadan (Jordan Rose, 前 Swift 编译器工程师)
source_key: belkadan
source_url: 'https://belkadan.com/blog/2008/01/NSNumber-CFNumber-and-CFBoolean/'
original_language: en
published: ''
status: active
license: Copyright 2012–2020 Jordan Rose → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:c98e0a9d3f3fb303'
translated: false
---

> 原文：[NSNumber, CFNumber, and CFBoolean](https://belkadan.com/blog/2008/01/NSNumber-CFNumber-and-CFBoolean/)　·　Belkadan (Jordan Rose, 前 Swift 编译器工程师)

« [GenericToolbar and IB3](https://belkadan.com/blog/2007/12/GenericToolbar-and-IB3/)

[Alerts Without Apps (or nibs)](https://belkadan.com/blog/2008/03/Alerts-Without-Apps/) »

« [Performance Optimization: Why We Can't Use valueForKeyPath:](https://belkadan.com/blog/2007/10/Performance-Optimization-Why-We-Cannot-Use-valueForKeyPath/?tag=cocoa)

[Alerts Without Apps (or nibs)](https://belkadan.com/blog/2008/03/Alerts-Without-Apps/?tag=cocoa) »

## [NSNumber, CFNumber, and CFBoolean](#)

Interesting fact of the day. NSNumber and CFNumber are toll-free bridged, right?

[Not according to Apple.](http://developer.apple.com/documentation/Cocoa/Reference/Foundation/Classes/NSNumber_Class/Reference/Reference.html) Nowhere on NSNumber’s class page nor in the “Number and Value Programming” guide does it mention that NSNumber and CFNumber are toll-free bridged.

Next question. CFNumber and NSNumber are toll-free bridged, right?

[Of course.](http://developer.apple.com/documentation/CoreFoundation/Reference/CFNumberRef/Reference/reference.html)

Recently I’ve been working on an outline view property list editor for Dockyard, and I think I have a bit of a clue as to what’s going on. Most NSNumber types are instances of NSCFNumber, similar to most of Apple’s bridged classes.

But NSNumbers created with BOOL values are instances of NSCFBoolean. And CFBooleans aren’t CFNumbers.

So NSCFBoolean implements enough of NSNumber’s methods to pass as an NSNumber…and NSNumber subclasses can already pass as CFNumbers. The most definitive toll-free bridging reference, [Interchangeable Data Types](http://developer.apple.com/documentation/Cocoa/Conceptual/CarbonCocoaDoc/Articles/InterchangeableDataTypes.html), does say CFNumber and NSNumber are toll-free bridged. My hypothesis is because all CFNumbers are NSNumbers but not vice versa, some documentation writer decided not to include the usual toll-free bridging footnote.

Even though it should be there. The [Property List Programming Guide](http://developer.apple.com/documentation/Cocoa/Conceptual/PropertyLists/Articles/XMLPListsConcept.html) implies the same thing. Interestingly, while CFBooleans are also valid NSNumbers, _not_ all NSNumbers are valid CFBooleans. Which is why CFBoolean is not “toll-free bridged” with NSNumber, even though it will, in fact, work perfectly well to cast a `CFBooleanRef` to `NSNumber *`.

Also interesting is that while CFBooleans are not CFNumbers in the CoreFoundation hierarchy, they can be casted as if they were. Weird, huh?

Lack of bridging info for NSNumber filed as documentation bug [#5688009](rdar://problem/5688009)

This entry was posted on [January](https://belkadan.com/blog/2008/01) 14, [2008](https://belkadan.com/blog/2008) and is filed under [Technical](https://belkadan.com/blog/technical). Tags: [Cocoa](https://belkadan.com/blog/tags/cocoa)
