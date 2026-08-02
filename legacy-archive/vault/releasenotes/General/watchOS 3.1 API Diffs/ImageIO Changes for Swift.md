---
title: watchOS 3.1 API Diffs
apple_id: TP40017546
resource_type: Release Note
platform: watchOS
topic: General
technology: null
published: '2016-10-27'
source_url: https://developer.apple.com/library/archive/releasenotes/General/watchOS31APIDiffs/Swift/ImageIO.html
archived_at: '2026-07-18T02:58:38.638660Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [watchOS 3.1 API Diffs](watchOS%203.0%20to%20watchOS%203.1%20API%20Differences.md)


# ImageIO Changes for Swift

### ImageIO

Modified [CGImageMetadataEnumerateTagsUsingBlock(_: CGImageMetadata, _: CFString?, _: CFDictionary?, _: ImageIO.CGImageMetadataTagBlock)](https://developer.apple.com/documentation/imageio/1465182-cgimagemetadataenumeratetagsusin)

|  | Declaration |
| --- | --- |
| From | ``` func CGImageMetadataEnumerateTagsUsingBlock(_ metadata: CGImageMetadata, _ rootPath: CFString?, _ options: CFDictionary?, _ block: ImageIO.CGImageMetadataTagBlock) ``` |
| To | ``` func CGImageMetadataEnumerateTagsUsingBlock(_ metadata: CGImageMetadata, _ rootPath: CFString?, _ options: CFDictionary?, _ block: @escaping ImageIO.CGImageMetadataTagBlock) ``` |

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
