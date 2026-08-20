---
title: watchOS 2.1 API Diffs
apple_id: TP40016636
resource_type: Release Note
platform: watchOS
topic: General
technology: null
published: '2015-12-08'
source_url: https://developer.apple.com/library/archive/releasenotes/General/watchOS21APIDiffs/Swift/ObjectiveC.html
archived_at: '2026-07-18T02:58:09.093533Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [watchOS 2.1 API Diffs](watchOS%202.0%20to%20watchOS%202.1%20API%20Differences.md)


# ObjectiveC Changes for Swift

### ObjectiveC

Modified [NSObject](https://developer.apple.com/documentation/objectivec/nsobject)

|  | Protocols |
| --- | --- |
| From | AnyObject, CVarArgType, CustomStringConvertible, Equatable, Hashable, NSObjectProtocol |
| To | CVarArgType, CustomStringConvertible, Equatable, Hashable, NSObjectProtocol |

Modified [objc_AssociationPolicy [enum]](https://developer.apple.com/documentation/objectivec/objc_associationpolicy)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [Selector [struct]](https://developer.apple.com/documentation/objectivec/selector)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct Selector : StringLiteralConvertible, ExtendedGraphemeClusterLiteralConvertible, UnicodeScalarLiteralConvertible, NilLiteralConvertible {     init(_ str: String)     init(unicodeScalarLiteral value: String)     init(extendedGraphemeClusterLiteral value: String)     init(stringLiteral value: String)     init()     init(nilLiteral nilLiteral: ()) } extension Selector : Equatable, Hashable {     var hashValue: Int { get } } extension Selector : CustomStringConvertible {     var description: String { get } } extension Selector : _Reflectable { } ``` | CustomStringConvertible, Equatable, ExtendedGraphemeClusterLiteralConvertible, Hashable, NilLiteralConvertible, StringLiteralConvertible, UnicodeScalarLiteralConvertible |
| To | ``` struct Selector : StringLiteralConvertible, NilLiteralConvertible {     init(_ str: String)     init(unicodeScalarLiteral value: String)     init(extendedGraphemeClusterLiteral value: String)     init(stringLiteral value: String)     init()     init(nilLiteral nilLiteral: ()) } extension Selector : Equatable, Hashable {     var hashValue: Int { get } } extension Selector : CustomStringConvertible {     var description: String { get } } extension Selector : _Reflectable { } ``` | CustomStringConvertible, Equatable, Hashable, NilLiteralConvertible, StringLiteralConvertible |

## Sending feedback…

## We’re sorry, an error has occurred.

Please try submitting your feedback later.

## Thank you for providing feedback!

Your input helps improve our developer documentation.

## How helpful is this document?

\*

Very helpful

Somewhat helpful

Not helpful

## How can we improve this document?

Fix typos or links

Fix incorrect information

Add or update code samples

Add or update illustrations

Add information about...

\*

_\* Required information_

To submit a product bug or enhancement request, please visit the
[Bug Reporter](https://developer.apple.com/bugreporter/)
page.

Please read [Apple's Unsolicited Idea Submission Policy](http://www.apple.com/legal/policies/ideas.html)
before you send us your feedback.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
