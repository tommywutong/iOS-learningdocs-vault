---
title: watchOS 3.1 API Diffs
apple_id: TP40017546
resource_type: Release Note
platform: watchOS
topic: General
technology: null
published: '2016-10-27'
source_url: https://developer.apple.com/library/archive/releasenotes/General/watchOS31APIDiffs/Swift/UIKit.html
archived_at: '2026-07-18T02:58:39.111664Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [watchOS 3.1 API Diffs](watchOS%203.0%20to%20watchOS%203.1%20API%20Differences.md)


# UIKit Changes for Swift

### UIKit

Modified [UIEdgeInsets [struct]](https://developer.apple.com/documentation/uikit/uiedgeinsets)

|  | Declaration |
| --- | --- |
| From | ``` struct UIEdgeInsets {     var top: CGFloat     var left: CGFloat     var bottom: CGFloat     var right: CGFloat     init()     init(top top: CGFloat, left left: CGFloat, bottom bottom: CGFloat, right right: CGFloat)     static var zero: UIEdgeInsets { get } } extension UIEdgeInsets {     static var zero: UIEdgeInsets { get } } extension UIEdgeInsets : Equatable { } ``` |
| To | ``` struct UIEdgeInsets {     var top: CGFloat     var left: CGFloat     var bottom: CGFloat     var right: CGFloat     init()     init(top top: CGFloat, left left: CGFloat, bottom bottom: CGFloat, right right: CGFloat)     static var zero: UIEdgeInsets { get } } extension UIEdgeInsets {     static var zero: UIEdgeInsets { get } } extension UIEdgeInsets : Equatable { } extension UIEdgeInsets { } ``` |

Modified [UIOffset [struct]](https://developer.apple.com/documentation/uikit/uioffset)

|  | Declaration |
| --- | --- |
| From | ``` struct UIOffset {     var horizontal: CGFloat     var vertical: CGFloat     init()     init(horizontal horizontal: CGFloat, vertical vertical: CGFloat)     static var zero: UIOffset { get } } extension UIOffset {     static var zero: UIOffset { get } } extension UIOffset : Equatable { } ``` |
| To | ``` struct UIOffset {     var horizontal: CGFloat     var vertical: CGFloat     init()     init(horizontal horizontal: CGFloat, vertical vertical: CGFloat)     static var zero: UIOffset { get } } extension UIOffset {     static var zero: UIOffset { get } } extension UIOffset : Equatable { } extension UIOffset { } ``` |

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
