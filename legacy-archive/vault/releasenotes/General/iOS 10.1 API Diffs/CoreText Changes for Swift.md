---
title: iOS 10.1 API Diffs
apple_id: TP40017545
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2016-10-27'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS101APIDiffs/Swift/CoreText.html
archived_at: '2026-07-18T02:54:46.379798Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 10.1 API Diffs](iOS%2010.0%20to%20iOS%2010.1%20API%20Differences.md)


# CoreText Changes for Swift

### CoreText

Modified [CTFontDescriptorMatchFontDescriptorsWithProgressHandler(_: CFArray, _: CFSet?, _: CoreText.CTFontDescriptorProgressHandler) -> Bool](https://developer.apple.com/documentation/coretext/1511433-ctfontdescriptormatchfontdescrip)

|  | Declaration |
| --- | --- |
| From | ``` func CTFontDescriptorMatchFontDescriptorsWithProgressHandler(_ descriptors: CFArray, _ mandatoryAttributes: CFSet?, _ progressBlock: CoreText.CTFontDescriptorProgressHandler) -> Bool ``` |
| To | ``` func CTFontDescriptorMatchFontDescriptorsWithProgressHandler(_ descriptors: CFArray, _ mandatoryAttributes: CFSet?, _ progressBlock: @escaping CoreText.CTFontDescriptorProgressHandler) -> Bool ``` |

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
