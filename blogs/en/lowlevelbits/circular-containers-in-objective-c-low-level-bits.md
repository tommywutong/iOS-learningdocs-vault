---
title: Circular Containers in Objective-C - Low Level Bits 🇺🇦
source: Low Level Bits (Alex Denisov)
source_key: lowlevelbits
source_url: 'https://lowlevelbits.org/circular-containers-in-objective-c/'
original_language: en
published: ''
status: active
license: © 2014-2025 → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:314df30b292eeaf4'
translated: false
---

> 原文：[Circular Containers in Objective-C - Low Level Bits 🇺🇦](https://lowlevelbits.org/circular-containers-in-objective-c/)　·　Low Level Bits (Alex Denisov)

# Circular Containers in Objective-C

_Published on Apr 13, 2015_

Some time ago I accidentally wrote this code:

```objective
NSMutableArray *environments = [NSMutableArray new];
for (NSString *key in [dictionary allKeys]) {
    XCCEnvironment *environment = [[XCCEnvironment alloc] initWithName:key
                                                            parameters:dictionary[key]];
    [environments addObject:environments];
}
return environments;
```

Did you notice the problem here? Well, I didn’t.

### Problem

When I run the program I got a crash:

```
-[__NSArrayM someSelector]: unrecognized selector sent to instance 0x100211d80
```

Consumer of `environments` expected to get `XCCEnvironment`, but got `NSMutableArray`.

At the beginning it wasn’t clear why it actually happened, but I took a closer look at the code and found that I put array into itself:

```objective
// ...
NSMutableArray *environments = [NSMutableArray new];
// ...
[environments addObject:environments];
// ...
```

Documentation says nothing about collection’s behaviour in such situation, the only valuable (imo) reading I’ve found is Mike Ash’s blog-post [Let’s break Cocoa](https://www.mikeash.com/pyblog/friday-qa-2014-01-10-lets-break-cocoa.html).

The post says that mutable arrays, dictionaries and sets are going really crazy if you make so-called circular containers. Another problem is that they cause a memory leak when ARC is enabled: collection retains itself.

### Solution

I believe that normally developers do not put collection inside the collection. Though, it is the same kind of belief as ‘programmers do not dereference null pointers’ - it is still happens and probably it’s kinda unexpected behaviour.

I was pretty sure that clang is able to prevent me and other people from doing this mistake, but I didn’t find any warning/flag/setting that does this check.

Eventually I decided to implement it. Implementation took a couple of evenings but now it’s [in trunk](https://github.com/llvm-mirror/clang/commit/5dc6c6cd87f3a86fe9d5ba9d1b3892252c7de248).

Actual patch checks the following mutable collections:

- NSMutableArray
- NSMutableDictionary
- NSMutableSet
- NSMutableOrderedSet
- NSCountedSet

And shows warning if you trying to put collection inside itself

The warning could be enabled/disabled with `-wobjc-circular-container`/`-wno-objc-circular-container` respectively, though it’s enabled ‘by default’.

### Conclusion

Recent clang version contains this feature, but it’s not yet available within Xcode, and I guess it’ll appear with the next major release - in a year or so.

But, anyway, having open-source tools is really amazing: you can tweak it, extend it and make your life and, probably, lives of other people a bit better.

Happy hacking!

**UPD**

This feature got into WWDC 2016, [What’s new in LLVM](https://developer.apple.com/videos/play/wwdc2016/405/)

![](https://lowlevelbits.org/img/circular-containers/wwdc.png)
