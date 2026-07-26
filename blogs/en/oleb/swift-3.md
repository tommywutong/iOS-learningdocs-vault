---
title: Swift 3
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2016/06/swift-3/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:2d26b165e127f631'
translated: false
---

> 原文：[Swift 3](https://oleb.net/blog/2016/06/swift-3/)　·　Ole Begemann

# Swift 3

I’m a big fan of Swift 3. There’s a bunch of [relatively small syntax changes](https://github.com/apple/swift-evolution/blob/master/README.md#implemented-proposals-for-swift-3) that make the language more consistent. The most important of these is certainly the [consistent handling of parameter labels](https://github.com/apple/swift-evolution/blob/master/proposals/0046-first-label.md) in functions (yay!). Another small change I really like is that [the `@warn_unused_result` behavior is now the default](https://github.com/apple/swift-evolution/blob/master/proposals/0047-nonvoid-warn.md). It’s one of those little things that make it harder to screw up unless you explicitly opt in. The biggest modification to the standard library is the [new indexing model for collections](https://github.com/apple/swift-evolution/blob/master/proposals/0065-collections-move-indices.md).

From an app developer’s perspective, however, the biggest changes are how Swift imports Objective-C code (including Apple’s Cocoa frameworks) and the fantastic improvements Apple has made to Foundation and other frameworks to make using them in Swift feel more natural:

## The Grand Renaming

The [_Grand Renaming_](https://github.com/apple/swift-evolution/blob/master/proposals/0005-objective-c-name-translation.md) is the automatic (with optional manual adjustments) application of the [Swift API naming guidelines](https://swift.org/documentation/api-design-guidelines/) by the C and Objective-C importer. The names of most Cocoa APIs will be more concise in Swift, removing “needless” words that duplicate information that is already present in argument and return types.

## Foundation value types

Many Foundation data types are now [exposed in Swift as value types](https://github.com/apple/swift-evolution/blob/master/proposals/0069-swift-mutability-for-foundation.md), dropping the `NS` prefix and behaving as you would expect. The value types bridge to their Objective-C counterparts, just like `NSArray`, `NSDictionary`, `NSSet`, `NSString`, and `NSNumber` already do.

I love [the rationale Apple gives](https://github.com/apple/swift-evolution/blob/master/proposals/0069-swift-mutability-for-foundation.md#do-nothing) in SE-0069 for doing this:

> We know from our experience with Swift so far that if we do not provide these value types then others will, often by wrapping our types. It would be better if we provide one canonical API for greater consistency across all Swift code. This is, after all, the purpose of the Foundation framework.

## Type-safe string constants

Stringly-typed Objective-C constants can be annotated to be [imported into Swift as enums or structs](https://github.com/apple/swift-evolution/blob/master/proposals/0033-import-objc-constants.md), providing type safety and namespacing without losing the ability to add new constants to an existing “namespace”. This may not sound like much, but I think this change is actually one of the most beneficial in day-to-day use, if only because code completion becomes more accurate.

Apple has added the necessary annotations to many (all?) of their frameworks. For example, `NSCalendarIdentifierGregorian` becomes `Calendar.Identifier.gregorian`, and `UIApplicationDidFinishLaunchingNotification` is now `NSNotification.Name.UIApplicationDidFinishLaunching`.

## Type-safe selectors and key paths

There is a new syntax for Objective-C [selectors](https://github.com/apple/swift-evolution/blob/master/proposals/0022-objc-selectors.md) and [key paths](https://github.com/apple/swift-evolution/blob/master/proposals/0062-objc-keypaths.md) that can be checked for typos by the compiler. No more string literals!

## Import C functions as methods

C functions can be annotated to be [imported as methods](https://github.com/apple/swift-evolution/blob/master/proposals/0044-import-as-member.md), providing an object-oriented interface that feels completely natural in Swift. Apple has adopted this in Core Graphics. SE-0044 mentions the importer’s ability to [infer these mappings automatically](https://github.com/apple/swift-evolution/blob/master/proposals/0044-import-as-member.md#automatic-inference) on an opt-in basis. I haven’t investigated this, but this could mean that existing C libraries could adopt this with minimal effort.

## Swiftified Dispatch API

The GCD API has been [thoroughly revamped](https://github.com/apple/swift-evolution/blob/master/proposals/0088-libdispatch-for-swift3.md) for Swift.

---

I love all of these changes. Taken together, they go a long way in bringing Cocoa closer to idiomatic Swift.^[1](#fn:1) If you had told me in 2014 it would take Apple only two years to turn their frameworks into (almost) first-class Swift citizens, I don’t think I would have believed it.

The migration from Swift 2 to Swift 3 will probably be painful, but I think it will be worth it (and we don’t have a choice anyway, do we?). Almost every line in your code that calls into a Cocoa API will have to change, and the lack of [ABI](https://en.wikipedia.org/wiki/Application_binary_interface) stability means that you have to make the switch at the same time for all your dependencies. The Swift 3 migrator in Xcode 8 should be able to handle most of the grunt work, and the fact that the compiler knows about the old names is also a big help. If you don’t know the new name of an API, simply type the old name and apply the fix-it.

To learn more about the API design guidelines and how Apple has applied them to their frameworks, watch sessions [403 (Swift API Design Guidelines)](https://developer.apple.com/videos/play/wwdc2016/403/) and [207 (What’s New in Foundation for Swift)](https://developer.apple.com/videos/play/wwdc2016/207/). They are both excellent.

# Open-source Swift

None of the changes I mention in this article were revealed at WWDC. On the contrary, they have been developed in the open during the past six months, and Apple has actively asked for and listened to input from the community. The [Swift Evolution process](https://github.com/apple/swift-evolution/blob/master/process.md) is a great gift to the developer community, whether we actively participate in it or just read along.^[2](#fn:2)

Imagine for a moment Apple had not open-sourced Swift, or that they had open-sourced it but continued development behind closed doors. We would not have known about any of the changes before WWDC, nor would we have had the opportunity to voice our opinion about them. Who knows if Swift 3 would have turned out as well as it has?

1. Meanwhile, not surprisingly for a young language, the notion of what constitutes “idiomatic” Swift has shifted in the past and may continue to do so. [↩︎](#fnref:1)
2. Reading every message on the mailing list is a huge time investment that few people can afford. I recommend you subscribe to Jesse Squires’s [Swift Weekly Brief](https://swiftweekly.github.io). Jesse does a great job summarizing the most important discussions and new proposals. Or just look at new proposals directly in the [Swift Evolution repository](https://github.com/apple/swift-evolution/tree/master/proposals) from time to time. [↩︎](#fnref:2)
