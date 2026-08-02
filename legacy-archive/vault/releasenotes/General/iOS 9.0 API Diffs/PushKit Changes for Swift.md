---
title: iOS 9.0 API Diffs
apple_id: TP40016222
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS90APIDiffs/Swift/PushKit.html
archived_at: '2026-07-18T02:56:57.429257Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 9.0 API Diffs](iOS%208.3%20to%20iOS%209.0%20API%20Differences.md)


# PushKit Changes for Swift

### PushKit

Added [PKPushTypeComplication](https://developer.apple.com/documentation/pushkit/pkpushtypecomplication)Modified [PKPushRegistry](https://developer.apple.com/documentation/pushkit/pkpushregistry)

|  | Declaration |
| --- | --- |
| From | ``` class PKPushRegistry : NSObject {     weak var delegate: PKPushRegistryDelegate!     var desiredPushTypes: Set<NSObject>!     func pushTokenForType(_ type: String!) -> NSData!     init!(queue queue: dispatch_queue_t!) } ``` |
| To | ``` class PKPushRegistry : NSObject {     weak var delegate: PKPushRegistryDelegate?     var desiredPushTypes: Set<NSObject>!     func pushTokenForType(_ type: String!) -> NSData!     init!(queue queue: dispatch_queue_t!) } ``` |

Modified [PKPushRegistry.delegate](https://developer.apple.com/documentation/pushkit/pkpushregistry/1614468-delegate)

|  | Declaration |
| --- | --- |
| From | ``` weak var delegate: PKPushRegistryDelegate! ``` |
| To | ``` weak var delegate: PKPushRegistryDelegate? ``` |

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
