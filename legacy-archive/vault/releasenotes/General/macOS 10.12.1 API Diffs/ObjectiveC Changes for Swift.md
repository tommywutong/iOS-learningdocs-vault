---
title: macOS 10.12.1 API Diffs
apple_id: TP40017565
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2016-10-27'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOS10_12_1/Swift/ObjectiveC.html
archived_at: '2026-07-18T02:51:47.039881Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [macOS 10.12.1 API Diffs](macOS%2010.12%20to%20macOS%2010.12.1%20API%20Differences.md)


# ObjectiveC Changes for Swift

### ObjectiveC

Modified [objc_setEnumerationMutationHandler(_: ((Any?) -> Swift.Void)!)](https://developer.apple.com/documentation/objectivec/1418751-objc_setenumerationmutationhandl)

|  | Declaration |
| --- | --- |
| From | ``` func objc_setEnumerationMutationHandler(_ handler: (@escaping (Any?) -> Swift.Void)!) ``` |
| To | ``` func objc_setEnumerationMutationHandler(_ handler: ((Any?) -> Swift.Void)!) ``` |

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
