---
title: OS X v10.11.4 API Diffs
apple_id: TP40016680
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2016-03-21'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_11_4/Swift/VideoToolbox.html
archived_at: '2026-07-18T02:53:54.948174Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.11.4 API Diffs](OS%20X%20v10.11.4%20API%20Diffs.md)


# VideoToolbox Changes for Swift

### VideoToolbox

Modified [VTCompressionSession](https://developer.apple.com/documentation/videotoolbox/vtcompressionsession)

|  | Name | Declaration |
| --- | --- | --- |
| From | VTCompressionSessionRef | ``` typealias VTCompressionSessionRef = VTCompressionSession ``` |
| To | VTCompressionSession | ``` class VTCompressionSession { } ``` |

Modified [VTDecompressionSession](https://developer.apple.com/documentation/videotoolbox/vtdecompressionsession)

|  | Name | Declaration |
| --- | --- | --- |
| From | VTDecompressionSessionRef | ``` typealias VTDecompressionSessionRef = VTDecompressionSession ``` |
| To | VTDecompressionSession | ``` class VTDecompressionSession { } ``` |

Modified [VTFrameSilo](https://developer.apple.com/documentation/videotoolbox/vtframesiloref)

|  | Name | Declaration |
| --- | --- | --- |
| From | VTFrameSiloRef | ``` typealias VTFrameSiloRef = VTFrameSilo ``` |
| To | VTFrameSilo | ``` class VTFrameSilo { } ``` |

Modified [VTMultiPassStorage](https://developer.apple.com/documentation/videotoolbox/vtmultipassstorage)

|  | Name | Declaration |
| --- | --- | --- |
| From | VTMultiPassStorageRef | ``` typealias VTMultiPassStorageRef = VTMultiPassStorage ``` |
| To | VTMultiPassStorage | ``` class VTMultiPassStorage { } ``` |

Modified [VTPixelTransferSession](https://developer.apple.com/documentation/videotoolbox/vtpixeltransfersessionref)

|  | Name | Declaration |
| --- | --- | --- |
| From | VTPixelTransferSessionRef | ``` typealias VTPixelTransferSessionRef = VTPixelTransferSession ``` |
| To | VTPixelTransferSession | ``` class VTPixelTransferSession { } ``` |

Modified [VTSession](https://developer.apple.com/documentation/videotoolbox/vtsession)

|  | Declaration |
| --- | --- |
| From | ``` typealias VTSessionRef = VTSession ``` |
| To | ``` typealias VTSession = CFTypeRef ``` |

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
