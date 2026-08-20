---
title: iOS 8.1 API Diffs
apple_id: TP40014994
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2014-10-06'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS81APIDiffs/modules/VideoToolbox.html
archived_at: '2026-07-18T02:56:18.126398Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 8.1 API Diffs](iOS%208.0%20to%208.1%20API%20Differences.md)


# VideoToolbox Changes

## VideoToolbox

Removed VTCompressionSessionOptionFlags.valueAdded VTCompressionSessionOptionFlags.init(rawValue: UInt32)Modified VTCompressionSessionOptionFlags [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct VTCompressionSessionOptionFlags : RawOptionSetType {     init(_ value: UInt32)     var value: UInt32     static var BeginFinalPass: VTCompressionSessionOptionFlags { get } } ``` |
| To | ``` struct VTCompressionSessionOptionFlags : RawOptionSetType {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     static var BeginFinalPass: VTCompressionSessionOptionFlags { get } } ``` |

Modified VTCompressionSessionOptionFlags.init(_: UInt32)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: UInt32) ``` |
| To | ``` init(_ rawValue: UInt32) ``` |

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
