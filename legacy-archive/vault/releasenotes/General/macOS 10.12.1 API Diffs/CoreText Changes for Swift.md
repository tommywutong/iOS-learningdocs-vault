---
title: macOS 10.12.1 API Diffs
apple_id: TP40017565
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2016-10-27'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOS10_12_1/Swift/CoreText.html
archived_at: '2026-07-18T02:51:45.434332Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [macOS 10.12.1 API Diffs](macOS%2010.12%20to%20macOS%2010.12.1%20API%20Differences.md)


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
